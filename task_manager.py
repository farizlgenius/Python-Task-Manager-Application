import file_manager as fm
import task as tk
import datetime as dt

class TaskManager:
    def __init__(self):
        datas = fm.FileManager().read_file()
        for data in datas:
            if data['status'] == 'pending' and 'due_date' in data and dt.datetime.strptime(data['due_date'], "%Y-%m-%d").date() < dt.datetime.now().date():
                data['status'] = 'overdue'
        self.tasks = datas

    def create_task(self,title, description, due_date):
        id = 0
        for task in self.tasks:
          if id <= task['id']:
            id = task['id'] + 1
        data = {
            "id": id,
            "title": title,
            "description": description,
            "status": "pending",
            "due_date": due_date
        }
        self.save_task(data)

    def show_all_tasks(self):
        completed_tasks = [task for task in self.tasks if task['status'].lower() == 'complete']
        overdue_tasks = [task for task in self.tasks if task['status'].lower() == 'overdue']
        pending_tasks = [task for task in self.tasks if task['status'].lower() == 'pending']
        self.print_table(completed_tasks, "Here are all the tasks with COMPLETE status:")
        self.print_table(overdue_tasks, "Here are all the tasks with OVERDUE status:")
        self.print_table(pending_tasks, "Here are all the tasks with PENDING status:")

    def show_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task['status'].lower() == 'complete']
        self.print_table(completed_tasks, "Here are all the tasks with COMPLETE status:")

    def show_overdue_tasks(self):
        overdue_tasks = [task for task in self.tasks if task['status'].lower() == 'overdue']
        self.print_table(overdue_tasks, "Here are all the tasks with OVERDUE status:")

    def show_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if task['status'].lower() == 'pending']
        self.print_table(pending_tasks, "Here are all the tasks with PENDING status:")
        return pending_tasks.__len__()

    def complete_task(self):
        num = self.show_pending_tasks()
        if num == 0:
            print("No pending tasks to complete.")
            return
        try:
            input_id = int(input("Enter the Task ID to mark as complete: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid Task ID.")
            return
        for task in self.tasks:
            if task['id'] == input_id:
                task['status'] = 'complete'
                fm.FileManager().write_file(self.tasks)
                return
        print(f"Task with ID {input_id} not found.")

    def save_task(self, task):  
        self.tasks.append(task)
        fm.FileManager().write_file(self.tasks)

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
