

def is_equation(equ):
	raise NotImplementedError()

	for current_char in equ:
		pass


def parser(equ):
	# initialisation

	WHITESPACE = " \n\t"

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

		if current_char == "^":
			equation.pop(-1)
			equation.append("**")

		
		#print(current_char)

		
		

	
	equation = ''.join(map(str, equation))
	answer = eval(str(equation))
	print(answer)

