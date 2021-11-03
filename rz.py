# import httplib
import urllib3
import json

url = "http://192.168.2.231/"
with open('user.json', 'r') as f:
    data = json.load(f)

if __name__ == "__main__":
    print(data)
