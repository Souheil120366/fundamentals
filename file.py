# variables declarations
num1 = 42 
num2 = 2.3 
boolean = True 
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')

print(type(fruit)) # type check

print(pizza_toppings[1]) #output: 'Sausage'
pizza_toppings.append('Mushrooms') #add 'Mushrooms' at the end of pizza_toppings
print(person['name']) #output: value of property 'name' in person dict 'John'
person['name'] = 'George' #replace property value 'name' in dict with 'George' 
person['eye_color'] = 'blue' #add property 'eye_color' to dictionary person with 'blue' value 
print(fruit[2]) #output: 'banana'

if num1 > 45: #conditional if
    print("It's greater")
else: #conditional else
    print("It's lower")
    
if len(string) < 5: #conditional if,length check
    print("It's a short word!")
elif len(string) > 15: #conditional else if
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5): #for loop, start 0, stop 4, increment 1 
    print(x) #sequence : 0 -> 4
for x in range(2,5): #for loop, start 2, stop 5, increment 1
    print(x) #sequence : 2 -> 4
for x in range(2,10,3): #for loop, start 2, stop 10, increment 3
    print(x) #sequence : 2, 5, 8

   
x = 0
while(x < 5): # while loop, start 0, stop 4 
    print(x) #sequence: 0 -> 4
    x += 1 # increment 1

pizza_toppings.pop() #delete last item from pizza_toppings array 'Olives'
pizza_toppings.pop(1) #delete item indexed 1 from pizza_toppings array 'Sausage'

print(person) #output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') #delete 'eye_color' property from person dict

print(person) #output : {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings: #for loop start: first item in array, stop: last item in array
    if topping == 'Pepperoni': #conditional if
        continue #continue loop if condition satisfied
    print('After 1st if statement')
    if topping == 'Olives':  #conditional if
        break #break loop if condition satsified 

def print_hello_ten_times():
    for num in range(10): #for loop start 0, stop 9 
        print('Hello')

print_hello_ten_times() #output: 10 times 'Hello'

def print_hello_x_times(x):
    for num in range(x): #for loop start 0, stop x-1
        print('Hello') 

print_hello_x_times(4) #output 4 times 'Hello'

def print_hello_x_or_ten_times(x = 10): 
    for num in range(x): #for loop start 0, stop x-1 (here 9)
        print('Hello')

print_hello_x_or_ten_times() #output 10 times 'Hello'
print_hello_x_or_ten_times(4) #output 4 times 'Hello'


"""
Bonus section
"""

#print(num3) #output: NameError: name 'num3' is not defined
num3 = 72 # variable declaration
fruit[0] = 'cranberry' #output: TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) #output KeyError: 'favorite_team'
print(pizza_toppings[7]) #output: IndexError: list index out of range
print(boolean) #output: True
fruit.append('raspberry') #output: AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #output: AttributeError: 'tuple' object has no attribute 'pop'