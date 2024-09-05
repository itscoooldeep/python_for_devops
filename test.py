text = "python is awsome"
length = len(text)
print("length is:", length)

## concat
str1 = "Hello"
str2 = "world"
result = str1 + "  " + str2
print(result)

##lowercase uppercase
text = "kuldeep is awsome"
uppercase = text.upper()
lowercase = text.lower()
print("uppercase:", uppercase)
print("lowercase:", lowercase)

###replace
text = "kuldeep is awsome"
new_text = text.replace("awsome","great")
print("modified text:", new_text)

##split func
word = text.split()
print("words:", word)

###strip func (removes spaces)
text = "      some spaces around    "
stripped_text = text.strip()
print("stripped text:", stripped_text)

## subtsting string
text = "kul is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")

##float
num1 = 5.0
num2 = 2.5

result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("subtraction:", result2)

result3 = num1 * num2
print("multiplication", result3)

result4 = num1 / num2
print("Division", result4)

## rounding
result5 = round(3.1459265359,2) #deminal will become 2 decimal
print("Rounded:", result5)

##integer var
num3 = 10
num4 = 5 

result6 = num3 // num4
print("integer division:", result6)
## modulus (remainder)
result7 = num3 % num4
print("modulos (reminder):", result7)
## absolute value
result8 = abs(-70)
print("absolute value:",result8)









