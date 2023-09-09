from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x300')
root.title("Website Blocker")
root.iconbitmap(r"D:\user_interface_worldwide_globe_web_ui_website_icon_221097.ico")
# Dark Theme Style
style = ttk.Style()
style.theme_use('clam')
style.configure('.', background='gray15', foreground='white', fieldbackground='gray15')
style.configure('TLabel', background='gray15', foreground='white')
style.configure('TButton', background='gray', foreground='white', font='Arial 12 bold')
style.map('TButton', background=[('active', 'gray')])

# Content Frame
content_frame = ttk.Frame(root, padding=20)
content_frame.pack(expand=True, fill='both')

# Heading Label
heading_label = ttk.Label(content_frame, text='Website Blocker', font='Arial 20 bold')
heading_label.pack()

# Website Entry Label and Text Entry
website_label = ttk.Label(content_frame, text='Enter Website:', font='Arial 13 bold')
website_label.pack(pady=10)

websites_entry = Text(content_frame, font='Arial 10', height=2, width=40)
websites_entry.pack()

# Block Button
def blocker():
    website_lists = websites_entry.get(1.0, END)
    website = list(website_lists.split(","))
    with open('C:\Windows\System32\drivers\etc\hosts', 'r+') as host_file:
        file_content = host_file.read()
        for web in website:
            if web in file_content:
                result_label.config(text='Already Blocked')
            else:
                host_file.write('127.0.0.1 ' + web + '\n')
                result_label.config(text='Blocked')

block_button = ttk.Button(content_frame, text='Block', command=blocker)
block_button.pack(pady=10)

# Result Label
result_label = ttk.Label(content_frame, font='Arial 12 bold')
result_label.pack()

# Make Window Resizable
root.resizable(True, True)

root.mainloop()
