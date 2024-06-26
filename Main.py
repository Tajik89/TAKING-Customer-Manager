from customtkinter import *

root = CTk()
root.title('_TAKING COMPANY customer')
root.geometry('500x600')
root.resizable(width=False, height=False)

CTkLabel(master=root, text='Customer Manager', font=('',35)).place(x= 100, y= 20)
CTkLabel(master=root, text='From _TAKING Company', text_color='green').place(x= 170, y= 60)

customer_name = CTkEntry(master=root, placeholder_text='Name', width=100, border_color='white')
customer_name.place(x= 10, y= 120)

customer_last_name = CTkEntry(master=root, placeholder_text='Last Name', width=100, border_color='white')
customer_last_name.place(x= 120, y= 120)

history = CTkEntry(master=root, placeholder_text='yyyy/mm/dd', width=100, border_color='red')
history.place(x= 200, y= 160)

CTkLabel(master=root, text='Commands', font=('', 20)).place(x= 25, y= 200)
commands= CTkTextbox(master=root, text_color='white', width=450, height=300)
commands.place(x= 25, y=250)

btn_save = CTkButton(master=root, text_color='white', text='Save', fg_color='green')
btn_save.place(x= 170, y= 560)

btn_exit = CTkButton(master=root, text_color='white', text='Exit', fg_color='red', width=50)
btn_exit.place(x= 10, y= 560)

btn_open = CTkButton(master=root, text_color='black', text='open', fg_color='yellow', width=50)
btn_open.place(x= 430, y= 560)

root.mainloop()