from flask import Flask, jsonify
from salesforce import get_access_token, query_salesforce_accounts

app = Flask(__name__)


# Flask route to trigger Salesforce query
@app.route('/accounts', methods=['GET'])
def get_accounts():
    access_token, instance_url = get_access_token()
    if access_token and instance_url:
        accounts = query_salesforce_accounts(access_token, instance_url)
        if accounts:
            return jsonify(accounts)
        else:
            return jsonify(
                {'error': 'Failed to query Salesforce Accounts'}
            ), 500
    else:
        return jsonify(
            {'error': 'Failed to authenticate with Salesforce'}
        ), 500


if __name__ == '__main__':
    app.run(debug=True)
