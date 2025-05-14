import tkinter as tk
from tkinter import messagebox
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = entry_course.get()
    address = address_entry.get("1.0", "end").strip()
    
    if name and age and course:
        messagebox.showinfo("Form Submission", "Form Submitted Successfully!")
        with open("form_data.txt", "a") as file:
            file.write(f"Name: {name}, Age: {age}, Course: {course}, Address: {address}\n")
        #print(f"Name: {name}, Age: {age}, Gender: {gender}, Course: {course}, Address: {address}")
    else:
        messagebox.showwarning("Error", "Please fill all required fields!")


def about_con():
    messagebox.showinfo("About","This GUI is done by Neels")

def new_form():
    messagebox.showinfo("New","Fill new form")

def delete():
    with open("form_data.txt", "w") as file:
        pass  # This clears the file
    messagebox.showwarning("Warning","All data deleted!")

def view():
    output_text.delete("1.0", "end")
    try:
        with open("form_data.txt", "r") as file:
            data = file.read()
            output_text.insert("1.0", data)
    except FileNotFoundError:
        output_text.insert("1.0", "No data file found.")


root =tk.Tk()
root.geometry("750x300")
root.title("Student Information Form")

name =tk.Label(root,text="Name:").grid(row=0,column=0)
entry_name=tk.Entry(root)
entry_name.grid(row=0,column=1)


age =tk.Label(root,text="Age:").grid(row=1,column=0)
entry_age=tk.Entry(root)
entry_age.grid(row=1,column=1)

gender =tk.Label(root,text="Gender:").grid(row=2,column=0)
gender_var=tk.StringVar(value="MALE")
female_var=tk.IntVar()
check1=tk.Radiobutton(root,text="MALE",variable=gender_var,value="MALE")
check1.grid(row=2,column=1,padx=5)
check2=tk.Radiobutton(root,text="FEMALE",variable=gender_var,value="FEMALE")
check2.grid(row=2,column=1,sticky='e')

course=tk.Label(root,text="Course:").grid(row=3,column=0)
entry_course=tk.Entry(root)
entry_course.grid(row=3,column=1)

address=tk.Label(root,text="Address:").grid(row=4,column=0)
address_entry=tk.Text(root,height=4)
address_entry.grid(row=4,column=1)

submit=tk.Button(root,text="Submit",command=submit_form).grid(row=5,column=1)

menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_form)
file_menu.add_command(label="Delete", command=delete)
file_menu.add_command(label="View", command=view)
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_con)
menu_bar.add_cascade(label="Help", menu=help_menu)

#Output Viewer
output_text = tk.Text(root, height=10)
output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.config(menu=menu_bar)

root.mainloop()