import os, re, csv, sys

class Problem:
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

def resource_path(relative):
    #print(os.environ)
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    #print(application_path)
    return os.path.join(application_path, relative)

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

with open(resource_path("output.csv"), "w", encoding="utf8", newline='') as outf:
    outfwriter = csv.writer(outf)
    p = Problem()
    outfwriter.writerow(["chapter", "question", "a", "b", "c", "d", "e", "answer", "topic", "figure"])
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
                    outfwriter.writerow([p.chapter, p.question, p.a, p.b, p.c, p.d, p.e, p.answer, p.topic, p.figure])
                


