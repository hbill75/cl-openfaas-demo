import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def handle(req):

    build_info = json.loads(req)

    url = "https://{}/dna/intent/api/v1/site?__runsync=true".format(build_info["hostname"])
    headers = {
        "Content-Type": "application/json",
        "x-auth-token": build_info["Token"]
        }

    site = requests.request("POST", url, data=json.dumps(build_info["payload"]), headers=headers, verify=False)
    # print(site.text)
    return site.text
