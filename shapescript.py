import sys

def interpret(code, stack = None):
	if stack == None:
		stack = ['' if sys.stdin.isatty() else sys.stdin.read()]

	tail_call = True

	while tail_call:
		if len(code) and code[-1] == '!':
			code = code[:-1]
		else:
			tail_call = False

		stringing = 0

		for char in code:
			quote = 1 + '\'\"'.find(char)

			if quote or stringing:
				if not stringing:
					string = ''
					stringing = quote
				elif stringing == quote:
					stack.append(string)
					stringing = 0
				else:
					string += char
			elif char in '0123456789':
				stack.append(int(char))
			else:
				x = stack.pop()

				if char == '!':
					interpret(x, stack)
				else:
					if char == '?':
						y = stack[~x]
					elif char == '_':
						y = len(x)
					else:
						y = stack.pop()

						if char == '@':
							stack.append(x)
						elif char == '$':
							y = y.split(x)
						elif char == '~':
							y = x.join(map(str, y))
						else:
							y = eval(repr(y) + char + repr(x))

					stack.append(y)

		if tail_call:
			code = stack.pop()

		return stack
