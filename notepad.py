def add_task(tasks, descrs):
    task=input("Enter a task: ")
    if task in tasks:
        print("Oops! already have this task")
    else:
        descr=input("Enter a description: ")
        if descr in descrs:
            print("Oops! already have this description")
        else:
            print(f'The task and description has been succesfully added!')
            tasks.append(task)
            descrs.append(descr)


def view_task(tasks, descrs):
    if tasks:
        print("The tasks are:")
        for index, task in enumerate(tasks, start=1):
         print(f"task {index}: {task}")
    if descrs:
        print("The descriptions are: ")
        for index, descr in enumerate(descrs, start=1):
         print(f'Description {index}: {descr}')
    else:
        print("There are no tasks yet! ")
        

def save_tasks(tasks, descrs, filename="tasks.txt"):
 with open(filename, 'w') as file:
        for index, task in enumerate(tasks, start=1):
            file.write(f"Task {index}: {task}\n")
        for index, descr in enumerate(descrs, start=1):
            file.write(f"Description {index}: {descr}\n")
 print(f"File succesfully loaded! in {filename}")


def delete_tasks(tasks, descrs):
    task=input("Choose a task delete: ")
    if task in tasks:
        tasks.remove(task)
        print("task succesfully deleted!")
    else:
        print("task does not exist")
    descr=input("Choose a description to delete: ")
    if descr in descrs:
        descrs.remove(descr)
        print("description succesfully deleted!")
    else:
        print("description does not exist")
    

def rename_tasks(tasks):
    task=input("Enter a task to rename: ")
    if task in tasks:
        index=tasks.index(task)
        rename=input("Rename the task: ")
        tasks[index]=rename
        print("Sucessfuly renamed!")
    else:
        print("task does not exist")


def rename_descriptions(descrs):
    descr=input("Enter a description to rename: ")
    if descr in descrs:
        index=descrs.index(descr)
        rename=input("Rename the description: ")
        descrs[index]=rename
        print("Succesfully renamed!")
    else:
        print("Description does not exist")


def main():
    tasks=[]
    descrs=[]
    while True:
     print("1. Add Task ")
     print("2. View Tasks")
     print("3. Save Tasks")
     print("4. Rename Tasks")
     print("5. Rename Descriptions")
     print("6. Delete Tasks")
     print("7. Exit")

     choice=input("Enter a choice: ")
     if choice == '1':
        add_task(tasks, descrs)
     elif choice =='2':
        view_task(tasks,descrs)
     elif choice =='3':
        save_tasks(tasks, descrs)
     elif choice =='4':
        rename_tasks(tasks)
     elif choice =='5':
        rename_descriptions(descrs)
     elif choice=='6':
        delete_tasks(tasks,descrs)
     elif choice =='7':
        print("Goodbye")
        break
     else:
        print("invalid choice try again!")
    


if __name__=="__main__":
    main()

