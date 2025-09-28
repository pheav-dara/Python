# Type Error: len can not use number
print(123[0])

# Type Checking
print(type("123"))
print(type(123))
print(type(3.14159))
print(type(True))

# Type Converting
print(int("123") + int("345"))

# If you try convert the text it will get error 
print(int("abc"))

# You can convert 
int()
float()
str()
bool()

# Test
name_of_the_user = input("Enter your name:")
length_of_name = len(name_of_the_user)

# print(type(name_of_the_user)) #str
# print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))

