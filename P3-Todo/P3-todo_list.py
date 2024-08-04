
todo_list = []

while(True):
    user_action = input("Enter a command (add, view, remove, exit): ")

    if(user_action == "add"):
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added.")
        
    elif todo_list:    
        if(user_action == "view"):
            for task in todo_list:
                print(task)
        elif(user_action == "remove"):
            task = input('task name: exit')
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        else:
            print("No tasks to display.")
            
    elif(user_action == "exit"):
        break
    else:
        print("Invalid command")

