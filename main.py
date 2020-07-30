from dmc import gettoken
import http.client
import json
import logging

logging.basicConfig(level=logging.DEBUG)

headers = {
    "X-CENTRIFY-NATIVE-CLIENT": "true",
    "X-CFY-SRC": "python",
    "Authorization": "Bearer %s" % gettoken("YOUR_SCOPE")
}
conn = http.client.HTTPSConnection("aaa0001-hk.my.centrify-dev.net")
conn.request("POST", "/security/whoami", headers = headers)
response = conn.getresponse()
print(response.status)
ret = json.loads(response.read().decode())
print(ret["Result"]["User"])