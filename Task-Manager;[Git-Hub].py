# Title: Task Manager
# Date: 2022-11-30
# Author: Jordaan Clarke

# Description:
# A task manager application that has functionality to add users, add tasks, view tasks assigned, generate reports and display statistics from those reports.


# Define a function that asks the user to select an option from a menu and executes a defined function based on that choice.
def task_mgr():
    

# Block laying the groundwork for the other functions in the program | Reads from the task file and converts it into a usable format. 


    # Import the following modules: 'os' (everything); 'datetime' (specific functions: datetime and date). 
    import os
    from datetime import datetime, date

    DATETIME_STRING_FORMAT = "%Y-%m-%d"
    
    # Obtain the current date using the .today() method and assign to 'curr_date'. This will be used as the assigned date.
    curr_date = date.today()  
    
    # Access the filesystem and if 'tasks.txt' doesn"t exist, create the file.
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass

    # Open the file 'tasks.txt' in read-only mode. Read the contents, split using a newline as the delimiter and assign to a new list called 'task_data'.
    with open("tasks.txt", "r") as file:
        task_data = file.read().split("\n")
        
        # Use a list comprehension to loop through 'task_data' (ignoring empty strings) and reassign the result to 'task_data'.
        task_data = [x for x in task_data if x != ""]

    # Assign an empty list to a variable called 'task_list'. This will be used to capture output inside a for loop.
    task_list = []

    # Start a for loop that splits string values in 'task_data' using a semi-colon delimiter and assign them to a new list called 'task_components'. Create an empty dictionary within the loop.
    for x in task_data:
        
        # Assign an empty dictionary to a variable called 'current'.
        current = {}

        # Split the values in task_data using a semi-colon delimiter and assign them to a new list called 'task_components'.
        task_components = x.split(";")
        
        # Update 'current' with manual keys appropriate to the data they will store.
        # Iterate through the elements of "task_components" to populate the value pairs (i.e. {"first key": task_components[0], "second key": task_components[1]} etc.).
        current["username"] = task_components[0]
        current["title"] = task_components[1]
        current["description"] = task_components[2]
        current["due_date"] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        current["assigned_date"] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        current["completed"] = True if task_components[5] == "Yes" else False

        # Append the values from 'current' to 'task_list'.
        task_list.append(current)


