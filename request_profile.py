import requests
from bs4 import BeautifulSoup

def request_profile(scholar_id='3TK9yz8AAAAJ'):
    base_url = "https://scholar.google.com/citations?user="
    url = f"{base_url}{scholar_id}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example: Extract the name of the person
            # You will need to modify the selectors based on the actual page structure
            name_selector = 'div[id="gsc_prf_in"]'
            name = soup.select_one(name_selector).text

            # Extract more profile information as needed
            # ...

            return {
                "name": name,
                # ... other profile information ...
            }
        else:
            return "Failed to retrieve data. Status code: " + str(response.status_code)
    except Exception as e:
        return str(e)

# Example usage
profile = request_profile()
print(profile)
