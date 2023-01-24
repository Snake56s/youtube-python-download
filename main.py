from backEnd import Descargar,descargar_play_list
from tkinter import Tk, ttk, StringVar, messagebox,BooleanVar
Ventana = Tk()
Ventana.geometry("400x300")
Ventana.title("Youtube Downloader")
texto_parrafo = StringVar()#Variable de texto
texto_parrafo.set("Bienvenido")#Dar valor a la variable
checkbox_valor = BooleanVar()

parrafo = ttk.Label(Ventana, textvariable=texto_parrafo)
parrafo.pack()
combo_box = ttk.Combobox(
    values=["Video", "Audio"],
    state="readonly"
)
combo_box.set("Video")
combo_box.pack()
texto_I_caja = StringVar()
texto_I_caja.set("Inserte el link de youtube")
cajaTexto = ttk.Entry(Ventana,textvariable=texto_I_caja)
cajaTexto.pack()

def Iniciar():
    global checkbox_valor,texto_parrafo
    URL = cajaTexto.get()
    TIPO = combo_box.get()
    if(checkbox_valor == False):
        retorno = Descargar(url=URL,tipo=TIPO)
        if(retorno == True):
            texto_parrafo.set("Descargado")
            cajaTexto.pack_forget()
            combo_box.pack_forget()
            boton_descargar.pack_forget()
            boton_repetir.pack()
        else:
            messagebox.showerror(message="Error en el enlace a youtube",title="Error")
    else:
        retorno = descargar_play_list(url=URL, tipo=TIPO)
        if(retorno==False):
            messagebox.showerror(message="Error al descargar playlist",title="Error")
        else:

            messagebox.showinfo(message="Descargado",title="Notificacion")
def repetir():
    global texto_parrafo
    texto_parrafo.set("Bienvenido")
    combo_box.pack()
    cajaTexto.pack()
    boton_descargar.pack()
    boton_repetir.pack_forget()

chb_playlist = ttk.Checkbutton(Ventana,text="Play list",onvalue=True,offvalue=False,variable=checkbox_valor)
chb_playlist.pack()
boton_descargar = ttk.Button(Ventana,text="Descargar",command=Iniciar)
boton_repetir = ttk.Button(Ventana,text="Volver a descargar",command=repetir)
boton_descargar.pack()

Ventana.mainloop()