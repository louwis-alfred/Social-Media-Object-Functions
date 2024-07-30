# Using object Functions
# Big credits for SDPT for this wonderful lesson 

class User:
    def __init__(self,firstName,lastName,likesCount,friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName
        
    def display(self):
        print(f"Firstname  : {self.firstName}")
        print(f"Lastname   : {self.lastName}")
        print(f"Likes count: {self.likesCount}")
        print('Friends: ')
        for friend in self.friendsName:
            print(f"-{friend}")

firstName = input("Enter firstname:")
lastName = input('Enter lastname  :')
likesCount = int(input('Enter Likes count: '))
friendsName = input('Enter Friend name: ') 

friendList = friendsName.split(',')

user1 = User(firstName,lastName,likesCount,friendList)
user1.display()       

