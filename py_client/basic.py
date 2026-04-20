import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/send/"

get_response = requests.post(endpoint, 
                    json={
                        "title": "Title #1",
                        "content": "Hello World",
                        "price": 11.11
                    })

print(get_response.status_code)

# HTTP Request returns html 
# REST API HTTP Request returns JSON (JavaScript Object Notation)
print(get_response.json())