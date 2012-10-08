from gmusicapi.api import Api

class User:
	api = Api()
	library = []

	def __init__(self, userName, password):
		self.api.login(userName, password)
		self.library = self.api.get_all_songs()

	def getLibItem(self, index):
		return self.library[index]

	def getLib(self):
		return self.library