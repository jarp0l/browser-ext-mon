import httpx
import os

PB_API_URL = os.getenv("PB_API_URL", "http://localhost:8090/api")
SERVICE_TOKEN = os.getenv("PB_OSQUERY_SERVICE_TOKEN", "osquery-be")


def enroll(api_key):
    url = f"{PB_API_URL}/collections/organizations/records"
    # headers = {
    #     "X-SERVICE-TOKEN": SERVICE_TOKEN,
    # }
    params = {"filter": f"(api_key='{api_key}')"}
    
    response = httpx.get(url, params=params)
    print(response.json())
    
    
    try:
        response = httpx.get(url, params=params)
        
        response.raise_for_status()
        
        data = response.json()

        items = data.get("items", [])
        for item in items:
            org_id = item.get("id")
            if org_id:
                
                return org_id
                # Test other endpoints with this org_id
               
        
        return data["totalItems"] > 0
        
        
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None

def test_endpoint(org_id):
    # Example of testing an endpoint with the organization ID
    url = f"{PB_API_URL}/collections/nodes/records"
    params = {"filter": f"(org_id='{org_id}')"}
    response = httpx.get(url, params=params)
    try:
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        for item in items:
 
            print("Collection ID:", item.get("collectionId"))
            print("Collection Name:", item.get("collectionName"))
            print("Created:", item.get("created"))
            print("ID:", item.get("id"))
            print("Org ID:", item.get("org_id"))
            print("Owner Email:", item.get("owner_email"))
            print("Updated:", item.get("updated"))
            print("UUID:", item.get("uuid"))
            print()
        return data["totalItems"] > 0
        # Process data from the endpoint
        print("Response from endpoint:")
        print(data)
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
api_key = "mW9oUTfiryOJvZPX"

exists = enroll(api_key)
print(exists)
org_id = enroll(api_key)

if org_id:
    print("Organization ID:", org_id)
    # Test other endpoints with this org_id
    test_endpoint(org_id)
else:
    print("Organization ID not found")
    

