# The following program enables a business to manage tasks by assigning them to users. 
# Users are able to login, add tasks, view all tasks and view only their tasks.
# Admin is able to login, register users, add tasks, view all tasks, view only their task and generate reports with statistics on the tasks and users.

from datetime import datetime
import os.path

# Functions defined below:

# The 'print_menu' function prints out a menu of options - with different menus depending on whether admin or other is logged in.
    # The input is converted to lower case so that both upper and lower case responses are allowed.


def print_menu(name_entered):
    if name_entered=="admin":
        menu = input('''\nSelect one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate Reports
    s - Display statistics
    e - Exit
    : ''').lower()
        return menu
    else:
        menu = input('''\nSelect one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
        return menu

 # The 'reg_user' function allows the admin to register a new user.  An if statement is used to check admin is logged in.  
            # Within a while loop, the user is prompted to enter a new username. A try except else statement checks if the username is in the list of existing usernames. If it is, the user is asked to try again.
            # If the username is not in the list the user is prompted to enter a password, and re-enter to confirm.
            # An if statement checks that the passwords match and the new data is written to the 'user.txt' file. 
        # Error messages are returned if admin is not logged in or passwords do not match.

def reg_user(name_entered,user_list):
    f=open("user.txt","a+")
    if name_entered=="admin":
        while True:
            new_username=input("Enter the new username:")
            try:
                find_duplicates=user_list.index(new_username)
            except ValueError:
                new_password=input("Enter the new password:")
                password_confirm=input("Re-enter the new password to confirm:")
                if new_password==password_confirm:
                    f.write(f"\n{new_username}, {new_password}")
                    break
                else:
                    print("The passwords did not match.  Please try again.")
            else:
                print("The username you have entered has already been used. Please try another username:")
    else:
        print("Admin login required to register new users.")
    f.close()

 # The 'add_task' function allows the user to add a task.
        # The user enters information about the task including the person assigned to, the title, task description and due date.
        # The current date is imported from the datetime library.
        # The information is written to the 'tasks.txt' file. 'No' is added to the information, giving the completion status of the task.

def add_task():
    f2=open("tasks.txt","a+")
    name_task=input("Enter the username of the person whom the task is assigned to:")
    title_task=input("Enter the title of the task:")
    descript_task=input("Enter a description of the task:")
    duedate_task=input('''Enter the due date of the task using the format as shown in the example-
    Example format for date: 30 Jan 2023
    Enter your due date here: ''')
    today=datetime.today()
    current_date=today.strftime("%d %b %Y")
    task=str(f"\n{name_task}, {title_task}, {descript_task}, {current_date}, {duedate_task}, No")
    f2.write(task)
    f2.close()

# The 'view_all' function allows the user to view all the tasks. The data is read from the file 'tasks.txt'.
    # A for loop is used to go through the file line by line, storing the information from each line in a list.
        # The information is printed in the specified format.

def view_all():
    f2=open("tasks.txt","r")
    for line in f2:
        if line!="\n":
            line=line.split(", ")
            print(f'''
        ________________________________________________________________________
            Task:\t\t\t{line[1]}
            Assigned to:\t\t{line[0]}
            Date assigned:\t\t{line[3]}
            Due date:\t\t\t{line[4]}
            Task Complete?\t\t{line[5]}
            Task description:
            {line[2]}
        ________________________________________________________________________
            ''')
    f2.close()

# The 'view_mine' function allows the user who is logged in to see their tasks only. It displays tasks with a task number and the user may then select the task to edit it.
    # A dictionary named 'task_database' is created where the task number is the key and the value is the task data in list format.
    # This is achieved by using a for loop and enumerate object to give each task a number, which is then used as the key in 'task_database'. The data for each task is stored in a list using the split() method.
        # If the person assigned to the task is the same as the user logged in, the task is printed.
    # The user is then given the option to return to the main menu or select a task. If a task is selected, they are given the option to mark the task as completed or edit the task if the task status is showing it is not complete. 
    # If they choose to edit the task, they may choose between changing the due date of the task and the person the task is assigned to.
    # Each change is made to the 'task_database' dictionary.
    # A for loop iterates through the values in the 'task_database' dictionary, joining the lists of data into strings and writing the tasks back to the 'tasks.txt' file. 

def view_mine(name_entered):
    f2=open("tasks.txt","r")
    task_database={}
    for line_num,line in enumerate(f2,1):
        line=line.replace("\n","")
        task_database[line_num]=line.split(", ")
    for task in task_database:
        if task_database[task][0]==name_entered:
                print(f'''
        ________________________________________________________________________
            Task number {task}
            Task:\t\t\t{task_database[task][1]}
            Assigned to:\t\t{task_database[task][0]}
            Date assigned:\t\t{task_database[task][3]}
            Due date:\t\t\t{task_database[task][4]}
            Task Complete?\t\t{task_database[task][5]}
            Task description:
            {task_database[task][2]}
        ________________________________________________________________________
            ''')       
    f2.close()

    task_selection=int(input("Select a task by entering the task number or enter '-1' to return to the main menu:"))
    if task_selection!=-1:
        edit_selection=input("Type 'c' to mark the task as complete or 'e' to edit the task:")
        if edit_selection=="c":
            task_database[task_selection][5]="Yes"
        else:
            if task_database[task_selection][5]=="No":
                edit_user_or_due_date=input("Type 'a' to change the person the task is assigned to or 'd' to change the due date:")
                if edit_user_or_due_date=="a":
                    new_user=input("Enter the username of the new person that the task will be assigned to:")
                    task_database[task_selection][0]=new_user
                else:
                    new_due_date=input('''Enter the new due date of the task using the format as shown in the example-
    Example format for date: 30 Jan 2023
    Enter your due date here: ''')
                    task_database[task_selection][4]=new_due_date
            if task_database[task_selection][5]=="Yes":
                print("\nThe task you have selected cannot be edited as it is marked as complete.")

    f2=open("tasks.txt","w")

    for value in task_database.values():   
        f2.write(str(f"{', '.join(value)}\n"))

    f2.close()

# The 'generate_reports' function generates 2 reports in text files named 'task_overview' and 'user_overview'. 
# The 'task_overview' report gives statistics on the total number of tasks, the number of completed, uncompleted, and uncompleted and overdue tasks.
# The 'user_overview' report gives statistics for each user on the total number of tasks assigned to the user, as well as the percentage of completed, uncompleted and overdue tasks.

def generate_reports():
    f2=open("tasks.txt","r")
    f2_overview=open("task_overview.txt","w+")
    f_overview=open("user_overview.txt","w+")
    f=open("user.txt","r")

    contents=""
    count_tasks=0
    count_overdue_tasks=0
    count_users=0
    users=[]
    tasks_assigned_to_user=[]
    tasks_assigned_to_user_completed=[]
    tasks_assigned_to_user_overdue=[]

    # The 'user.txt' file is read below. The data is looped through and an if statement ensures that any blank rows are ignored. 
    # The number of users is counted and a list of users is generated, as well as creating lists to be populated to record the total/completed and overdue number of tasks assigned by user.


    for line in f:
        if line!="\n":
            count_users+=1
            line=line.strip()
            line=line.split(", ")
            users.append(line[0])
            tasks_assigned_to_user.append(0)
            tasks_assigned_to_user_completed.append(0)
            tasks_assigned_to_user_overdue.append(0)

    # The 'tasks.txt' file is read below. The data is looped through and an if statement ensures that any blank rows are ignored. The number of tasks is counted and each task is split into list form.
            # An if statement checks if the task is incomplete and the due date has passed, to count overdue tasks.
            # A for loop checks each task for each user and counts occurences where the task is assigned to the user, the task is completed and the task is not complete and overdue.
    # The statistics are then written to the 'task_overview' and 'user_overview' files.

    for line in f2:
        if line!="\n":
            count_tasks+=1
            contents+=line
            line=line.strip()
            line=line.split(", ")
            due_date=line[4]
            due=datetime.strptime(due_date, "%d %b %Y")
            present=datetime.today()
            if line[5]=="No" and due.date() < present.date():
                count_overdue_tasks+=1
            for i in range(0,len(users)):
                if line[0]==users[i]:
                    tasks_assigned_to_user[i]+=1
                if line[0]==users[i] and line[5]=="Yes":
                    tasks_assigned_to_user_completed[i]+=1
                if line[0]==users[i] and line[5]=="No" and due.date() < present.date():
                    tasks_assigned_to_user_overdue[i]+=1
        
    complete_tasks=contents.count("Yes")
    uncompleted_tasks=count_tasks-complete_tasks
    percent_incomplete=round((uncompleted_tasks/count_tasks)*100)
    percent_overdue=round((count_overdue_tasks/count_tasks)*100)

    f2_overview.write(f'''
    ********************************Task Report********************************

    The total number of tasks that have been generated and tracked: {count_tasks}
    The total number of completed tasks: {complete_tasks}
    The total number of uncompleted tasks: {uncompleted_tasks}
    The total number of tasks that haven't been completed and are overdue: {count_overdue_tasks}
    The percentage of tasks that are incomplete: {percent_incomplete}%
    The percentage of tasks that are overdue: {percent_overdue}%

    ***************************************************************************
    ''')

    f_overview.write(f'''
    ********************************User Overview******************************

    The total number of users: {count_users}
    The total number of tasks that have been generated and tracked: {count_tasks}

    ***************************************************************************
    ''')
    for i in range(0,len(users)):
        if tasks_assigned_to_user[i]!=0:
            f_overview.write(f'''
    ********************************{users[i]} Report********************************
    The total number of tasks assigned to {users[i]}: {tasks_assigned_to_user[i]}
    The percentage of total tasks assigned to {users[i]}:{round((tasks_assigned_to_user[i]/count_tasks)*100)}%
    The percentage of tasks assigned to {users[i]} that have been completed:{round((tasks_assigned_to_user_completed[i]/tasks_assigned_to_user[i])*100)}%
    The percentage of the tasks assigned to {users[i]} that must still be completed:{round(100-((tasks_assigned_to_user_completed[i]/tasks_assigned_to_user[i])*100))}%
    The percentage of the tasks assigned to {users[i]} that have not yet been completed and are overdue:{round((tasks_assigned_to_user_overdue[i]/tasks_assigned_to_user[i])*100)}%
    *********************************************************************************
            ''')
        else:
            f_overview.write(f'''
    ********************************{users[i]} Report********************************
    The total number of tasks assigned to {users[i]}: {tasks_assigned_to_user[i]}
    The percentage of total tasks assigned to {users[i]}:n/a
    The percentage of tasks assigned to {users[i]} that have been completed:n/a
    The percentage of the tasks assigned to {users[i]} that must still be completed:n/a
    The percentage of the tasks assigned to {users[i]} that have not yet been completed and are overdue:n/a
    *********************************************************************************
            ''')


    f.close()
    f2.close()
    f_overview.close()
    f2_overview.close()

        
# The 'statistics' function checks whether the 'task_overview.txt' file exists. If it does, the data is read and printed from the task_overview.txt' and 'user_overview.txt' files.
# In the event that the 'task_overview.txt' file does not exist, the generate_reports() function is called to create them.


def statistics():
    check_file=os.path.exists("task_overview.txt")
    if check_file==False:
        generate_reports()

    f2_overview=open("task_overview.txt","r")
    f_overview=open("user_overview.txt","r")
    for line in f2_overview:
        print(line)
    for line in f_overview:
        print(line)
    
    f_overview.close()
    f2_overview.close()

# This section of the code reads the user and password data from 'user.txt'.  
# Spaces are removed and new lines replaced by commas so that the data can be converted to a list using split() method, where the comma is the separator.

f=open("user.txt","r+")
users=f.read()
users=users.replace(" ","")
users=users.replace("\n",",")
list_userpw=users.split(",")
user_list_1=[]
for i in range(0,len(list_userpw)):
    if i%2==0:
        user_list_1.append(list_userpw[i])
f.close()

# The next section uses the while loop to elicit the username and password input from the user and check they are valid.
    # First, the 'try' function uses the index() method to search for the name entered and return its position in the list. 
    # Except is used to return an error message when the username is not found.
    # If the name is on the list, the 'else' code firstly checks that the position of the username entered is even, so that it is a valid username, not a password on the list,else an error message is returned.
            # Once that is established as a valid username, the 'try' function asks for the user to input a password and searches for the password in the list, returning its position or returning an error message using the 'except' function.
            # The 'else' section checks that the password is the correct password for the given user name and returns an error message if not.


while True:
   
    try:
        name_entered=input("Enter your username:")
        user_check=list_userpw.index(name_entered)
    except ValueError:
        print("Oops!  That is not a valid username.  Please try again.")
    else:
        if user_check%2==0:
            try:
                pw_entered=input("Enter your password:")
                pw_check=list_userpw.index(pw_entered)
            except ValueError:
                print("Oops!  That is not a valid password.  Please try again.")
            else:
                if pw_check==user_check+1:
                    break
                else:
                    print("Oops!  That is not a valid password.  Please try again.")

        else:
            print("Oops!  That is not a valid username.  Please try again.")

while True:
    menu=print_menu(name_entered) 

    if menu=="r":
        reg_user(name_entered,user_list_1)
    elif menu=="a":
        add_task()
    elif menu=="va":
        view_all()
    elif menu=="vm":
        view_mine(name_entered)
    elif menu=="s":
        statistics()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    elif menu=="gr":
        generate_reports()
    else:
        print("You have made a wrong choice, Please Try again")


