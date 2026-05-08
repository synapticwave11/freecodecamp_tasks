
print("FCC stuff")

#Lists
Fruits = ["Apple", "Banana", "Cherry"]
print(Fruits[0]) #Apple
print(Fruits[1]) #Banana


#Tuples
Coordinates = (10.0, 20.0)
print(Coordinates[0]) #10.0 #Tuples are immutable, meaning you cannot change their values after they are created.
print(Coordinates[1]) #20.0


#Dictionaries
Student = {"Name": "Aluu", 
           "Age":92, 
           "Marks": "97%"
}

print(Student["Age"])


#Sets
#NO DUPLICATES club
A= {8,4,6,0}
B= {6,9,0,3} #INTERSECTION
print(A & B) # {0, 6}


#Integers
my_integer_var= 11
print("Integer:", my_integer_var) #11


#Floats
my_float_var= 1.11 #integer with decimal point
print("Float:", my_float_var) #1.11

#Booleans(true or false)
my_boolean_var= True
print("Boolean:", my_boolean_var) #True

#example of boolean
username = "aluu"
password = "1234"

if username == "aluu" and password == "1234":
    print("Login successful")
else:
    print("Wrong credentials")

#Range
my_range_var = range(11) 
print("Range:", my_range_var) #range(0, 11) 

#example of range
for i in range(11):
    print(i)

#Indexing
fruits = ["apple", "banana", "cherry"] #acessing an item using its position
print(fruits[2]) #cherry

#String contatenation
first_name= "Alia"
Last_name= "Singh"
full_name= Last_name +"  " + first_name
print("Full Name:", full_name) #Singh Alia

#F strings
name= "ALU"
age= 18
print(f"My name is {name} and I am {age} years old.") #My name is ALU and I am 18 years old.

#another example of f string
temperature = 25
temperature_2= 10
print(f"The current tempreture is {temperature} but it feels like {temperature+temperature_2} degrees.") #The current tempreture is 25 but it feels like 35 degrees.


#String Splicing
my_string = "Hello, World!"
print(my_string[-3]) #l
print(my_string[0:5]) #Hello
print(my_string[7:12]) #World

# To specify the increment between each index in the slice, you can use a third parameter in the slice notation. For example, to get every second character from the string, you can do:
# Syntax:string[start:stop:step]
print(my_string[1:8:2]) #elo ol
print(my_string[7:4:-2]) #W,

#BUILT IN STRING METHODS:

#Uppercase, lowercase, replace

print(my_string.upper()) #HELLO, WORLD!
print(my_string.lower()) #hello, world!
print(my_string.replace("World", "Universe")) #Hello, Universe!

#Join and split
my_str= "Hello, World!"
split_words= my_str.split(", ") #['Hello', 'World!']
print(split_words) #['Hello', 'World!']

my_list = ['Hello', 'World!']
joined_my_str= ', '.join(my_list)
print(joined_my_str)

#Strip
text_1="helloooooossssh"
print(text_1.strip("h"))
#Varients
text= "whatyoudoingw"
print(text.lstrip("w"))
text_2= "wwnothinggsw"
print(text_2.rstrip("w"))

my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6

o_count = my_str.count('o')
print(o_count)




print("End of FCC stuff")

















    