import file_manager as fm
import task as tk

class TaskManager:
    def __init__(self):
        pass
    
    def create_task(self,title, description, due_date):
        tasks = fm.FileManager().read_file()
        id = 0
        for task in tasks:
          if id <= task['id']:
            id = task['id'] + 1
        data = {
            "id": id,
            "title": title,
            "description": description,
            "status": "incomplete",
            "due_date": due_date
        }
        self.save_task(data)

    def show_all_tasks(self):
        tasks = fm.FileManager().read_file()
        completed_tasks = [task for task in tasks if task['status'].lower() == 'complete']
        overdue_tasks = [task for task in tasks if task['status'].lower() == 'overdue']
        pending_tasks = [task for task in tasks if task['status'].lower() == 'pending']
        self.print_table(completed_tasks, "Here are all the tasks with COMPLETE status:")
        self.print_table(overdue_tasks, "Here are all the tasks with OVERDUE status:")
        self.print_table(pending_tasks, "Here are all the tasks with PENDING status:")

    def show_completed_tasks(self):
        tasks = fm.FileManager().read_file()
        completed_tasks = [task for task in tasks if task['status'].lower() == 'complete']
        self.print_table(completed_tasks, "Here are all the tasks with COMPLETE status:")

    def show_overdue_tasks(self):
        tasks = fm.FileManager().read_file()
        overdue_tasks = [task for task in tasks if task['status'].lower() == 'overdue']
        self.print_table(overdue_tasks, "Here are all the tasks with OVERDUE status:")

    def show_pending_tasks(self):
        tasks = fm.FileManager().read_file()
        pending_tasks = [task for task in tasks if task['status'].lower() == 'pending']
        self.print_table(pending_tasks, "Here are all the tasks with PENDING status:")

    def save_task(self, task):  
        tasks = fm.FileManager().read_file()
        tasks.append(task)
        fm.FileManager().write_file(tasks)

    def print_table(self,tasks, title):
      if not tasks:
        print(f"\n{title}")
        print("No tasks found.\n")
        return

      print(f"\n{title}")
      print("-" * 78)
      print(f"{'ID':<4} | {'Title':<20} | {'Description':<25} | {'Status':<10} | {'Due Date':<10}")
      print("-" * 78)

      for task in tasks:
        print(f"{task['id']:<4} | {task['title']:<20} | {task['description']:<25} | {task['status']:<10} | {task['due_date']:<10}")

      print("-" * 78)
