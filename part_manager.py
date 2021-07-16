from os import name
from tkinter import * 
import sqlite3
# Creamos una ventana 
app = Tk()

# Database

# Create a database or connect to one 
conn = sqlite3.connect('address_book.db')
# Create cursor
c = conn.cursor()

# ******** solo necesitamos crearla una vez ******* 
"""
# Create a table 
c.execute("CREATE TABLE addresses (Name text, Apellido text, DNI text, Matricula text)")
"""

def submit(): 
   #Create a database or connect to one 
   conn = sqlite3.connect('address_book.db')
   c = conn.cursor()
   # Insert Into Table
   c.execute("INSERT INTO addresses VALUES (:name_entry, :apellido_entry, :dni_entry, :matricula_entry)", 
         {
            'name_entry': name_entry.get(),
            'apellido_entry': apellido_entry.get(),
            'dni_entry': dni_entry.get(),
            'matricula_entry': matricula_entry.get()
         })

   conn.commit()
   conn.close()

   # Clear the text boxes 
   name_entry.delete(0,END)
   apellido_entry.delete(0,END)
   dni_entry.delete(0,END)
   matricula_entry.delete(0,END)


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


# Widgets - todo lo que le añade a la ventana

# Nombre 
name_text = StringVar()
name_label = Label(app, text='Nombre', font=('bold', 10), pady = 5, padx=10)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(app, textvariable=name_text)
name_entry.grid(row=0, column=1)

# Apellido
apellido_text = StringVar()
apellido_label = Label(app, text='Apellido', font=('bold', 10), pady = 5, padx=10)
apellido_label.grid(row=1, column=0, sticky=W)
apellido_entry = Entry(app, textvariable=apellido_text)
apellido_entry.grid(row=1, column=1)

# DNI
dni_text = StringVar()
dni_label = Label(app, text='DNI', font=('bold', 10), pady = 5, padx=20)
dni_label.grid(row=0, column=3, sticky=W)
dni_entry = Entry(app, textvariable=dni_text)
dni_entry.grid(row=0, column=4)

# Matricula del coche
matricula_text = StringVar()
matricula_label = Label(app, text='Matrícula', font=('bold', 10), pady = 5, padx=20)
matricula_label.grid(row=1, column=3, sticky=W)
matricula_entry = Entry(app, textvariable=matricula_text)
matricula_entry.grid(row=1, column=4)

# *Botones*

# Quit 
exit_button = Button(app, text="Salir", fg="red", command= app.destroy)
exit_button.grid(row=15, column=0, columnspan=2, padx=10, ipadx=137)

# Añadir a la base datos 
submit_btn = Button(app, text="Añadir a la base de datos", command= submit)
submit_btn.grid(row = 6, column=0, columnspan=2, pady=10, padx= 10, ipadx= 137)

# Enseñar los que están en la base de datos 
query_btn = Button(app, text="Enseñar la base de datos", command= query)
query_btn.grid(row = 7, column=0, columnspan=2, pady=10, padx= 10, ipadx= 137)


app.title('Cool program')
app.geometry('700x400')


# Iniciamos el programa 

app.mainloop()


