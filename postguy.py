import tkinter as tk


root = tk.Tk()
root.geometry('565x1000')
root.title('PostGuy')

upper_bar = tk.Frame(root)
upper_bar.place(relx=0, rely=0)

headers_bar = tk.Frame(root)
headers_bar.place(relx=0, rely=0.06)

body_bar = tk.Frame(root)
body_bar.place(relx=0, rely=0.3)

send_bar = tk.Frame(root)
send_bar.place(relx=0, rely=0.5)

error_bar = tk.Frame(root)
error_bar.place(relx=0, rely=0.6)

status_bar = tk.Frame(root)
status_bar.place(relx=0, rely=0.65)

response_bar = tk.Frame(root)
response_bar.place(relx=0, rely=0.75)

clear_bar = tk.Frame(root)
clear_bar.place(relx=0, rely=0.95)


url_label = tk.Label(upper_bar, text='URL')
url_label.grid(row=0, column=0)
url_entry = tk.Entry(upper_bar, width=60)
url_entry.grid(row=1, column=0)
method_label = tk.Label(upper_bar, text='METHOD')
method_label.grid(row=0, column=1)
method = tk.StringVar(upper_bar)
method.set('GET')
method_menu = tk.OptionMenu(upper_bar, method, *['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
method_menu.grid(row=1, column=1)

headers_label = tk.Label(headers_bar, text='Headers')
headers_label.pack()
headers_box = tk.Text(headers_bar, width=69, height=10)
headers_box.insert(tk.INSERT, '{\n}')
headers_box.pack()

body_label = tk.Label(body_bar, text='Body')
body_label.pack()
body_box = tk.Text(body_bar, width=69, height=10)
body_box.insert(tk.INSERT, '{\n}')
body_box.pack()

left_void = tk.Label(send_bar, text=" " * 45)
left_void.pack(side=tk.LEFT)
send_button = tk.Button(send_bar, text='Send', command=lambda: print('ok'))
send_button.pack()
right_void = tk.Label(send_bar, text=" " * 45)
right_void.pack()

error_label = tk.Label(error_bar, text=' \tError happened during request?\t')
error_label.grid(row=0, column=0)
error_output = tk.Text(error_bar, width=27, height=1)
error_output.insert(tk.INSERT, 'NO ERRORS')
error_output.configure(state='disabled')
error_output.grid(row=0, column=1)


status_label = tk.Label(status_bar, text='\tStatus Code\t\t\t')
status_label.grid(row=0, column=0)
status_output = tk.Text(status_bar, width=27, height=1)
status_output.insert(tk.INSERT, '---')
status_output.configure(state='disabled')
status_output.grid(row=0, column=1)

response_label = tk.Label(response_bar, text='Response')
response_label.pack()
response_box = tk.Text(response_bar, width=69, height=10)
response_box.pack()

left_void2 = tk.Label(clear_bar, text=" " * 45)
left_void2.pack(side=tk.LEFT)
clear_button = tk.Button(clear_bar, text='Clear', command=lambda: print('alright'))
clear_button.pack()
right_void2 = tk.Label(clear_bar, text=" " * 45)
right_void2.pack()

root.mainloop()
