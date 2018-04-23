def questao1():
    return print(5**2, 9*5, 15/12, 12/15, 15//12, 12//15, 5%2, 9%5, 15%12, 12%15, 6%6, 0%7)


def questao2():
    return print ("O alarme irá tocar às 5 da tarde.")


def questao3(h,t):

    x=(h+t)%24

    return print ("O alarme irá despertar às {} horas".format(x))


def questao4(a,c):
    from datetime import date
    a=date.today()
    futuro=date.fromordinal (a.toordinal()+c)
    dias= ('segunda','terça','quarta','quinta','sexta','sábado','domingo')
    return dias[futuro.weekday()]


def questao5():
    a=str("Só")
    b=str("trabalho")
    c=str("sem")
    d=str("diversão")
    e=str("faz")
    f=str("de")
    g=str("João")
    h=str("em")
    i=str("chato")

    return print ((a), (b), (c), (d), (e), (f), (g), (h), (i))


def questao6(a,b,c):
    t=a*(b+c)
    return print ("{}".format(t))


def questao7(t):
    a=1000*((1+(0.08/12))**(12*t))
    return print ("Valor final de juros compostos: {:.2f}".format(a))


def questao8(r):
    ac=3.14159*(r**2)
    return print ("Àrea do círculo: {:.2f}".format(ac))


def questao9(a,b):
    r=b*a
    return print ("Àrea do retângulo: {}".format(r))


def questao10(km, l):
    c=km/l
    return print ("{:.2f} km/l".format(c))


def questao11(c):
    f=(c*1.8)+32
    return print ("{:.0f}ºF".format(f))


def questao12(f):
    c=(f-32)/(1.8)
    return print ("{:.0f}ºC".format(c))
