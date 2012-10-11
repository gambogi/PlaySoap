from pyramid.view import view_config
import queue
from user import *
import json

userList = []

@view_config(route_name='home', renderer='loginpage.mak')
def my_view(request):
	return {'project':'MyProject','string':'MyString'}

@view_config(route_name='addToAjaxQueue', renderer='string')
def ajaxQueue(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	queue.UserCenter.addListItem(userList[0].library[id])
	print len(queue.UserCenter.queueList)
	return {"a":"a"}

@view_config(route_name='returnQueue', renderer='json')
def returnQueue(request):
	queue.UserCenter.addListItem(userList[0].library[1])
	jsonqueue = json.dumps(queue.UserCenter.queueList)
	print (jsonqueue)
	return {"queue":queue.UserCenter.queueList}

@view_config(route_name='login', renderer = 'gmusicuser.mak')
def myview(request):
	firstname = request.params['username']
	lastname = request.params['password']
	userList.append(User(firstname,lastname))
	return {'items':userList[0].library, 'username' : firstname}