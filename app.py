import file_manager as fm
import task as tk
import task_manager as tm


# Main application loop
runnning_flag = True 
file_path = 'data.json'


while runnning_flag:
    print('''
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
          Please select an option from the menu (1,2,3,4,5,6).
          
          ####################################
          ''')
    
    user_input = input("Enter the menu option: ").strip()

    # Handle user input and call appropriate methods
    # Exit the application
    if user_input == '6':
        runnning_flag = False
        print("Exiting the program...")
    # Invalid option handling
    elif user_input not in ['1', '2', '3','4','5','6']:
        print("Invalid option. Please try again.")
    # Add Task
    elif user_input == '1':
        title = input("Enter Task Title: ").strip()
        description = input("Enter Task Description: ").strip()
        due_date = input("Enter Task Due Date (YYYY-MM-DD): ").strip()
        task_manager = tm.TaskManager()
        task_manager.create_task(title, description, due_date)
        tm.TaskManager().show_all_tasks()
    # View Tasks
    elif user_input == '2':
        tm.TaskManager().show_all_tasks()
    # Mark Complete Task
    elif user_input == '3':
        tm.TaskManager().complete_task()
    # Delete Task
    elif user_input == '4':
        tm.TaskManager().delete_task()
    # Search Task
    elif user_input == '5':
        search_query = input("Enter search query: ").strip()
        tm.TaskManager().search_task(search_query)
    # Invalid option handling
    else:
        print("Invalid option. Please try again.")