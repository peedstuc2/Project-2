user = "griffin"
root = "/home/"
userOS = "@archlinux"
MainFolders = ["Android","Desktop", "Documents", "Downloads",
"Labs", "Music", "Pictures", "Projects", "pt", "Public", "search-env", "Templates", "Videos", "yay"
]

overall = ["drwxr-xr-x 2 griffin griffin 4096 16 Oct 16:33 Android",
"drwxr-xr-x 4 griffin griffin 8299 12 Sep 17:23 Desktop",
"drwxr-xr-x 4 griffin griffin 4556 12 Apr 12:43 Documents",
"drwxr-xr-x 6 griffin griffin 7374 17 May 12:12 Downloads",
"drwxr-xr-x 7 griffin griffin 8482 11 Jul 16:00 Labs",
"drwxr-xr-x 8 griffin griffin 2343 04 Mar 13:23 Music",
"drwxr-xr-x 2 griffin griffin 7738 12 Jun 12:01 Pictures",
"drwxr-xr-x 4 griffin griffin 7722 12 Dec 04:23 Projects",
"drwxr-xr-x 5 griffin griffin 2344 23 May 12:12 pt",
"drwxr-xr-x 7 griffin griffin 7738 12 Aug 13:02 Public",
"drwxr-xr-x 5 griffin griffin 4775 30 Sep 13:02 search-env",
"drwxr-xr-x 4 griffin griffin 1234 14 Feb 12:23 Templates",
"drwxr-xr-x 4 griffin griffin 1234 15 Nov 00:00 Videos",
"drwxr-xr-x 3 griffin griffin 2333 11 Jan 13:58 yay"
]

while True:
    userInput = input(f"[{user}{userOS} ~]$ ")

    if userInput == "pwd":
        print(root+user)

    elif userInput == "ls":
        print(*MainFolders)

    elif userInput == "ls -l":
        print(*overall, sep="\n")

    else:
        print(f"bash: {userInput} command not found")

