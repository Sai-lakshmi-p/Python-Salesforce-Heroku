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

# Step 1: Get OAuth2 Access Token
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
    # Parse the response
    access_token = response.json().get('access_token')
    instance_url = response.json().get('instance_url')
    print(f"Access Token: {access_token}")
    print(f"Instance URL: {instance_url}")
else:
    print(f"Error: {response.text}")
    exit()

# Step 2: Query Salesforce Accounts
query_url = f"{instance_url}/services/data/v52.0/query/"
query_params = {
    'q': 'SELECT Id, Name, BillingCity FROM Account LIMIT 10'
}
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Send the query request
query_response = requests.get(query_url, headers=headers, params=query_params)

# Step 3: Check and print query results
if query_response.status_code == 200:
    accounts = query_response.json()
    # Print each account in a simple format, breaking lines for readability
    for account in accounts['records']:
        print(
            f"ID: {account['Id']}, "
            f"Name: {account['Name']}, "
            f"Billing City: {account.get('BillingCity', 'N/A')}"
        )
else:
    print(f"Query Error: {query_response.text}")
