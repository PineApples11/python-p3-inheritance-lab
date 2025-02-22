#!/usr/bin/env python

from user import User

class Student(User):
    # knowledge=[]
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # self.first_name=first_name
        # self.last_name=last_name
        self.knowledge=[]
    
    def learn(self,new_knowledge):
        # if new_knowledge == str:
            self.knowledge.append(new_knowledge)
        