# break terminates the execution of a for or while loop. 
# Code in the loop after the break statement does not execute.


i = 0

while i < 4:
    print(i)
    i = i+1
    if i == 2:
        break
