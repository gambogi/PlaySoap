class Queue:
	queueList = []
	def __init__(self, queueName):
		self.queueName = queueName
		print ("queueCREATED!")
	def getListItem(self, index):
		return self.queueList[index]
	def addListItem(self, item):
		item["upvote"] = 0
		item["downvote"] = 0
		self.queueList.append(item)
	def upvoteItem(self, index, amount):
		pass
	def downvoteItem(self, index, amount):
		pass
	def getList(self):
		pass

UserCenter = Queue("UserCenter")
Lounge = Queue("Lounge")