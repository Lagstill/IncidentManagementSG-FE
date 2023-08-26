import streamlit as st
import requests

def get_resolution(query):
    api_endpoint = 'https://socgen.azurewebsites.net/query'
    params = {'question': query}
    
    response = requests.post(api_endpoint, json=params)
    print(response.status_code, response.json())
    if response.status_code == 200:

        return response.json()
    else:
        return 'Error fetching resolution'

def main():
    st.title('Error Resolution System')
    
    error_types = [
        'FTR', 'Essbase', 'Database', 'Application', 'Server Outage',
        'Database Performance Degradation', 'Network Connectivity Issues',
        'Application Performance Drop', 'Data Import Failure'
    ]
    
    selected_error_type = st.selectbox('Select Error Type:', error_types)
    user_query = st.text_input('Enter Your Query:')
    
    if st.button('Get Resolution'):
        if user_query:
            resolution = get_resolution( user_query)
            st.write('**Resolution:**')
            st.write(resolution)
        else:
            st.warning('Please enter a query.')

if __name__ == '__main__':
    main()
