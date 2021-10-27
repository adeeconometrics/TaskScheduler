"""
This module contain the scheduling algorithms used for the Application. 
Implementation on this project will contain FIFO and SJFS algorithm. 
"""

try:
    from typing import List, Union
    from uuid import uuid4
except Exception as e:
    print(f'Importing module {e} has caused an error.')


class Task:
    """
    Representation of Task inputted by the user. 
    """
    def __init__(self, id_number:int, title:str, 
                size:float, priority:int) -> None:

        if not (type(id_number) is int and type(priority) is int):
            raise TypeError(f'id_number and priority arguments must me of type int.')

        self.id_number = id_number
        self.title = title
        self.size = size
        self.priority = priority
        self.is_completed = False    

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

    def set_completed_task(self, task:Union[List[Task], Task]) -> None: 
        """
        Set completed task and update the status of that task.

        Args:
            task (Union[List[Task], Task]): pool of tasks that will be updated.
        """

        if type(task) is Task: 
            for item in filter(lambda x:x.id_number == task.id_number, self.task_list):
                self.task_list[self.task_list.index(item)].is_completed = True
            return None
        
        if isinstance(task,List):
            for id in [i.id_number for i in task]:
                for item in filter(lambda x:x.id_number == id, self.task_list):
                    self.task_list[self.task_list.index(item)].is_completed = True
            return None

        raise TypeError(f'task type is not valid: prescribed types are List[Task] or Task')

    def get_completed_task(self) -> List[Task]:
        """
        Returns:
            List[Task]: Independent copy completed tasks.
        """
        return list(filter(lambda x: x.is_completed, self.task_list))
        

    def get_pending_task(self) -> List[Task]:
        """
        Returns:
            List[Task]: Independent copy of pending tasks. 
        """
        return list(filter(lambda x: not x.is_completed, self.task_list))
        
    
if __name__ == '__main__':
    t1 = Task(1,'T2',5.5,1)
    t2 = Task(2,'T3',3.4,1)
    t3 = Task(3,'T4',1.4,2)
    t4 = Task(4,'T5',2.4,2)
    t5 = Task(5,'T6',3.5,3)
    t6 = Task(6,'T7',3.7,4)


    s = Scheduler([t1,t2,t3,t4,t5,t6])
    s.set_completed_task([t1, t2, t5])
    # print(*s.fifo(), sep='\n')
    print(*s.get_pending_task(), sep='\n')
    print('Completed tasks\n')
    print(*s.get_completed_task(), sep='\n')
    print('done!')