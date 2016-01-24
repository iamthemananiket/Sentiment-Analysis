from sys import argv
import urllib2
import json
import urlparse


readURL = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\playURL.txt", "r")

playstoreURL = readURL.read()

readURL.close()

result = urlparse.urlparse(playstoreURL)

newResult=result.query.split("=") 		##To trim the url

packageName = newResult[1]      # package com.whatsapp for WhatsApp
apiKey      = '67ebee3e33243c17ac63fd0b65307f34'  


url = 'http://api.playstoreapi.com/v1.1/apps/{0}?key={1}'

response = urllib2.urlopen(url.format(packageName, apiKey))

data = json.load(response)   ##Loads the received JSON object into python

##def getScore():
##	return data['score']

ls = data['topReviews']

target = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\pappName.txt", "w")
target.truncate()
target.write(data['appName'])

target = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\score.txt", "w")
target.truncate()
target.write(data['score'])

target=open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\preview.txt", "w")
target.truncate()


for i, test in enumerate(ls):
		target.write(test['reviewText'].encode("utf-8"))
		target.write("\n")

			
print 'Writing to file done!'		
target.close()
		
