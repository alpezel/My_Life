#Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output: 
#Enter line: Beautiful is better than ugly.
#Are there more lines y/n? y
#Enter line: Explicit is better than implicit.
#Are there more lines y/n? y
#Enter line: Simple is better than complex.
#Are there more lines y/n? n 

# defining the adding of line to the txt file
def Add_line():
    #ask user to input line
    my_line = input(green +"\nEnter line: ")
    # open txt file where the line will be appended
    with open("My_Life.txt","a") as my_life_file:
        my_life_file.write(str(my_line) +"\n")

# change colors in output
red ="\033[1;31m"
green ="\033[3;32m"
white = "\033[1;37m"

# add while true to keep running the program when the user answer "y"
print(white+"=================================================================")
while True:
    Add_line()

    # ask the user if there are more lines
    more_lines = input(red+"\nAre there more lines y/n? ")

    while more_lines.lower() != "y" and  more_lines.lower() != "n":
        more_lines = input(red+"Are there more lines y/n? ")
    if more_lines.lower() == "n":
        break
print(white+"\n=================================================================")
