from customtkinter import *

def save() :
    name = customer_name.get()
    last_name = customer_last_name.get()
    full_name = name + last_name
    day = history.get()
    with open(f'{full_name} ({day}).txt', 'w') as file :
        file.write(f'Day: {day}\nName: {name}\nLast Name: {last_name}\nCommands:\n{commands}')

def open() :
    name = customer_name.get()
    last_name = customer_last_name.get()
    full_name = name + last_name
    day = history.get()
    with open(f'{full_name} ({day}).txt', 'r') as file :
        txt = file.read()

    win_open = CTk()
    win_open.title(f'{full_name} ({day})')
    win_open.geometry('300x300')
    win_open.resizable(width= False, height= False)
    
    CTkLabel(master= win_open, text=f'{txt}').pack()

    win_open.mainloop()

def out_co () :
    exit(0)

def out() :
    win_out = CTk()
    win_out.title('Danger Massage')
    win_out.geometry('400x100')
    win_out.resizable(width=False, height=False)

    CTkLabel(master=win_out, text='WARNING!', text_color='red', font=('', 20)).place(x= 150, y= 20)
    CTkLabel(master=win_out, text='Are You want to exit ?!', text_color='white', font=('', 15)).place(x=130, y= 60)
    btn_exit_co = CTkButton(master=win_out, text='Exit', text_color='white', fg_color='red', width=50, height=15, command=out_co).place(x= 340, y= 70)

    win_out.mainloop()

root = CTk()
root.title('_TAKING customer manager')
root.geometry('500x600')
root.resizable(width=False, height=False)

CTkLabel(master=root, text='Customer Manager', font=('',35)).place(x= 100, y= 20)
CTkLabel(master=root, text='From _TAKING', text_color='red').place(x= 200, y= 60)

customer_name = CTkEntry(master=root, placeholder_text='Name', width=100, border_color='white')
customer_name.place(x= 10, y= 120)

customer_last_name = CTkEntry(master=root, placeholder_text='Last Name', width=100, border_color='white')
customer_last_name.place(x= 120, y= 120)

history = CTkEntry(master=root, placeholder_text='yyyy/mm/dd', width=100, border_color='red')
history.place(x= 200, y= 160)

CTkLabel(master=root, text='Commands', font=('', 20)).place(x= 25, y= 200)
commands = CTkTextbox(master=root, text_color='white', width=450, height=300)
commands.place(x= 25, y=250)

btn_save = CTkButton(master=root, text_color='white', text='Save', fg_color='green', command=save)
btn_save.place(x= 170, y= 560)

btn_exit = CTkButton(master=root, text_color='white', text='Exit', fg_color='red', width=50, command=out)
btn_exit.place(x= 10, y= 560)

btn_open = CTkButton(master=root, text_color='black', text='open', fg_color='yellow', width=50, command=open)
btn_open.place(x= 430, y= 560)

root.mainloop()