import pickle
from pathlib import Path
import requests
# import pandas as pd  
# import plotly.express as px  # pip install plotly-express
import subprocess
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth 

subprocess.run(["pip", "install", "streamlit-authenticator"])


def get_resolution(query):
    api_endpoint = 'https://socgen.azurewebsites.net/query'
    params = {'question': query}
    
    response = requests.post(api_endpoint, json=params)
    print(response.status_code, response.json())
    if response.status_code == 200:

        return response.json()
    else:
        return 'Error fetching resolution'

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

names = ["Alagu Prakalaya", "Pragathi"]
usernames = ["alagu", "pragathi"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)


credentials = {
    "usernames":{
        usernames[0]:{
            "name":names[0],
            "password":hashed_passwords[0]
            },
        usernames[1]:{
            "name":names[1],
            "password":hashed_passwords[1]
            }            
        }
    }


# load hashed passwords


authenticator = stauth.Authenticate(credentials,"incident_management_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.title('Incident Management System')
    
    error_types = [
        'FTR', 'Essbase', 'Database', 'Application', 'Server Outage',
        'Database Performance Degradation', 'Network Connectivity Issues',
        'Application Performance Drop', 'Data Import Failure'
    ]
    
    # selected_error_type = st.selectbox('Select Error Type:', error_types)
    user_query = st.text_input('Enter Your Query:')
    
    if st.button('Get Resolution'):
        if user_query:
            resolution = get_resolution( user_query)
            st.write('**Resolution:**')
            st.write(resolution)
        else:
            st.warning('Please enter a query.')


