import requests
import json

url = "http://192.168.2.231/srun_portal_pc.php?ac_id=1&"
with open('user.json', 'r') as f:
    data = json.load(f)

if __name__ == "__main__":
    # print(data)
    r = requests.post(url=url, data=data)
    print(r)
    requests.Response.ok(r)
