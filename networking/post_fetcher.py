import requests

class NetworkingException(Exception):
    pass

def fetchPost():
    try:
        request = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        return request.json()["title"]
    except:
        raise NetworkingException("Something went wrong")
