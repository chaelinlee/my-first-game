from C3 import* 
from C1 import*
class CLController(object):
	DEALER_NAME = "Doh"
	def __init__(self,name):
		self.player = Process(name)
		self.dealer = Process(CLController.DEALER_NAME)

	def play(self):
		player = self.player
		dealer = self.dealer
		for __ in range(4):
			Show.show_card(player.card)
			pc = player.remove() #player 카드 한장 선택해서 내고 지운다.
			dc = dealer.computer_remove()	
			if pc > dc:
				print(player.name,"이 이겼습니다.")
				player.win()
			elif pc == dc:
				print("비겼습니다.")
			else:
				print(dealer.name,"이겼습니다.")
				dealer.win()
			print("현재상황은",player.name,":",player.score,dealer.name,":",dealer.score)

		if player.score > dealer.score:
			print(player.name,"이 최종적으로 이겼습니다.")
		elif player.score == dealer.score:
			print("비겼습니다.")
		else:
			print(dealer.name,"이 최종적으로 이겼습니다.")


def main():
	print("Welcome to Game World!")
	name = input("Enter your name: ")
	game = CLController(name)
	game.play()
	print("Bye! Never see you again. ")

main()

