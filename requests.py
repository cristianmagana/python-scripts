import requests
from concurrent.futures import ThreadPoolExecutor

# Function 1: Check a single endpoint
def check_endpoint(endpoint):
    try:
        resp = requests.get(endpoint['url'], timeout=10)
        if resp.status_code == 200:
            print(f"✓ {endpoint['name']} [{endpoint['url']}] - OK")
        else:
            print(f"✗ {endpoint['name']} [{endpoint['url']}] - Status: {resp.status_code}")
    except Exception as e:
        print(f"✗ {endpoint['name']} [{endpoint['url']}] - Error: {e}")

# Function 2: Get endpoints and check all concurrently
def health_check(endpoints_url):
    try:
        # Get endpoints from API
        resp = requests.get(endpoints_url, timeout=10)
        if resp.status_code != 200:
            print(f"Failed to get endpoints, status: {resp.status_code}")
            return
        
        endpoints = resp.json()['endpoints']
        
        # Check all endpoints concurrently
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(check_endpoint, endpoints)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    endpoints_url = "https://api.example.com/endpoints"
    health_check(endpoints_url)