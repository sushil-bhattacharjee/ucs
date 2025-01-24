# pylint: skip-file

import requests
import xmltodict
from rich import print

prefix = input("Enter the prefix/server name you want to create: ")
instances = input("Enter the number of instances you want to create: ")

log_response = requests.post(
    "http://10.1.10.5/nuova",
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data='<aaaLogin inName="ucspe" inPassword="ucspe"/>',
)

log_response.raise_for_status()
log_output = xmltodict.parse(log_response.text)
real_cookie = log_output["aaaLogin"]["@outCookie"]

payload = f"""
<lsInstantiateNTemplate
    dn="org-root/ls-SBtemplate"
    cookie="{real_cookie}"
    inTargetOrg="org-root"
    inServerNamePrefixOrEmpty="{prefix}"
    inNumberOf="{instances}"
    inHierarchical="no">
</lsInstantiateNTemplate>
"""

req_response = requests.post(
    "http://10.1.10.5/nuova",
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data=f"{payload}",
)

print(req_response.text)
req_response.raise_for_status()
req_output = xmltodict.parse(req_response.text)
looper = req_output["lsInstantiateNTemplate"]["outConfigs"]["lsServer"]

for server in looper:
    parse_template = server["@srcTemplName"]
    parse_name = server["@name"]
    parse_id = server["@intId"]
    print(
        f"Server {parse_name} has been created with (ID: {parse_id})"
        f"- based on template {parse_template}"
    )
