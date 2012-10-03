from pyramid.view import view_config
from gmusicapi.api import Api

@view_config(route_name='home', renderer='mytemplatetest.mak')
def my_view(request):
	return {'project':'MyProject','string':'MyString'}

@view_config(route_name='tab', renderer='gmusicuser.mak')
def testTabs(request):
	return {'project':'HerpDerp', 'string':'HerpString'}

@view_config(route_name='uc', renderer='gmusicuser.mak')
def uc(request):
	return {'abc':'cba'}


@view_config(route_name='login', renderer = 'gmusicuser.mak')
def myview(request):
	firstname = request.params['username']
	lastname = request.params['password']
	api = Api()
	api.login(firstname,lastname)
	idx = 0
	library = api.get_all_songs()
	queue = [library[1]]
	print (queue)
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
