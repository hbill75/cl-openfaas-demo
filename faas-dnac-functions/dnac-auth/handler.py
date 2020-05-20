import requests
import base64
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def handle(req):
	
	req_body = json.loads(req)

	userAndPassword = req_body["username"] + ":" + req_body["password"]
	base64AuthString = base64.b64encode(userAndPassword.encode())
	
	payload = ""
	headers = {"Authorization": "Basic " + base64AuthString.decode("utf-8")}
	url = "https://{}/dna/system/api/v1/auth/token".format(req_body["hostname"])
	
	response = requests.request("POST", url, data=payload, headers=headers, verify=False)
	
	return response.text
