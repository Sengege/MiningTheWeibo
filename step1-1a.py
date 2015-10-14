from pymongo import MongoClient
client=MongoClient()
db=client.test
cursor=db.weibo.find()
i=0
for document in cursor:
	i=i+1
	if i>100:
		break
	print(document)
#vim othersave w filename	
