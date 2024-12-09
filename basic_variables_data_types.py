## STRINGS IN PYTHON
text1 = 'Alice'
text2 = 'is in Paris'

print(text1 + ' ' + text2) #this concat the first and second texts
print(len(text1)) #with 'len' we can get the lenght of the string
print(text1 + ' ' + text2[6:11]) #we can slice string on a range or specific position

## INTEGER IN PYTHON
integer1 = 5
integer2 = 6

print(integer1 + integer2)  # we can perform basic operations like sum
print(integer1 // integer2)  # division too (just integer part)

## FLOAT IN PYTHON
float1 = 5.5
float2 = 6.6

print(float1 + float2)  # with this type the decimal part is considered
print(float1 // float2)  # division too (integer and decimal part)

## BOOLEAN IN PYTHON
is_active = True
has_permission = False

if is_active & has_permission: # more conditionals
    print("Active with permission")
else:
    print("Active with no permission")

## CASTING IN PYTHON
num_int = 5 # integer value
print(num_int)

num_float = float(num_int) #this cast the integer to a float
print(num_float) # the output should include the decimal part

string_num = '10'
print(string_num)

integer_num_casted = int(string_num)
print(integer_num_casted)