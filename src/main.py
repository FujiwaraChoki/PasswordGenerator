import random

def main():
	chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
	password = ""
	length = 0
	while True:
		strength = int(input("Please decide Password Strength (1-5): "))
		if strength == 1:
			length = 8
			break
		elif strength == 2:
			length = 12
			break
		elif strength == 3:
			length = 16
			break
		elif strength == 4:
			length = 20
			break
		elif strength == 5:
			length = 24
			break
		else:
			print("Please select a valid strength.")
	
	for i in range(length):
		password += random.choice(chars)
	
	print("Your password is: " + password)


if __name__ == '__main__':
	main()