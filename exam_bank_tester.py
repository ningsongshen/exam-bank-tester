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
    print("Enter another chapter to be tested on (or press e to continue): ")
    try:
        chapters.append(int(input()))
    except ValueError:
        done = True

print("Enter the number of questions to work on: ")
num_questions = int(input())

relevant_questions = data[data.chapter.astype(int).isin(chapters)]

# remove questions that contain 'figure', because there are no images in this system yet. 
# Make sure to add this info to the database itself
ignore_keywords = ["Figure", "Table", "Fact"]
non_figure_questions = relevant_questions[~relevant_questions.question.str.contains("|".join(ignore_keywords))]

selected_questions = non_figure_questions.sample(n=num_questions, replace=True)

# for testing purposes
# print(selected_questions.head())

for row in selected_questions.itertuples(index=False):
    print("", row[1], row[2], row[3], row[4], row[5], row[6], "", sep="\n")
    response = input()

    if response.upper() == row[7]:
        print("Correct!")
    else:
        print("~~INCORRECT~~")
        print("Answer:", row[7])
    print("\nPress enter to continue")
    contine = input()
