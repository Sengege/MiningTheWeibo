from pymongo import MongoClient
client=MongoClient()
db=client.test
cursor=db.weibo.find()

for document in cursor:

#document type is dict 类型为字典 也就是php中的关系数组
	try:	
		print(document['text'])
	except:
#如果没有text内容就输出它的ObjectId
		print('Waring :'+str(document['_id'])+'该ID无text内容')
	

#vim othersave w filename	
