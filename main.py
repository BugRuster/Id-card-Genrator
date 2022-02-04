import csv
import png
import pyqrcode
from tkinter import *
from datetime import *
from time import strftime

date_now = date.today()
with open('index.txt', 'r') as f:
	index = [int(i) for i in f.read().split()][-1]


def time():
	time_string = strftime('%H:%M:%S %p')
	time_now.config(text=time_string)
	time_now.after(1000, time)


def id_card():
	global index
	index += 1
	with open('index.txt', 'a') as f:
		f.write('%d' % index + '\n')

	data = [i for i in csv.reader(open('data.csv'))]
	card_window = Toplevel()
	card_window.title("ID card")
	card_window.geometry("300x150")

	name = Label(card_window, text="Name:")
	name.grid(row=1, column=0, ipadx="30")
	Label(card_window, text=data[index-1][0]).grid(row=1, column=1)

	course = Label(card_window, text="Course:")
	course.grid(row=2, column=0)
	Label(card_window, text=data[index-1][1]).grid(row=2, column=1)

	form_no = Label(card_window, text="Roll No:")
	form_no.grid(row=3, column=0)
	Label(card_window, text=data[index-1][3]).grid(row=3, column=1)

	contact_no = Label(card_window, text="Contact No:")
	contact_no.grid(row=4, column=0)
	Label(card_window, text=data[index-1][4]).grid(row=4, column=1)

	Name = data[index-1][0]
	RollNo = data[index-1][3]
	Batch = data[index-1][1]
	ContactNo = data[index-1][4]

	dic = f"Name: {Name} \nRoll No: {RollNo} \nBatch: {Batch} \nContact No: {ContactNo}"
	pyqrcode.create(dic).png(f"{Name}.png", scale=2)

	qr_code = PhotoImage(file=f"{Name}.png")

	Button(card_window, image=qr_code).grid(row=0, rowspan=4, column=2)
	card_window.mainloop()


def login_info():
	data_window = Toplevel()
	data_window.title("Enter the data")
	data_window.config(padx=20, pady=20, background="#219F94")

	heading = Label(data_window, text="Information", bg="#219F94")
	heading.grid(row=0, column=1, columnspan=2)

	name = Label(data_window, text="Name:", bg="#219F94")
	name.grid(row=1, column=0, ipadx="30")

	course = Label(data_window, text="Course:", bg="#219F94")
	course.grid(row=2, column=0)

	sem = Label(data_window, text="Semester:", bg="#219F94")
	sem.grid(row=3, column=0)

	form_no = Label(data_window, text="Roll No.:", bg="#219F94")
	form_no.grid(row=4, column=0)

	contact_no = Label(data_window, text="Contact No:", bg="#219F94")
	contact_no.grid(row=5, column=0)

	email_id = Label(data_window, text="Email id:", bg="#219F94")
	email_id.grid(row=6, column=0)

	address = Label(data_window, text="Address:", bg="#219F94")
	address.grid(row=7, column=0)

	name_field = Entry(data_window, highlightthickness=0)
	name_field.grid(row=1, column=1)

	course_field = Entry(data_window, highlightthickness=0)
	course_field.grid(row=2, column=1)

	sem_field = Entry(data_window, highlightthickness=0)
	sem_field.grid(row=3, column=1)

	form_no_field = Entry(data_window, highlightthickness=0)
	form_no_field.grid(row=4, column=1)

	contact_no_field = Entry(data_window, highlightthickness=0)
	contact_no_field.grid(row=5, column=1)

	email_id_field = Entry(data_window, highlightthickness=0)
	email_id_field.grid(row=6, column=1)

	address_field = Entry(data_window, highlightthickness=0)
	address_field.grid(row=7, column=1)

	def entries():
		entry_list = [
			name_field.get(),
			course_field.get(),
			sem_field.get(),
			form_no_field.get(),
			contact_no_field.get(),
			email_id_field.get(),
			address_field.get()
		]
		with open("data.csv", 'a') as data_file:
			writer_object = csv.writer(data_file)
			writer_object.writerow(entry_list)
			data_file.close()

	submit_button = Button(
		data_window,
		text="Submit",
		command=lambda: [entries(), id_card(), data_window.destroy()],
		highlightbackground="#219F94")
	submit_button.grid(row=8, column=1)

	data_window.mainloop()


def login_page():
	login_window = Toplevel()
	login_window.title("Login")
	login_window.config(padx=80, pady=60, background="#D3ECA7")

	Label(login_window, text="Username: ", bg="#D3ECA7").pack()
	username_entry = Entry(login_window, highlightthickness=0)
	username_entry.pack()

	Label(login_window, text="Password: ", bg="#D3ECA7").pack()
	password_entry = Entry(login_window, highlightthickness=0, show="*")
	password_entry.pack()

	def checking_func():
		if (username_entry.get() == "admin") and (password_entry.get() == "admin"):
			login_info()
			login_window.destroy()
		else:
			Label(login_window, text="Error! Enter correct login id and password", fg="red", bg="#D3ECA7").pack()

	Button(login_window, text="Login", command=checking_func, highlightbackground="#D3ECA7").pack()
	login_window.mainloop()


window = Tk()
window.title("Attendance Manager")
window.config()

bg_img = PhotoImage(file="images/backdrop.png")
start_img = PhotoImage(file="images/login_button.png")

canvas = Canvas(width=750, height=500)
canvas.create_image(375, 250, image=bg_img)
canvas.create_text(380, 330, text="WELCOME TO JKLU", font=("Montserrat", 50, "bold"))
canvas.create_text(70, 15, text=f"Date: {date_now}")

canvas.create_text(640, 15, text=f"Time: ")

canvas.pack()
Button(
	window,
	image=start_img,
	highlightbackground='#ACACAC',
	command=login_page
).place(x=310, y=400)

time_now = Label(window, text="00:00:00", background='#CBCBCB')
time_now.place(x=660, y=3)

time()
window.mainloop()
