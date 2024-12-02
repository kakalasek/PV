def vydej_obedu():
    yield "vitaminovy napoj"
    yield ["polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko"]


corutina1 = vydej_obedu()

napoje = next(corutina1)
print(napoje)

jidla = next(corutina1)
print(jidla)