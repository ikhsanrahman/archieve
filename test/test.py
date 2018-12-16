number = 23
running = True

while running :
	guess = int(input("Enter an Integer :"))

	if guess==number :
		print ('congratulations, you guessed it.')
		
	elif guess< number :
		print (' No, it is little higher than that')
	elif guess > number:
		print	('No, it is a little bigger than that')

	else:
		print ('the whole loop is over')
	break
print ('Done')