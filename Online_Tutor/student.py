class Student:
    def __init__(self, name):
        self.name = name
        self.num_correct = 0
        self.num_incorrect = 0
    
    def get_name(self):
        return self.name

    def addCorrect():
        self.num_correct += 1

    def addIncorrect():
        self.num_incorrect += 1

    def get_num_correct(self):
        return self.num_correct

    def get_num_incorrect(self):
        return self.num_incorrect

    def get_score(self):
        return self.num_correct / (self.num_correct + self.num_incorrect)