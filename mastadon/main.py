import requests
import json

def foo ():
    response = requests.get("https://fosstodon.org/api/v1/timelines/public?limit=2")
    responseJson = json.loads(response.text)
    print (responseJson[0]["content"])
    


if __name__ == "__main__":
    foo()
    print ("hello world")