from pocketbase.api import PocketBase
import os
# Replace with your PocketBase server URL
pocketbase_url = "http://your-pocketbase-url:port"  # Replace with your actual URL and port

# Create a PocketBase client instance
pb = PocketBase(pocketbase_url)

# Replace with your credentials

PB_OSQUERY_USER_EMAIL = os.getenv("PB_OSQUERY_USER_EMAIL","osquery@localhost.dev")
PB_OSQUERY_USER_PASSWORD = os.getenv("PB_OSQUERY_USER_PASSWORD","osquery@localhost.dev")

try:
    # Attempt authentication
    auth_data = pb.collection("users").auth_with_password(PB_OSQUERY_USER_EMAIL, PB_OSQUERY_USER_PASSWORD)

    if auth_data:
        # Check if authentication is valid
        print(pb.auth_store.is_valid)

        # Print authentication data (if successful)
        print(pb.auth_store.token)
        print(pb.auth_store.model.get("id"))  # Access user ID from the model

    else:
        print("Authentication failed: Invalid credentials or network error.")

except Exception as e:
    print(f"Authentication failed: {e}")

# Clear authentication (logout)
pb.auth_store.clear()
print("Logged out successfully")
