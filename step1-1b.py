from pymongo import MongoClient
client=MongoClient()
db=client.test
cursor=db.weibo.find()
i=0
for document in cursor:
	i=i+1
	if i>1:
		break
	print(type(document))
#document type is dict 类型为字典 也就是php中的关系数组
	print(document['text'])
	

#vim othersave w filename	
