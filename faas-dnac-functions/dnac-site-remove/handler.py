import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def handle(req):

    remove_info = json.loads(req)

    site_details_url = "https://{}/dna/intent/api/v1/site?name={}".format(remove_info["hostname"], remove_info["siteNameHierarchy"])

    headers = {
                'x-auth-token': remove_info["Token"]
              }

    site_details = requests.request("GET", site_details_url, headers=headers, data=json.dumps(payload), verify=False)

    site_details_data = site_details.json()
    #print(site_id)

    site_object_id = site_details_data["response"]["id"]

    site_delete_url = "https://{}/dna/intent/api/v1/site/{}".format(remove_info["hostname"], site_object_id)
    
    site_delete_response = requests.request("DELETE", site_delete_url, headers=headers, data=json.dumps({}), verify=False)

    site_delete_response_data = site_delete_response.json()


