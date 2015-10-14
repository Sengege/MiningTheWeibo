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
	i=i+1
	if i>100:
		break
	
	try:	
		content.append(document['text'])
	except:
 		pass
	
	
weibo_size=str(len(content))
@app.route('/')
def index():
	message='The weibo message count:'+weibo_size
	return '<h1>'+message+'</h1>'
if __name__ =='__main__':
	app.run(host='0.0.0.0')	
