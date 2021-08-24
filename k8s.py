#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print("Access-Control-Allow-Origin:*")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
o = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/kube_works/admin.conf")
print(o)
