tabla = [["0", "0", "0"],
         ["0", "0", "0"],
         ["0", "0", "0"]]

def ganar(tabla):
    if "0" in (tabla[0][0] and tabla[0][1] and tabla[0][2]) or (tabla[1][0] and tabla[1][1] and tabla[1][2]) or (tabla[2][0] and tabla[2][1] and tabla[2][2]) or (tabla[0][0] and tabla[1][1] and tabla[2][2]) or (tabla[2][0] and tabla[1][1] and tabla[0][2]):
        print("GANO EL 0")
    if "X" in (tabla[0][0] and tabla[0][1] and tabla[0][2]) or (tabla[1][0] and tabla[1][1] and tabla[1][2]) or (tabla[2][0] and tabla[2][1] and tabla[2][2]) or (tabla[0][0] and tabla[1][1] and tabla[2][2]) or (tabla[2][0] and tabla[1][1] and tabla[0][2]):
        print("GANO LA X")

def ingresar():
    return

ganar(tabla)

