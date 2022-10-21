

list1 = [1,2,3,4]
print("Before : ",list1, type(list1))
tup1 = tuple(list1)
print("After : ",tup1, type(tup1))


t1 = (10,43,2,532,53,64,24,25,53)
print("Iterate the tuple")
for each in t1:
    print(each)

le = len(t1)
for  ind in range(le):  # range(9)
    print(ind," : ",t1[ind])


# Find index of 64
t1 = (10, 43, 2, 532, 53, 64, 24, 25, 24, 10,  53, 10)

for ind in range(len(t1)):
    if t1[ind] == 64:
        print("Index is : ",ind)

print("Count : ", t1.count(10))

print("Index : ", t1.index(64))








#------------------------------------------------------------------------------------------------------------------
"""

											OOPs by me
											----------

-->the oop is a method of structuring a program by bundling related properties and behaviour into individual objects.
Conceptually objects are like the components of a system. an object contains the data.

what is oop in python:
----------------------
-->object oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviour are bundled into individual objects. 

-->For instance, an object could represent a person with properties like a name, age, an address and behaviour such as walking, talking, breathing and running. or it could represent an email with properties like recipient list, subject, and boy and behaviour like addding attachments and sending. 

-->put another way, object oriented programinning is an approach for modeling concete, real-world things, like cars, as well as relations between things, like companies and empolyees, students and teachers, and so on. oop models real-world entities as software object that have some data associated with them and can perfrom certain functions. 

-->another common programming paradigm is procedural programming, which strucutres a program like a recipe in that ti provides a set of steps, in the form of functions and code blocks, that flow sequentially in order to complete a task. 

-->the key takeaway is that objects are at the center of object-oriented programming in python, not only representing the data, as in procedural programming, but in the overall structure of the program as well. 

singleton classes:
------------------
-->Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code.

Define classes in python:
-------------------------
-->primitive data structures like numbers, and list are designed to represent simple pieces of information, such as the cost of an apple, the name of a poem, or you favotite colors, respectively. what if you want to represent something more complex ?

-->for example, let's say you want ot track employees in an organization. you need to store some basic information about each employee, such as thier name, age, position, and the year they started  working. 

One way to do this is to represent each employee as a list:

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

-->There are a number of issues with this approach.

1)First, it can make larger code files more difficult to manage. If you reference kirk[0] several lines away from where the kirk list is declared, will you remember that the element with index 0 is the employee’s name?

2)Second, it can introduce errors if not every employee has the same number of elements in the list. In the mccoy list above, the age is missing, so mccoy[1] will return "Chief Medical Officer" instead of Dr. McCoy’s age.

A great way to make this type of code more manageable and more maintainable is to use classes.


-------------------------------------------------------------------------------------------------------------

									class vs instance:
									------------------

classes are used to create user-defined data structures. classes define functions called 'methods', which identify the behaviour and actions that an object created from the class can perform with its data. 

-->a class is blueprint for how something should be defined. it don't actually contain any data. the dog class specifies that a name, and an age are necessary for defining a dog, but it doesn't contain the name or age of any specific dog. 

-->while the class is the blueprint, an instance is an object that is built from a class and contains real data, an instance of the dog class is not a blueprint anymore, its an actual dog with a name. 

Defining a class:
-----------------
-->all class definitions start with the class keyword, which is followd by name of the class and a colon. 

class Dog:
	pass

-->here the body of dog class consistes of a single statement : the pass keyword. 'pass' is often used as a placeholder indicating where code will eventually go, it allows you to run this code without python throwing the error. 

Note: Python class names are written in CapitalizedWords notation by convention. For example, a class for a specific breed of dog like the Jack Russell Terrier would be written as JackRussellTerrier.

-->The properties that all Dog objects must have are defined in a method called .__init__(). Every time a new Dog object is created, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.

-->You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. When a new class instance is created, the instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object.

-->Let’s update the Dog class with an .__init__() method that creates .name and .age attributes:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


-->Notice that the .__init__() method’s signature is indented four spaces. The body of the method is indented by eight spaces. This indentation is vitally important. It tells Python that the .__init__() method belongs to the Dog class.

-->In the body of .__init__(), there are two statements using the self variable:

1)self.name = name creates an attribute called name and assigns to it the value of the name parameter.

2)self.age = age creates an attribute called age and assigns to it the value of the age parameter.

-->Attributes created in .__init__() are called "INSTANCE ATTRIBUTES". An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.

-->On the other hand, "CLASS ATTRIBUTES" are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().


-->For example, the following Dog class has a class attribute called species with the value "Canis familiaris":

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


-->Class attributes are defined directly beneath the first line of the class name and are indented by four spaces. They must always be assigned an initial value. When an instance of the class is created, class attributes are automatically created and assigned to their initial values.

-------------------------------------------------------------------------------------------------------------

            					when to use class attributes and instance attribute:
            					----------------------------------------------------

-->Python class variables are declared within a class and their values are the same across all instances of a class. Python instance variables can have different values across multiple instances of a class. Class variables share the same value among all instances of the class.

-->Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one instance to another.


Instantiating object:
---------------------
-->class syntax : 

>>> class Dog:
...     pass


-->This creates a new Dog class with no attributes or methods.

-->Creating a new object from a class is called instantiating an object. You can instantiate a new Dog object by typing the name of the class, followed by opening and closing parentheses:

>>> Dog()
<__main__.Dog object at 0x106702d30>

-->You now have a new Dog object at 0x106702d30. This funny-looking string of letters and numbers is a memory address that indicates where the Dog object is stored in your computer’s memory. Note that the address you see on your screen will be different.

Now instantiate a second Dog object:

>>> Dog()
<__main__.Dog object at 0x0004ccc90>

-->To see this another way, type the following:

>>> a = Dog()
>>> b = Dog()
>>> a == b
False

-->In this code, you create two new Dog objects and assign them to the variables a and b. When you compare a and b using the == operator, the result is False. Even though a and b are both instances of the Dog class, they represent two distinct objects in memory.

-------------------------------------------------------------------------------------------------------------

    								Class and Instance Attributes:
    								------------------------------

-->Python class variables are declared within a class and their values are the same across all instances of a class. Python instance variables can have different values across multiple instances of a class. Class variables share the same value among all instances of the class.

-->Now create a new Dog class with a class attribute called .species and two instance attributes called .name and .age:

>>> class Dog:
...     species = "Canis familiaris"
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age


-->To instantiate objects of this Dog class, you need to provide values for the name and age. If you don’t, then Python raises a TypeError:

>>> Dog()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Dog()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'


-->To pass arguments to the name and age parameters, put values into the parentheses after the class name:

>>> buddy = Dog("Buddy", 9)
>>> miles = Dog("Miles", 4)

-->This creates two new Dog instances—one for a nine-year-old dog named Buddy and one for a four-year-old dog named Miles.

The Dog class’s .__init__() method has three parameters, so why are only two arguments passed to it in the example?

When you instantiate a Dog object, Python creates a new instance and passes it to the first parameter of .__init__(). This essentially removes the self parameter, so you only need to worry about the name and age parameters.

-->After you create the Dog instances, you can access their instance attributes using dot notation:

>>> buddy.name
'Buddy'
>>> buddy.age
9

>>> miles.name
'Miles'
>>> miles.age
4

-->You can access class attributes the same way:

>>> buddy.species
'Canis familiaris'

Note : for class variable, we can't access them outside of the class directly. we have to access them either by using the class name or by object of that class. for instance variables, we can't access them outside of the class directly. we can only access the instance variables using their object only. we can't access the instance variables using the class name. 

-------------------------------------------------------------------------------------------------------------

											Instance methods:
											-----------------


Features	class methods		Instance methods
--------    -------------       ----------------
Binding		Class				An instance of the class
Calling		Class.method()		object.method()
Accessing	Class attributes	Instance & class attributes

constructor:
------------
-->The constructor is a method that is called when an object is created. This method is defined in the class and can be used to initialize basic variables.

-->Instance methods are functions that are defined inside a class and can only be called from an instance of that class. Just like .__init__(), an instance method’s first parameter is always self. be default all the methods in the class are instance methods.
example:
--------
class HelloWorld(object):

    def __init__(self, message):
        self.message = message

    def display(self):
        print(self.message)

s1 = HelloWorld('hi')
s2 = HelloWorld('hello')
s3 = HelloWorld('whats up')

s1.display()
s2.display()
s3.display()


-->here the method display() is the instance method. the instance method is called with the object name and also it recievs the object name as it's first argument. we can also call the instance method directly with the constructor syntax. we can write the above program in another way : 
example:
--------
class HelloWorld(object):

    def __init__(self, message):
        self.message = message

    def display(self):
        print(self.message)

HelloWorld('hi').display()
HelloWorld('hello').display()
HelloWorld('whats up').display()

-->here with the constructor syntax, we created the object and passed value to the '__init__()' and called the method display(). but this is not a good practice. because this is called as the anonymous objects. we can't use them anywhere.


deleting the instance method:
-----------------------------
example:
--------
class HelloWorld(object):

    def __init__(self, message):
        self.message = message

    def display(self):
        print(self.message)    

s1 = HelloWorld('hi')
s2 = HelloWorld('hello')
s1.display()

#instance method accessable outside class
print(s1.display)
#but gives error while deleting using the instance
del s1.display
output:
-------
hi
<bound method HelloWorld.display of <__main__.HelloWorld object at 0x029CC640>>
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 13, in <module>
    del s1.display
AttributeError: display


-->Here the instance method is accessable outside the class and we know that. but here I deleted that instance method using the object name. it gave me error. so i tried it differently. see below : 
example:
--------
class HelloWorld(object):

    def __init__(self, message):
        self.message = message

    def display(self):
        print(self.message) 
    
s1 = HelloWorld('hi')
s2 = HelloWorld('hello')

#this deletes the reference to the function
del HelloWorld.display

#this raises the AttributeError
s2.display()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 14, in <module>
    s2.display()
AttributeError: 'HelloWorld' object has no attribute 'display'

 
-->here I deleted the instance method using the class name with syntax "del HelloWorld.display". but this statement don't give error, because the delete operation is successful. now the display() method which is connected to s1, s2 is gone. so if call the display method with one of object , it gives the error. 
-->there is another way to delete the instance method. delete the function reference directly in the class scope. see below : 
example:
--------
class HelloWorld(object):

    def __init__(self, message):
        self.message = message

    def display(self):
        print(self.message)

    # delete the reference
    del display
    
s1 = HelloWorld('hi')
s2 = HelloWorld('hello')

s2.display()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 14, in <module>
    s2.display()
AttributeError: 'HelloWorld' object has no attribute 'display'

-------------------------------------------------------------------------------------------------------------

											class method:
											-------------
NOTE : BETTER US THE @classmethod DECORATOR FOR CREATING CLASS METHODS. OTHERWISE, PYTHON TREATS THEM AS THE INSTANCE METHODS.

Features	class methods		Instance methods
--------    -------------       ----------------
Binding		Class				An instance of the class
Calling		Class.method()		object.method()
Accessing	Class attributes	Instance & class attributes

1)Python class methods aren’t bound to any specific instance, but classes. we can call the class method with the object.
2)Use @classmethod decorator to change an instance method to a class method. Also, pass the cls as the first parameter to the class method.
3)Use class methods for factory methods.

-->A class method is a method which is bound to the class and not the object of the class. They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance. It can modify a class state that would apply across all the instances of the class. 
-->for class methods, we call them using the class name and the class object also. 
example:
--------
class HelloWorld(object):

    message = 'hello world'

    def print_message(cls):
        print(cls.message)
        
HelloWorld.print_message()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 8, in <module>
    HelloWorld.print_message()
TypeError: print_message() missing 1 required positional argument: 'cls'

-->Normally class method takes the class name as the argument. but here it returns the error. But here we need to mention the method as the class method using the @classmethod decorator. see below : 
example:
--------
class HelloWorld(object):

    message = 'hello world'

    @classmethod
    def print_message(cls):
        print(cls.message)
        
HelloWorld.print_message()
output:
-------
hello world


-->we can access the class variable and the class method using the class object.
example:
--------
class HelloWorld(object):

    message = 'hello world'

    def __init__(self, name):
        self.name = name        

    @classmethod
    def print_message(cls):
        print(cls.message)
        
obj = HelloWorld('venkat')
obj.print_message()
output:
-------
hello world

-->here I called the static method with object and accessed the class variable with object. but the class method print_message() has no access to the instance attributes. see below : 
example:
--------
class HelloWorld(object):

    message = 'hello world'

    def __init__(self, name):
        self.name = name        

    @classmethod
    def print_message(self):
        print(self.name)
        
obj = HelloWorld('venkat')
#the below 2 lines gives the same error
obj.print_message()
HelloWorld.print_message()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 14, in <module>
    HelloWorld.print_message()
  File "C:\Users\this\Desktop\sample1.py", line 10, in print_message
    print(self.name)
AttributeError: type object 'HelloWorld' has no attribute 'name'


-->if you remember the internal structure of the decorator, then write the decorator @classmethod, in the old style. see below : 
example:
--------
class HelloWorld(object):

    message = 'hello world'

    def printname(cls):
        print(cls.message)

HelloWorld.printname = classmethod(HelloWorld.printname)
HelloWorld.printname()
output:
-------
hello world


example:
--------
class HelloWorld(object):

    message = 'hello world'

    @classmethod
    def printname():
        print('this is the static method')

HelloWorld.printname()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 10, in <module>
    HelloWorld.printname()
TypeError: printname() takes 0 positional arguments but 1 was given

-->this program is giving the error. the reason is the class method take the class name as the argument. but to recieve the class name as the argument, we didn't mention the parameter 'cls', to recieve the class name. see below program it don't give any error. 
example : 
---------
class HelloWorld(object):

    message = 'hello world'

    @classmethod
    def printname(cls):
        print('this is the class method')

HelloWorld.printname()
output:
-------
this is the class method

-------------------------------------------------------------------------------------------------------------

											static method
											-------------

NOTE : BETTER CREATE THE STATIC METHODS USING THE @staticmethod DECORATOR, OTHERWISE PYTHON TREATS THEM AS THE INSTANCE METHODS. 

Features	class methods		Instance methods
--------    -------------       ----------------
Binding		Class				An instance of the class
Calling		Class.method()		object.method()
Accessing	Class attributes	Instance & class attributes

-->A static method is also a method that is bound to the class and not the object of the class. A static method can't access or modify the class state. It is present in a class because it makes sense for the method to be present in class.

-->Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class. This also means that static methods cannot modify the state of an object as they are not bound to it. Let’s see how we can create static methods in Python.

creating static method:
-----------------------
class Calculate:   
    
    @staticmethod
    def addition(x,y):
        print('addition is : ', x + y)

Calculate.addition(10, 20)
output:
-------
addition is :  30

-->as we said earlier we can call the static method with class name. we can also call the static method with object also. see below : 
example:
--------
class Calculate:   

    @staticmethod
    def addition(x,y):
        print('addition is : ', x + y)

Calculate.addition(10, 20)

#calling the static method with object
c = Calculate()
c.addition(20, 30)
output:
-------
addition is :  30
addition is :  50


-->if you remember the internal mechanism of the decorators, use the old style decorators to create the static methods using the method "staticmethod()"
example : 
---------
class Calculate:   

    def addition(x,y):
        print('addition is : ', x + y)

Calculate.addition = staticmethod(Calculate.addition)
Calculate.addition(10, 20)
output:
-------
addition is :  30

-->instead of the addition() method, we can give any other names to store the return value of the staticmethod. see below : 
example :
---------
class Calculate:   

    def addition(x,y):
        print('addition is : ', x + y)

Calculate.add = staticmethod(Calculate.addition)
Calculate.add(10, 20)
output:
-------
addition is :  30

-->here the 'add' becomes the function variable and it points to the static method 'addition'.

NO ACCEES TO CLASS VARIABLES FOR STATIC METHOD:
-----------------------------------------------
-->the static method don't have the direct access to the class variables. see below : 
example :
---------
class Calculate:   

    message = 'hello'

    @staticmethod
    def addition():
        print('class variable is : ', message )

Calculate.addition()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 9, in <module>
    Calculate.addition()
  File "C:\Users\this\Desktop\sample1.py", line 7, in addition
    print('class variable is : ', message )
NameError: name 'message' is not defined


-->if you want to access the class variable inside the static method, just pass the class name as the argument to the static method and then access the class variable with the class name.
example : 
---------
class Calculate:   

    message = 'hello'

    @staticmethod
    def addition(cls):
        print('class variable is : ', cls.message )

Calculate.addition(Calculate)
output:
-------
class variable is :  hello


NO ACCEES TO INSTANCE VARIABLES FOR STATIC METHOD:
-----------------------------------------------
-->the static method don't have the direct access to the instance variables. see below : 
class Calculate:   

    message = 'hello'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def addition(self):
        print('class variable is : ', self.name )

c = Calculate('venkat')
c.addition()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 13, in <module>
    c.addition()
TypeError: addition() missing 1 required positional argument: 'self'

-->Here when I call the addition() method with the object c, the addition method didn't recieved it, even though it has the self in it's definition. the reason is the static method don't recieve the object or classname as it's first argument. we have to pass the object or class name explicitely. see below program : 
example : 
---------
class Calculate:   

    message = 'hello'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def addition(self):
        print('class variable is : ', self.name )

c = Calculate('venkat')
c.addition(c)
output:
-------
class variable is :  venkat

Advantages of Python static method:
-----------------------------------
-->Static methods have a very clear use-case. When we need some functionality not w.r.t an Object but w.r.t the complete class, we make a method static. This is pretty much advantageous when we need to create Utility methods as they aren’t tied to an object lifecycle usually.

-->Finally, note that in a static method, we don’t need the self to be passed as the first argument.


--------------------------------------------------------------------------------------------------------------
            
                                                Constructors
                                                ------------

-->The constructor is a method that is called when an object is created. this methid is defined in the class and can be used to initialize basic varaibles. 

-->if you create four objects, the class constructor is called four times. every class has a constructor, but it's not required to explicitly define it. 

-->the constructor always has the name 'init' and the name init is prefixed and suffixed with a double underscore(__). we declare a constructor using 'def' keyword, just like methods. we are calling this as constructor because this init also constructing the object attributes. 

def __ini__(self):
    #body of the constructor

-->usually we default constructor and parameterized constructor.


                                        default constructor:
                                        ---------------------

-->this constructor don't accept any arguments. an object can't to be created if don't have a constructor in our program. this is why when we don't declare a constructor in our program, python does it for us. let's have a look at the example below :

example:
--------
-->in this we don't have a constructor but still we are abble to create an object for the class. this is because there is a default constructor(__init__()) implicitly injected by python during program compilation, this is an empty default constructor that looks like this : 

class DemoClass:
    num = 101

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()
Output:
-------
101

-->python assumes the above program as below : 
example:
--------
class Demo():
    num = 101

    def __init__(self): #default constructor
        pass  #to perform generic action
    
    def read_number(self):
        print(self.num)


obj = Demo()

obj.read_number()

-->we create an object without arguments like obj = Demo(), we should not come to conclusion that, the constructor is a defualt constructor. because even though we didn't gave any argument during object creattion like obj = Demo(), the constructor might have the default parameters like below :

class Demo:
    num = 101

    def __init__(self, a = 10, b = 20, c = 30):
        self.a = a
        self.b = b
        self.c = c

-->so when every we see obj = Demo() kind of syntax, constructor can be parameterized or may be defualt. we have check and confirm. 


                                    parameterized constructor:
                                    --------------------------

-->this is a constructor with parameters.
-->When we declare a constructor in such a way that it accepts the arguments during object creation then such type of constructors are known as Parameterized constructors. As you can see that with such type of constructors we can pass the values (data) during object creation, which is used by the constructor to initialize the instance members of that object.

example:
--------
class DemoClass:
    num = 101

    # parameterized constructor
    def __init__(self, data):
        self.num = data

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)

# calling the instance method using the object obj
obj.read_number()

# creating another object of the class
obj2 = DemoClass(66)

# calling the instance method using the object obj
obj2.read_number()
Output:

55
66


                                        overloading a constructor:
                                        --------------------------


-->same like the methods, we can overload the constructors. but python don't support the method or constructor overloading. see below : 
example:
--------
class Demo():
    num = 101

    def __init__(self): #default constructor
        pass  #to perform generic action

    def __init__(self, a):
        self.a = a

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def read_number(self):
        print(self.num)

obj = Demo(10, 20)

obj.read_number()
output:
-------
101

-->here is I overloaded the costructor, it don't give any error. Python does not support method overloading like other languages. It will just replace the last defined function as the latest definition. Python doesn't support method overloading on the basis of different number of parameters in functions. We can however try to achieve a result similar to overloading using *args or using an optional arguments. see the below gets the error : 
example:
--------
class Demo():
    num = 101

    def __init__(self): #default constructor
        pass  #to perform generic action

    def __init__(self, a):
        self.a = a

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __init__(self,a):
        self.a = a
    
    def read_number(self):
        print(self.num)

obj = Demo(10, 20)

obj.read_number()
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 20, in <module>
    obj = Demo(10, 20)
TypeError: __init__() takes 2 positional arguments but 3 were given

-->here when obj = Demo(10, 20) is executed, it goes to the last __init__() definition which takes only one argument. so it raises the error.

constructor overloading with default parameters:
------------------------------------------------
-->we can achieve the constructor overloading using the default parameters. see below : 

example:
---------
class Demo():
    num = 101

    def __init__(self, a = 10, b = 20):
        self.a = a
        self.b = b
    
    def read_number(self):
        print(self.a, self.b)

obj = Demo(20)
obj.read_number()

obj1 = Demo(10, 20)
obj1.read_number()

obj2 = Demo()
obj2.read_number()
output:
-------
20 20
10 20
10 20

-->here constructor can be invoked in 3 different ways. that means we are able to call the same constructor in 3 ways. this is called constructor polymorphism.


-------------------------------------------------------------------------------------------------------------


                                            Encapsulation
                                            -------------

-->Encapsulation in Python is the process of wrapping up variables and methods into a single entity.In programming, a class is an example that wraps all the variables and methods defined inside it.

-->When working with classes and dealing with sensitive data, providing global access to all the variables used within the program is not a good choice. Encapsulation offers a way for us to access the required variables without providing the program full-fledged access to any of those variables.

-->Updating, modifying, or deleting data from variables can be done through the use of methods that are defined specifically for the purpose. The benefit of using this approach to programming is improved control over the input data and better security.

-->The concept of encapsulation is the same in all object-oriented programming languages. The difference is seen when the concepts are applied to particular languages.

-->Compared to languages like Java that offer access modifiers (public or private) for variables and methods, Python provides access to all the variables and methods globally.

-->Check the below demonstration of how variables can easily be accessed.
example:
--------
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
 
    def display(self):
        print(self.name)
        print(self.age)
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#accessing directly from outside
print(person.name)
print(person.age)
output:
-------
Dev
30
Dev
30

-->There are multiple methods that are offered by Python to limit variable and method access across the program. Let’s go over the methods in detail.

Using Single Underscore:
------------------------
-->A common Python programming convention to identify a private variable is by prefixing it with an underscore. Now, this doesn’t really make any difference on the compiler side of things. The variable is still accessible as usual. But being a convention that programmers have picked up on, it tells other programmers that the variables or methods have to be used only within the scope of the class.

See the below example:

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age
 
    def display(self):
        print(self.name)
        print(self._age)
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#accessing directly from outside
print(person.name)
print(person._age)
Output:
------
Dev
30
Dev
30

-->It’s clear that the variable access is unchanged. But can we do anything to really make it private? Let’s have a look further.

Using Double Underscores:
-------------------------
-->If you want to make class members i.e. methods and variables private, then you should prefix them with double underscores. But Python offers some sort of support to the private modifier. This mechanism is called Name mangling. With this, it is still possible to access the class members from outside it.

Name Mangling:
--------------
-->In Python, any identifier with __Var is rewritten by a python interpreter as _Classname__Var, and the class name remains as the present class name. This mechanism of changing names is called Name Mangling in Python.

-->In the below example, in Class person, the age variable is changed and it’s prefixed by leading double underscores.

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def display(self):
        print(self.name)
        print(self.__age)
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#accessing directly from outside
print('Trying to access variables from outside the class ')
print(person.name)
print(person.__age)
Output:
-------
Dev
30
Trying to access variables from outside the class
Dev
Traceback (most recent call last):
  File "Person.py", line 16, in <module>
    print(person.__age)
AttributeError: 'Person' object has no attribute '__age'

-->You can observe that variables are still be accessed using methods, which is a part of the class. But you cannot access age directly from outside, as it is a private variable.


Using Getter and Setter methods to access private variables:
------------------------------------------------------------
example:
--------
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def display(self):
        print(self.name)
        print(self.__age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
        
 
person = Person('Dev', 30)
print('age is : ', person.age)
person.age = 20
print('age is : ',person.age)

-->here to access the private variable __age, I created the property object age and I write some getter and setter methods to access and modify the __age attribute. this is not a good idea to access the private variable. age should be the positive value. but if we gave the permission someone could make it as negative value. this is where the private variables are helpful.


Benefits of Encapsulation in Python:
------------------------------------
-->Encapsulation not only ensures better data flow but also protects the data from outside sources. The concept of encapsulation makes the code self-sufficient. It is very helpful in the implementation level, as it prioritizes the ‘how’ type questions, leaving behind the complexities. You should hide the data in the unit to make encapsulation easy and also to secure the data.

What is the need for Encapsulation in Python:
---------------------------------------------
-->The following reasons show why developers find the Encapsulation handy and why the Object-Oriented concept is outclassing many programming languages.

-->Encapsulation helps in achieving the well-defined interaction in every application.
1)The Object-Oriented concept focuses on the reusability of code in Python. (DRY – Don’t Repeat Yourself).
2)The applications can be securely maintained.
3)It ensures the flexibility of the code through a proper code organization.
4)It promotes a smooth experience for the users without exposing any back-end complexities.
5)It improves the readability of the code. Any changes in one part of the code will not disturb another.
6)Encapsulation ensures data protection and avoids the access of data accidentally. The protected data can be accessed with the methods discussed above.
7)Encapsulation in Python is, the data is hidden outside the object definition. It enables developers to develop user-friendly experience. This is also helpful in securing data from breaches, as the code is highly secured and cannot be accessed by outside sources.

-------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------


                                        Inheritance and composition
                                        ---------------------------


Inheritance:
------------
-->The process of inheriting the properties of the parent class into a child class is called inheritance. The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.

-->In this Python lesson, you will learn inheritance, method overloading, method overriding, types of inheritance, and MRO (Method Resolution Order).

-->In Object-oriented programming, inheritance is an important aspect. The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class instead of creating it from scratch.

-->In inheritance, the child class acquires all the data members, properties, and functions from the parent class. Also, a child class can also provide its specific implementation to the methods of the parent class.

-->For example, In the real world, Car is a sub-class of a Vehicle class. We can create a Car by inheriting the properties of a Vehicle such as Wheels, Colors, Fuel tank, engine, and add extra properties in Car as required.

Syntax:
-------
class BaseClass:
  Body of base class

class DerivedClass(BaseClass):
  Body of derived class


Types Of Inheritance:
---------------------
-->In Python, based upon the number of child and parent classes involved, there are five types of inheritance. The type of inheritance are listed below:

1)Single inheritance
2)Multiple Inheritance
3)Multilevel inheritance
4)Hierarchical Inheritance
5)Hybrid Inheritance


Single Inheritance:
-------------------
-->In single inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.

Example:
--------
-->Let’s create one parent class called ClassOne and one child class called ClassTwo to implement single inheritance.

# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()

Output:
------
Inside Vehicle class
Inside Car class


Multiple Inheritance:
---------------------
-->In multiple inheritance, one child class can inherit from multiple parent classes. So here is one child class and multiple parent classes.

Example:
--------
# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')
Output:
--------
Inside Person class
Name: Jessa Age: 28

Inside Company class
Name: Google location: Atlanta

Inside Employee class
Salary: 12000 Skill: Machine Learning

-->In the above example, we created two parent classes Person and Company respectively. Then we create one child called Employee which inherit from Person and Company classes.


Multilevel inheritance:
-----------------------
-->In multilevel inheritance, a class inherits from a child class or derived class. Suppose three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B. In other words, we can say a chain of classes is called multilevel inheritance.

Example:
--------
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()

Output:
-------
Inside Vehicle class
Inside Car class
Inside SportsCar class

-->In the above example, we can see there are three classes named Vehicle, Car, SportsCar. Vehicle is the superclass, Car is a child of Vehicle, SportsCar is a child of Car. So we can see the "chaining of classes".



Hierarchical Inheritance:
--------------------------
-->In Hierarchical inheritance, more than one child class is derived from a single parent class. In other words, we can say one parent class and multiple child classes.

Example:
--------
-->Let’s create ‘Vehicle’ as a parent class and two child class ‘Car’ and ‘Truck’ as a parent class.

class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)

class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)

obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')
Output:
-------

This is Vehicle
Car name is: BMW

This is Vehicle
Truck name is: Ford


Hybrid Inheritance:
-------------------
-->When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.

Example:
--------
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()

Note:
-----
-->In the above example, hierarchical and multiple inheritance exists. Here we created, parent class Vehicle and two child classes named Car and Truck this is hierarchical inheritance.

-->Another is SportsCar inherit from two parent classes named Car and Vehicle. This is multiple inheritance.


Python super() function:
------------------------
-->When a class inherits all properties and behavior from the parent class is called inheritance. In such a case, the inherited class is a subclass and the latter class is the parent class.

-->In child class, we can refer to parent class by using the super() function. The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method.

Benefits of using the super() function:
---------------------------------------
1)We are not required to remember or specify the parent class name to access its methods.
2)We can use the super() function in both single and multiple inheritances.
3)The super() function support code reusability as there is no need to write the entire function
Example:
--------
class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()

Output:
-------
Jessa works at Google

-->In the above example, we create a parent class Company and child class Employee. In Employee class, we call the parent class method by using a super() function.


issubclass():
------------- 
-->In Python, we can verify whether a particular class is a subclass of another class. For this purpose, we can use Python built-in function issubclass(). This function returns True if the given class is the subclass of the specified class. Otherwise, it returns False.

Syntax:
-------
issubclass(class, classinfo)
Where,

class: class to be checked.
classinfo: a class, type, or a tuple of classes or data types.

Example:
--------
class Company:
    def fun1(self):
        print("Inside parent class")

class Employee(Company):
    def fun2(self):
        print("Inside child class.")

class Player:
    def fun3(self):
        print("Inside Player class.")

# Result True
print(issubclass(Employee, Company))

# Result False
print(issubclass(Employee, list))

# Result False
print(issubclass(Player, Company))

# Result True
print(issubclass(Employee, (list, Company)))

# Result True
print(issubclass(Company, (list, Company)))


Method Overriding:
------------------
-->In inheritance, all members available in the parent class are by default available in the child class. If the child class does not satisfy with parent class implementation, then the child class is allowed to redefine that method by extending additional functions in the child class. This concept is called method overriding.

-->When a child class method has the same name, same parameters, and same return type as a method in its superclass, then the method in the child is said to override the method in the parent class.

Example:
--------
class Vehicle:
    def max_speed(self):
        print("max speed is 100 Km/Hour")

class Car(Vehicle):
    # overridden the implementation of Vehicle class
    def max_speed(self):
        print("max speed is 200 Km/Hour")

# Creating object of Car class
car = Car()
car.max_speed()

Output:
-------
max speed is 200 Km/Hour

-->In the above example, we create two classes named Vehicle (Parent class) and Car (Child class). The class Car extends from the class Vehicle so, all properties of the parent class are available in the child class. In addition to that, the child class redefined the method max_speed().


                                Method Resolution Order in Python:
                                -----------------------------------
                                
-->In Python, Method Resolution Order(MRO) is the order by which Python looks for a method or attribute. First, the method or attribute is searched within a class, and then it follows the order we specified while inheriting.

-->This order is also called the Linearization of a class, and a set of rules is called MRO (Method Resolution Order). The MRO plays an essential role in multiple inheritances as a single method may found in multiple parent classes.

-->In multiple inheritance, the following search order is followed.

-->First, it searches in the current parent class if not available, then searches in the parents class specified while inheriting (that is left to right.)
We can get the MRO of a class. For this purpose, we can use either the mro attribute or the mro() method.
Example:
--------
class A:
    def process(self):
        print(" In class A")

class B(A):
    def process(self):
        print(" In class B")

class C(B, A):
    def process(self):
        print(" In class C")

# Creating object of C class
C1 = C()
C1.process()
print(C.mro())
# In class C
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

-->In the above example, we create three classes named A, B and C. Class B is inherited from A, class C inherits from B and A. When we create an object of the C class and calling the process() method, Python looks for the process() method in the current class in the C class itself.

-->Then search for parent classes, namely B and A, because C class inherit from B and A. that is, C(B, A) and always search in left to right manner.

Overriding the attributes:
--------------------------
-->One of the core purposes of a subclass is to change the behavior of the parent class in some useful way. We call this overriding the inherited behavior. Overriding attributes of a parent class in Python is as simple as creating a new attribute with the same name:
example:
--------
class Circle(object):
    color = 'red'

class New_Circle(Circle):
    #modifying the super class's variable
    color = 'blue'

nc = New_Circle()
print(nc.color)
output:
-------
blue

-->we can access the super class's class varaiable and can also modify it using the sub class's object. but we can't access and modify the super class's instance attribute using the sub class's object.
example:
--------
class vehicle():

    vehicle_name = 'benz'

    def __init__(self):
        self.a = 10
        self.b = 20

    def vehicle_info(self):
        print('inside the vehicle class')

class car(vehicle):

    def __init__(self):
        pass

    def car_info(self):
        print('inside the car class')

v = vehicle()
c = car()
#super class's variable is accessable
print(c.vehicle_name)
#super class's instance attributes are not accessable
print(c.a)
output:
-------
10
benz
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 25, in <module>
    print(c.a)
AttributeError: 'car' object has no attribute 'a'


Overriding methods:
--------------------
-->Overriding methods works in exactly the same way (remember, a method is an attribute in python).
example:
--------
import math

class Circle():

    def __init__(self):
        self.diameter = 10

    def grow(self, factor = 2):
        self.diameter = self.diameter * factor
        print(self.diameter)


class NewCircle(Circle):

    def grow(self, factor = 2):
        self.diameter = self.diameter * math.sqrt(2)
        print(self.diameter)

c = Circle()
c.grow()
n = NewCircle()
n.grow()
        
-->Instances of the new circle class will have the new behavior for the grow method. Instances of the existing class will continue to have the old behavior.

-->When overriding behavior for a subclass, remember that in good OO programming a subclass should be substantially similar to its parents. If you have a system which uses the parent class, you should be able to use the subclass in all the same places, and in all the same ways. This is known as the “Liskov Substitution Principle”. The authors of Think Python put it this way:

note:
-----
-->whenever you override a method, the interface of the new method should be the same as the old.  It should take the same parameters, return the same type, and obey the same preconditions and postconditions.

-->If you obey this rule, you will find that any function designed to work with an instance of a superclass, like a Deck, will also work with instances of subclasses like a Hand or PokerHand.  If you violate this
rule, your code will collapse like (sorry) a house of cards. -- [ThinkPython 18.10] 


scenario 1:
-----------
example:
--------
class Vehicle():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_data(self):
        print('super class data is : ', self.a , self.b)

class Car(Vehicle):

    def get_data(self):
        print('sub class data is : ', self.a , self.b)

c = Car(10, 20)
c.get_data()

output:
-------
sub class data is :  10 20

-->here the sub class has no init constructor. so the python will automatically search for init in the super class. even though if there is no get_dat() in the sub class, python searches for the if there is any method with the same name in the super class.

scenario 2:
-----------
-->in the sub class I want to add 2 more instance attributes. at that we can use the existing init constructor of the super class see below : 
example:
--------
class Vehicle():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_data(self):
        print('super class data is : ', self.a , self.b)

class Car(Vehicle):

    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d
        
    def get_data(self):
        print('sub class data is : ', self.a , self.b, self.c, self.d)

C = Car(10, 20, 30, 40)
C.get_data()
output:
-------
sub class data is :  10 20 30 40

--->actually there is another way to add the instance attributes to the subclass, but there is one disadvantage. see below :
example:
--------
class Vehicle():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_data(self):
        print('super class data is : ', self.a , self.b)

class Car(Vehicle):
     
    def get_data(self):
        print(self.c, self.d)

C = Car(10, 20)
C.c = 30
C.d = 40

C.get_data()

-->here I created the attributes after the object has been already created. but with this process, the readability is missing.


Attribute resolution order:
----------------------------
-->We have discussed how Python looks up attributes of a class instance. It starts in the namespace of the instance, and then looks in the namespace of the class. What happens when your class is a subclass? If the name is not found in the namespace of our instance, or in the class, then the search continues in the parent class, and so on.

Is it an instance attribute?
Is it a class attribute?
Is it a superclass attribute?
Is it a super-superclass attribute?

-->The process of looking up attributes of a class in an inheritance hierarchy seems relatively straightforward. But Python also supports multiple inheritance (two or more names in the base class list). What happens then?

In Python 2.3 a new algorithm was added to Python to clarify this question. The clearest documentation of it can be found in the release notes for 2.3 and in a blog post on the History of Python blog.


Method resolution order:
------------------------
-->MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.


-->In Python, a class can inherit features and attributes from multiple classes and thus, implements multiple inheritance. MRO or Method Resolution Order is the hierarchy in which base classes are searched when looking for a method in the parent class. The syntax is quite simple, as shown below : 

class A:
    def whereiam(self):
        print "I am in A"


class B:
    def whoiam(self):
        print "I am a method"

        
class C(A, B):
    pass

-->An implementation of this is shown below
>>>c = C()
>>>dir(c)
['__doc__', '__module__', 'whereiam', 'whoiam']
>>>c.whoiam()
I am a method
>>>c.whereiam()
I am in A


-->The above example shows that all the properties of classes A and B are in the directory or scope of class C as it inherits from both and can be seen using the ‘dir’ command. ‘dir’ command gives all the names in the current scope. Now, let us look at a much more complex example of multiple inheritance.

class A:
    def whereiam(self):
        print "I am in A"

        
class B(A):
    def whereiam(self):
        print "I am in B"

        
class C(A):
    def whereiam(self):
        print "I am in C"
        
        
class D(B, C):
    def whereiam(self):
        print "I am in D"

-->An implementation is shown here
>>>d = D()
>>>d.whereiam()
I am in D

-->Most of us expected this, but what if we comment or remove the whereiam method in D? Let us do this and understand what happens next.

class A:
    def whereiam(self):
        print "I am in A"

        
class B(A):
    def whereiam(self):
        print "I am in B"

        
class C(A):
    def whereiam(self):
        print "I am in C"
        
        
class D(B, C):
    pass

>>>d = D()
>>>d.whereiam()
I am in B

-->Pretty easy to guess again, B will be invoked. Here’s an exercise for the readers, remove the method from B and check what happens. It is supposed to print “ I am in A”. Again remove the method from A and you will see it prints “ I am in C”. So, how is the method resolution order working? At this point, be patient, I will give a few more examples and you will appreciate this exercise.


Advantages of inheritance:
-------------------------- 
-->One of the key benefits of inheritance is to minimize the amount of duplicate code in an application by sharing common  code amongst several subclasses. Where equivalent code exists in two related classes, the hierarchy can usually be  refactored to move the common code up to a mutual superclass. This also tends to result in a better organization of  code and smaller, simpler compilation units.

-->Inheritance can also make application code more flexible to change because classes that inherit from a common  superclass can be used interchangeably. If the return type of a method is superclass

Reusability -- facility to use public methods of base class without rewriting the same
Extensibility -- extending the base class logic as per business logic of the derived class
Data hiding -- base class can decide to keep some data private so that it cannot be altered by the derived class

Overriding--With inheritance, we will be able to override the methods of the base class so that meaningful  implementation of the base class method can be designed in the derived class.
 
Disadvantages of inheritance:
------------------------------ 
1.One of the main disadvantages of inheritance in Java (the same in other object-oriented languages) is the increased  time/effort it takes the program to jump through all the levels of overloaded classes. If a given class has ten levels of  abstraction above it, then it will essentially take ten jumps to run through a function defined in each of those classes

2.Main disadvantage of using inheritance is that the two classes (base and inherited class) get tightly coupled.
This means one cannot be used independent of each other.

3. Also with time, during maintenance adding new features both base as well as derived classes are required to be  changed. If a method signature is changed then we will be affected in both cases (inheritance & composition)

4. If a method is deleted in the "super class" or aggregate, then we will have to re-factor in case of using that  method.Here things can get a bit complicated in case of inheritance because our programs will still compile, but the  methods of the subclass will no longer be overriding superclass methods. These methods will become independent  methods in their own right.


-------------------------------------------------------------------------------------------------------------


                                            Inheritance by RP(must read)
                                            -----------------

-->Inheritance and composition are 2 important concepts in object oriented programming that model the realtionship between 2 classes. they dirve the disign of an application and determine how the application should evolve as new feature are added or requirements change. both of them enable code reuse, but they do it in different ways. there is not such a rule what design or method you should choose when you are solving problems. most people suggest that 'use composition when you can' and 'use inheritance only when you must'. becuase there are lot of things to deal with inheritance. as soon as you inherite things from the super class, you have not choice but to inherite every thing from super class. you will have lot of problems with inheritance. there can be naming clashes, there can methods with the same name in the super and the sub classes. you may inherite characteristics which may be undesirable. most people use composition. 

Inheritance:
-------------
-->inheritance models what is called an 'is a' relationship. this means that when you have derived clsass that inheris from "base class", you created a relationship where "derived class" 'is a' specialized version of 'base'. the other reason for calling this as the 'is a' relation is the sub classes are tightly coupled to the super classes, like dog 'is a' type of animal, cat 'is a', type of animal. when dog imports the animal, most of the properties of the animal class will get inherited down to dog.

Note:
-----
1)classes that inherit from another are called derived classes, subclasses, or subtypes.
2)classes from which other classes are derived are called base classes or super classes.
3)a derived class is said to derive, inherit, or extend a base class. 

-->lets say you have a base class 'Animal' and you derive from it to create a 'Horse' class. the inheritance relationsip states htat a Horse 'is a ' Animal. this means that Horse inherits the 'interface' and implementation of 'Animal', and Horse object can e used to replace Animal objects in application. 

-->this is known as the "liskov substitution principle". the principle states that 'in a computer program, if 'S' is subtype of 'T', htne object of the type T may be replaced with objects of type "S" without altering any of the desired properties of the program.


Composition:
------------
-->composition is a concept that models a 'has a' relationship. it enables creating complex types by combining objects of other types. this means that class 'composite' can contain an object of another class 'component'. this relationship means that a 'composite' 'has a' 'component'. see the diagram in the real python site. https://files.realpython.com/media/ic-basic-composition.8a15876f7db2.jpg

-->in this diagram above, the 1 represents that the 'composite' class contains one object of type 'component'. cardinality can be expressed in the following ways :
1) a number : indicates the no of 'component' instances that contained in the 'composite'.
2)the * symbol : indicates that the 'composite' class can contain a variable number of 'component' instances. 
3)a range 1...4 : indicates that the 'composite' class can contain a range of 'component' instances. the range is indicated with the minimum and maximum number of instances, or minimum and many instances like 1... *.

note:
-----
-->classes that contain objects of other classes are usually referred to as 'composites', where classes that are used to create more complex type are referred to as 'components'. 

-->for example, you Horse class can be composed by another object of type Tail. Composition allows you to express that relationship by saying a Horse has Tail. 

-->Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes. both Horse and Dog classes can leverage the functionality of Tail composition without deriving one class from the other. 


The Object Super Class:
-----------------------
-->The easiest way to see inheritance in Python is to jump into the Python interactive shell and write a little bit of code. You’ll start by writing the simplest class possible:

>>> class MyClass:
...     pass
...

-->You declared a class MyClass that doesn’t do much, but it will illustrate the most basic inheritance concepts. Now that you have the class declared, you can use the dir() function to list its members:

>>> c = MyClass()
>>> dir(c)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__']

-->dir() returns a list of all the members in the specified object. You have not declared any members in MyClass, so where is the list coming from? You can find out using the interactive interpreter:

>>> o = object()
>>> dir(o)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__']

-->As you can see, the two lists are nearly identical. There are some additional members in MyClass like __dict__ and __weakref__, but every single member of the object class is also present in MyClass.

-->This is because every class you create in Python implicitly derives from object. You could be more explicit and write class MyClass(object):, but it’s redundant and unnecessary.

Exceptions Are an Exception:
-----------------------------
-->Every class that you create in Python will implicitly derive from object. The exception to this rule are classes used to indicate errors by raising an exception.

-->You can see the problem using the Python interactive interpreter:

>>> class MyError:
...     pass
...
>>> raise MyError()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exceptions must derive from BaseException

-->You created a new class to indicate a type of error. Then you tried to use it to raise an exception. An exception is raised but the output states that the exception is of type TypeError not MyError and that all exceptions must derive from BaseException.

-->BaseException is a base class provided for all error types. To create a new error type, you must derive your class from BaseException or one of its derived classes. The convention in Python is to derive your custom error types from Exception, which in turn derives from BaseException.

-->The correct way to define your error type is the following:

>>> class MyError(Exception):
...     pass
...
>>> raise MyError()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyError

-->As you can see, when you raise MyError, the output correctly states the type of error raised.


-------------------------------------------------------------------------------------------------------------


"""
