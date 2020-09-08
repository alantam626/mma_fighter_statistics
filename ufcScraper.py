import requests, bs4    #Importing Requests library and BeautifulSoup 4 scrapper

res = requests.get('http://www.ufcstats.com/fighter-details/cf946e03ba2e7666') #Requesting webdata
res.raise_for_status()  #Check for error, if error produce exception
KevinUFC = bs4.BeautifulSoup(res.text, "html.parser") #Create a BeautifulSoup object from the html text named kevin
fighterDetails = KevinUFC.select('div > ul > li') #Querying Kevin object and getting an iterable object (we can use a for loop on, almost like a list) with Kevin's info 

fighterDetailsList = [] #Creating an empty list
for info in fighterDetails: #For loop, iterating through the fighter details
	'''
	>>>test.contents
	['\n', <i class="b-listbox-item-title b-listbox-item-title_type_width">
	        Height:
	      </i>, '\n      5' 7"\n    ']
	'''
	strippedInfo = info.contents[2].strip() #Refer to lines 11-14. Index 0 and 1 not usable. Only 2 usable (5' 7") Stripped whitespace (new line and spaced included) 
	if strippedInfo != '': 					#This if statement will only non whitespace data to the list
		fighterDetailsList.append(strippedInfo) #This adds the information to the end of the list

res = requests.get('http://www.fightmatrix.com/fighter-profile/Kevin+Aguilar/58629/') #Requesting webdata
res.raise_for_status()  #Check for error, if error produce exception
KevinMatrix = bs4.BeautifulSoup(res.text, "html.parser") #Create a BeautifulSoup object from the html text named kevin
fighterDetails = KevinMatrix.select('.tdRank > div') #Querying Kevin object and getting an iterable object (we can use a for loop on, almost like a list) with Kevin's info 
for info in fighterDetails: #For loop, iterating through the fighter details
	fighterDetailsList.append(info.get_text().strip())
print(fighterDetailsList) #Print displays the current list
