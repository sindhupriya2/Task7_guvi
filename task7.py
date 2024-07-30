# Program 1 - Write a program using function which will create a text file with current timestamp.

from datetime import datetime
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date & time : ", current_datetime)
str_current_datetime = str(current_datetime)
file_name = str_current_datetime+".txt"
file = open(file_name, 'w')
print("File created : ", file.name)
file.close()


# Program 2 - write a python function to read from a text file which display the content

x=str(input("Enter the name of the file with .txt extension:"))
file2=open(x,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close

