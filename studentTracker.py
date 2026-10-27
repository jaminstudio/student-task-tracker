import uuid
Tasks = [

]

Users = [

]

usernames = []

def login():
    username = input("Enter your username")
    password = input("Enter your Password")

    for user in Users:
        if user.username == username and user.password == password:
            print(f"Welcome {user.firstname} {user.lastname}")
            return user.id

    print("Username or Password incorrect")
    return None


def signup():
    usernameExists = True
    username = None
    password = None
    while usernameExists:
        username = input("Enter your preferred username")

        if not username in usernames:
            usernameExists = False
        else:
            usernameExists = True
            print("Username already exists please choose another")

        

    passwordMatch = False

    while not passwordMatch:
        password = input("Enter your Password")
        confirmPassword = input("Enter your password")

        if password == confirmPassword:
            passwordMatch = True
        else:
            print("Password don't macth please choose another")

    firstname = input("Enter your First Name")
    lastname = input("Enter your Last Name")
    id = uuid.uuid4
    user = {
        id:id,
        username:username,
        firstname:firstname,
        lastname:lastname,
        password:password,
    }

    usernames.append(username)

    Users.append(user)

    return user[id]

def addTask(user_id):
    taskName = input("Enter task name")
    taskDesc = input("Enter the task description")

    Tasks.append({
        "id" : uuid.uuid4,
        "owner" : user_id,
        "taskname" : taskName,
        "taskdesc" : taskDesc,
        "completed" : False
    })

def helpDeleteTask(id):
    for task in Tasks:
        if task["id"] == id:
            del task

def markTask(id):
    for task in Tasks:
        if task["id"] == id:
            task["completed"] = True

def viewTasks(user_id):
    userTasks = [

    ]

    for task in Tasks:
        if task["owner"] == user_id and task["completed"] == False:
            userTasks.append(task)

    for userTask in userTasks:
        print("--------------------------------")
        print(userTask["taskname"])
        print(userTask["taskdesc"])
        print("--------------------------------")



def completeTask(user_id):
    userTasks = [

    ]

    for task in Tasks:
        if task["owner"] == user_id:
            userTasks.append(task)

    i = 1
    for userTask in userTasks:
        print(f"{i}: ")
        print(userTask["taskname"])
        print(userTask["taskdesc"])
        print()

    task = int(input("Enter Task to mark complete"))

    taskId = userTasks[task - 1]["id"]

    markTask(taskId)

    print("task marked")

def deleteTask(user_id):
    userTasks = [

    ]

    for task in Tasks:
        if task["owner"] == user_id:
            userTasks.append(task)

    i = 1
    for userTask in userTasks:
        print(f"{i}: ")
        print(userTask["taskname"])
        print(userTask["taskdesc"])
        print()

    task = int(input("Enter Task to mark complete"))

    taskId = userTasks[task - 1]["id"]

    helpDeleteTask(taskId)

    print("task deleted")

def main():
    user = None
    while user == None:
        print("""
        1. Login
        2. Signup
        3. Quit
    """)
        userInput = input("")
        match (userInput):
            case "1":
                user = login()
            case "2":
                user = signup()
            case "3":
                break
            case _:
                print("Unknown Parameter")

    while user != None:
        print("""
        1. AddTask
        2. ViewTask
        3. Mark Task Completed
        4. Delete a Task
        5. Logout
    """)
        userInput = input("")
        match (userInput):
            case "1":
                addTask(user)
            case "2":
                viewTasks(user)
            case "3":
                completeTask(user)
            case "4":
                deleteTask
            case "5":
                pass

if __name__ == "__main__":
    main()