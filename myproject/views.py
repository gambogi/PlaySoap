from pyramid.view import view_config
from user import *
import os
from mutagen import File
import queue
import requests

userList = dict()
serviceList = dict()
#penisNIS
@view_config(route_name='login', renderer='json')
def login(request):
	cshUserName = request.headers["X-Webauth-User"]
	username = request.params['username']
	password = request.params['password']
	tempUser = userList[cshUserName]
	tempUser.playLogin(username,password)
	return {'username' : username, 'userNumber' : 0}

@view_config(route_name='returnLibrary', renderer='json')
def libraryUpdate(request):
	cshUserName = request.headers["X-Webauth-User"]
	tempUser = userList[cshUserName]
	matchdict = request.matchdict
	queue = matchdict.get('queue', None)
	service = matchdict.get('service', None)
	if (service == "play"):
		return {"library":userList[cshUserName].playlibrary}
	elif (service == "hactar"):
		fileList = []
		rootdir="/home/jeid/hactar" + tempUser.cshHomeDirectory
		fileList = unix_find(rootdir)
		for songFile in fileList:
			song = File(songFile, easy=True)
			print song
			songDict = dict()
			songDict["album"] = song["album"][0]
			songDict["title"] = song["title"][0]
			songDict["artist"] = song["artist"][0]
			songDict["fileLocation"] = songFile
			tempUser.cshlibrary.append(songDict)
		return{"library":tempUser.cshlibrary}

@view_config(route_name='addToAjaxQueue', renderer='string')
def ajaxQueue(request):
	matchdict = request.matchdict
	cshUserName = request.headers["X-Webauth-User"]
	queueToAdd = matchdict.get('queue', None)
	service = matchdict.get('service', None)
	id = (int (matchdict.get('id', None)))
	# if (Queue == "lounge"):
	# 	queue.Lounge.addListItem(userList[userNumber].library[id], userNumber, service)
	# 	if (len(queue.Lounge.queueList) == 1):
	# 		playSong(Queue, userNumber)
	# elif (Queue == "userCenter"):
	# 	queue.UserCenter.addListItem(userList[userNumber].library[id], userNumber, service)
	# 	if (len(queue.UserCenter.queueList) == 1):
	# 		playSong(Queue, userNumber)
	if (service == "play"):
		queueBeingAdded = queue.queueList[queueToAdd]
		queueBeingAdded.addListItem(userList[cshUserName].playlibrary[id], cshUserName, service)
	elif (service == "hactar"):
		queueBeingAdded = queue.queueList[queueToAdd]
		queueBeingAdded.addListItem(userList[cshUserName].cshlibrary[id], cshUserName, service)
	return {"a":"a"}

def playsong(queueName):
	#have to work on pop.
	queueToPop = queue.queueList[queueName]
	queueSongList = queueToPop.queueList
	service = queueSongList[0]["service"]
	uploadedBy = queueSongList[0]["uploadedby"]
	if (service == "play"):
		songStream = userList[uploadedBy].api.get_stream_url(queueSongList[0]["id"])
		payload = {"stream":songStream}
		r=requests.post(queueToPop.ipAddress, data=payload)
		print(r.text)
		# print(songStream)
		# payload = {"stream":songStream}
		# r = requests.post('http://129.21.50.27:8081/play/', data=payload)
		# print(r.text)
	elif (service == "hactar"):
		print(uploadedBy)
		songStream = queueSongList[0]["fileLocation"]
		print(songStream)
		payload = {"stream":songStream}
		r=requests.post(queueToPop.ipAddress, data=payload)
		print(r.text)

@view_config(route_name='nextSong', renderer='string')
def timeSong(request):
	matchdict = request.matchdict
	queueToPop = matchdict.get('queue', None)
	queueDictPop = queue.queueList[queueToPop]
	queueSongList = queueDictPop.queueList
	queueSongList.pop(0)
	playsong(queueToPop)
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	print("START THREAD")
	return {"a":"a"}


@view_config(route_name='returnQueue', renderer='json')
def returnQueue(request):
	matchdict = request.matchdict
	queueToReturn = matchdict.get('queue', None)
	return {"queue":queue.queueList[queueToReturn].queueList}

def unix_find(pathin):
	"""Return results similar to the Unix find command run without options
	i.e. traverse a directory tree and return all the file paths
	"""
	fileList = []
	for r,d,f in os.walk(pathin):
		for files in f:
			if files.endswith('.mp3'):
				fileList.append(os.path.join(r,files))
			elif files.endswith('.m4a'):
				fileList.append(os.path.join(r,files))
			elif files.endswith('.flac'):
				fileList.append(os.path.join(r,files))

	return fileList

@view_config(route_name='home', renderer='home.mak')
def my_view(request):
	cshUserName = request.headers["X-Webauth-User"]
	cshHomeDirectory = request.headers["X-Webauth-Ldap-Homedirectory"]
	tempUser = User(cshUserName, cshHomeDirectory)
	userList[cshUserName] = tempUser
	return {'a':'a'}
