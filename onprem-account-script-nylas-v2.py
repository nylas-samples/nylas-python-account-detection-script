import requests
import time
import csv
import base64

# Configuration
client_id = 'YOUR CLIENT ID'  # Replace with your actual client ID
client_secret = 'YOUR CLIENT SECRET'  # Replace with your actual client secret
api_endpoint = 'https://api.nylas.com/a/{}/accounts'.format(client_id)
request_limit = 100  # Max accounts per request
requests_per_second = 5  # Configurable rate of requests per second, max 10
personal_microsoft_domains = ['outlook.com', 'hotmail.com', 'msn.com']  # List of personal Microsoft account providers

# Base64 encode the client secret
auth_string = base64.b64encode(f"{client_secret}:".encode()).decode()

# Headers for the API request
headers = {
    'Authorization': f'Basic {auth_string}',
    'Content-Type': 'application/json'
}

# Function to get accounts from Nylas
def get_accounts(offset):
    params = {
        'limit': request_limit,
        'offset': offset
    }
    response = requests.get(api_endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching accounts: {response.text}")
        return None

# Main script
def main():
    offset = 0
    all_accounts = []

    while True:
        accounts = get_accounts(offset)
        if not accounts:
            break

        for account in accounts:
            if (account['provider'] == 'ews' or account['provider'] == 'eas') and account['authentication_type'] == 'password':
                domain = account['email'].split('@')[-1]
                if domain not in personal_microsoft_domains:
                    all_accounts.append(account)

        offset += request_limit
        time.sleep(1 / requests_per_second)

        if len(accounts) < request_limit:
            break

    # Write to CSV
    if(all_accounts.__len__() > 0):
        with open('nylas_accounts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=all_accounts[0].keys())
            writer.writeheader()
            writer.writerows(all_accounts)
            print(f'Found {all_accounts.__len__()}')
    else:
        print("No accounts found")

if __name__ == "__main__":
    main()
