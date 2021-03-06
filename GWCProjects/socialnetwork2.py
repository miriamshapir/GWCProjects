class User:
    def __init__(self, user_name, user_id):
        #recommended attributes
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []

    def addConnection(self, connection_id):
        self.connections.append(connection_id)

    def getUserName(self):
        return self.user_name

    def getConnections(self):
        return self.connections

    def getUserID(self):
        return self.user_id
class Network:
    def __init__(self):
        self.users = []

    def numUsers(self):
        return len(self.users)
        #returns the number of users in the network

    def addUser(self, username):
        user_id = len(self.users)
        newUser = User(username, user_id) #created an instance of a new user
        self.users.append(newUser)
        # creates a new user, assigns them an ID
        # and adds them to the network

    def getUserID(self, username):
        for person in self.users:
            if (person.getUserName() == username):
                return person.getUserID()
        #returns the user id when given the users username

    def addConnection(self, user1, user2):
        #This function
        # 1) gets the user ids of user1 and user2
        user_id1 = self.getUserID(user1)
        user_id2 = self.getUserID(user2)
        # 2) checks to see if these users are already connected
        user1 = self.users[user_id1]
        user2 = self.users[user_id2]
        # 3) If theyre not, adds user1 to user2's connections and viceversa
        user1.addConnection(user2)
        user2.addConnection(user1)
#    def printUsers(self):
        #BONUS
        #this function goes through the users in the network and prints them


#    def printConnections(self, username):
        #BONUS
        #This function takes in a username, finds the corresponding user, and
        #then prints that users connections

def main():
    facebook = Network()
    username = input("username: ")
    facebook.addUser(username)

    print(facebook.users[0].getUserName())
    print(facebook.users[0].getUserID())


main()
