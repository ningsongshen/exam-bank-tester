# Convert all exams to JSON File

import sys

exam_count = 0
question_count = 0
questions_output = open('output/questions.json', 'w', encoding='utf8')
questions_output.write('{\n')

cluster_exams_output = open('output/examIds.json', 'w', encoding='utf8')
cluster_questions_output = open('output/examQuestions.json', 'w', encoding='utf8')
cluster_statistics_output = open('output/examStatistics.json', 'w', encoding='utf8')
cluster_exams_output.write('{\n')
cluster_questions_output.write('{\n')
cluster_statistics_output.write('{\n')

clusters = ['BA', 'BMA', 'ENT', 'FIN', 'HOSP', 'MKTG']
print_clusters = ['principles', 'bma', 'entrepreneurship', 'finance', 'hospitality', 'marketing']
exams = [
    ['1027', '1037', '1044', '1054', '1061', '1068', '1075', '1092', '1102', '1120', '1140', '2010', '2011', '2012', '2013', '2014', '2016'],
    ['872', '902', '943', '964', '976', '997', '1024', '1027', '1031', '1041', '1048', '1061', '1065', '1072', '1079', '1096', '1106', '1124', '1153', '2010', '2011', '2012', '2013', '2014 Sample', '2014'],
    ['2017', '1167', '1176'],
    ['10A', '10B', '1022', '1029', '1047', '1057', '1064', '1071', '1078', '1088', '1095', '1105', '1152', '2010', '2011', '2012', '2014'],
    ['10A', '10B', '1087', '1094', '1104', '1151', '2009-Regional', '2010-ICDC', '2010-Provincial', '2011-ICDC', '2014-Sample', '2014', '2015-Sample', '2016-Sample', '2018-Sample', '1039', '1131'],
    ['10A', '10B', '1021', '1028', '1038', '1045', '1062', '1069', '1150', '1076', '1086', '1093', '1103', '2010', '2011', '2012', '2013', '2014']
]

