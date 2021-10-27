"""
This module contain the scheduling algorithms used for the Application. 
Implementation on this project will contain FIFO and SJFS algorithm. 
"""

try:
    from typing import List
    from uuid import uuid4
except Exception as e:
    print(f'Importing module {e} has caused an error.')


class Task:
    """
    Representation of Task inputted by the user. 
    """
    def __init__(self, title:str, size:float, priority:int, is_completed:bool = False) -> None:
        self.id_number = uuid4()
        self.title = title
        self.size = size
        self.priority = priority
        self.is_completed = is_completed    

    def __str__(self) -> str:
        return (f'id number: {self.id_number} \n'
                f'title: {self.title} \n'
                f'size: {self.size} \n'
                f'priority: {self.priority} \n' 
                f'is completed: {self.is_completed} \n')

class Scheduler:
    """
    Responsible for handling the schedule of the task.
    """
    task_list:List[Task] = []
    is_sorted:bool = False

    def __init__(self, task:List[Task]) -> None:
        self.task_list.extend(task)
        
    def __shortest_job_next(self)->None:
        """
        Implementation of Shortest Job First Scheduling algorithm.
        """
        self.task_list.sort(key = lambda x: (x.priority, x.size))
        self.is_sorted = True
    
    def fifo(self) -> List[Task]:
        """
        Returns:
            List[Task]: FIFO wrapper of the SJF algorithm.
        """
        if not self.is_sorted:
            self.__shortest_job_next()

        task_queue = self.task_list.copy()
        return task_queue

    def create_schedule(self, task:List[Task]) -> None:
        """
        Extends constructor so you would not need to instantiate over and over.
        
        Args:
            task (List[Task]): pool of tasks to be scheduled.
        """
        self.task_list.extend(task)
        self.is_sorted = False

    def view_schedule(self) -> None:
        """
        Prints the scheduled pooled in the scheduler.
        """
        for i in self.fifo():
            print(i) 
        
    
if __name__ == '__main__':
    t2 = Task('T2', 5.5, 1)
    t1 = Task('T1', 3.4, 1)

    s = Scheduler([t1,t2])
    for i in s.fifo():
        print(i)
    print('done!')