# Functions.
# Block defining various functions used in the program | Contains all the key program logic.


    # Define a function that provides information about usernames and passwords, and can add users to a file.
    def check_cred(credential, choice, optional = "optional"):        
        
        
        # Open the file "user.txt" in read-only mode, split the values using whitespace as the delimiter and assign to a list called "user_data".
        with open("user.txt", "r") as user_file:
            user_data = user_file.read().split("\n")

        # Assign an empty dictionary to a variable called "username_password". This will be used to capture output from a for loop.
        username_password = {}

        # Start a for loop that iterates over 'user_data'.
        for x in user_data:
            
            # Split each line using a semi-colon as the delimiter. Everything preceding the semi-colon should be assigned to a variable called "username"; everything after should be assigned to "password". 
            username, password = x.split(";")
            
            # Assign 'username' and 'password' as a key:value pair in 'username_password'.
            username_password[username] = password            
            
        
        # Define an inner function that checks if the argument 'credential' passed to 'check_cred()' matches a key in the dictionary 'username_password'.
        def check_user():
            
            
            # If the user exists, returns 'True'; else, return 'False'.
            if credential in username_password.keys(): return True            
            else: return False      
    
    
        # Define an inner function that checks if the arguments 'credential' and 'optional' passed to 'check_cred()' match a key:value pair in the dictionary 'username_password'.
        def check_pass():
            
        
            # If 'optional' matches the value pair for the key 'credential', return 'True'; else, return 'False'.
            if username_password[credential] == optional: return True
            else: return False
    
    
        # Define an inner function that takes the arguments 'credential' and 'optional' and writes them to the file 'user.txt'.
        def add_user():
            
            
            # Update the dictionary 'username_password' with the passed key:value pair.
            username_password[credential] = optional
            
         # Open 'user.txt' in write mode and create an empty list called 'user_data' to capture the dictionary values.
            with open("user.txt", "w") as file:
                user_data = []
                
                # Iterate over 'username_password' and append the values to 'user_data'. Use an f-string to get the correct formatting and write the list to 'file'.
                for x in username_password:
                    user_data.append(f"{x};{username_password[x]}")
                file.write("\n".join(user_data))
                
        
        # Define an inner function that takes calculates how many users are registered.
        def check_length():
            return len(username_password)
        
        
        # Define an inner function that returns all users.
        def get_users():
            return username_password.keys()
         
         
        # Conditional block that calls 'check_user()', 'check_pass()' or 'add_user()' depending on the value of 'choice', and passes the result of the inner function as the return value of 'check_cred()'.
        if choice == True: return check_user()
        elif choice == False: return check_pass()
        elif choice == "add": return add_user()
        elif choice == "length": return check_length()
        elif choice == "users": return get_users()



    # Define a function that registers a new user.
    def reg_user():
        
        
        # Read input for a new username.
        new_username = input("New Username: ")
        
        # Conditional block that captures input for existing users.
        while check_cred(new_username, True) == True:
            print()
            print("Username already exists. Please enter a different username or enter 'break' to return to the menu.")
            new_username = input("New Username: ")
            
            # Conditional block that tests for the exit condition for this menu option.
            if new_username == "break": break
            else: continue
        
        
        # Conditional block for a valid new user.
        else:

            # Read input for a new password.
            new_password = input("New Password: ")

            # Confirm input for the password.
            confirm_password = input("Confirm Password: ")
            
            print()
            
            # Conditional block for valid password entry.
            if new_password == confirm_password:
                
                # Display an appropriate message and write the login credentials to 'user.txt'.
                print("New user added")
                check_cred(new_username, "add", new_password)
               

            # Conditional block for valid password entry.
            else:
                print("Passwords do no match")

        
    
    # Define a function that captures input for a date and converts it into a useable format.
    def update_date():
    
    
        while True:          
                    
            # Read input for the due date and convert using the .strptime() method.
            try:
                task_due_date = input("Enter the due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                return due_date_time
                break
            
            # Capture invalid date input.
            except ValueError:
                print("Invalid datetime format. Please use the format specified")
                print()



    # Define a function that writes tasks to a file.        
    def write_task():
        
    
        # Open the file 'tasks.txt' in write mode and assign an empty list to a variable called 'task_list_to_write'.
        with open("tasks.txt", "w") as file:
            task_list_to_write = []
            
            # Start a for loop that iterates over 'task_list' and manually assign the value pairs from the dictionary 'new_task' to a new list called 'str_attrs'.
            for x in task_list:
                str_attrs = [x["username"],
                             x["title"],
                             x["description"],
                             x["due_date"].strftime(DATETIME_STRING_FORMAT),
                             x["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                             "Yes" if x["completed"] else "No"
                             ]
                
                # Append the values from 'str_attrs' to 'task_list_to_write' and separate using a semi-colon delimter.
                task_list_to_write.append(";".join(str_attrs))
                
            # Write the values from 'task_list_to_write' to 'file' using a join with a newline delimiter.
            file.write("\n".join(task_list_to_write))
        
        # Display a message to indicate that the operation has completed.
        print()
        print("Changes have been saved.")
        
        
            
    # Define a function that enables the user to makes changes to task completion status, the assigned user or the due date.
    def edit_task():
        
        
        while True:
        
    
            # Read input for a task to edit, or to return to the menu.
            try:
                
                task_num = int(input("Enter the number of a task to update, or enter -1 to return to the menu: "))
                print()
                
                # Conditional block to explicitly return to the menu.    
                if task_num <= -1 or task_num == "": break
            
                # Conditional block to capture invalid task numbers, returning to the menu.
                elif task_num > len(task_list):
                    print("Input out of range. Returning to the main menu.")
                    break
                
                else:

                    
                    if task_num in range(len(task_list)):
                        
                        # Capture instances where the logged in user attempts to edit a task that isn't assigned to them.                        
                        if task_list[task_num]["username"] != curr_user:
                            print("This task is not assigned to you.")
                            print()
                            break
                        
                        # Conditional block that checks if the task has already been completed.
                        elif task_list[task_num]["completed"] == True: print("This task has already been completed. It cannot be edited."); break
                        
                        # Conditional block for the logged in user attempting to edit a valid selected task.
                        else:
                            print()
                            print("""Select one of the following options below: 

                    1:    Update task status
                    2:    Allocate task to another user
                    3:    Update due date
                    """)
                    
                    print()
                    
                    # Try block capturing logic to mark a task as complete, update a user, and update task due date.
                    try:
                        
                        # Read user input for the edit task menu selection.
                        edit_sel = int(input())                                                
                        
                        # Conditional block for marking task as complete.
                        if edit_sel == 1:                            
                                                        
                            # Read input for task completion state, and update the value pair for the key 'completed' in the selected dictionary.                            
                            task_cmplt = str.upper(input("Do you wish to mark the task as complete? Enter 'Y' or 'N': "))
                        
                            if task_cmplt == "Y": task_list[task_num]["completed"] = True
                            else: task_list[task_num]["completed"] = False
                        
                        
                        # Conditional block for updating the allocated user. 
                        elif edit_sel == 2:
                            
                            # Check if 'update_user' matches an existing key in the dictionary 'username_password'.
                            # If True, update the value pair in the seleted dictionary, otherwise, print a message and continue.
                            update_user = input("Enter the username of the person to allocate this task to: ")
                             
                            if check_cred(update_user, True) == True:
                                task_list[task_num]["username"] = update_user                            
                                
                            else:
                                print("Username not found.")
                                print()
                                continue             
                        
                        
                        # Conditional block for updating task due date.
                        elif edit_sel == 3:
                            
                            # Read input for a new task due date, and update the value pair for the key 'due_date' in the selected dictionary.
                            new_date = update_date()
                            task_list[task_num]["due_date"] = new_date
                            print("Due date updated.")
                            print()             
                                
                       
                    # Capture non-integer input for the edit menu option.  
                    except ValueError:
                        print("Menu option not recognised. Please try again.")
                        continue
                        
            
            # Capture invalid input for task selection, and return to the main menu.
            except ValueError:
                print("Invalid input. Returning to the main menu.")
                break
            
            
            # Save the changes to a file.
            write_task()

    
    
    # Define a function that adds a task.
    def add_task():
        

        # Read user input for who the task will be allocated to and assign to a variable called 'task_username'.
        task_username = input("Enter the username of the person assigned to the task: ")
        
        # Start a while loop that checks if the username provided is valid; offer the option to return to the menu if the username is invalid.
        while check_cred(task_username, True) == False:
            print("User does not exist. Please enter a valid username")
            print()
            task_username = input("Enter the username of the person assigned to the task, or enter 'break' to return to the menu: ")
            
            if task_username == "break": break
        
        else:
            
            # Read user input for a title and description of the task to be added and assign to the variables 'task_title' and 'task_description' respectively.
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
            
            # Capture the due date using the 'update_date()' function and assign to a variable called 'user_date'.
            user_date = update_date()      
            
            # Create a dictionary called 'new_task', set six keys ("username", "title", "description", "due_date", "assigned_date" and "completed").
            # The value pairs should be taken from the previously collected user input. The key "completed" should be assigned the value pair 'False'.
            new_task = {"username": task_username,
                        "title": task_title,
                        "description": task_description,
                        "due_date": user_date,
                        "assigned_date": curr_date,
                        "completed": False
                        }

            # Appent the the dictionary 'new_task' to 'task_list'.
            task_list.append(new_task)        
        
        
        # Save the changes to a file.
        write_task()
           


    # Define a function that displays different tasks based on the argument passed. It will display all tasks by default.
    def get_tasks(view = "va"):


        # Define an inner function that formats and prints tasks.
        def display_tasks():        
                      
            # Track the task number, create a new variable called 'disp_str' to capture the values, then use an f-string to concatenate and present the data in a user-friendly format.
            print(f"Task {count}:")
            disp_str = f"Task: \t\t {x['title']}\n"
            disp_str += f"Assigned to: \t {x['username']}\n"
            disp_str += f"Date Assigned: \t {x['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {x['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {x['description']}\n"
            print(disp_str)
            print("-----------------------------------")
            

        # Conditional block to display all tasks regardless of the user logged in.
        if view == "va":
            
            print("-----------------------------------")
            for count, x in enumerate(task_list, start = 0):
                display_tasks()
                
        # Conditional block to display tasks for the logged in user only.
        elif view == "vm":
             
             print("-----------------------------------")
             for count, x in enumerate(task_list, start = 0):                                       
                if x["username"] == curr_user: display_tasks()
                   

    
    # Define a function that displays all tasks.
    def view_all():
        
        
        # Start a while loop that prints all recorded tasks.
        while True:
            get_tasks()
            print()
            break
        
    
    
    # Define a function that displays all tasks assigned to the user logged in.
    def view_mine():
        
        # Display tasks for the logged in user.
        get_tasks("vm")
        
        # Enable the user to edit tasks assigned to them.    
        edit_task()
        
      
        
    # Define a function that generates reports about tasks and users.
    def gen_rep():
        
    
        # Import the copy module for use of the deepcopy() function.
        import copy
        
        # Calculate the total number of tasks that have been generated and tracked in the task manager.
        total_tasks = len(task_list)

        # Calculate the total number of completed and uncompleted tasks, and capture the result in two variables.
        complete = 0
        incomplete = 0
        
        for x in (task_list):
            if x["completed"] == True: complete += 1
            else: incomplete +=1
        
        # Calculate the total number of tasks that haven’t been completed and that are overdue, and capture the result in a variable.
        overdue = 0
        for x in (task_list):
            
            if curr_date > datetime.date(x["due_date"]): overdue += 1

        # Calculate the percentage of tasks that are incomplete.
        per_incmplt = (incomplete / total_tasks) * 100

        # Calculate the percentage of tasks that are overdue.
        per_ovrd = (overdue / total_tasks) * 100

        # Calculate the total number of users registered.
        total_users = check_cred("pass", "length")        

        # Capture the all users within a variable.
        user_list = check_cred("pass", "users")
        
        # Declare an empty dictionary which will be populated inside a for loop.
        user_task = {}
        
        # Start a for a loop that iterates over all users, dynamically populates a dictionary taking the username as the key, and assigns a list with four 0 integers as the value pair.
        # The list's value pairs {x: [0, 0, 0, 0} refer to: {username: [total tasks, # completed, # uncompleted, # overdue]} where '#' is shorthand for 'number of tasks'. 
        for y in user_list:
            user_task.update({y: [0, 0, 0, 0]})     
                
        # Start a for loop that iterates over all users, then iterates over all tasks, and if the user is assigned to a task, tracks and updates:
        # the number of tasks, the number of completed and uncompleted tasks, and of the uncompleted tasks, how many are overdue.
        for y in user_list:
            for x in (task_list):
                
                # Update total tasks per user.
                if x["username"] == y:
                    user_task[y][0] += 1                    
                
                    # Update the number of completed and uncompleted tasks per user.
                    if x["completed"] == True: user_task[y][1] += 1
                    else: user_task[y][2] += 1
                    
                    # Update the number of uncompleted tasks overdue.
                    if x["completed"] == False and curr_date > datetime.date(x["due_date"]): user_task[y][3] += 1
                
        
        # Declare a new dictionary as a deepcopy of 'user_task' so that calculations on values in this dictionary do not affect the original.
        user_perc = copy.deepcopy(user_task)
        
        # Start a for loop that iterates over 'user_list', peforms calculations on values in 'user_task' and assigns the results to the corresponding indices in 'user_perc'.
        for x in user_list:
            
            # Calculate the percentage of tasks assigned per user out of all tasks registered.
            try:
                user_perc[x][0] = (user_task[x][0] / total_tasks) * 100
            except ZeroDivisionError: pass
            
            # Calculate the percentage of tasks assigned per user that have been completed.
            try:                
                user_perc[x][1] = (round(user_task[x][1] / user_task[x][0], 2)) * 100
            except ZeroDivisionError: pass
            
            # Calculate the percentage of tasks assigned per user that haven't been completed.
            try:
                user_perc[x][2] = (round(user_task[x][2] / user_task[x][0], 2)) * 100
            except ZeroDivisionError: pass
            
            # Calculate the percentage of tasks assigned per user that haven't been completed and are overdue.
            try:
                user_perc[x][3] = (round(user_task[x][3] / user_task[x][0], 2)) * 100
            except ZeroDivisionError: pass
        

        # Open 'task_overview.txt' in write mode, creating the file if it doesn't exist.
        with open("task_overview.txt", "w") as file:        

            # Format the data as strings in a user-friendly way, assign and concatenate to a temporary variable called 'rep_str'.
            rep_str = "-----------------------------------\n\n"
            rep_str += f"Total tasks: \t\t   {total_tasks}\n"
            rep_str += f"Completed tasks: \t   {complete}\n"
            rep_str += f"Uncompleted tasks: \t   {incomplete}\n"
            rep_str += f"Overdue tasks: \t\t   {overdue}\n"
            rep_str += f"% of tasks uncompleted:    {round(per_incmplt, 2)}%\n"
            rep_str += f"% of tasks overdue: \t   {round(per_ovrd, 2)}%\n\n"
                 
            # Write the values from 'rep_str' to 'file'.
            file.write(rep_str)
       
       
        # Declare an empty list which will capture output inside a for loop. 
        rep_to_write = []
       
        # Open 'user_overview.txt' in write mode, creating the file if it doesn't exist.
        with open("user_overview.txt", "w") as file:
            
            # Format the total number of tasks and user in a user friendly way.
            rep_str = "-----------------------------------\n\n"
            rep_str += f"Total tasks: {total_tasks}\n"
            rep_str += f"Total users: {total_users}\n"
            rep_to_write.append(rep_str)
            
            # Start a for loop that iterates over the keys and values in 'user_perc'.
            # Format the data as strings in a user-friendly way, assign and concatenate to a temporary variable called 'rep_str'.
            for x, y in user_perc.items():
                rep_str = ["-----------------------------------\n\n",
                           f"Task information for user: {x} \n\n",                
                           f"Total tasks assigned: \t   {user_task[x][0]}\n",
                           f"% of all users' tasks: \t   {round(y[0], 2)}%\n",
                           f"% Completed: \t\t   {round(float(y[1]), 2)}%\n",
                           f"% Uncompleted: \t\t   {round(float(y[2]), 2)}%\n",
                           f"% Uncompleted and overdue: {round(float(y[3]), 2)}%"
                           ]
                
                # Append 'rep_str' to the list 'rep_to_write'.
                rep_to_write.append("".join(rep_str))
                
            # Write the values from 'rep_to_write' to 'file', joining each element with a newline delimiter.
            file.write("\n".join(rep_to_write))

        # Display a message to indicate that the operation has completed.
        print()
        print("Report data has been saved.")
        
 

    # Define a function that provides statistics about users and tasks.
    def stats():
        
        
        # Generate the task and user reports.
        gen_rep()  
        
        # Open the file 'task_overview.txt' in read-only mode. Read the contents, split using a newline as the delimiter and assign to a new list called 'task_rep'.
        with open("task_overview.txt", "r") as task_rep_file:
            task_rep = task_rep_file.read().split("\n")
        
        # Use a list comprehension to loop through 'task_rep' (ignoring empty strings) and reassign the result to 'task_rep'.
        task_rep = [x for x in task_rep if x != ""]
        
        # Open the file 'user_overview.txt' in read-only mode. Read the contents, split using a newline as the delimiter and assign to a new list called 'user_rep'.
        with open("user_overview.txt", "r") as user_rep_file:
            user_rep = user_rep_file.read().split("\n")
        
        # Use a list comprehension to loop through 'user_rep' (ignoring empty strings) and reassign the result to 'user_rep'.
        user_rep = [x for x in user_rep if x != ""]
        
        print()
        
        # Display task statistics on the console.
        print("Task Statistics:\n")
        for x in task_rep:
            print(x)
            
        print()
        
        # Display user statistics on the console.
        print("User Statistics:\n")
        for y in user_rep:
            print(y)
    
    

    # Define a function that triggers the exit routine and ends the program.
    def end():
        
        
        # Print a message about ending the program.
        # Raise a SystemExit exception with a '0' argument to indicate a successful termination.
        print("Logging you out.")     
        raise SystemExit(0) 


    print()



# Block controlling access to the other functions | Reads username and password data from a file, asks the user to enter their credentials and checks if they match any valid credentials in the file.


    # Open the file "user.txt" in write mode. If the file does not exist, create the file and add values for a default account in the format: "username;password".
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")
    

    # Assign the value 'False' to a variable called 'logged_in'. This will be used for comparison in a while loop.
    logged_in = False

    # Start a while loop that checks user input against values stored in the dictionary 'username_password'.
    while not logged_in:

        # Display a message to the user and prompt user input for a username and password.
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        
        # Conditional block for input not matching an existing key in the dictionary. 
        if check_cred(curr_user, True) == False:
            print("Username not found.")
            print()
            continue
        
        # Conditional block for input not matching an existing value in the dictionary. 
        elif check_cred(curr_user, False, curr_pass) == False:
            print("Password not recognised.")
            print()
            continue
        
        # Conditional block capturing valid input for an existing key:value pair in the dictionary.
        else:
            print("Login Successful!")
            logged_in = True


# Block enabling access to the functions through a menu | Presents a menu, requests input and executes the relevant area of the function block depending on that input.


    # Admin login credentials.
    # Username: admin | Password: password


    # Start a while loop that presents different options to the user and prompts them to choose one, executes a conditional block for that option, then prompts for a further choice. End the loop when the last option is selected. 
    while True:
        
        print()
        
        # Assign program options to a list called "menu". This will be used to compare with user input, executing the applicable conditional block and calling the respective function.
        menu = ["r", "a", "va", "vm", "gr", "ds", "e"] 
        
        
        # Present the options to the user.    
        print("""Select one of the following options below: 

    r:    Register a user
    a:    Add a task
    va:   View all tasks
    vm:   View my tasks
    gr:   Generate reports
    ds:   Display Statistics
    e:    Exit""")
        
        print()
        
        # Read user input. Force lowercase entry for simpler comparison against valid input.
        menu_sel = input().lower()
        

        # Conditional block for menu choices. Captures restricted access for the 'gr' and 'ds' options.
        if menu_sel == menu[0]: reg_user()
        elif menu_sel == menu[1]: add_task()
        elif menu_sel == menu[2]: view_all()
        elif menu_sel == menu[3]: view_mine()
        
        elif menu_sel == menu[4]:
            if curr_user == "admin": gen_rep()
            else:
                print("This account does not have sufficient privileges to do this.")
                continue
        
        elif menu_sel == menu[5]:            
            if curr_user == "admin": stats()
            else:
                print("This account does not have sufficient privileges to do this.")
                continue
            
        elif menu_sel == menu[6]: end()
        else: print("Menu option not recognised. Please try again.")


# Start the program.
task_mgr()