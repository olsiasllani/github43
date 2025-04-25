from tkinter import Tk, Label, Entry, W, E, Button

root = Tk()
root.geometry("300x170")
root.title('Sign up')
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)


username_label = Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=W, padx=15, pady=10)

username_input = Entry(root, width=30)
username_input.grid(column=1, row=0, sticky=W, padx=15, pady=10)

email_label = Label(root, text="Email:")
email_label.grid(column=0, row=1, sticky=W, padx=15, pady=10)

email_label = Entry(root, width=30)
email_label.grid(column=1, row=1, sticky=W, padx=15, pady=10)

password_label = Label(root, text="Password:")
password_label.grid(column=0, row=2, sticky=W, padx=15, pady=10)


password_entry = Entry(root, show="*", width=30)
password_entry.grid(column=1, row=2, sticky=W, padx=15, pady=10)

signup_button = Button(root, text="Sign up")
signup_button.grid(column=1, row=3, sticky=E, padx=15, pady=10)

root.mainloop()
