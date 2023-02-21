import random
import sys
from tkinter import *
from tkinter import messagebox

task = []


def getTask():
    print('***THIS IS FOR THOSE PEOPLE WHO DO KNOW WHAT TO DO IN THEIR LIFE****')
    print('***THOSE WHO ARE STUPID ENOUGH TO LET RANDOM SCRIPTS DECIDE WHAT THEY SHOULD DO FIRST****')
    print('________________________________________________________________')
    print("INSTRUCTION: ENTER 'many' TO INPUT A LOT OF TASK and enter'x' WHEN YOU'RE DONE. If you have specific number of task you can directly input its number")
    print('********************************************')
    taskNumber = input('Did you read the instruction? Great! You know what to put in here: ')

    if taskNumber == 'many' or taskNumber == 'MANY':
        x = 'y'
        iterCount = 1
        while x != 'x':

            x = input(f'{iterCount}. ')
            task.append(x)
            iterCount+= 1
        task.remove('x')

    else:
        try:
            taskNum = int(taskNumber)
            if taskNum > 0:
                for i in range(taskNum):
                    tasks = input('What you do?: ')
                    task.append(tasks)
            else:
                print('Just play some game dumbass')
                messagebox.showwarning("bobo", "DID YOU FUCKING READ THE INSTRUCTION?")
                sys.exit('DID YOU FUCKING READ THE INSTRUCTION?')

        except ValueError:
            print('Just play some game dumbass')
            messagebox.showwarning("bobo", "DID YOU FUCKING READ THE INSTRUCTION?")
            sys.exit('DID YOU FUCKING READ THE INSTRUCTION?')

    print('--------------------------------')

    print("This is the random order of your task: ")
    print('--------------------------------')

    random.shuffle(task)

    for item in task:
        print(f'{task.index(item) + 1}. {item}')
    print('---------------------------------------')

    goOut = input("Enter 'exit' to exit or 'again' to try again: ")

    if goOut == 'exit':
        sys.exit('oke salamat sa lahat')
    elif goOut == 'again':
        getTask()
        print('********************************')
    else:
        sys.exit('Di ka ba marunong magbasa?')

print('********************************')
getTask()

