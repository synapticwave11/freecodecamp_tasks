
print("FCC stuff")

#Lists
Fruits = ["Apple", "Banana", "Cherry"]
print(Fruits[0]) #Apple
print(Fruits[1]) #Banana


#Tuples
Coordinates = (10.0, 20.0)
print(Coordinates[0]) #10.0
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
fruit= ["apple", "banana", "cherry"]
print(fruits[2]) #cherry

print("End of FCC stuff")


















    
