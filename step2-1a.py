from pymongo import MongoClient
from flask import Flask

#flask框架初始化
app=Flask(__name__)
#pymongo驱动初始化
client=MongoClient()
db=client.test
cursor=db.weibo.find()
i=0
content=[]

for document in cursor:

#document type is dict 类型为字典 也就是php中的关系数组
	i=i+1
	try:	
		content.append(document['text'])
	except:
 		pass
	
	
print(len(content))
	
