# Ejercicio 2 Paulina Cajamarca 
def ejercicio_2():
    menor = int(input("Ingresa el número menor: "))
    mayor = int(input("Ingresa el número mayor: "))

    if menor >= mayor:
        print("Error: el primer número debe ser menor.")
        return

    pares = [i for i in range(menor, mayor + 1) if i % 2 == 0]
    cantidad_total = (mayor - menor) + 1

    print(f"\nNúmeros pares entre {menor} y {mayor}:")
    print(", ".join(map(str, pares)))
    print(f"Cantidad total de números en el intervalo: {cantidad_total}")

    # Ejecutar programa
if __name__ == "__main__":

    print("\n" + "="*40 + "\n")
    ejercicio_2()
