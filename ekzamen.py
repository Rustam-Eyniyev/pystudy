#1
def concat(*string, sep=' '):
    a = list(map(str, string))
    return sep.join(a)
  

    
    
#2    
from functools import reduce

def product_of_odds(data):
    result = reduce(lambda x, y: x * y,filter(lambda x: x % 2 == 1,data),1)
    return result
  
  



#3
words = 'the world is mine take a look what you have started'.split()

print(*list(map(lambda x: '"'+x+'"', words)))



#4
numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x) != str(x)[::-1], numbers))

  
#5  
numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, key = lambda x: sum(x)/ len(x), reverse = True)

print(sorted_numbers)


#6
def call(f, *args):
    return f(*args)


#7
def compose(f, g):
    return lambda x: f(g(x))

#8
from operator import *

def arithmetic_operation(operation):
    result = {'+': add, '-': sub, '*': mul, '/': truediv}
    return result[operation]

#9
i = input().split()
a = sorted(i, key = lambda x: x.lower())
print(*a)

#10
i= int(input())
p= list()
for j in range(i):
    a = input()
    p.append(a)
p = sorted(p)
p = sorted(p, key=(lambda word: sum([ord(i) - ord('A') for i in word.upper()])))
print(*p, sep = '\n')


#11
def sorter_key(some_list):
    return some_list[0]*(256**3) + some_list[1]*(256**2) + some_list[2]*(256**1) + some_list[3]*(256**0)
n = int(input())
list_of_ip = list()
for i in range(n):
    z = input().split('.')
    a = list(map(int, z))
    list_of_ip.append(a)
b = sorted(list_of_ip, key = sorter_key)
for el in b:
    print(*el, sep = '.')


#1
