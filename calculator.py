import sys
num1 = 10
num2 = 5

addition = num1 + num2
print(addition)

sub = num1 - num2
print(sub)

##
#num3 = 10
#num4 = 5

def addition():
    add = num3 + num4
    return add

def sub():
    s = num3 - num4
    return sub

num3 = float(sys.argv[1])
operation = sys.argv[2]
num4 = float(sys.argv[3])

if operation == "add":
    output = add(num3,num4)
    print (output)