
WHITESPACE = " \n\t"
to_the_power = False
to_the_power_count = 0



def is_equation(equ):
	raise NotImplementedError()


def parser(equ):
	# initialisation

	WHITESPACE = " \n\t"
	to_the_power = False
	to_the_power_count = 0
	temp = []
	temp1 = ""

	iter_count = 0
	equation = []

	# done initialisation

	if "=" in equ: # check if it is a equation
		is_equation(equ)
	
	for current_char in equ:
		if current_char in WHITESPACE or current_char == None:
			continue

		iter_count += 1
		equation.append(current_char)

		if current_char == "^" or to_the_power:
			to_the_power = True
			to_the_power_count += 1
			if to_the_power_count <= 1:
				continue
			else:
				if current_char != "(" and to_the_power_count == 2:
					print(f"\nSYNTAX ERROR: expected a \"(\" after \"{equation[-3]}\"")
					exit()
				else: # syntax is right so continue
					# current_char is still "(" so we restart
					if to_the_power_count == 2:
						continue
					
					if current_char == ")":

						# TODO change ^ to ** understanded by the eval function
						print(temp)
						temp = ''.join(map(str, temp))
						print(temp)
						temp1 = equ.index("^")
						print(equation)

						# done so reset all variables
						to_the_power_count = 0
						to_the_power = False
						temp = []
						temp1 = ""
						continue
					temp.append(current_char)

		
		#print(current_char)

		
		

	
	equation = ''.join(map(str, equation))
	answer = eval(str(equation))
	print(answer)

