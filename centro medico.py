edad=float(input("ingrese la edad del niño en meses"))
if edad<12:
    peso=float(input("ingrese el peso del niño"))
    dosis=((peso+10)/(10*edad))+8
    print("la dosis a colocarle al niño es: ",dosis)
else:
    print("no tiene edad adecuada para la vacuna")