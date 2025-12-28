# Task Manager Application

A simple command-line based Task Manager application written in Python.  
It allows users to create, view, complete, delete, and search tasks, with task data stored locally.

## 📌 Project Description

The Task Manager Application is a terminal-based program that helps users manage their daily tasks efficiently.  
Users can:

- Add new tasks with a title, description, and due date
- View all existing tasks
- Mark tasks as completed
- Delete tasks
- Search for tasks using keywords

The application runs in a loop until the user chooses to exit.

## 🎯 Purpose

The purpose of this project is to:

- Practice modular Python programming
- Demonstrate basic file handling and task management logic
- Provide a simple productivity tool for personal task tracking

## 🛠 Installation

### Prerequisites

- Python 3.8 or higher installed

### Steps

1. Clone or download this repository.
2. Navigate to the project folder:

   ```bash
   cd task-manager
   ```

## ▶ How to Run the Program

Run the main script from your terminal:

```bash
python app.py
```

You will see a menu like:

```code
          ####################################
          Welcome to Task Manager Application!
          ####################################

          Please see menu details below:
          1. Add Task
          2. View Tasks
          3. Mark Complete Task
          4. Delete Task
          5. Search Task
          6. Exit
          Please select an option from the menu
          (1,2,3,4,5,6).

          ####################################

Enter the menu option:

```

Enter a number from 1–6 to perform an action.

## ⭐ Key Features

- Add Task — Create a task with title, description, and due date
- View Tasks — Display all saved tasks
- Complete Task — Mark a task as finished
- Delete Task — Remove a task permanently
- Search Task — Find tasks by keyword
- Persistent Storage — Tasks are saved to a local file (data.json)

## 🧪 Usage Examples

### Adding a Task

```code
Enter the menu option: 1
Enter Task Title: Finish homework
Enter Task Description: Math and Science exercises
Enter Task Due Date (YYYY-MM-DD): 2025-01-10
```

### Viewing Tasks

```code
Enter the menu option: 2
```

### Searching for task

```code
Enter the menu option: 5
Enter search query: homework
```

### Exiting

```code
Enter the menu option: 6
```

## 📁 Project Structure

```code
task-manager/
│
├── main.py
├── task.py
├── task_manager.py
├── file_manager.py
├── data.json
└── README.md

```
