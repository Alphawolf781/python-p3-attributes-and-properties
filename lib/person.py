#!/usr/bin/env python3

# List of approved jobs
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
    def __init__(self, name='Guido', job='Sales'):
        self.name = name  # Initialize using the property setter
        self.job = job    # Initialize using the property setter

    def get_name(self):
        return self._name
    
    
    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)

    def get_job(self):
        return self._job
    
    
    def set_job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job= property(get_job, set_job)
