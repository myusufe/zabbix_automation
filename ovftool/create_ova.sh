#!/bin/sh

#
# Muhammad Efendi
# myusufe@gmail.com
# Akaicloud Technology Solution
#

vcenter_hostname='vcenter.akaicloud.com'
vcenter_username='admin2%40akaicloud.com'
vcenter_password='password123!'
vcenter_datacenter='Datacenter01'
template_folder_name='Template'
template_name='ubuntu1604_template_16GB'
ova_path='./'

ovftool \
--X:logFile=upload.log --X:logLevel=verbose --noSSLVerify --allowExtraConfig \
       --targetType=ova \
       "vi://$vcenter_username:$vcenter_password@$vcenter_hostname:443/$vcenter_datacenter/vm/$template_folder_name/$template_name" \
       $ova_path/$template_name.ova
