#25 pts Calculadora con interfaz gráfica (Debe sumar, restar, multiplicar y dividir 2 números)

from tkinter import *
#Configuracion Ventana
root=Tk()
root.config(bg='#FFFFFF')
root.resizable(FALSE,FALSE)
root.overrideredirect(1)

#Centreado de ventana
root.withdraw()
ejex=root.winfo_screenwidth()/2
ejey=root.winfo_screenheight()/2
root.geometry('%dx%d+%d+%d' % (235,340,ejex-(235/2),ejey-(340/2)))
root.wm_deiconify()

#Funciones para operar
def suma(x1,x2):
    res.set(x1.get()+x2.get())
    clear()
def resta(x1,x2):
    res.set(x1.get()-x2.get())
    clear()
def mult(x1,x2):
    res.set(x1.get()*x2.get())
    clear()
def div(x1,x2):
    res.set(x1.get()/x2.get())
    clear()
def clear():
    x.set(0)
    y.set(0)

#Declaracion de Variables
x=DoubleVar(value=0)
y=DoubleVar(value=0)
res=DoubleVar(value=0)

#Textos Label lado izquierdo
titulo=Label(root,text='',bg='#E64A19',height=1)
titulo.grid(row=0,column=0,sticky='nsew',columnspan=2)
titulo=Label(root,text='CALCULADORA',bg='#FF5722',fg='white',font=('',15, "bold"),height=2)
titulo.grid(row=1,column=0,sticky='nsew',columnspan=2)
lbNum1=Label(root,text='1er Numero',bg='white')
lbNum1.grid(row=2,column=0,sticky='e',padx=10,pady=10)
lbNum2=Label(root,text='2do Numero',bg='white')
lbNum2.grid(row=3,column=0,sticky='e',padx=10,pady=10)
lbNumR=Label(root,text='Resultado',bg='white')
lbNumR.grid(row=4,column=0,sticky='e',padx=10,pady=10)

#Entry lado derecho
txtNum1=Entry(root,relief='solid',textvariable=x,justify='right')
txtNum1.grid(row=2,column=1,padx=10,pady=10)
txtNum2=Entry(root,relief='solid',textvariable=y,justify='right')
txtNum2.grid(row=3,column=1,padx=10,pady=10)
txtNumR=Entry(root,relief='solid',state='disable',textvariable=res,justify='right')
txtNumR.grid(row=4,column=1,padx=10,pady=10)

#Botones
btnS=Button(root,text='Suma',bg='#607D8B',relief='flat',fg='white',command=lambda:suma(x,y),cursor='hand2')
btnS.grid(row=5,column=0,sticky='nsew',padx=8,pady=4,columnspan=2)
btnR=Button(root,text='Resta',bg='#607D8B',relief='flat',fg='white',command=lambda:resta(x,y),cursor='hand2')
btnR.grid(row=6,column=0,sticky='nsew',padx=8,pady=4,columnspan=2)
btnM=Button(root,text='Multiplicacion',bg='#607D8B',relief='flat',fg='white',command=lambda:mult(x,y),cursor='hand2')
btnM.grid(row=7,column=0,sticky='nsew',padx=8,pady=4,columnspan=2)
btnD=Button(root,text='Division',bg='#607D8B',relief='flat',fg='white',command=lambda:div(x,y),cursor='hand2')
btnD.grid(row=8,column=0,sticky='nsew',padx=8,pady=4,columnspan=2)
btnSalir=Button(root,text='Salir',bg='#D32F2F',fg='white',height=1,relief='flat',command=root.destroy,cursor='hand2')
btnSalir.grid(row=0,column=1,sticky='e')

#Funciones Eventos de los botones
def hoverS(e):
    btnS.config(bg='#BDBDBD')
def leaveS(e):
    btnS.config(bg='#607D8B')
def hoverR(e):
    btnR.config(bg='#BDBDBD')
def leaveR(e):
    btnR.config(bg='#607D8B')
def hoverM(e):
    btnM.config(bg='#BDBDBD')
def leaveM(e):
    btnM.config(bg='#607D8B')
def hoverD(e):
    btnD.config(bg='#BDBDBD')
def leaveD(e):
    btnD.config(bg='#607D8B')
def hoverD(e):
    btnSalir.config(bg='#F44336')
def leaveD(e):
    btnSalir.config(bg='#D32F2F')

btnS.bind('<Motion>',hoverS)
btnS.bind('<Leave>',leaveS)
btnR.bind('<Motion>',hoverR)
btnR.bind('<Leave>',leaveR)
btnM.bind('<Motion>',hoverM)
btnM.bind('<Leave>',leaveM)
btnD.bind('<Motion>',hoverD)
btnD.bind('<Leave>',leaveD)
btnSalir.bind('<Motion>',hoverD)
btnSalir.bind('<Leave>',leaveD)

root.mainloop()