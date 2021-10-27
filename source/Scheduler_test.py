from unittest import TestCase
from Scheduler import Scheduler, Task

class TestScheduler(TestCase): 
    def setUp(self) -> None:
        self.t1 = Task(1,'T2',5.5,1)
        self.t2 = Task(2,'T3',3.4,1)
        self.t3 = Task(3,'T4',1.4,2)
        self.t4 = Task(4,'T5',2.4,2)
        self.t5 = Task(5,'T6',3.5,3)
        self.t6 = Task(6,'T7',3.7,4)

        self.s = Scheduler([self.t1,self.t2,self.t3,self.t4,self.t5,self.t6])
    
    def test_fifo(self): 
        self.assertEqual(self.s.fifo()[0], self.t2)
        self.assertEqual(self.s.fifo()[-1], self.t6)

    def test_get_completed_task(self): 
        self.s.set_completed_task([self.t1, self.t2, self.t5])
        self.assertTrue(all(lambda x: x in self.s.get_completed_task() for x in [self.t1, self.t2, self.t5]))

    def test_pending_task(self): 
        self.assertTrue(all(lambda x: x in self.s.get_pending_task() for x in [self.t3, self.t4, self.t6]))