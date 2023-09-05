import tkinter as tk
import requests
from ast import literal_eval as leval
import json


# Reading from widget
def read(obj):
	try:
		return obj.get('1.0', tk.END)
	except Exception:
		return obj.get()


# Writing in disabled widget
def write(obj, message):
	obj.configure(state='normal')
	obj.delete('1.0', tk.END)
	obj.insert(tk.INSERT, message)
	obj.configure(state='disabled')


# Send button command
def send():
	global method, url_entry, headers_box, body_box
	global response_box, error_output, status_output
	global METHODS_FUNCTIONS

	clear()

	f = METHODS_FUNCTIONS[method.get()]
	url = read(url_entry)
	headers = read(headers_box)
	body = read(body_box)

	try:
		response = f(url, headers=leval(headers), json=leval(body))
		status_code = str(response.status_code)
		data = json.dumps(response.json(), indent=2, ensure_ascii=False)

		write(error_output, "NO ERRORS")
		write(status_output, status_code)
		write(response_box, data)

	except Exception as e:
		write(error_output, e.__class__.__name__)


# Clear button command
def clear():
	global response_box, error_output, status_output

	write(response_box, "")
	write(error_output, "NO ERRORS")
	write(status_output, "---")


# Storing methods
METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
METHODS_FUNCTIONS = {m: getattr(requests, m.lower()) for m in METHODS}


# Main Window
root = tk.Tk()
root.geometry('572x1000')
root.title('PostGuy')

# Frames of the Main Window
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


# Upper Bar
url_label = tk.Label(upper_bar, text='URL')
url_label.grid(row=0, column=0)
url_entry = tk.Entry(upper_bar, width=60)
url_entry.grid(row=1, column=0)
method_label = tk.Label(upper_bar, text='METHOD')
method_label.grid(row=0, column=1)
method = tk.StringVar(upper_bar)
method.set('GET')
method_menu = tk.OptionMenu(upper_bar, method, *METHODS)
method_menu.grid(row=1, column=1)

# Headers Bar
headers_label = tk.Label(headers_bar, text='Headers')
headers_label.pack()
headers_scroll = tk.Scrollbar(headers_bar, orient='vertical')
headers_scroll.pack(side=tk.RIGHT, fill='y')
headers_box = tk.Text(headers_bar, width=69, height=10, yscrollcommand=headers_scroll.set)
headers_box.insert(tk.INSERT, '{\n}')
headers_scroll.config(command=headers_box.yview)
headers_box.pack()

# Body Bar
body_label = tk.Label(body_bar, text='Body')
body_label.pack()
body_scroll = tk.Scrollbar(body_bar, orient='vertical')
body_scroll.pack(side=tk.RIGHT, fill='y')
body_box = tk.Text(body_bar, width=69, height=10, yscrollcommand=body_scroll.set)
body_box.insert(tk.INSERT, '{\n}')
body_scroll.config(command=body_box.yview)
body_box.pack()

# Send Button Bar
left_void = tk.Label(send_bar, text=" " * 45)
left_void.pack(side=tk.LEFT)
send_button = tk.Button(send_bar, text='Send', command=send)
send_button.pack()
right_void = tk.Label(send_bar, text=" " * 45)
right_void.pack()

# Error Bar
error_label = tk.Label(error_bar, text=' \tError happened during request?\t')
error_label.grid(row=0, column=0)
error_output = tk.Text(error_bar, width=27, height=1)
error_output.insert(tk.INSERT, 'NO ERRORS')
error_output.configure(state='disabled')
error_output.grid(row=0, column=1)

# Status Bar
status_label = tk.Label(status_bar, text='\tStatus Code\t\t\t')
status_label.grid(row=0, column=0)
status_output = tk.Text(status_bar, width=27, height=1)
status_output.insert(tk.INSERT, '---')
status_output.configure(state='disabled')
status_output.grid(row=0, column=1)

# Response Bar
response_label = tk.Label(response_bar, text='Response')
response_label.pack()
response_scroll = tk.Scrollbar(response_bar, orient='vertical')
response_scroll.pack(side=tk.RIGHT, fill='y')
response_box = tk.Text(response_bar, width=69, height=10, yscrollcommand=response_scroll.set)
response_box.configure(state='disabled')
response_scroll.config(command=response_box.yview)
response_box.pack()

# Clear Button Bar
left_void2 = tk.Label(clear_bar, text=" " * 45)
left_void2.pack(side=tk.LEFT)
clear_button = tk.Button(clear_bar, text='Clear', command=clear)
clear_button.pack()
right_void2 = tk.Label(clear_bar, text=" " * 45)
right_void2.pack()

# Main Loop
if __name__ == '__main__':
	root.mainloop()
