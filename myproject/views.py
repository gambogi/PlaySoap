from pyramid.view import view_config
import queue
from user import *
import json
import requests
import time
from threading import Thread

userList = []

# @view_config(route_name='home', renderer='loginpage.mak')
# def my_view(request):
# 	for i in request.headers:
# 		print(i)
# 	return {"a":"a"}

@view_config(route_name='login', renderer='json')
def login(request):
	username = request.params['username']
	password = request.params['password']
	tempuser = User(username,password)
	userList.append(tempuser)
	userNumber = userList.index(tempuser)
	return {'username' : username, 'userNumber' : userNumber}

@view_config(route_name='searchSpotify', renderer='json')
def searchSpotify(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	Queue = matchdict.get('queue', None)
	song = matchdict.get('song', None)
	print(song)
	print(song)
	print(song)

@view_config(route_name='returnLibrary', renderer='json')
def libraryUpdate(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	Queue = matchdict.get('queue', None)
	service = matchdict.get('service', None)
	if (service == "play"):
		return {"library":userList[userNumber].library}
	elif (service == "spotify"):
		pass

@view_config(route_name='addToAjaxQueue', renderer='string')
def ajaxQueue(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	Queue = matchdict.get('queue', None)
	service = matchdict.get('service', None)
	if (Queue == "lounge"):
		queue.Lounge.addListItem(userList[userNumber].library[id], userNumber, service)
		if (len(queue.Lounge.queueList) == 1):
			playSong(Queue, userNumber)
	elif (Queue == "userCenter"):
		queue.UserCenter.addListItem(userList[userNumber].library[id], userNumber, service)
		if (len(queue.UserCenter.queueList) == 1):
			playSong(Queue, userNumber)
	return {"a":"a"}

@view_config(route_name='downvote', renderer='string')
def downvote(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	return {"a":"a"}

@view_config(route_name='upvote', renderer='string')
def upvote(request):
	matchdict = request.matchdict
	songid = (int (matchdict.get('id', None)))
	userNumber = (int (matchdict.get('userNumber', None)))
	Queue = matchdict.get('queue', None)
	if (Queue == "lounge"):
		if not queue.Lounge.queueList[songid]["upvotedby"]:
			print ("ADDED!")
		else:
			if not userNumber in queue.Lounge.queueList[songid]["upvotedby"]:
				queue.Lounge.queueList[songid]["upvotedby"].append(userNumber)
				queue.Lounge.queueList[songid]["upvote"] += 1
				queue.Lounge.queueList[songid]["totalvotes"] = queue.Lounge.queueList[songid]["upvote"] - queue.Lounge.queueList[songid]["downvote"]
				queue.Lounge.sortList()
		print(queue.Lounge.queueList[songid]["upvotedby"])		
	elif (Queue == "userCenter"):
		if not queue.UserCenter.queueList[songid]["upvotedby"]:
			print ("ADDED!")
		else:
			if not userNumber in queue.UserCenter.queueList[songid]["upvotedby"]:
				queue.UserCenter.queueList[songid]["upvotedby"].append(userNumber)
				queue.UserCenter.queueList[songid]["upvote"] += 1
				queue.UserCenter.queueList[songid]["totalvotes"] = queue.UserCenter.queueList[songid]["upvote"] - queue.UserCenter.queueList[songid]["downvote"]
				queue.UserCenter.sortList()
		print(queue.UserCenter.queueList[songid]["upvotedby"])	
	return {"a":"a"}

@view_config(route_name='nextSong', renderer='string')
def timeSong(request):
	matchdict = request.matchdict
	id = (int (matchdict.get('id', None)))
	#userNumber = (int (matchdict.get('userNumber', None)))
	Queue = matchdict.get('queue', None)
	if (Queue == "lounge"):
		print("lounge")
		queue.Lounge.queueList.pop(0)
		if (len(queue.Lounge.queueList) > 0):
			userNumber = queue.Lounge.queueList[0]["uploadedby"]
			playSong(Queue, userNumber)
	elif (Queue == "userCenter"):
		print ("uc")
		queue.UserCenter.queueList.pop(0)
		if (len(queue.UserCenter.queueList) > 0):
			userNumber = queue.UserCenter.queueList[0]["uploadedby"]
			playSong(Queue, userNumber)
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	return {"a":"a"}


def playSong(Queue, userNumber):
	if (Queue == "lounge"):
		user = userList[userNumber]
		playid = queue.Lounge.queueList[0]["id"]
		startTime = queue.Lounge.queueList[0]["durationMillis"] // 1000
		songStream = user.api.get_stream_url(playid)
		print(songStream)
		payload = {"stream":songStream}
		r = requests.post('http://129.21.50.93:8081/play/', data=payload)
		print(r.text)
	elif (Queue == "userCenter"):
		user = userList[userNumber]
		playid = queue.UserCenter.queueList[0]["id"]
		startTime = queue.UserCenter.queueList[0]["durationMillis"] // 1000
		songStream = user.api.get_stream_url(playid)
		print(songStream)
		payload = {"stream":songStream}
		r = requests.post('http://129.21.50.217:8081/play/', data=payload)
		print(r.text)

@view_config(route_name='returnQueue', renderer='json')
def returnQueue(request):
	matchdict = request.matchdict
	userNumber = (int (matchdict.get('userNumber', None)))
	Queue = matchdict.get('queue', None)
	if (Queue == "lounge"):
		return {"queue":queue.Lounge.queueList}
	elif (Queue == "userCenter"):
		return {"queue":queue.UserCenter.queueList}

@view_config(route_name='home', renderer = 'gmusicuser.mak')
def myview(request):
	return {'a':'a'}
