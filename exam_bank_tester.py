from typing import Iterator, List
import pandas as pd 

def get_integer() -> int:
    done = False
    while not done:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Invalid input, try again.")
            continue

def select_chapters() -> List:
    """Prompt users for chapters to be tested on"""
    
    done = False
    chapters = []
    print("Enter a chapter to be tested on: ")
    chapters.append(get_integer())
    while not done:
        print("Enter another chapter to be tested on (or press any non-integer to continue): ")
        try:
            chapters.append(int(input()))
        except ValueError:
            done = True

    return chapters

def select_length() -> int:
    """Prompt users for number of questions to be tested on"""

    print("Enter the number of questions to work on: ")
    num_questions = get_integer()
    return num_questions
    
def get_questions(filepath: str, chapters: List, num_questions: int) -> pd.DataFrame:
    data = pd.read_csv(filepath)
    relevant_questions = data[data.chapter.astype(int).isin(chapters)]

    # Remove questions that contain 'figure' because there are no images on the command line
    ignore_keywords = ["Figure", "Table", "Fact"]
    non_figure_questions = relevant_questions[~relevant_questions.question.str.contains("|".join(ignore_keywords))]

    selected_questions = non_figure_questions.sample(n=num_questions, replace=True)

    return selected_questions

def render_question(row: Iterator) -> None:
    print("", row[1], row[2], row[3], row[4], row[5], row[6], "", sep="\n")

def evaluate_response(row: Iterator, response: str) -> int:
    if response.upper() == row[7]:
        print("Correct!")
        return 1
    else:
        print("~~INCORRECT~~")
        print("Answer:", row[7])
        return 0

def main():
    """Main event loop"""
    
    question_data_path = "output.csv"
    total_points = 0

    selected_chapters = select_chapters()
    selected_num_questions = select_length()

    selected_question_data = get_questions(question_data_path, selected_chapters, selected_num_questions)

    # Iterate over selected questions
    for row in selected_question_data.itertuples(index=False):
        render_question(row)
        response = input()

        total_points += evaluate_response(row, response)
        
        print("\nPress enter to continue")
        prompt = input()

if __name__ == "__main__":
    main()