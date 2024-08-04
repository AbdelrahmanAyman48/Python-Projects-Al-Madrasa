todo_list = []

while True:
    user_action = input("Enter a command (add, view, remove, exit): ")

    if user_action == "add":
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added.")
        
    elif user_action == "view":
        if todo_list:
            for task in todo_list:
                print(task)
        else:
            print("No tasks to display.")
            
    elif user_action == "remove":
        if todo_list:
            task = input('Enter the task name to remove: ')
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        else:
            print("No tasks to remove.")
            
    elif user_action == "exit":
        break
        
    else:
        print("Invalid command")
