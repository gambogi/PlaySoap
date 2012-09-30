from pyramid.view import view_config
from gmusicapi.api import Api

@view_config(route_name='home', renderer='mytemplatetest.mak')
def my_view(request):
	return {'project':'MyProject','string':'MyString'}

@view_config(route_name='tab', renderer='mytemplatetest.mak')
def testTabs(request):
	return {'project':'HerpDerp', 'string':'HerpString'}

@view_config(route_name='login', renderer = 'gmusic.mak')
def myview(request):
	print "FUCK FUCK FUCK"
	firstname = request.params['username']
	lastname = request.params['password']
	api = Api()
	api.login(firstname,lastname)
	idx = 0
	library = api.get_all_songs()
	for item in library:
		if (idx < 5):
			item["songURL"] = api.get_stream_url(item["id"])
			idx+=1
		else:
			break
#	api = login(firstname,lastname)
#	library = getLib(api)
#	print(library)
	
	return {'items':library}

def login(username,password):
	api = Api()
	if not api.is_authenticated():
		print ("failed to get api object")
		return False
	else:
		print("got api object")
		return api

def getLib(api):
	library = api.get_all_songs()
	if ((len(library))> 0):
		return library
	else:
		return false
