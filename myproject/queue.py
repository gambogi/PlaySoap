class Queue:
	
	def __init__(self, queueName):
		self.queueList = []
		self.queueName = queueName
		print ("queueCREATED!")
	def getListItem(self, index):
		return self.queueList[index]
	def addListItem(self, item, uploadedby, service):
		item["uploadedby"] = uploadedby
		item["upvote"] = 0
		item["downvote"] = 0
		item["service"] = service
		upvote = [999]
		downvote = [999]
		item["upvotedby"] = upvote
		item["downvotedby"] = downvote
		item["totalvotes"] = 0
		self.queueList.append(item)
	def upvoteItem(self, index, amount):
		pass
	def downvoteItem(self, index, amount):
		pass
	def getList(self):
		pass
	def sortList(self):
		sorted(self.queueList,key = self.sort_key)
		print (self.queueList)
	def sort_key(self, row):
		return row["totalvotes"]

UserCenter = Queue("UserCenter")
Lounge = Queue("Lounge")