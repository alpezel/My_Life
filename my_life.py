#Write a method in python to write multiple line of text
#contents into a text file mylife.txt. See sample output:
#Enter line: Beautiful is better than ugly.
#Are there more lines y/n? y
#Enter line: Explicit is better than implicit.
#Are there more lines y/n? y
#Enter line: Simple is better than complex.
#Are there more lines y/n? n 


def Add_line():
    #ask user to input line
    my_line = input("Enter line:")
    # open txt file where the line will be appended
    with open("My_Life.txt","a") as my_life_file:
        my_life_file.write(str(my_line) +"\n")

    #test if working
    print ("lines added in txt file:",my_line)

# add while true to keep running the program when the user answer "y"
while True:
    Add_line()

    # ask the user if there are more lines
    more_lines = input("Are there more lines y/n?")

    while more_lines.lower() != "y" and  more_lines.lower() != "n":
        more_lines = input("Are there more lines y/n?")
    if more_lines.lower() == "n":
        break

                   
    

