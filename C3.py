class Show(object):
	@staticmethod
	def show_card(card):
		print("당신이 가지고 있는 카드는")
		for c in card:
			print(c,end=" ")
		print("")
	@staticmethod
	def choose(card):
		ans = input("무엇을 내시겠습니까?")
		while not int(ans) in card:
			ans = input("무엇을 내시겠습니까?")
		return int(ans)




