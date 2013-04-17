from gmusicapi.api import Api

class User:
	def __init__(self, cshUsername, cshHomeDirectory):
		self.cshlibrary = []
		self.cshUsername = cshUsername
		self.cshHomeDirectory = cshHomeDirectory

	def playLogin(self, username, password):
		self.api = Api()
		self.api.login(username, password)
		self.playlibrary = self.api.get_all_songs()