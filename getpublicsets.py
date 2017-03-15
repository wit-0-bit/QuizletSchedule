import requests,time,pprint

setsrequest = requests.get('https://api.quizlet.com/2.0/users/wuzza_face/sets/?client_id=pyjFb2bnBN')
setsrequestjson = setsrequest.json()
titledateurl=([(item["title"],time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item["created_date"])),item["url"]) for item in setsrequestjson])
for item in titledateurl:
	print("Set Name: " + item[0])
	date,time = item[1].split()
	print("Date Created: " + date)
	print("Link: " + "https://www.quizlet.com" + item[2])
