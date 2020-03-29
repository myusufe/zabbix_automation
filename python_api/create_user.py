#!/usr/bin/env python

##
##  http://akaicloud.com
##  Muhammad Y efendi
##  myusufe@gmail.com
##
##

import requests
import json

#
# Zabbix server information
#
zabbix_api_url = "http://192.168.128.10/zabbix/api_jsonrpc.php"
zabbix_username = "automation"
zabbix_password = "password"

#
# Create Zabbix token
#
r = requests.post(zabbix_api_url,
    json = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": zabbix_username,
            "password": zabbix_password
        },
        "id": 1
    })

print(json.dumps(r.json(), indent = 4, sort_keys = True))
AUTHTOKEN = r.json()["result"]

# Get groupid of Zabbix
print("\nGet groupid of flowdock")
r = requests.post(zabbix_api_url,
                  json={
                        "jsonrpc": "2.0",
                        "method": "usergroup.get",
                        "params": {
                                "output": "extend",
                                "status": 0,
                                "filter": {
                                   "name": [
                                       "Operation managers"
                                   ]
                                }
                        },
                        "id": 2,
                        "auth": AUTHTOKEN
                  })

print(json.dumps(r.json(), indent=4, sort_keys=True))
GROUPID =r.json()["result"][0]["usrgrpid"]


#
# Create User
#

r = requests.post(zabbix_api_url,
    json = {
        "jsonrpc": "2.0",
        "method": "user.create",
        "params": {
        "alias": "John",
        "passwd": "Doe123",
        "usrgrps": [
            {
                "usrgrpid": GROUPID
            }
        ],
        "user_medias": [
            {
                "mediatypeid": "1",
                "sendto": [
                    "support@company.com"
                ],
                "active": 0,
                "severity": 63,
                "period": "1-7,00:00-24:00"
            }
        ]
    },
        "auth": AUTHTOKEN,
       "id": 1
})

print(json.dumps(r.json(), indent = 4, sort_keys = True))



#Logout user
print("\nLogout user")
r = requests.post(zabbix_api_url,
    json = {
        "jsonrpc": "2.0",
        "method": "user.logout",
        "params": {},
        "id": 2,
        "auth": AUTHTOKEN
    })

print(json.dumps(r.json(), indent = 4, sort_keys = True))
