import file_manager as fm
import task as tk
import task_manager as tm


runnning_flag = True
file_path = 'data.json'


while runnning_flag:
    print('''
          ####################################
          Welcome to Task Manager Application!
          ####################################

          Please see menu details below:
          1. Add Task
          2. View All Tasks
          4. Complete Task
          5. Delete Task
          6. Search Task
          7. Exit
          Please select an option from the menu (1,2,3,4).
          
          ####################################
          ''')
    user_input = input("Enter the menu option: ").strip()

    if user_input == '7':
        runnning_flag = False
        print("Exiting the program...")
    elif user_input not in ['1', '2', '3','4','5','6','7']:
        print("Invalid option. Please try again.")
    elif user_input == '1':
        title = input("Enter Task Title: ").strip()
        description = input("Enter Task Description: ").strip()
        due_date = input("Enter Task Due Date (YYYY-MM-DD): ").strip()
        task_manager = tm.TaskManager()
        task_manager.create_task(title, description, due_date)
        tm.TaskManager().show_all_tasks()
    elif user_input == '2':
        print("You selected: View Tasks")
        tm.TaskManager().show_all_tasks()
    elif user_input == '3':
        print("You selected: Delete Task")