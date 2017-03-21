from C3 import*

import random
class Process(object):
	def __init__(self,name):
		self.name = name
		self.card = [1,2,3,4]
		self.score = 0

	def remove(self):
		delete = Show.choose(self.card)
		self.card.remove(delete)
		return delete

	def computer_remove(self):
		random.shuffle(self.card)
		ans2 = self.card[0]
		self.card.remove(self.card[0])
		return ans2

	def win(self):
		self.score += 1


