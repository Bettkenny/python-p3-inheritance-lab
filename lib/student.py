#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, new_knowledge):
        self.knowledge = []

        self.knowledge.append(new_knowledge)

        pass