## One-liner, lambda, zip, enumerate
import numpy as np

## one-liner

# for loop
# long 
mlist = [] 
for i in range(10):
    mlist.append(i)

# one line
mmlist = [i for i in range(10)]
mmlist = [i**2+100 for i in range(20)]

# if
status = False
# long
if status:
    xvar = 5
else:
    xvar = 4
    
# one-line
yvar = 5 if status else 4
yvar = "a string" if isinstance("bayar",str) else "not a string"
# yvar = 5 if 5>6 else 4

# if else and for loop
# long
mlist = []
for i in range(10):
    if np.mod(i,2)==0:
        mlist.append(i)
    else:
        mlist.append(i-1)
print(mlist)

# one line
lst = [i if np.mod(i,2)==0 else i-1 for i in range(0,10)]
print(lst)


## lambda 

func = lambda a : a + 10
func(15)

lst = [i*2 if np.mod(i,2)==0 else (i-1)*2 for i in range(0,10)]
print(lst)

# filter
def pos(input1):
    return True if input1 > 0 else False

res = filter(pos,[1,-10,3,-7,4,-9])
res = list(filter(pos,[1,-10,3,-7,4,-9]))

def neg(input1):
    return False if input1 >0 else True

res = list(filter(neg,[1,-10,3,-7,4,-9]))

# lambda in filter
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_list = list(filter(lambda x: (x%2 == 0), my_list))
print(even_list)

odd_list = list(filter(lambda x: (x%2 != 0), my_list))
print(odd_list)

# map
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list)) # F C 32 +5/9*C
print(new_list)

# zip
list1 = range(0,10)
list2 = range(10,20)

for i in list1:
    for j in list2:
        print(i, j)

print(zip(list1, list2))

for i in zip(list1, list2):
    print(i)
    print("-----------------")


# enumerate

for value in list2:
    print(value)
for i, item in enumerate(list2):
    print(i, item)


    
for count, value in enumerate(['Maralmaa','Gerel','Batdelger']):
    print(count, value)


# assert
func_output = (lambda x : x*2 + 18)(5)
expected_output = 23

assert func_output == expected_output