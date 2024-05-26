#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name = 'john doe',job = 'Sales'):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name
        pass

    def set_name(self,name):
        if (type(name) is str) and (len(name) > 1 and len(name) < 25):
            name = name.title()
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.") 

    name = property(get_name,set_name)

    def get_job(self):
        return self._job
    
    def set_job(self,job):
        self._job = None
        for approvedJob in APPROVED_JOBS:
            if job == approvedJob:
                self._job = job
        if self._job == None:
            print("Job must be in list of approved jobs.")        
        pass

    job =  property(get_job,set_job)
Jane = Person()
print(Jane.name)