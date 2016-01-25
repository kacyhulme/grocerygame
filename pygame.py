#This game will take you through the grocery store where you will
#be asked questions regarding your health and the subsequent food
#choices you should then make

# python 2

# to play: python pygame.py

from sys import exit

def choose_aisle():
	print "This is a slippery slope. There is a lot of processed food in these aisles."
	print "If you go down aisle 6, you will be in the cookie aisle."
	print "If you go down aisle 5, you will be in the canned foods aisle."
	print "Which aisle do you you want? Type 'cookies' for 'canned foods'."

	aisle = raw_input(">> ")

	if aisle == "cookies":
		print "Cookies make you fat"
		sure_and_sudden_death()

	elif aisle == "canned foods":
		print "Canned foods have a lot of sodium in them"
		sure_and_sudden_death()

	else: 
		"That is an inconclusive choice"
		exit_out()

def sure_and_sudden_death():
	print "Dude. You are gonna die a long and painful death with clogged arteries and an inability to poop."

def eternal_health():
	print "For making such great food choices, you are now eligible for the eternal life lottery!"
	print "Pick a number between 1-10 and see if you qualify."

	num = raw_input(">> ")

	if num.isdigit():
		lottery_num = int(num)
	else: 
		exit_out("You need to enter a number")

	if lottery_num == 5 or lottery_num == 7:
		print "YOU SHALL LIVE FOREVER!"
	elif lottery_num == 2 or lottery_num == 8:
		print "You just added 5 additional years of healthy living to your life!"
	elif lottery_num == 1 or lottery_num == 3:
		print "You have some seriously great health. People are saying that you glow!"
	elif lottery_num == 9 or lottery_num == 4:
		print "You're ripped! Do you lift? Jk, jk."
	elif lottery_num == 6:
		print "I'm sorry, despite your best efforts, it looks like your genes are just bad and your health is still terrible."
	else: 
		exit("Something isn't working")

def choose_produce():
	print "Great choice! This will lead you down a path of health."
	print "You are now in a sea of great choices. Anything you choose here with make you healthy and keep you young"
	print "You can earn maximum health depending on what you choose. Pick one from ",
	print "The following fruits and vegetables and receive points depending on the level of health of the item"
	print "Kale, spinach, carrots, potatoes, apples, oranges, bananas"

	food = raw_input(">> ")

	if food == "kale":
		print "Congrats! You earned 100 health points! Kale contains the most vitamins and minerals!"
		eternal_health()

	elif food == "spinach":
		print "Congrats! You earned 85 health points! Spinach contains the a lot of vitamins and minerals!"
		eternal_health()

	elif food == "carrots":
		print "Congrats! You earned 55 health points! Carrots contains the a lot of vitamins and minerals!"
		eternal_health()

	elif food == "Potatoes":
		print "Congrats! You earned 65 health points! Potatoes contains the a lot of vitamins and minerals!"
		eternal_health()

	elif food == "Apples":
		print "Congrats! You earned 50 health points! Apples contains the a lot of vitamins and minerals!"
		eternal_health()

	elif food == "Oranges":
		print "Congrats! You earned 70 health points! Oranges contains the a lot of vitamins and minerals!"
		eternal_health()

	elif food == "Bananas":
		print "Congrats! You earned 80 health points! Bananas contains the a lot of vitamins and minerals!"
		eternal_health()

	else: 
		exit_out("That is an inconclusive choice")

def exit_out(message):
	print message
	exit(0)

def start():
	print "Your health is in jeopordy if you don't make some changes... fast!"
	print "You are in the grocery store about ready to make some decisions about the",
	print "food you eat."
	print "You are at the front of the store. You can either 1) Go down an aisle or ",
	print "2) Go to the produce section"
	
	initial_choice = raw_input(">> ")
	if initial_choice.isdigit():
		number_choice = int(initial_choice)
	else: 
		exit_out("You need to enter a number")

	if number_choice == 1:
		choose_aisle()

	else:
		number_choice == 2
		choose_produce()

start()