import random
q=0
num=random.randint(1,7)
while (True):
	if(q==6):
		print(f"You have failed to guess the answer after {q} attempts")
		break
	inp=int(input("Enter the Number?"))
	if(num==inp):
		print(f"You have guessed the right number i.e,{num} in {q+1} Attempt")
		break
	else:
		print("Try again!")
		q=q+1