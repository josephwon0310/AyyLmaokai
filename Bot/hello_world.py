import zxlolbot

class helloworld(zxlolbot.zxLoLBoT):
	def __init__(self, username, password, region="NA"):
		zxlolbot.zxLoLBoT.__init__(self, username, password, region)
	@zxlolbot.botcommand
	def verifySummoner(self, sender):
		#print(sid)
		#Remove friend first
		self.remove_friend_by_name(sender);
		#Add friend
		self.add_friend_by_name(sender)
		#Create a random string

		#Send the string to user

		#self.add_friend_by_id('30860163)
		self.remove_friend_by_name(sender)
	
if __name__ == "__main__":
	bot = helloworld("leaguetutorbot", "bronze5bois")
	#bot = helloworld("joseph0310", "tmdwo0831") j0shl 33984703
	bot.connect()
	bot.verifySummoner("Silverhand Champ")