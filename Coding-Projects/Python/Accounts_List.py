# This is just a simple code I wrote to test lists in Python

num = int(input("Enter the number of accounts to add: "))

usernames = []
passwords = []

for x in range (0, num):
    usernames.append(input("Enter Account " + str(x + 1) + " Username: "))
    passwords.append(input("Enter Account " + str(x + 1) + " Password: "))

for x in range (0, num):
    print("Username " + str(x + 1) + ": " + usernames[x])
    print("Password " + str(x + 1) + ": " + passwords[x])