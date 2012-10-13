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
	userNumber = (int (matchdict.get('userNumber', None)))
	queue.UserCenter.addListItem(userList[userNumber].library[id])
	return {"a":"a"}

@view_config(route_name='returnQueue', renderer='json')
def returnQueue(request):
	jsonqueue = json.dumps(queue.UserCenter.queueList)
	return {"queue":queue.UserCenter.queueList}

@view_config(route_name='login', renderer = 'gmusicuser.mak')
def myview(request):
	firstname = request.params['username']
	lastname = request.params['password']
	tempuser = User(firstname,lastname)
	userList.append(tempuser)
	userNumber = userList.index(tempuser)
	return {'items':userList[userNumber].library, 'username' : firstname, 'userNumber' : userNumber}