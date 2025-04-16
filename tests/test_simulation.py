# tests/test_simulation.py
import unittest
from main import Manager, Worker

class TestDistributedSystem(unittest.TestCase):
    
    def test_worker_creation(self):
        worker = Worker("Worker-1")
        self.assertEqual(worker.name, "Worker-1")
    
    def test_manager_creation(self):
        worker1 = Worker("Worker-1")
        manager = Manager("Manager", [worker1], ["Task-1"])
        self.assertEqual(manager.name, "Manager")

if __name__ == "__main__":
    unittest.main()
