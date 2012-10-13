from gmusicapi.api import Api

class User:
	def __init__(self, userName, password):
		self.library = []
		self.api = Api()
		self.api.login(userName, password)
		self.library = self.api.get_all_songs()

	def getLibItem(self, index):
		return library[index]

	def getLib(self):
		return library

	def sendStream(self, index):
		pass