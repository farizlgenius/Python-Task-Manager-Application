runnning_flag = True

while runnning_flag:
    print('''
          ####################################
          Welcome to Task Manager Application!
          ####################################
          Please see menu details below:
          1. Add Task
          2. View Tasks
          3. Delete Task
          4. Exit
          Please select an option from the menu (1,2,3,4).
          ####################################
          ''')
    user_input = input("Enter the menu option: ").strip()

    if user_input == '4':
        runnning_flag = False
        print("Exiting the program.")
    elif user_input not in ['1', '2', '3']:
        print("Invalid option. Please try again.")
    elif user_input == '1':
        print("You selected: Add Task")
    elif user_input == '2':
        print("You selected: View Tasks")
    elif user_input == '3':
        print("You selected: Delete Task")