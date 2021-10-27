"""
This module contains the implementation of 
classes for the Application Interface.    
"""

try:
    import os, sys # check the reference on project specification.
    from typing import List, Dict 
    from Scheduler import Task, Scheduler
except Exception as e:
    print(f'Importing module {e} has caused an error.')


class FileHandler:
    """
    Responible for handling files. 
    """
    def __init__(self):
        ...

    def read_file(self):
        ...
    
    def write_file(self):
        ...

class Interface:
    """
    Responsible for communicating with the user.
    """
    def __init__(self, task:Task, file:FileHandler, scheduler:Scheduler):
        ...
    
    def view_project(self):
        ...
    
    def get_project(self):
        ...


if __name__ == '__main__':
    # todo
    # implement the interface of the application. 

    # while True:
        # show all choices