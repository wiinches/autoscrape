import random
import itertools
import os
import socket
import subprocess
with open('./1msites/top-1m.txt', 'r')as f:
    myNames = [line.strip() for line in f]
    sites_list = list(myNames)
random.shuffle(sites_list,random.random)
print len(sites_list)
total_sites = len(sites_list)
dwn_number = raw_input("how many sites?: ")

download = sites_list[0:int(dwn_number)]
website = []
ipaddress = []
for i in download:
    print i
    website.append(i)
    ip = socket.gethostbyname(str(i))
    path = os.system("pwd")
    ipaddress.append(ip)
print(website, ipaddress)

for i in website:
    archive_name = i
    print i
    docker_run = str('docker run -itd --name %s ') % (i)
    docker_copy = str('docker cp ./%s/. %s:/usr/local/apache2/htdocs') % (i, archive_name)
    print(docker_copy)
    subprocess.call(["httrack", i, "-O", archive_name, i, "-r2"])
    for item in ipaddress:
        ipaddr = item
        print i
        docker_run2 = str('-p %s:8080:80 httpd') % (i)
        #use this to test locally
        #docker_run2 = str('-p 8080:80 httpd')
        container = (docker_run + docker_run2)
        print container
        os.system(container)
        os.system(docker_copy)
