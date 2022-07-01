from tkinter import *
from diccionario import *
window = Tk()
window.title("Cálculo Cultivo")

lblgr=[]
lblpr=[]
lblkcal=[]
lblrend=[]
sld=[]


def valores(val):
    metros = float(0)
    calo = 0

    ena = float(0)
    for i in range (len(lista)):
        lblgr[i].config(text = sld[i].get())
        lblkcal[i].config(text = int(lista[i]['kcal'])*int(sld[i].get())//100)
        var1, var2 = 12,slidere.get()
        rendimiento = "{0:.2f}".format((float(sld[i].get()/1000))/(float(lista[i]['rendimiento'])/1000)*var1*var2)

        if 'nu' in lista[i]:
            rend = float(lista[i]['nu'])/10000*float(rendimiento)
            lblrend[i].config(text = rendimiento + ' ' +"{0:.1f}".format(rend))
        else:
            lblrend[i].config(text = rendimiento)

        metros = float(metros) + float(rendimiento)
        lblMet.config(text = "{0:.2f}".format(metros))

        calo = calo + int(lista[i]['kcal'])*int(sld[i].get())//100//30
        lblkca.config(text = calo)

        if ('poda' in lista[i] and int(sld[i].get())!=0):
            ena = float(lista[i]['poda']) * float(metros) / 12
            lblleña.config(text = "{0:.2f}".format(ena))

for i in range (len(lista)):
    conta = 0
    a,b,c,d,e = 2,4,0,1,3
    if i >= 16 and i < 32:
        a,b,c,d,e = 7,9,5,6,8
        f = i - 16
    elif i >= 32 and i < 48:
        a,b,c,d,e = 12,14,10,11,13
        f = i - 32
    elif i >= 48 and i < 64:
        a,b,c,d,e = 17,19,15,16,18
        f = i - 48
    else:
        f = i
    lblgr.append(Label(window, text="Gr/Mes"))
    lblgr[i].grid(column=a, row=f)

    sld.append(Scale(window,from_=0,to=(float(lista[i]['maxMes'])*1000),orient=HORIZONTAL,command=valores))
    sld[i].grid(column=b, row=f)


    indice = float(lista[i]['rendimiento'])*float(lista[i]['kcal'])/20000

    lblpr.append(Label(window, text=lista[i]['producto']+"("+str("{0:.1f}".format(indice))+")"))

    lblpr[i].grid(column=c, row=f)

    lblkcal.append(Label(window, text=lista[i]['kcal']))
    lblkcal[i].grid(column=d, row=f)

    lblrend.append(Label(window, text=lista[i]['rendimiento']))
    lblrend[i].grid(column=e, row=f)

lblMetros = Label(window, text="Metros")
lblMetros.grid(column=0,row=18)
lblMet = Label(window, text=0)
lblMet.grid(column=1,row=18)

lblkcalo = Label(window, text="kcal dia")
lblkcalo.grid(column=2,row=18)
lblkca = Label(window, text=0)
lblkca.grid(column=3,row=18)

lblred = Label(window, text="redimension")
lblred.grid(column=4,row=18)


slidere = Scale(window,from_=1,to=3,orient=HORIZONTAL,command=valores)
slidere.grid(column=5,row=18)

lblkgleña = Label(window, text="Kg Leña Mes")
lblkgleña.grid(column=6,row=18)
lblleña = Label(window, text=0)
lblleña.grid(column=7,row=18)

window.mainloop()