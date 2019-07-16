''' Exercises
Problem 1: Write a function called 'intercept' that takes two lists and returns a list containing only the items common to both lists
Problem 2: Think about how function 'intercept' is different than or similar to creating a list from the intersection of two sets
    list(set(list_a)).intersection(list_b)
Problem 3: Without using zip, write a function that takes two lists and prints the values of each, separated by commas
Problem 4: How is 'pair' different from:  for (x,y) in zip(list_a, list_b): print "{0}, {1}".format(x,y)
'''

list1 = ['one', 'two', 'three', 'four']
list2 = ['two', 'five', 'six', 'one', 'eight']

# Problem 1
print ("########## Problem 1 ##########")

final_list = []

def intercept(l1, l2):
    for name in l1:
        if name in l2:
            final_list.append(name)
    print(*final_list)

intercept(list1, list2)

# Problem 2
'''
not sure?
'''

# problem 3
print ("###################### Problem 3 #########################")
min_list_length = min(len(list1), len(list2))
print(min_list_length)
def pair(a, b):
    for item in range(0, min_list_length):
        print("{0}, {1}".format(a[item], b[item]))

pair(list1, list2)


# Problem 4
print ("###################### Problem 4 #########################")
for (x,y) in zip(list1, list2): print("{0}, {1}".format(x,y))

##### Beyond Basics II: Error Handling and Files
#1
'''
  Given: pets = {'bird': 3.5, 'cat': 5.0, 'dog': 7.25, 'gerbil': 1.5}
  Ask user to enter a pet, and tell them the price.
  If an invalid pet is picked, tell the user nicely and try again.
'''
print ("#### Beyond Basics II: Error Handling and Files, Problem 1 ####")

pets = {'bird': 3.5, 'cat': 5.0, 'dog': 7.25, 'gerbil': 1.5}

# Continue prompting for pet until user types something valid
while True:
  inp = input("Enter a pet: ")
  if inp in pets:
    print("The price of a {0} is {1}".format(inp, pets[inp]))
    break
  else:
    print("That's not a valid pet, please try again!")

#2
'''
  Write a simple calculator that answers questions like:
  3+5
  8/2
  4*4
  18-36
  (include exception handling if user gives something invalid)
'''
print ("#### Beyond Basics II: Error Handling and Files, Problem 2 ####")

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

if operation not in ('+', '-', '*', '/'):
  print("Invalid operator!")
  exit()

try:
  num1 = int(input("Enter the first number: "))
except (ValueError, NameError):
  print("That's not a valid number!")
  exit()

try:
  num2 = int(input("Enter the second number: "))
except (ValueError, NameError):
  print("That's not a valid number!")
  exit()

if operation == '+':
  answer = num1 + num2
  print('{0} + {1} = {2}'.format(num1, num2, answer))
elif operation == '-':
  answer = num1 - num2
  print('{0} - {1} = {2}'.format(num1, num2, answer))
elif operation == '*':
  answer = num1 * num2
  print('{0} * {1} = {2}'.format(num1, num2, answer))
elif operation == '/':
  answer = num1 / num2
  print('{0} / {1} = {2}'.format(num1, num2, answer))
