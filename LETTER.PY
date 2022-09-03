letter =''' dear name
\tyou are selected 
<|date|>'''
name = input("enter your name \n")
date =input("enter date\n \t")
letter =letter.replace("name",name)
letter =letter.replace("<|date|>",date)
print(letter)