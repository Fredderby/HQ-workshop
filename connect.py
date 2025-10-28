import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# Load environment variables from .env file
load_dotenv()

def cred():
    # 1. Scopes for Sheets and Drive access
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # 2. Load service-account details from environment variables
    project_id      = os.getenv("PROJECT_ID")
    private_key_id  = os.getenv("PRIVATE_KEY_ID")
    private_key     = os.getenv("PRIVATE_KEY").replace('\\n', '\n')
    client_email    = os.getenv("CLIENT_EMAIL")
    client_id       = os.getenv("CLIENT_ID")
    client_cert_url = os.getenv("CLIENT_X509_CERT_URL")

    credentials_dict = {
        "type": "service_account",
        "project_id": project_id,
        "private_key_id": private_key_id,
        "private_key": private_key,
        "client_email": client_email,
        "client_id": client_id,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": client_cert_url
    }

    # 3. Authorize gspread client
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, SCOPES)
    client = gspread.authorize(creds)
    return client


# Optional: Quick test
if __name__ == "__main__":
    cred()
       