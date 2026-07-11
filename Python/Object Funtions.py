"""
User in a Social Media
Create a User with attributes (USE CONSTRUCTOR)
- firstName
- lastName
- likesCount
- friendsName [LIST]

PS: You can make a List an Attribute and also pass it as a Parameter.

Object functions:
    introduce
        "Hi I'am (firstName} {lastName}"

    fullProfile
        Outputs every Information of the User Example OUTPUT

        Full Name: Lucas Smith
        Likes: 87
        Friends
            -friendsOne
            -friendsTwo
            -friendsThree
            -friendsFour
"""

class user:

    # NOTE: I used tuples instead of List
    def __init__(self,firstName,lastName,likesCount,*friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName #These are passed as tuples

    def introduce(self):
        print("Introduce:")
        print(f"Hi I am {self.firstName} {self.lastName}")
        print()

    def fullProfile(self):
        print(f"Full name: {self.firstName} {self.lastName}")
        print(f"Likes    : {str(self.likesCount)}")
        print()
        print("Friends: ")
        for x in self.friendsName:
            print(" - " + x)

userOne = user("Tristan","Underson",100,"Mikasa","Sasha","Eren","Armin","Levi")
userOne.introduce()
userOne.fullProfile()