Role Name
=========

Automation to build Zabbix cluster using Ansible playbook.
You can take this course to follow how to deploy Zabbix cluster and how to use github scripts.

https://www.udemy.com/course/draft/2871094/?referralCode=2F198B4E2606BE3DC11D

Requirements
------------

- Ubuntu 16.04 and CentOS 7 tested
- VMWare for Template (You can use for AWS/Azur/Alibaba Cloud)
- python Zabbix API

Tree
--------------
.
|-- README.md
|-- ansible_automation
|   |-- all_vars.yml
|   |-- host_inventory
|   |-- roles
|   |   |-- create_group
|   |   |   |-- README.md
|   |   |   |-- defaults
|   |   |   |   `-- main.yml
|   |   |   |-- handlers
|   |   |   |   `-- main.yml
|   |   |   |-- meta
|   |   |   |   `-- main.yml
|   |   |   |-- tasks
|   |   |   |   `-- main.yml
|   |   |   |-- tests
|   |   |   |   |-- inventory
|   |   |   |   `-- test.yml
|   |   |   `-- vars
|   |   |       `-- main.yml
|   |   |-- create_host
|   |   |   |-- README.md
|   |   |   |-- defaults
|   |   |   |   `-- main.yml
|   |   |   |-- handlers
|   |   |   |   `-- main.yml
|   |   |   |-- meta
|   |   |   |   `-- main.yml
|   |   |   |-- tasks
|   |   |   |   `-- main.yml
|   |   |   |-- tests
|   |   |   |   |-- inventory
|   |   |   |   `-- test.yml
|   |   |   `-- vars
|   |   |       `-- main.yml
|   |   |-- create_macros
|   |   |   |-- README.md
|   |   |   |-- defaults
|   |   |   |   `-- main.yml
|   |   |   |-- handlers
|   |   |   |   `-- main.yml
|   |   |   |-- meta
|   |   |   |   `-- main.yml
|   |   |   |-- tasks
|   |   |   |   `-- main.yml
|   |   |   |-- tests
|   |   |   |   |-- inventory
|   |   |   |   `-- test.yml
|   |   |   `-- vars
|   |   |       `-- main.yml
|   |   |-- create_mediatype
|   |   |   |-- README.md
|   |   |   |-- defaults
|   |   |   |   `-- main.yml
|   |   |   |-- handlers
|   |   |   |   `-- main.yml
|   |   |   |-- meta
|   |   |   |   `-- main.yml
|   |   |   |-- tasks
|   |   |   |   `-- main.yml
|   |   |   |-- tests
|   |   |   |   |-- inventory
|   |   |   |   `-- test.yml
|   |   |   `-- vars
|   |   |       `-- main.yml
|   |   `-- create_proxy
|   |       |-- README.md
|   |       |-- defaults
|   |       |   `-- main.yml
|   |       |-- handlers
|   |       |   `-- main.yml
|   |       |-- meta
|   |       |   `-- main.yml
|   |       |-- tasks
|   |       |   `-- main.yml
|   |       |-- tests
|   |       |   |-- inventory
|   |       |   `-- test.yml
|   |       `-- vars
|   |           `-- main.yml
|   `-- zabbix.yml
|-- ovftool
|   `-- create_ova.sh
`-- python_api
    |-- create_mediatype.py
    |-- create_user.py
    |-- create_usergroups.py
    `-- sample.py


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------
Muhammad Yusuf Efendi
myusufe@gmail.com

