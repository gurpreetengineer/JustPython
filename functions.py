
# LAMBDA FUNCTION + HIGHER ORDER FUNCTION
def aFunc(newVal2):
	return lambda newVal = None: newVal2 + 200 # None defines optional argument for functions


x = lambda a, b, c: a + b + c()
print(x(5, 6, aFunc(2)))