import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import filedialog


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
#color
fondo_entrar= "#810024"
Blanco = "#fefefe"
Plomo = "#141414"

Ventana=tk.Tk()
Ventana.title("Login")
Ventana.geometry("785x443")
Ventana.resizable(width=False, height=False)

Fondo = tk.PhotoImage(file="Login.png")
fondo1= tk.Label(Ventana, image=Fondo).place(x= 0, y=0, relwidth=1, relheight= 1)
#BoImg


#Entrada
usuario = tk.StringVar()
Password = tk.StringVar()
entradauser = tk.Entry(Ventana, textvar= usuario, width=60, relief="flat",bg= Blanco)
entradauser.place(x=220, y=195)
entradapass = tk.Entry(Ventana, textvar= Password, width=60, relief="flat",bg= Blanco)
entradapass.place(x=220, y=260)
#temporal

#-----------
def login():
    nombre=usuario.get()
    contraseña=Password.get()
    if nombre == "admin" and contraseña == "123":
        correcta()
    else:
        correcta()

def correcta():
    #Ventana.withdraw()
    window = tk.Toplevel()
    window.title("Compartiendo amor")
    FondoI = tk.PhotoImage(file="Compartiendo amor 2.png")
    FondoII= tk.Label(window, image=FondoI).place(x= 0, y=0, relwidth=1, relheight= 1)
    window.geometry("1279x639")
    window.resizable(width=False, height=False)
    comprar = tk.PhotoImage(file="Comprar.png" )
    #web
    def Internet():
        import webbrowser
        webbrowser.open("https://www.google.com/")
    def video1():
        import webbrowser
        webbrowser.open("https://www.facebook.com/106582008815735/videos/795414908225361")
    

    #Interacciones

    def inicio():
        facebook.place(x=2000,y=2000)
        tiktok.place(x=2000,y=2000)
        Whatsapp.place(x=2000,y=2000)

        Navidad1.place(x=570,y=185)
        Navidad2.place(x=860,y=185)
        Catalogo1.place(x=195,y=180)
        Web.place(x=738,y=410)

    
    def catalogo():
        Navidad1.place(x=2000,y=2000)
        Navidad2.place(x=2000,y=2000)
        Catalogo1.place(x=2000,y=2000)
        Web.place(x=2000,y=2000)

        facebook.place(x=2000,y=2000)
        tiktok.place(x=2000,y=2000)
        Whatsapp.place(x=2000,y=2000)

    def redes():
        Navidad1.place(x=2000,y=2000)
        Navidad2.place(x=2000,y=2000)
        Catalogo1.place(x=2000,y=2000)
        Web.place(x=2000,y=2000)

        facebook.place(x=254,y=203)
        tiktok.place(x=254,y=335)
        Whatsapp.place(x=254,y=470)
    def compras():        
        Navidad1.place(x=2000,y=2000)
        Navidad2.place(x=2000,y=2000)
        Catalogo1.place(x=2000,y=2000)
        Web.place(x=2000,y=2000)

        facebook.place(x=2000,y=2000)
        tiktok.place(x=2000,y=2000)
        Whatsapp.place(x=2000,y=2000)
        
    #borrar inicio
    def borrar_inicio():
        Navidad1.place(x=2000,y=2000)
        Navidad2.place(x=2000,y=2000)
        Catalogo1.place(x=2000,y=2000)
        Web.place(x=2000,y=2000)
    
    def borrar_redes():
        facebook.place(x=2000,y=2000)
        tiktok.place(x=2000,y=2000)
        Whatsapp.place(x=2000,y=2000)






    #borrar catalogo
     
    
    #borrar compras 

    #botones

    Inicio= tk.Button(window, fg= Blanco ,text="Inicio",command=inicio ,cursor="hand2", bg = Plomo, width=5, relief="flat", font=("Open Sauce", 25 , "bold"))
    Inicio.place(x=510, y=25)
    Catalogo = tk.Button(window, command=catalogo,fg= Blanco, text="Catalogo" ,cursor="hand2", bg = Plomo, width=8, relief="flat", font=("Open Sauce", 25 , "bold"))
    Catalogo.place(x=650, y=25)
    Redes = tk.Button(window, fg= Blanco, text="Redes" ,command=redes,cursor="hand2", bg = Plomo, width=6, relief="flat", font=("Open Sauce", 25 , "bold"))
    Redes.place(x=840, y=25)
    Compras = tk.Button(window, command=compras,fg= Blanco,image= comprar ,cursor="hand2", bg = Plomo, width=100, relief="flat", font=("Open Sauce", 2 , "bold"))
    Compras.place(x=1040, y=-1)
    comparte = tk.Button(window, command= Internet, fg= Blanco, text="COMPARTIENDO AMOR" ,cursor="hand2", bg = Plomo, width=20, relief="flat", font=("Brixton Sans", 25 ))
    comparte.place(x=113, y=25)
    

    
    
    #inicio
    curso1=tk.PhotoImage(file="choco1.png")
    Navidad1=tk.Button(window,image= curso1 ,cursor="hand2", bg = fondo_entrar, width=188, relief="flat")
    Navidad1.place(x=570,y=185)
    curso2=tk.PhotoImage(file="choco2.png")
    Navidad2=tk.Button(window,image= curso2 ,cursor="hand2", bg = fondo_entrar, width=188, relief="flat")
    Navidad2.place(x=860,y=185)
    Meer1=tk.PhotoImage(file="Catalogo1.png")
    Catalogo1=tk.Button(window,image= Meer1,cursor="hand2", bg = fondo_entrar, width=318, relief="flat")
    Catalogo1.place(x=195,y=180)
    Video1= tk.PhotoImage(file="video1.png")
    Web=tk.Button(window,image= Video1,cursor="hand2", bg = fondo_entrar, width=149, relief="flat")
    Web.place(x=738,y=410)


    #catalogo


    #redes
    face=tk.PhotoImage(file="face.png")
    facebook=tk.Button(window,image= face,cursor="hand2", bg = fondo_entrar, width=725, relief="flat")
    tik=tk.PhotoImage(file="tik.png")
    tiktok=tk.Button(window,image= tik,cursor="hand2", bg = fondo_entrar, width=725, relief="flat")
    whats=tk.PhotoImage(file="whats.png")
    Whatsapp=tk.Button(window,image= whats,cursor="hand2", bg = fondo_entrar, width=725, relief="flat")






    window.mainloop()





#boton
boton1= tk.Button(Ventana, text="Ingresar", fg=["White"] ,command=login ,cursor="hand2", bg = fondo_entrar, width=12, relief="flat", font=("Comic Sans MS", 12 , "bold"))
boton1.place(x=330, y=353)
Ventana.mainloop()
