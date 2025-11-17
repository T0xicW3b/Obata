import csv
import random

class Question:
    def __init__(self, id, ask, a, b, c, d, e, correct):
        self.id = id
        self.ask = ask
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.correct = correct
def gen_questions(path, number_of_questions, ask, response):
    list_of_questions = []
    with open(path, encoding="utf-8") as file:
        data = list(csv.DictReader(file))
        for i in range(10):
            nums = random.sample(range(number_of_questions), 6)
            x = random.randint(1,5);
            question = Question(i, data[nums[0]][ask], data[nums[1]][response], data[nums[2]][response], data[nums[3]][response], data[nums[4]][response], data[nums[5]][response], data[nums[0]][response])
            if x == 1:
                question.a = question.correct
            elif x == 2:
                question.b = question.correct
            elif x == 3:
                question.c = question.correct
            elif x == 4:
                question.d = question.correct
            elif x == 5:
                question.e = question.correct

            list_of_questions.append(question)
        return list_of_questions;




