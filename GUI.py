from tkinter import *
from tkinter import messagebox
import sqlite3

top = Tk()
top.geometry("400x400")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")


# Database 

# Create a database or connect to one 
conn = sqlite3.connect('address_book.db')
# Create cursor
c = conn.cursor()
'''
# Create a table 
c.execute("CREATE TABLE addresses (first_name text, last_name text, address text)")
'''

# Create Submit function for database
def submit(): 
   #Create a database or connect to one 
   conn = sqlite3.connect('address_book.db')
   c = conn.cursor()
   # Insert Into Table
   c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address)", 
         {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address_name.get()
         })

   conn.commit()
   conn.close()

   # Clear the text boxes 
   f_name.delete(0,END)
   l_name.delete(0,END)
   address_name.delete(0,END)

# Create Query Function 
def query():
   conn = sqlite3.connect('address_book.db')
   c = conn.cursor()
   print_records = ""
   c.execute("SELECT *, oid FROM addresses")
   records = c.fetchall()
   print(records)  #just for testing 
   # Loop thru results 
  

   # commit and close the data 
   conn.commit()
   conn.close()
# Create Text Boxes 
f_name = Entry(top, width = 40)
f_name.grid(row = 0, column=1, padx=20)

l_name = Entry(top, width = 40)
l_name.grid(row = 1, column=1, padx=20)

address_name = Entry(top, width = 40)
address_name.grid(row = 2, column=1, padx=20)

# Create Text Box Labels 
f_name_label = Label(top, text= "Nombre")
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(top, text= "Apellidos")
l_name_label.grid(row = 1, column = 0)

address_label = Label(top, text= "Dirección")
address_label.grid(row = 2, column = 0)

# Create Submit Button 
submit_btn = Button(top, text="Añadir a la base de datos", command= submit)
submit_btn.grid(row = 6, column=0, columnspan=2, pady=10, padx= 10, ipadx= 100)

# Create Query Button
query_btn = Button(top, text="Show Records", command= query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# commit changes 
conn.commit()
# close connections to the db 
conn.close() 

top.mainloop()