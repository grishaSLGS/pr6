class Task:
    def __init__(self, title):  
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self): 
        status = "✓" if self.completed else "✗"
        return f"{status} {self.title}"

class TaskScheduler:
    def __init__(self): 
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

if __name__ == "__main__":  # Исправлено: name на __name__
    scheduler = TaskScheduler()
    scheduler.add_task("Купить молоко")
    scheduler.add_task("Сделать домашнее задание")
    scheduler.show_tasks()

