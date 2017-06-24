#!/usr/bin/python3
# coding: UTF-8
import requests
import sys
argv = sys.argv[1:]
print (len(argv))
appno = argv[0]
apikey = argv[1]
title = argv[2]
body = argv[3]
url = argv[4]
if(len(argv)==5):
	r = requests.get("https://api.push7.jp/api/v1/"+appno+"/head").json()
	icon = r["icon"]
else:
	icon = argv[5]
data={
	"title":title,
	"body":body,
	"url":url,
	"icon":icon,
	"apikey":apikey
}
r=requests.post("https://api.push7.jp/api/v1/"+appno+"/send",json=data).json()
if(r.get("error")):
	print (r["error"])
	exit(1)
