mesesnino=float(input("ingrese la edad calculando en meses"))
if mesesnino<12:
    libras=float(input("ingrese el peso calculando en libras"))
    vacuna=((libras+10)/(10*mesesnino))+8
    print("la cantidad de vacuna: ",vacuna)
else:
    print("no se puede vacunar")