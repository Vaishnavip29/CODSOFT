
#Task 1 : TO-DO LIST

import tkinter 
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do-List")
root.geometry("500x500")
def add_task():
    task = entry_task.get()
    if task !="":
          listbox_tasks.insert(tkinter.END,task)
          entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning !", message="You must enter a task.")
def delete_task():
    try:
        task_index = listbox_tasks.curselection()
        listbox_tasks.delete(task_index)
    except:
         tkinter.messagebox.showwarning(title="warning !", message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0,tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END,task)
    except:
         tkinter.messagebox.showwarning(title="warning !", message="Cannot find tasks.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks,open("tasks.dat","wb"))
    listbox_tasks.delete(0,tkinter.END)

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
listbox_tasks = tkinter.Listbox(frame_tasks,font="cilibry",height=8,width=100)
listbox_tasks.pack(side=tkinter.LEFT)


entry_task = tkinter.Entry(root,font="cilibry",width=100)
entry_task.pack(ipady=5,padx=10)

Button_add_task =tkinter.Button(root,text="Add Task",font="cilibry",bg="grey",height=1,width=30,command =add_task )
Button_add_task.pack(pady=10)

Button_delete_task =tkinter.Button(root,text="Delete Task",font="cilibry",bg="grey",height=1,width=30,command =delete_task )
Button_delete_task.pack(pady=5)

Button_load_tasks =tkinter.Button(root,text="Load Task",font="cilibry",bg="grey",height=1,width=30,command =load_tasks)
Button_load_tasks.pack(pady=5)

Button_save_tasks =tkinter.Button(root,text="Save Task",font="cilibry",bg="grey",height=1,width=30,command =save_tasks)
Button_save_tasks.pack(pady=5)



root.mainloop()