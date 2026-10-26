user = "griffin"
root = "/home/"
userOS = "@archlinux"

while True:
    userInput = input(f"[{user}{userOS} ~]$ ")

    if userInput == "pwd":
        print(root+user)
