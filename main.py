import asyncio
import random
from rich import print
import logging

# Set up logging
logging.basicConfig(
    filename="task_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)
logger = logging.getLogger()

class Node:
    def __init__(self, name):
        self.name = name
        self.inbox = asyncio.Queue()

    async def send(self, message, to_node):
        await asyncio.sleep(random.uniform(0.1, 0.5))  # Simulate network delay
        await to_node.inbox.put((self.name, message))
        print(f"[green]{self.name} sent task: '{message}' to {to_node.name}[/green]")

class Manager(Node):
    def __init__(self, name, workers, tasks):
        super().__init__(name)
        self.workers = workers
        self.tasks = tasks
        self.completed_tasks = 0

    async def assign_tasks(self):
        # Assign tasks only to eligible workers (matching specialization)
        for task in self.tasks:
            eligible_workers = [w for w in self.workers if w.task_type in task]

            if eligible_workers:
                worker = random.choice(eligible_workers)  # Choose a worker who can handle the task
                await self.send(task, worker)
                await asyncio.sleep(0.3)  # Simulate time between assignments
            else:
                print(f"[red]No worker available for task {task}[/red]")
        await self.monitor_tasks()

    async def monitor_tasks(self):
        # Monitor completion of tasks
        while self.completed_tasks < len(self.tasks):
            await asyncio.sleep(1)
        print(f"\n[bold green]All tasks completed![/bold green]")

class Worker(Node):
    def __init__(self, name, task_type=None):
        super().__init__(name)
        self.task_type = task_type  # Task specialization

    async def listen(self):
        while True:
            sender, message = await self.inbox.get()
            print(f"[cyan]{self.name} got task: '{message}' from {sender}[/cyan]")

            # Check if task matches worker's specialization
            if self.task_type and self.task_type not in message:
                print(f"[red]{self.name} cannot process task '{message}'[/red]")
                continue

            # Simulate task processing (No failure simulation now)
            process_time = random.uniform(0.5, 1.5)
            await asyncio.sleep(process_time)
            print(f"[yellow]{self.name} completed task: '{message}' in {process_time:.2f}s[/yellow]")

            # Log completion to file
            logger.info(f"{self.name} completed: {message}")
            manager.completed_tasks += 1


async def main():
    # Create workers with task specialization
    workers = [Worker(f"Worker-{i}", task_type=f"Type-{i % 3}") for i in range(1, 6)]
    
    # Tasks to assign: Ensure they match worker types better
    tasks = []
    for i in range(1, 11):
        task_type = f"Type-{i % 3}"
        tasks.append(f"Task-{i} {task_type}")

    # Create manager
    manager = Manager("Manager", workers, tasks)

    # Start worker listeners
    for w in workers:
        asyncio.create_task(w.listen())

    # Assign tasks
    await manager.assign_tasks()

    # Wait for everything to finish
    await asyncio.sleep(5)

asyncio.run(main())
