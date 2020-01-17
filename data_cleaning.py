import os, re, csv

class Problem:
    pid = 0
    chapter = 0
    question = ""
    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    answer = ""
    topic = ""
    figure = False

def get_type(line):
    
    chapter_text = re.match('^Chapter \d+.+$', line)
    if chapter_text:
        # print(line)
        return "chapter"

    question_text = re.match('^\d{1,3}\).+$', line)
    if question_text:
        # print(line)
        return "question"

    answer_text = re.match('^[A-E]{1,3}\).+$', line)
    if answer_text:
        # print(line)
        return "answer"

    correct = re.match('^Answer: .+$', line)
    if correct:
        # print(line)
        return "correct"

    topic = re.match('^Topic: .+$', line)
    if topic:
        # print(line)
        return "topic"

    return "none"

with open("output.csv", "w", encoding="utf8", newline='') as outf:
    outfwriter = csv.writer(outf)
    p = Problem()
    for filename in os.listdir("banks"):
        print(filename)
        with open("banks/"+filename, "r", encoding="utf8", errors="ignore") as inf:
            for dline in inf:
                line = dline.strip()
                line_type = get_type(line)

                if line_type == "chapter":
                    p.chapter +=1
                    continue

                elif line_type == "question":
                    p.question = line

                elif line_type == "answer":
                    letter = line[0]
                    if letter == "A":
                        p.a = line
                    elif letter == "B":
                        p.b = line
                    elif letter == "C":
                        p.c = line
                    elif letter == "D":
                        p.d = line
                    elif letter == "E":
                        p.e = line
                
                elif line_type == "correct":
                    p.answer = line[9]
                
                elif line_type == "topic":
                    p.topic = line [8:]
                    outfwriter.writerow([p.pid, p.chapter, p.question, p.a, p.b, p.c, p.d, p.e, p.answer, p.topic, p.figure])
                    p.pid += 1
                


