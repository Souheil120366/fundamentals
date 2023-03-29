def countdown (x):
    array=[]
    for i in range(x,-1,-1):
        array.append(i)
    return array

print(countdown(5))

def print_and_return (arr):
    print(arr[0])
    return arr[1]

print(print_and_return([1,2])) 
    
def first_plus_length (arr):
    return arr[0]+len(arr)    

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(arr):
    res=[]
    if len(arr) > 1 :
        for i in range(len(arr)):
            if arr[i] > arr[1]:
                res.append(arr[i])
        print(len(res))
    else:
        res=False
        
    return res

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value (length,value):
    arr=[]
    for i in range(length):
        arr.append(value)
    return arr

print(length_and_value(4,7))
print(length_and_value(6,2))