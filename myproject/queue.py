from views import playsong

class Queue:
	
	def __init__(self, queueName, ipAddress):
		self.queueList = []
		self.queueName = queueName
		self.ipAddress = ipAddress
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
		print("SHIT SHIT SHIT GREAT GREAT GREAT")
		if(len(self.queueList) == 1):
			print("SHIT SHIT SHIT GREAT GREAT GREAT")
			playsong(self.queueName)


queueList = dict()
queueList["southside"] = Queue("southside", "http://129.21.50.61:8082/play/")
queueList["northside"] = Queue("northside", "http://129.21.49.166:8082/play/")