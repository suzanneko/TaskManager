# TaskManager

## Title: task_manager.py

### Description
This project was built with the goal of providing businesses with a task management system that reads and writes to two external files, the first listing user and password information, and the second listing task information.  Users are required to login with a username and password and view a menu of options, including adding tasks and viewing tasks.  The system enables administrator login which allows additional functionality, including registering new users and viewing statistics on the number of users and tasks. 

### Table of contents 
- [TaskManager](#taskmanager)
  * [Title: task_manager.py](#title--task-managerpy)
    + [Description](#description)
    + [Table of contents](#table-of-contents)
    + [How to install](#how-to-install)
    + [How to use](#how-to-use)
      - [Data source](#data-source)
        * [tasks.txt](#taskstxt)
        * [users.txt](#userstxt)
      - [Login](#login)
      - [Menu](#menu)
        * [r - registering a user](#r---registering-a-user)
        * [a - add a task](#a---add-a-task)
        * [va - View all tasks](#va---view-all-tasks)
        * [gr - Generate Reports](#gr---generate-reports)
        * [vm - View my task](#vm---view-my-task)
        * [s - Display statistics](#s---display-statistics)
    + [Credits](#credits)

### How to install

Ensure that the program file and the source data text files 'tasks.txt' and 'user.txt' are located in the same folder.

### How to use
#### Data source
The source of the data used by the program are two text files named 'tasks.txt' and 'user.txt'.  
##### tasks.txt
Each line of the 'tasks.txt file represents a different task. The information given is: the username of the user the task is assigned to, the task title, task description, date task was assigned, date task is due and whether the task is complete or not. Each item of data is separated by a comma and space. See example below:
e.g.admin, Assign initial tasks, Use taskManager.py to assign each team member with appropriate tasks, 10 Oct 2019, 25 Oct 2019, No

<img width="953" alt="image" src="https://user-images.githubusercontent.com/121255678/217745448-9ca5eba8-96e5-49ea-a05c-0f61a52158d0.png">

##### users.txt
Each line of the 'users.txt' file represents a different user. The information given is:  username and password. Each item of data is separated by a comma and space.  See example below:
e.g.admin, adm1n

<img width="271" alt="image" src="https://user-images.githubusercontent.com/121255678/217765285-ed4cdfa7-6075-4a03-9940-792650c5fd9c.png">

#### Login
When the program is initiated, user authentification is commenced. The user is asked to input their username. If the username entered is valid, they are then asked to enter their password. Otherwise, they are prompted to try again. If the password is correct, the user is shown a menu to select from. Otherwise, they are prompted to try to enter their username and password again.

#### Menu
Following successful authentification, the user is presented with a menu from which to select an option.  The menu presented to admin displays two options that are not given to other users: 'Generate Reports' and 'Statistics'. 

Admin menu:

<img width="270" alt="image" src="https://user-images.githubusercontent.com/121255678/217797870-026cb500-85bc-4ea1-9ab1-9c0305a3f4ee.png">

Menu for all other users:

<img width="217" alt="image" src="https://user-images.githubusercontent.com/121255678/217798070-0c91586e-b22b-4599-97c7-aeccdbd5174d.png">

##### r - registering a user
The user must be the 'admin' in order to register a user, otherwise a message is printed informing them that this is the case. If they are the admin, they will be prompted to add the new username, the new password and to reconfirm the password.  The 'user.txt' file is updated with the new information.


<img width="214" alt="image" src="https://user-images.githubusercontent.com/121255678/217796454-9b2e20ab-2163-4596-88ce-b9338582af41.png">

If the passwords do not match, an error message is printed, asking the user to try again.


<img width="238" alt="image" src="https://user-images.githubusercontent.com/121255678/217796977-23fa0adf-1182-496d-a580-2bc6ebddfb97.png">

##### a - add a task
All users may add a task. The user is prompted to enter: the username of the person the task is assigned to, the task title, the task description and the date the task is due. The 'tasks.txt' file is updated with the new task.

<img width="488" alt="image" src="https://user-images.githubusercontent.com/121255678/217798884-7a28119d-b875-4ca8-a23b-f6bd4997a5eb.png">

##### va - View all tasks
All users may view all tasks. All the tasks in 'tasks.txt' are displayed in a user-friendly format as shown in the image below:

<img width="611" alt="image" src="https://user-images.githubusercontent.com/121255678/217808966-0341b968-1c20-42ac-b9e8-3959690cc6ef.png">

##### gr - Generate Reports
Only the admin user is presented with this option in their menu.  The 'generate_reports' function generates 2 reports in text files named 'task_overview' and 'user_overview'. 

###### task_overview.txt
The 'task_overview' report gives statistics on the total number of tasks, the number of completed, uncompleted, and uncompleted and overdue tasks.

<img width="707" alt="image" src="https://user-images.githubusercontent.com/121255678/217853220-a858eff1-fcfb-4c1e-baac-3f4faf8e0343.png">

###### user_overview.txt
The 'user_overview' report gives statistics for each user on the total number of tasks assigned to the user, as well as the percentage of completed, uncompleted and overdue tasks.

<img width="758" alt="image" src="https://user-images.githubusercontent.com/121255678/217853086-e78305f5-f598-4cb0-8a9b-af30f63f775f.png">

##### vm - View my task

The 'view_mine' function displays the tasks assigned to the user who is logged in. It displays tasks with a task number and the user may then select the task to edit it. If a task is selected, they are given the option to mark the task as completed or edit the task if the task status is showing it is not complete. If they choose to edit the task, they may choose between changing the due date of the task or the person the task is assigned to.  All changes are written to the original 'tasks.txt' file.

<img width="580" alt="image" src="https://user-images.githubusercontent.com/121255678/217851614-ea3807ee-f5f7-4a37-8abe-9152c8d56019.png">

##### s - Display statistics

#The 'statistics' function checks whether the 'task_overview.txt' file exists. If it does, the data is read and printed from the task_overview.txt' and 'user_overview.txt' files.

<img width="727" alt="image" src="https://user-images.githubusercontent.com/121255678/217853382-f31baee4-0886-42f4-98d5-f7ad5270c9a9.png">

<img width="697" alt="image" src="https://user-images.githubusercontent.com/121255678/217853552-dd68f9ea-cfe1-43be-8f7c-ed967f23df7a.png">

    
### Credits
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

https://www.hyperiondev.com/ - task designed by HyperionDev as part og their Software Engineering Bootcamp
