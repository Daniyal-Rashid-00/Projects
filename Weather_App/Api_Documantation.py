import requests

api_key = "fa861ae77e724cef99c51659241411"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=gujranwala"

response = requests.get(url)
    
if response.status_code == 200:
    data = response.json()  # Assuming the response is JSON
    print(data)
else:
    print(f"Error: {response.status_code}")