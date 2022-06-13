
'''
Write a program to read /etc/passwd on a Unix computer. The first field
contains the username, and the final field contains the user’s shell,
the command interpreter. Display the shells in decreasing order of popularity,
such that the most popular shell is shown first, the second most popular
shell second, and so forth.
'''

user = "luke"
with open("etc_passwd.txt") as file:
    for line in file:
        if line.split(":")[0] == user:
            if line.rstrip("\n").split(":")[6] in ["/usr/sbin/nologin", "/bin/false"]:
                print("User is not allowed to login")
            else:
                print(line.rstrip("\n").split(":")[6])