for i in range(len(clusters)):
    cluster_exams_output.write('"' + print_clusters[i] + '": {')
    cluster_exams_output.write('\n')

    cluster_questions_output.write('"' + print_clusters[i] + '": {')
    cluster_questions_output.write('\n')

    cluster_statistics_output.write('"' + print_clusters[i] + '": {')
    cluster_statistics_output.write('\n')

    for j in range(len(exams[i])):
        try:
            test = clusters[i] + '-' + exams[i][j]
            test_data = open(clusters[i] + '/' + test + '.pdf.txt', 'r', encoding='utf8').read()
        except IOError:
            try:
                test_data = open(clusters[i] + '/' + test + '.doc.txt', 'r', encoding='utf8').read()
            except IOError:
                try:
                    test_data = open(clusters[i] + '/' + test + '.docx.txt', 'r', encoding='utf8').read()
                except IOError:
                    try:
                        test_data = open(clusters[i] + '/' + test + '.txt', 'r', encoding='utf8').read()
                    except IOError:
                        print('test ' + test + ' not found.')
        try:
            key = clusters[i] + '-' + exams[i][j] + '-KEY'
            key_data = open(clusters[i] + '/' + key + '.pdf.txt', 'r', encoding='utf8').read()
        except IOError:
            try:
                key_data = open(clusters[i] + '/' + key + '.doc.txt', 'r', encoding='utf8').read()
            except IOError:
                try:
                    key_data = open(clusters[i] + '/' + key + '.docx.txt', 'r', encoding='utf8').read()
                except IOError:
                    try:
                        key_data = open(clusters[i] + '/' + key + '.txt', 'r', encoding='utf8').read()
                    except IOError:
                        print('key ' + test + ' not found.')

        # makes sure quotes have a \ before
        index = 0
        while index < len(test_data):
            if test_data[index] == '"' or test_data[index] == '\\':
                test_data = test_data[:index] + '\\' + test_data[index:]
                index += 1
            index += 1

        index = 0
        while index < len(key_data):
            if key_data[index] == '"' or key_data[index] == '\\':
                key_data = key_data[:index] + '\\' + key_data[index:]
                index += 1
            index += 1

        test_data = test_data.split()
        key_data = key_data.split()

        class question:
            question = ""
            choiceA = ""
            choiceB = ""
            choiceC = ""
            choiceD = ""
            answer = ""
            explanation = ""
            unique = test + "-"

        exam_questions = []
        questions = []
        exams.append(test)
        num_questions = 1
        new_question = question()

        # test booleans
        is_question = False
        choiceA = False
        choiceB = False
        choiceC = False
        choiceD = False

        # key booleans
        is_answer = False
        is_explanation = False

        for word in test_data:
            if word == "A.":
                is_question = False
                choiceA = True
                choiceB = False
                choiceC = False
                choiceD = False
            if word == "B.":
                is_question = False
                choiceA = False
                choiceB = True
                choiceC = False
                choiceD = False
            if word == "C.":
                is_question = False
                choiceA = False
                choiceB = False
                choiceC = True
                choiceD = False
            if word == "D.":
                is_question = False
                choiceA = False
                choiceB = False
                choiceC = False
                choiceD = True
            if word == "Copyright" or word == "________________":
                is_question = False
                choiceA = False
                choiceB = False
                choiceC = False
                choiceD = False
            if word == str(num_questions) + ".":
                questions.append(new_question)
                new_question = question()
                new_question.unique += str(num_questions)
                num_questions += 1
                is_question = True
                choiceA = False
                choiceB = False
                choiceC = False
                choiceD = False

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
        
        questions.append(new_question)
        exam_questions.append(new_question.unique)

        #reset question counter
        num_questions = 0

        for word in key_data:
            if is_explanation:
                if word == "SOURCE:":
                    is_explanation = False
                else:
                    questions[num_questions].explanation += word + " "
            if is_answer:
                questions[num_questions].answer = word
                is_answer = False
                is_explanation = True
            if word == str(num_questions + 1) + ".":
                num_questions += 1
                is_answer = True

        # output questions
        for n in range(1, len(questions)):
            if len(questions[n].answer) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            if len(questions[n].choiceA) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            if len(questions[n].choiceB) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            if len(questions[n].choiceC) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            if len(questions[n].choiceD) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            if len(questions[n].explanation) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            if len(questions[n].question) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            if len(questions[n].unique) == 0:
                print('YELL: ' + test + ' question ' + str(n))
                sys.exit()
            questions_output.write('    "' + questions[n].unique + '": {')
            questions_output.write('\n')
            questions_output.write('        "content": "')
            questions_output.write(questions[n].question.strip(" "))
            questions_output.write('",\n')
            questions_output.write('        "choiceA": "')
            questions_output.write(questions[n].choiceA.strip(" "))
            questions_output.write('",\n')
            questions_output.write('        "choiceB": "')
            questions_output.write(questions[n].choiceB.strip(" "))
            questions_output.write('",\n')
            questions_output.write('        "choiceC": "')
            questions_output.write(questions[n].choiceC.strip(" "))
            questions_output.write('",\n')
            questions_output.write('        "choiceD": "')
            questions_output.write(questions[n].choiceD.strip(" "))
            questions_output.write('",\n')
            questions_output.write('        "answer": "')
            questions_output.write(questions[n].answer.strip(" "))
            questions_output.write('",\n')
            questions_output.write('        "explanation": "')
            questions_output.write(questions[n].explanation.strip(" "))
            questions_output.write('",\n')
            questions_output.write('        "identification": "')
            questions_output.write(questions[n].unique.strip(" "))
            questions_output.write('"\n')
            if n + 1 == len(questions) and i + 1 == len(clusters) and j + 1 == len(exams[i]):
                questions_output.write('    }')
            else:
                questions_output.write('    },')
            questions_output.write('\n')

        # output exam data
        exam_count += 1
        cluster_exams_output.write('    "' + test + '": {')
        cluster_exams_output.write('\n')
        cluster_exams_output.write('        "identification": "' + test + '"')
        cluster_exams_output.write('\n')
        if j + 1 < len(exams[i]):
            cluster_exams_output.write('    },')
            cluster_exams_output.write('\n')
        else:
            cluster_exams_output.write('    }')
            cluster_exams_output.write('\n')
        
        # output exam statistics
        cluster_statistics_output.write('    "' + test + '": {')
        cluster_statistics_output.write('\n')
        cluster_statistics_output.write('        "identification": "' + test + '",')
        cluster_statistics_output.write('\n')
        cluster_statistics_output.write('        "users": {')
        cluster_statistics_output.write('\n')
        cluster_statistics_output.write('            "init": ""')
        cluster_statistics_output.write('\n')
        cluster_statistics_output.write('        }')
        cluster_statistics_output.write('\n')
        if j + 1 < len(exams[i]):
            cluster_statistics_output.write('    },')
            cluster_statistics_output.write('\n')
        else:
            cluster_statistics_output.write('    }')
            cluster_statistics_output.write('\n')
        
        # output exam questions
        cluster_questions_output.write('    "' + test + '": {')
        cluster_questions_output.write('\n')
        # write questions here
        for n in range(1, len(questions)):
            cluster_questions_output.write('        "' + questions[n].unique + '": "' + questions[n].unique + '"')
            if n + 1 < len(questions):
                cluster_questions_output.write(',')
            question_count += 1
            cluster_questions_output.write('\n')
        if j + 1 < len(exams[i]):
            cluster_questions_output.write('    },')
            cluster_questions_output.write('\n')
        else:
            cluster_questions_output.write('    }')
            cluster_questions_output.write('\n')
    
    cluster_exams_output.write('}')
    if i + 1 < len(clusters):
        cluster_exams_output.write(',')
    cluster_exams_output.write('\n')

    cluster_questions_output.write('}')
    if i + 1 < len(clusters):
        cluster_questions_output.write(',')
    cluster_questions_output.write('\n')

    cluster_statistics_output.write('}')
    if i + 1 < len(clusters):
        cluster_statistics_output.write(',')
    cluster_statistics_output.write('\n')


questions_output.write('}\n')
cluster_exams_output.write('}\n')
cluster_questions_output.write('}\n')
cluster_statistics_output.write('}\n')

print('...done.')
print (str(question_count) + ' questions in ' + str(exam_count) + ' exams.')
