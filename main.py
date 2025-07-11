tasks = []

def add_tasks(tasks):
    task = input("enter the task desciption: ")
    tasks.append({"desc": task, "done": False})
    print(f"Task{task} added")

def view_tasks(tasks):
    if not tasks:
        print("no tasks available")
    else:
        for index, task in enumerate(tasks):
            status = "✔" if task["done"] else "❌"
            print(f"{index + 1}.{task['desc']}[{status}]")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        tasks_number = int(input("enter the tasks number to mark as complete: "))
        
        tasks[tasks_number-1]["done"] = True
        print("marked as completed!")
    except(ValueError , IndexError):
        print("Invalid task number")

def delete_task(tasks):
    view_tasks(tasks)
    
    try:
        task_number = int(input("enter the taks you want to delete"))
        task = tasks.pop(task_number-1)
        print(f"task{task} deleted")
    except (ValueError,IndexError):
        print('invalide taks number')

      


while True:
    print("\n To-D0 List App")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. mark task as completed")
    print("4. delete task")
    print("5. exit")

    choice = input("choose the an option(1-5): ")

    if choice == "1":
        view_tasks(tasks)
    elif choice == "2":
        add_tasks(tasks)
    elif choice == "3":
        mark_completed(tasks)
    elif  choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Exiting the To-Do App. Goodbye!")
        break
    else: 
        print("Invalid input")
