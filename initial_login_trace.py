import requests
import xmltodict
import ipdb


log_response = requests.post(
    "http://10.1.10.5/nuova",
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data='<aaaLogin inName="ucspe" inPassword="ucspe"/>',
)

log_response.raise_for_status()
print(log_response.text)
log_output = xmltodict.parse(log_response.text)


ipdb.set_trace()


