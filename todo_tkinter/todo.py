import tkinter
import tkinter.messagebox
import pickle

root=tkinter.Tk()
root.title("To Do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning",message="You must enter a task to add.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning",message="you must select a task")

def load_task():
    load_tasks=listbox_tasks.curselection()[0]
    listbox_tasks.location()

def save_task():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks,open("tasks.txt","wb"))




frame_task=tkinter.Frame(root)
frame_task.pack()


listbox_tasks=tkinter.Listbox(frame_task,height=3,width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_task)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task=tkinter.Entry(root,width=50)
entry_task.pack()

button_add_task=tkinter.Button(root,text="Add Task",width=48,command=add_task)
button_add_task.pack()

button_delete_task=tkinter.Button(root,text="Delete Task",width=48,command=delete_task)
button_delete_task.pack()

button_load_task=tkinter.Button(root,text="Load Task",width=48,command=load_task)
button_load_task.pack()

button_save_task=tkinter.Button(root,text="Save Task",width=48,command=save_task)
button_save_task.pack()




root.mainloop()