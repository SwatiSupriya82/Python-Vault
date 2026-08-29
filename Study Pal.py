import json
import time

print("\tWelcome to STUDY PAL :)\t")

try:
    with open("planner.json","r") as f:
        Tasks=json.load(f)
except FileNotFoundError:
    Tasks=[]
    
while True:
    print("--------What would you like to do?--------")
    print("1. Add a study task.")
    print("2. View my tasks.")
    print("3. Mark a task as completed.")
    print("4. Delete a task.")
    print("5. Study Progress.")
    print("6. Search & Filter.")
    print("7. Study Session Timer.")
    print("8. Exit.")
    
    choice=input("Enter your choice from 1 to 8:")

    
    if choice=="1":
        task_name=input("Task Name:")
        subject=input("Subject:")
        priority=input("Priority(High/Mid/Low):").strip().capitalize()
        if priority in ["High", "Low", "Mid"]:
            break
        else:
            print("Invalid Priority! Please enter High, Mid or Low.")
            priority=input("Priority(High/Mid/Low):").strip().capitalize()
                
        due_date=input("Due Date:")
        Task={ "Task Name": task_name, "Subject": subject, "Priority": priority, "Due Date": due_date, "Status": "Pending"}
        Tasks.append(Task)
        with open("planner.json","w") as f:
            json.dump(Tasks, f, indent=4)
            
                      
    elif choice=="2":
        if len(Tasks)==0:
            print("No study tasks found")
        else:
            print("--------MY TASKS--------")
            num=1
            for i in Tasks:
                print(str(num)+".","Task:",i["Task Name"])
                print("Subject:", i["Subject"])
                print("Priority:", i["Priority"])
                print("Due Date:", i["Due Date"])
                print("Status:", i["Status"])
                print()
                num=num+1
                
                
    elif choice=="3":
        if len(Tasks)==0:
            print("No study tasks found")
        else:
            num=1
            for i in Tasks:
                print(str(num)+".", "Task:", i["Task Name"])
                print("Subject:", i["Subject"])
                print("Priority:", i["Priority"])
                print("Due Date:", i["Due Date"])
                print("Status:", i["Status"])
                print()
                num=num+1
            tsk_num=int(input("Which task number do you want to mark as completed?:"))
            Tasks[tsk_num-1]["Status"]="Completed"
            print("Task marked as completed")
            
            with open("planner.json","w") as f:
                json.dump(Tasks, f, indent=4)
                
            
    elif choice=="4":
         if len(Tasks)==0:
            print("No study tasks found")
         else:
             num=1
             for i in Tasks:
                 print(str(num)+".", "Task:", i["Task Name"])
                 print("Subject", i["Subject"])
                 print("Priority:", i["Priority"])
                 print("Due Date:", i["Due Date"])
                 print("Status:", i["Status"])
                 print()
                 num=num+1
             tsk_num=int(input("Which task do you want to delete?:"))
             del Tasks[tsk_num-1]
             print("Task Deleted")

             with open("planner.json","w") as f:
                 json.dump(Tasks, f, indent=4)


    elif choice=="5":
        completed=0
        for i in Tasks:
            if i["Status"]=="Completed":
                completed=completed+1
        total=len(Tasks)

        if total>0:
            progress=(completed/total)*100
        else:
            progress = 0

        print("Total Tasks:", total)
        print("Completed Tasks:", completed)
        print("Progress:", round(progress,2),"%")
        

    elif choice=="6":
        search=input("What task do you want to search for?").strip().lower()
        filter_priority=input("What priority(High/Mid/Low/All) do you want to filter?").strip().capitalize()
        filter_status=input("what status do you want to filter(Completed/pending/All)?").strip().capitalize()
        
        found = False
        for task in Tasks:
            if search in task["Task Name"].lower() and (filter_priority=="All" or filter_priority==task["Priority"]) and (filter_status=="All" or filter_status==task["Status"]):
                print(task)
                found = True
        if not found:
            print("No such study tasks found")



    elif choice=="7":
        minutes=int(input("How many minutes do you wan to study?"))
        seconds= minutes*60
        while seconds>0:
            mins=seconds//60
            secs=seconds%60

            print(mins, "minutes", secs, "seconds remaining")
            time.sleep(1)
            seconds=seconds-1
        print("STUDY SESSON COMPLETED!!!!!")

        
    elif choice=="8":
        print("Goodbye!")
        break         

    else:
        print("Invalid Choice")
