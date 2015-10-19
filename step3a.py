
from pymongo import MongoClient
from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager


#flask框架初始化
app=Flask(__name__)
#pymongo驱动初始化
client=MongoClient()
db=client.test
#Bootstrap init
bootstrap=Bootstrap(app)
#Manager init
manager=Manager(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/weibo/count')
def weibo_count():

        dbcount=db.weibo.find().count()
        weibo_size=str(dbcount)
        message='The weibo message count:'+weibo_size
        return '<h1>'+message+'</h1>'

if __name__ =='__main__':
        manager.run()

