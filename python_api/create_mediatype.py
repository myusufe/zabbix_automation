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

#
# Create Mediatype user
#

print("\nCreate mediatype user")
r = requests.post(zabbix_api_url,
    json = {
        "jsonrpc": "2.0",
        "method": "mediatype.create",
        "params": {
          "name": "Email-2",
          "type": 0,
          "smtp_server": "rootmail@company.com",
          "smtp_helo": "company.com",
          "smtp_email": "zabbix@company.com",
          "content_type": 1
         },
        "id": 2,
        "auth": AUTHTOKEN
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
