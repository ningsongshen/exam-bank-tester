# Setting up the data
import numpy as np 
import pandas as pd 

data = pd.read_csv("output.csv")


# Prompting for test characteristics
done = False
chapters = []
print("Enter a chapter to be tested on: ")
chapters.append(int(input()))
while not done:
    print("Enter another chapter to be tested on (or press e to end): ")
    try:
        chapters.append(int(input()))
    except ValueError:
        done = True

print("Enter the number of questions to work on: ")
num_questions = int(input())
