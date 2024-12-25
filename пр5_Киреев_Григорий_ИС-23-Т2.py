class Task:
def init (self, title):
self.title = title
self.completed = False
def complete(self):
self.completed = True
def str (self):
status = "✓" if self.completed else "✗"
return f"{status} {self.title}"
class TaskScheduler:
def init (self):
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
if name == " main ":
scheduler = TaskScheduler()
scheduler.add_task("Купить молоко")
scheduler.add_task("Сделать домашнее задание")
scheduler.show_tasks()
