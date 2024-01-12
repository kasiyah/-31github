###################################################
OOP Concepts
###################################################git 
In OOP we are trying to model real life objects that have:
- Attributes - what it has, usually modeled with variables
- Methods - what it does, usually modeled with functions

Object - a way of combining some piece of data and some functionality all together in the same thing. 
We can have multiple objects generated from the same type.
Class - blueprint
Instance - object itself that is created from the blueprint.

###################################################################
Create Objects and Access Attributes and Methods
###################################################################

Every object in a computer program is self contained:
- it has its own identity separate from the other objects.
- it has own attributes that describe it's current state
- it has its own behaviors, things that it can do

But often software describe things that do not have tangible representations

A program cab represent more than physical things
- date, timer or bank account

To represent somethings as an object ---> need to identify if the things is a noun or not

Objects = Nouns | Behaviors = Verbs
-----------------------------------
Things          | Calling
Places          | Texting
Ideas           | Playing
People          |       
Concepts        |


Objects are created from a blueprint - Class.
Class - detailed description, definition, template of an object, but not an object itself.
Once we have written a class and defined it, we can use it to create as many objects based on this class as we want.
Different classes let us to create different types of objects.

Most OO Languages come with a collection of predefined classes, so you can just start creating objects right away. 
In Python, you have Python standard library with about thousands of classes available for you.


###################################################################
 Create Objects and Access Attributes and Methods
###################################################################

# Creating objects from Class - blueprint
robot_a = RobotBlueprint()  # for classes Pascal case is used, each word starts with a capital letter
robot_b = RobotBlueprint()
 
# Accessing object attributes
robot.battery_level
 
# Accessing object methods
robot.detect_speech()


### Classes
Class - code template for creating program objects

Class Components:
- Name: StarCookie - identifies what it is
- Attributes: weight, color - describe its properties
- Methods: decorate(), consume() - describe its behaviors

### Method

- a block of code or procedure that can be called to perform some actions and it may return a value.
- basically functions defined as a part of class ---> can only access the data that is known to that specific object.

Instantiation - process of creating objects based on blueprint. Creating instance of a particular class.


###################################################################
Creating a Custom Class
###################################################################
# Creating an empty class
class StarCookie:
    # denotes that this line si passed and it will continue to the next line of code
    pass
# creating an object  
star_cookie1 = StarCookie()
# print to make sure object is created in the memory
print(star_cookie1)


###################################################################
Class Attributes
###################################################################
# Creating class attributes
class StarCookie:
    pass
 
star_cookie1 = StarCookie()
# create attributes for our objects
weight.star_cookie1 = 15
color.star_cookie1  = "Red"
print(star_cookie1.weight)
print(star_cookie1.color)
weight.star_cookie2 = 16
color.star_cookie2 = "Red"
print(star_cookie2.weight)
print(star_cookie2.color)


###################################################################
Initializer - makes creating attributes easier
###################################################################
When the object is being initialized, we can set the variables or counters to their starting values.
In Python initializer is created by using init function.

# Initializer
class StarCookie:
    def __init__(self):

# Creating class initializer and attributes
class StarCookie:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
star_cookie1 = StarCookie("Red", 16)
print(star_cookie1.color)
print(star_cookie1.weight)


###################################################################
To set default Values in Initializer
###################################################################
# Creating class initializer and attributes
class Youtube:
    # set default value for all objects
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers
user1 = Youtube("Elshad")
print(user1.username)
print(user1.subscribers)
 
user2 = Youtube("Renad")
user2.subscribers = 5
print(user2.username)
print(user2.subscribers)


###################################################################
Defining Global Attributes:
###################################################################
# Creating class initializer and attributes
class  StarCookie:
    # global attributes, applies to all objects of this class
    milk = 0.1
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
star_cookie1 = StarCookie("Red", 16)
star_cookie2 = StarCookie("Blue", 15)
print(star_cookie1.milk)
print(star_cookie2.milk)
# prints instance dictionary 
print(star_cookie1.__dict__)
# prints class dictionary, including all functions
print(StarCookie.__dict__)
 
# override the object attribute, applies only to this object
star_cookie1.milk = 0.2
print(star_cookie1.__dict__)
 
# override the class attribute, applies only to every object of the class
StarCookie.milk = 0.2
print(StarCookie.__dict__)


###################################################################
Class Methods
###################################################################
- object's behavior

class Robot:
    # creating method
    def enter_charge_mode(self):
        self.battery_level += 1
# calling method
my_robot.enter_charge_mode()


class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
 
    # subscribe method
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1
 
user1 = Youtube("Elshad")
user2 = Youtube("Renad")
user1.subscribe(user2)
print(f"User 1 subscribers: {user1.subscribers}")
print(f"User 1 subscriptions: {user1.subscriptions}")
print(f"User 2 subscribers: {user2.subscribers}")
print(f"User 2 subscriptions: {user2.subscriptions}")