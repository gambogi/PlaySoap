from gmusicapi import Webclient

class User:
	def __init__(self, cshUsername, cshHomeDirectory):
		self.cshlibrary = []
		self.cshUsername = cshUsername
		self.cshHomeDirectory = cshHomeDirectory

	def playLogin(self, username, password):
		self.api = Webclient()
		self.api.login(username, password)
		self.playlibrary = self.api.get_all_songs()
