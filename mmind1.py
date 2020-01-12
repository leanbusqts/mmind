import random


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
codigo = ''
for i in range(4):
                candidato = random.choice(digits)
                while candidato in codigo:
                    candidato = random.choice(digits)
                codigo = codigo + candidato
# print("el codigo es: ", codigo)
print("mastermind!")
intentos = 0
game = True
while game:
            code = input("code: ")
            intentos = intentos + 1
            good = 0
            right = 0
            try:
                int(code)
                if len(code) != len(codigo):    # compara el largo de los strings
                    print("Debe ser un número entero de cuatro digitos. Prueba de nuevo!")
                    continue
                for l in set(code):             # Cuenta si se repite algun numero del string code
                    conter = code.count(l)
                if conter is not 1:
                    print("Los números no deben repetirse. Prueba de nuevo!")
                    continue
                for i in range(4):              # Compara las listas code y codigo
                    if code[i] == codigo[i]:
                        good = good + 1
                    elif code[i] in codigo:
                        right = right + 1
                print(good, "G -", right, "R")
            except ValueError:
                print("Valor inválido, deben ser números enteros")
            if code == codigo:
                    print("Felicitaciones adivinaste el número")
                    game = False
# print("Fin del juego! Gracias por jugar!")
