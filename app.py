import file_manager as fm
import task as tk


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
          7. Search Task
          6. Exit
          Please select an option from the menu (1,2,3,4).
          
          ####################################
          ''')
    user_input = input("Enter the menu option: ").strip()

    if user_input == '4':
        runnning_flag = False
        print("Exiting the program...")
    elif user_input not in ['1', '2', '3']:
        print("Invalid option. Please try again.")
    elif user_input == '1':
        print("You selected: Add Task")
        task_list = fm.FileManager(file_path).read_file()
        for task in task_list:
            task_obj = tk.Task(task['id'], task['title'], task['description'], task['status'], task['due_date'])
            print(task_obj)
    elif user_input == '2':
        print("You selected: View Tasks")
    elif user_input == '3':
        print("You selected: Delete Task")