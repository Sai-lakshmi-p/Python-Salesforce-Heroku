import requests

# Salesforce credentials and connected app details
CONSUMER_KEY = (
    '3MVG9fe4g9fhX0E4eEi0k1.NeeMFJ934LpNVtnq4dQtwHMxO2aqtvxl'
    '0rmQleyR_Dr2tQRUriZIBH84IRVakt'
)
CONSUMER_SECRET = (
    '27D317E58AB814ABABAB8A1748FD6915A93034BEF3733E17403C439'
    '3AB2FC2C3'
)
USERNAME = 'sailakshmi@salesforce.com'
PASSWORD = 'Welcome$2024QqtNVG1L466zl4fJqnQmUm2Z'
TOKEN_URL = 'https://login.salesforce.com/services/oauth2/token'


# Function to get Salesforce OAuth2 access token
def get_access_token():
    data = {
        'grant_type': 'password',
        'client_id': CONSUMER_KEY,
        'client_secret': CONSUMER_SECRET,
        'username': USERNAME,
        'password': PASSWORD
    }

    # Send request to Salesforce to get access token
    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        return (
            response.json().get('access_token'),
            response.json().get('instance_url')
        )
    else:
        return None, None


# Function to query Salesforce for Account data
def query_salesforce_accounts(access_token, instance_url):
    query_url = f"{instance_url}/services/data/v52.0/query/"
    query_params = {
        'q': (
            'SELECT Id, Name, BillingCity '
            'FROM Account LIMIT 10'
        )
    }
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Send the query request
    query_response = requests.get(
        query_url, 
        headers=headers, 
        params=query_params
    )

    if query_response.status_code == 200:
        return query_response.json()['records']
    else:
        return None
