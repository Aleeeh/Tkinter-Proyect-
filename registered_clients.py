from tkinter import *
from tkinter.font import BOLD 

"""Ventana en la que vamos a mostrar con una scrollbar todos los clientes añadidos"""

app = Tk()
app.title('Registered Clients')
app.geometry('400x400')
#
clients_label = Label(app, text= "Clientes Registrados")
clients_label.grid(row = 0, column = 0)

# (Listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=2, column=0, columnspan= 3, rowspan=6, pady=20, padx=20)
# Create a scrollbar 
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)




# Iniciamos la ventana 
app.mainloop()