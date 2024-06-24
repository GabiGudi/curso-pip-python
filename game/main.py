import random

options = ("piedra", "papel", "tijera")

def choose_options():
	user_option = input("¿piedra, papel o tijera?")
	user_option = user_option.lower()

	if not user_option in options:
		print("Esa opcion no es valida")
		#continue
		return None, None
	computer_option = random.choice(options)

	print("User option => ", user_option)
	print("computer option => ", computer_option)
	return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
	if user_option == computer_option:
		print("¡¡Empate!!")

	elif user_option == "piedra":
		if computer_option == "tijera":
			print("Piedra gana a tijera")
			print("¡¡user ganó!!")
			user_wins +=1
		else:
			print("Papel gana a piedra")
			print("¡¡El computer ganó!!")
			computer_wins +=1
	elif user_option == "papel":
		if  computer_option ==  "piedra":
			print("Papel gana a piedra")
			print("¡¡user ganó!!")
			user_wins +=1
		else:
			print("Tijera gana a papel")
			print("¡¡El computer ganó!!")
			computer_wins +=1
	elif user_option == "tijera":
		if  computer_option == "papel":
			print("Tijera gana a papel")
			print("¡¡user ganó!!")
			user_wins +=1
		else:
			print("Piedra gana a tijera")
			print("¡¡El computer ganó!!")
			computer_wins +=1
	return user_wins, computer_wins


def run_game():
	computer_wins = 0
	user_wins = 0
	ronda = 0

	while True:
		ronda += 1
		print("*" * 10)
		print("ronda:", ronda)
		print("*" * 10)

		user_option, computer_option =  choose_options()
		user_wins, computer_wins =  check_rules(user_option, computer_option, user_wins, computer_wins)

		if computer_wins == 2:
			print("El ganador es la computer")
			break
		if user_wins == 2:
			print("El ganador es el user")
			break
run_game()