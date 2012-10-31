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

@view_config(route_name='downvote', renderer='string')
def downvote(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	print("OMG")
	return {"a":"a"}

@view_config(route_name='upvote', renderer='string')
def upvote(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	if not queue.UserCenter.queueList[id]["upvotedby"]:
		print ("ADDED!")
	else:
		if not userNumber in queue.UserCenter.queueList[id]["upvotedby"]:
			queue.UserCenter.queueList[id]["upvotedby"].append(userNumber)
			queue.UserCenter.queueList[id]["upvote"] += 1
			queue.UserCenter.queueList[id]["totalvotes"] = queue.UserCenter.queueList[id]["upvote"] - queue.UserCenter.queueList[id]["downvote"]
			queue.UserCenter.sortList()
	print(queue.UserCenter.queueList[id]["upvotedby"])
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