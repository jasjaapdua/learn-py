'''
    Adds functionality to run the quiz game. Generates questions as well as
    asks them, calcualtes score.
'''

from data import question_data as qd
import question_model as qm

def gen_question():
    '''
        Generates the next question to ask.
    '''
    # for question in qd:
    #     new_q = qm.Question(question["question"], question["correct_answer"])
    #     yield new_q
    

class QuizBrain:
    '''
        Each QuizBrain object represents a Quiz session with its own score 
        number of attempted questions and a series of questions picked from the database (data.py)
    '''
    def __init__(self) -> None:
        self.questions = gen_question()
        self.score = 0
        self.attempted = 0

    def next_question(self) -> bool:
        '''
            Asks the next question by generating it using the generator
            gen_question(). Returns True if a question was successfully asked.
            False if out of questions.
        '''
        try:
            next_q = next(self.questions)
        except StopIteration:
            return False
        answer = input(f"{next_q.text}\nEnter your answer: ")
        if answer.lower() != next_q.answer.lower():
            print("It's giving wrong :(\n")
        else:
            print("It's giving correct.\n")
            self.score += 1
        self.attempted += 1
        return True

    def start_session(self) -> None:
        '''
            Continuously calls next_question() until no more questions remain.
        '''
        while self.next_question():
            continue
        print(f"All done! Your score is - {self.score}/{self.attempted}")
