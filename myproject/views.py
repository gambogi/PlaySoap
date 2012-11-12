from pyramid.view import view_config
import queue
from user import *
import json
import requests
import time
from threading import Thread

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
	songid = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	if not queue.UserCenter.queueList[songid]["upvotedby"]:
		print ("ADDED!")
	else:
		if not userNumber in queue.UserCenter.queueList[songid]["upvotedby"]:
			queue.UserCenter.queueList[songid]["upvotedby"].append(userNumber)
			queue.UserCenter.queueList[songid]["upvote"] += 1
			queue.UserCenter.queueList[songid]["totalvotes"] = queue.UserCenter.queueList[songid]["upvote"] - queue.UserCenter.queueList[songid]["downvote"]
			queue.UserCenter.sortList()
	print(queue.UserCenter.queueList[songid]["upvotedby"])
	playSong(userNumber, songid)
	return {"a":"a"}

@view_config(route_name='nextSong', renderer='string')
def timeSong(request):
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	queue.UserCenter.queueList.pop(0)
	if (len(queue.UserCenter.queueList) > 0):
		playSong(0, 0)
	return {"a":"a"}


def playSong(userNumber, songid):
	user = userList[userNumber]
	playid = queue.UserCenter.queueList[songid]["id"]
	startTime = queue.UserCenter.queueList[songid]["durationMillis"] // 1000
	songStream = user.api.get_stream_url(playid)
	print(songStream)
	payload = {"stream":songStream}
	r = requests.post('http://129.21.50.217:8082/play/', data=payload)
	print("Start time is " + str(startTime))
	print(r.text)

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