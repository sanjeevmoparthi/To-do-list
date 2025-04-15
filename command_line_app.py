import json
import os

TASKS_FILE = "tasks.json"

def load_task():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE,'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE,'r') as file:
        return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE,'W') as file:
        json.dump(tasks,file,indent = 2)


def view_tasks(tasks):
    if not tasks:
        print("No task yet")
    else:
        print("\nYour to-do_list:")
        for i,task in enumerate(tasks,start = 1):
            status = "done" if task['completed'] else " not done"
            print(f"{i}.{task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task title:").strip()
    if title:
        tasks.append({"title":title,"completed":False})
        print("Task added")
    else:
        print("task title can not be empty")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("enter task number to mark as complete: ")) -1
        if 0<= index <len(tasks):
            tasks[index]['completed'] = True
            print("task marked as complete.")
        else:
            print("please enter a valid number")

    except ValueError:
        print("please enter a valid number")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete")) -1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task:{removed['title']} ")
        else:
            print("invalid task number.")
    except ValueError:
        print("please enter a valid number.")



def main():
    tasks = load_tasks()

    while True:
        print("\n to do list mennu:")

        print("1.view Tasks")
        print("2.ADD Tasks")
        print("3.complete Tasks")
        print("4. delete task")
        print("5. save and exit")
        
        choice = input("enter your choice (1-5):")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    main()

        

        
