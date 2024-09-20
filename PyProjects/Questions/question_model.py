'''
    Definition for a class that describes a Question that a player must answer.
'''

class Question:
    '''
        Question class
    '''
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self) -> str:
        return f'Question: {self.text}\nAnswer: {self.answer}'
