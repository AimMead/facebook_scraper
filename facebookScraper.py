#!/usr/bin/python
#coding: utf-8
import time
import requests
import json
print("\t\t\t\t Coder -> Mostafa M. Mead")
print("[1] Get User Friends Id : ")
print("[2] Get Public Posts Likes Id : ")
print("[3] Scrape Birthdays And Emails And Phone Numbers")
myInput = input("Enter What Do You Want : ")
class facebookUserGrabber():
	def __init__(self, accessToken  , scrapingId , someFile):
		self.accessToken = accessToken
		self.scrapingId = scrapingId
		self.someFile = someFile
	def getIds(self):
		myRequest = "https://graph.facebook.com/{0}/friends?access_token={1}".format(self.scrapingId , self.accessToken)
		try:
			response = requests.get(myRequest , headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}).content
		except requests.exceptions.ConnectionError as e:
			print("Internet Error")
			pass
		myJson = json.loads(response)
		for i in (myJson.get("data")):
			myFile = open("ids.txt" ,'a+')
			myIds = i.get("id")
			print(myIds)
			myFile.write(str(myIds) + "\n")
			myFile.close()
		print("I Got ids , It Saved in ids.txt")
		time.sleep(150)
	def getIdFromPost(self):
		myRequest = "https://graph.facebook.com/{0}/likes?&access_token={1}".format(self.scrapingId , self.accessToken)
		try:
			response = requests.get(myRequest , headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}).content
		except requests.exceptions.ConnectionError as e:
			print("Internet Error")
			pass
		myJson = json.loads(response)
		try:
			for i in (myJson.get("data")):
				myFile = open("newids.txt" ,'a+')
				myIds = i.get("id")
				print(myIds)
				myFile.write(str(myIds) + "\n")
				myFile.close()
			print("I Got ids , It Saved in ids.txt")
			time.sleep(150)
		except Exception as e:
			print(e)
			time.sleep(1500)
	def startScript(self):
		with open(self.someFile) as f:
			lines = f.read().split("\n")
		for line in lines:
			myReq = "https://graph.facebook.com/{0}?fields=email,birthday,mobile_phone&access_token={1}".format(line , self.accessToken)		
			try:
				res = requests.get(myReq , headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}).content
			except requests.exceptions.ConnectionError as e:
				print("Internet Error")
				pass
			email = json.loads(res).get("email")
			if email == None:
				pass
			else:
				email = json.loads(res).get("email").replace("\u0040" , "@")
				print(email)
				emailFile = open("emails.txt" , 'a+')
				emailFile.write("{0}:{1}".format(email , line) + "\n")
				emailFile.close()
			birthday = json.loads(res).get("birthday")
			if birthday == None:
				pass
			else:
				birthdayFile = open("birthdays.txt" , 'a+')
				birthdayFile.write("{0}:{1}".format(birthday, line) + "\n")
				birthdayFile.close()
			number = json.loads(res).get("mobile_phone")
			if number == None:
				pass
			else:
				numberFile = open("number.txt" , 'a+')
				numberFile.write("{0}:{1}".format(number , line) + "\n")
				numberFile.close()
		print("Scrapped Done [+]")
if myInput == "1":
	myObject = facebookUserGrabber(input("Enter An Access Token : ") , input("Enter An Id : ") , None)
	myObject.getIds()
	print("Done")
elif myInput == "3":
	myObject = facebookUserGrabber(input("Enter Your Access Token : ") , None , input("Enter Your Ids File : "))
	myObject.startScript()
	print("Done")
elif myInput == "2":
	myObject = facebookUserGrabber(input("Enter Your Access Token : ") , input("Enter Scrapping Id : ") , None)
	myObject.getIdFromPost()

time.sleep(1000)