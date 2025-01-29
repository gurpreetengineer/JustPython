
# LAMBDA FUNCTION + HIGHER ORDER FUNCTION
def aFunc(newVal2):
	return lambda newVal = None: newVal2 + 200 # None defines optional argument for functions


x = lambda a, b, c: a + b + c()
print(x(5, 6, aFunc(2)));


def unknownArgsFunc(**doubleStar):
  return f'{doubleStar["keyIsMust"]} {doubleStar['ItBehavesLikeAnObjectNow']}';

print(unknownArgsFunc(keyIsMust = 'Because it is named args now and it is using \'=\' as default', ItBehavesLikeAnObjectNow = 'As We don\'t know how many args will be here.'));

# Positional arguments means DIRECT VALUES - THIS FUNCTION WON'T WORK
# def my_function(x, /):
#   print(x)

# my_function(x = 3)

# THIS WILL WORK. LOOK HOW WE GAVE DIRECT VALUE =====> `, /`
def my_function(x, /):
  print(x)

my_function(3)


# THIS WILL ALSO WORK
def my_function(x):
  print(x)

my_function(x = 33)


# OPPOSITE OF POSITIONAL ARGUMENTS: 
# 
# 
# 
# 	FUNCTIONAL ARGUMENTS ARE THE ONES WHERE YOU NEED TO SPECIFY ARGUMENT NAME. ======> `*, `
def my_function(*, x):
  print(x)

my_function(x = 3)


# COMBINATION OF BOTH AND NORMAL ARGUMENT
def my_function(a, b, /, f, g, *, c, d):
  print(a + b + c + d + f + g)

my_function(5, 6, 232, g = 500, c = 7, d = 8)

