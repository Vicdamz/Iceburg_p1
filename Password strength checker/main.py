from password_generator import generate_password
from typing import Dict
import string

action = input("What do you want to do: ")
password_directory = {}

if action == "new entry":
    password_count = int(input("how many password you want to enter "))
    ##this is how you initialize basic dictionary
    password_directory = {}

    for i in range(password_count):
        website = input("which website is this password for ")
        ##password_directory["password"] = generate_password()
        password = generate_password()
        password_directory[website] = password

    for website, password in password_directory.items():
        print(f"Website: {website} | Password: {password}")
        
    # code to append text to our file.......Open the file first, then write your items inside the indented block
    with open("passwords.txt", "a") as file:
        for website, pwd in password_directory.items():
            file.write(f"{website}: {pwd}\n")
    print("All passwords successfully saved to passwords.txt!")


# code to show all results in the file
if action == "show entry":
    with open("passwords.txt", "r") as file:
        for line in file:
            clean_line = line.strip("\n")   #this line removes all the \n given at the end of each line and saves it into a new variable

            if ": " in clean_line:
                website, password = clean_line.split(": ", maxsplit = 1)     #this line gives whatever comes before : to website and rest to password
                password_directory[website] = password                       #this line assigns the password to website
                print(f"site -> {website}, Password -> {password}")


#code to search all the password for a certain website
if action == "search entries":
    search_pw = input("which password do you want to search: ")
    Match_Found = False
    with open("passwords.txt", "r") as file:
        for line in file:
            clean_line = line.strip("\n")

            if ": " in clean_line:
                website, password = clean_line.split(": ", maxsplit = 1)     #this line gives whatever comes before : to website and rest to password
                password_directory[website] = password                       #this line assigns the password to website

                if search_pw == website:
                    Match_Found = True
                    print(f"Match found, the password is : {password}")
                    break
                    
    # Check if a match was found only after searching the whole file
    if not Match_Found:
        print("No match found")