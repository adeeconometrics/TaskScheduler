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
    try:
        completed_tasks = open('CompletedTasks.txt', 'x')
        pending_tasks = open('PendingTasks.txt', 'x')
    except FileExistsError:
        pass

    def __init__(self)->None:
        self.dirname = os.path.dirname(__file__)
        self.CompletedTasks_dir = os.path.join(self.dirname, 'CompletedTasks.txt')
        self.PendingTasks_dir = os.path.join(self.dirname, 'PendingTasks.txt')

    def read_completed_dir(self)->None:
        """
        Reads completed tasks in the completed directory.
        """
        with open(self.CompletedTasks_dir) as f:
            print(f.read())

    def read_pending_dir(self)->None:
        """
        Reads pending tasks in the pending directory.
        """
        with open(self.PendingTasks_dir) as f:
            print(f.read())

    def update_completed_dir(self, task:Task)->None:
        """
        Updates the status of completed tasks directory.
        :param name: task: Task instance that is marked as complete by the Scheduler.
        :param type: Task
        """
        with open(self.CompletedTasks_dir, 'a') as f:
            f.write(str(task))

    def update_pending_dir(self, task:Task)->None:
        """
        Updates the status of pending tasks directory.
        :param name: task: Task instance that is marked as complete by the Scheduler.
        :param type: Task
        """
        with open(self.PendingTasks_dir, 'a') as f:
            f.write(str(task))

class Interface:
    """
    Responsible for communicating with the user.
    """
    def __init__(self)->None:
        self.file_handler = FileHandler()
        self.scheduler = Scheduler()
    
    def view_project(self):
        ...
    
    def get_project(self):
        ...


    # todo
    # implement the interface of the application. 

    # while True:
        # show all choices

if __name__ == '__main__':
    t1 = Task(1,'T2',5.5,1)
    t2 = Task(2,'T3',3.4,1)
    t3 = Task(3,'T4',1.4,2)
    t4 = Task(4,'T5',2.4,2)
    t5 = Task(5,'T6',3.5,3)
    t6 = Task(6,'T7',3.7,4)

    file_handler = FileHandler()
    scheduler = Scheduler([t1,t2,t3,t4,t5,t6])
    scheduler.set_completed_task([t1, t2, t5])

    for task in scheduler.get_completed_task():
        file_handler.update_completed_dir(task)

    for task in scheduler.get_pending_task():
        file_handler.update_pending_dir(task)
        
    print('--- Pending tasks --- ')
    file_handler.read_pending_dir()
    print('--- Completed tasks --- ')
    file_handler.read_pending_dir()