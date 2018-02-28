import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []
    correct = 0

    def __init__(self):
        for _ in range(5):
            self.questions.append(Add(random.randint(0, 10), random.randint(0, 10)))
            self.questions.append(Multiply(random.randint(0, 10), random.randint(0, 10)))

    def take_quiz(self):
        start_time = datetime.datetime.now()

        # ask all the questions
        for question in self.questions:
            self.ask(question)

        end_time = datetime.datetime.now()
        diff = end_time - start_time
        self.summary(diff)

    def ask(self, question):
        start_time = datetime.datetime.now()
        answer = input(f"{question.text} = ? ")
        if int(answer) == question.answer:
            self.correct += 1
        end_time = datetime.datetime.now()
        diff = end_time - start_time
        print(f"The correct answer was {question.answer}")
        print(f"It took you {diff.days} days, {diff.seconds} seconds, {diff.microseconds} microseconds")
        input("Ready to continue? press RETURN")

    def summary(self, diff):
        print(f"You got {self.correct} out of ten right!")
        print(f"It took you {diff.days} days, {diff.seconds} seconds, {diff.microseconds} microseconds")
