class Task:
  def __init__(self, id, title, description, status, due_date):
    self.id = id
    self.title = title
    self.description = description
    self.status = status
    self.due_date = due_date

  def __str__(self):
    return f"Task(ID: {self.id}, Title: {self.title}, Description: {self.description}, Status: {self.status}, Due Date: {self.due_date})"