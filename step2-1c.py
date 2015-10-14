from pymongo import MongoClient
from flask import Flask

#flask框架初始化
app=Flask(__name__)
#pymongo驱动初始化
client=MongoClient()
db=client.test
dbcount=db.weibo.find().count()
#print(type(dbcount))
weibo_size=str(dbcount)
@app.route('/')
def index():
	message='The weibo message count:'+weibo_size
	return '<h1>'+message+'</h1>'
if __name__ =='__main__':
	app.run(host='0.0.0.0')	
