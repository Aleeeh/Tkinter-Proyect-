from tkinter import *  
"""
Ésta va a ser la ventana de inicio que nos va a llevar tanto a crear un nuevo cliente 
como a poder buscar uno existente en la base de datos 
"""

#Creamos una ventana 
app = Tk()
app.title('Welcome Window')
app.geometry('400x400')

# Función que llama a la ventana para añadir nuevos clientes a la base de datos
def clientwindow(): 
    import part_manager 

# Llama a la ventana que muestra todos los clientes guardados en la b.d. 
def old_clientwindow():
    import registered_clients

# New Client 
new_c_btn = Button(app, text="Añadir un nuevo cliente", command = clientwindow)
new_c_btn.grid(row=0, column=0, columnspan=2, padx=10, ipadx=137)

# Search for Already Registered Clients 
old_c_btn = Button(app, text="Añadir un nuevo cliente", command = old_clientwindow)
old_c_btn.grid(row=1, column=0, columnspan=2, padx=10, ipadx=137)
# Quit 
exit_button = Button(app, text="Quit", fg="red", command= app.destroy)
exit_button.grid(row=2, column=0, columnspan=2, padx=10, ipadx=137)


# Iniciamos la ventana 
app.mainloop()
