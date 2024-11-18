def vydej_obedu():
    yield "vitaminovy napoj"
    jidlo = yield

    if jidlo == 'A':
        yield ["polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko"]
    elif jidlo == 'B':
        yield ["polévka česneková s bramborem",
         "rizek s kasi",
         "jablko"]


corutina1 = vydej_obedu()

napoje = next(corutina1)
print(napoje)

next(corutina1)
jidla = corutina1.send("A")
corutina1.close()

print(jidla)