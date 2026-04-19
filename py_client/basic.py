import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, 
                    params={ 
                    },
                    json={
                        "query": "Hello World"
                    })

print(get_response.status_code)

# HTTP Request returns html 
# REST API HTTP Request returns JSON (JavaScript Object Notation)
print(get_response.json())