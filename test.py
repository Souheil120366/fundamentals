pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#pizza_toppings.pop(1)
pizza_toppings.append('Mushrooms')
print(pizza_toppings)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person['eye_color'] = 'blue'
person['name'] = 'George'
person.pop('eye_color')
print(person)
fruit = ('blueberry', 'strawberry', 'banana')
print(fruit[2])
pizza_toppings.pop() #delete last item from pizza_toppings array 'Olives'
pizza_toppings.pop(1)
print(pizza_toppings)
for topping in pizza_toppings: #for loop start: first item in array, stop: last item in array
    if topping == 'Pepperoni': #conditional if
        continue #continue loop if condition satisfied
    print('After 1st if statement')
    if topping == 'Olives':  #conditional if
        break #break loop if condition satsified 
    
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
        
#print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x): #for loop start 0, stop x-1
        print('Hello') 

#print_hello_x_times(4) #output 4 times 'Hello'

def print_hello_x_or_ten_times(x = 10): #output 10 times 'Hello'
    for num in range(x): #for loop start 0, stop 9
        print('Hello')

#print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

#print(num3)
num3 = 72
#fruit[0] = 'cranberry'
#print(person['favorite_team'])
boolean = True 
print(boolean)
#fruit.append('raspberry')
#fruit.pop(1)
print(type(fruit)) # type check