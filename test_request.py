import requests

url = "http://127.0.0.1:5000/predict"
data = {"text": "The delivery was super fast and the product is great!"}

response = requests.post(url, json=data)

print("Response from API:")
print(response.json())
