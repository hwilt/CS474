class Student:
    def __init__(self, name):
        self.name = name
        self.num_correct = 0
        self.num_incorrect = 0
    
    def get_name(self):
        return self.name

    def addCorrect(self):
        self.num_correct += 1

    def addIncorrect(self):
        self.num_incorrect += 1

    def reset_num_correct(self):
        self.num_correct = 0

    def reset_num_incorrect(self):
        self.num_incorrect = 0

    def get_score(self):
        return self.num_correct / (self.num_correct + self.num_incorrect)