print ("What is your name?")
user = raw_input() ##Collect the user's name.
##I prefer this method because I like the spacing on the command line better when using print for the prompt and a blank input
print("\n Hello, {0} \n".format(user)) ##Greet the user. The '.format' tells the print command what goes in between the {} brackets.
print(" Your pig-latin name is {0}{1}-{2}ay \n".format((user.upper())[1],(user.lower())[2:],(user.lower())[0]))
##The above line prints the users name in pig latin.

while True: ##repeat everything below unless it reaches any one of the 'break' lines below which will instantly end the loop
	print ("Do you mind telling me what my name is?")
	my_name = raw_input()
	print ("\nSo my name is {0}?".format(my_name))
	answer = raw_input()
	answer_lower = str(answer.lower()) ##convert answer input into a lower case string, otherwise if statements below may not work
	if answer_lower in ('y','yes','yep','mhm') : ##if the answer is any one a of a variety of 'yes' answers, then proceed and break the while loop
		print ("\n I'm {0}. Nice to meet you, {1}! \n".format(my_name,user))
		break
	elif answer_lower in ('n','no','nope','nah') : ##if the answer is negative, then repeat the loop
		print ("\nOh, ok. Then let's try that again! \n")
		continue
	else:
		print ("\n Sorry, I didn't quite understand that answer. \n") ##if the answer is neither, then repeat the loop
		continue

 
while True: ##repeat everything below unless it reaches any one of the 'break' lines below which will instantly end the loop
	print ("Last question: what is your favorite color?")
	color0 = raw_input()
	color = str(color0) ##convert color input into a string, otherwise if statements below may not work
	if color.lower() == 'black' : ##if statement uses the lower() method so that the input is case insensitive
		print("\033[1;30;47m") ##change color of text to black, and background to light grey
		break
	elif color.lower() == 'red' :
		print("\033[1;31;47m") #change text to red, background to light grey
		break
	elif color.lower() == 'green' :
		print("\033[1;32;47m") #change text to green, background to light grey
		break
	elif color.lower() == 'yellow' :
		print("\033[1;33;47m") #change text to yellow, background to light grey
		break
	elif color.lower() == 'blue' :
		print("\033[1;34;47m") #change text to blue, background to light grey
		break
	elif color.lower() == 'purple' :
		print("\033[1;35;47m") #change text to purple, background to light grey
		break
	elif color.lower() == 'cyan' :
		print("\033[1;36;47m") #change text to cyan, background to light grey
		break
	elif color.lower() == 'white' :
		print("\033[1;37;40m") #change text to white, background to black
		break
	else: ##executes these steps if the answer is anything other than a valid color selection
		print("\n Sorry, the only options are black, red, green, yellow, blue, purple, cyan, and white (you'll see why) \n")
		continue ##return to the very beginning of the 'while True' loop
	
print("Dear {0},\n	Your command line is now {1} ;) happy coding!\n\n	Sincerely,\n	{2} \n".format(user,color,my_name))