import sys

question_count = 0
questions_output = open('output/questions.json', 'w', encoding = 'utf8')
questions_output.write('{\n')

topics_output = open('output/topics.json', 'w', encoding='utf8')
topics_output.write('{\n')

banks = [f'chapter{x:02}.doc.txt' for x in range(1, 32)]

for i in range(len(banks)):
    question_data = open(banks[i], 'r', encoding='utf8').read()

    index = 0
    while index < len(question_data):
        if question_data[index] == '"' or question_data[index] == '\\':
            question_data = question_data[:index] + '\\' + question_data[index:]
            index += 1
        index += 1   

    class Question:
        question = ""
        choiceA = ""
        choiceB = ""
        choiceC = ""
        choiceD = ""
        choiceE = ""
        answer = ""
        chapter = ""
        topic = ""

    questions = []
    new_question = Question()

    is_question = False
    choiceA = False
    choiceB = False
    choiceC = False
    choiceD = False
    choiceE = False
    is_answer = False
    is_topic = False

    for word in question_data:
        if word == "A)":
            is_question = False
            choiceA = True
            choiceB = False
            choiceC = False
            choiceD = False
            choiceE = False
            is_answer = False
            is_topic = False
        if word == "B)":
            is_question = False
            choiceA = False
            choiceB = True
            choiceC = False
            choiceD = False
            choiceE = False
            is_answer = False
            is_topic = False
        if word == "C)":
            is_question = False
            choiceA = False
            choiceB = False
            choiceC = True
            choiceD = False
            choiceE = False
            is_answer = False
            is_topic = False
        if word == "D)":
            is_question = False
            choiceA = False
            choiceB = False
            choiceC = False
            choiceD = True
            choiceE = False
            is_answer = False
            is_topic = False
        if word =="E)":
            is_question = False
            choiceA = False
            choiceB = False
            choiceC = False
            choiceD = False
            choiceE = True
            is_answer = False
            is_topic = False
        if word == "Copyright" or word == "________________":
            is_question = False
            choiceA = False
            choiceB = False
            choiceC = False
            choiceD = False
            choiceE = False
            is_answer = False
            is_topic = False
        if word == str(num_questions) + ")":
            questions.append(new_question)
            new_question = Question()
            num_questions += 1
            is_question = True
            choiceA = False
            choiceB = False
            choiceC = False
            choiceD = False
            choiceE = False
            is_answer = False
            is_topic = False

        if word == "Answer:":
            is_question = False
            choiceA = False
            choiceB = False
            choiceC = False
            choiceD = False
            choiceE = False
            is_answer = True
            is_topic = False

        if word == "Topic:":
            is_question = False
            choiceA = False
            choiceB = False
            choiceC = False
            choiceD = False
            choiceE = False
            is_answer = False
            is_topic = True

        if is_question and (word != str(num_questions-1) + "."):
            new_question.question += word + " "
        if choiceA:
            new_question.choiceA += word + " "
        if choiceB:
            new_question.choiceB += word + " "
        if choiceC:
            new_question.choiceC += word + " "
        if choiceD:
            new_question.choiceD += word + " "
        if is_answer:
            new_question.answer += word + " "
        if is_topic:
            new_question.topic += word + " "

    questions.append(new_question)
