def calcular_primos_eratostenes(limite):
    """Función para calcular los números primos hasta un límite dado usando la Criba de Eratóstenes."""
    if limite < 2:
        return []
    
    criba = [True] * (limite + 1)
    criba[0] = criba[1] = False
    
    for num in range(2, int(limite**0.5) + 1):
        if criba[num]:
            criba[num*num : limite+1 : num] = [False] * len(criba[num*num : limite+1 : num])
    
    primos = [str(i) for i, es_primo in enumerate(criba) if es_primo]
    return primos

def main():
    try:
        limite = int(input("Ingrese el valor máximo para calcular números primos (máximo 1,000,000): "))
        if limite > 1000000:
            print("El valor máximo permitido es 1,000,000.")
            return
        if limite < 2:
            print("No hay números primos menores que 2.")
            return
            
        print(f"Calculando números primos hasta {limite}...")
        primos = calcular_primos_eratostenes(limite)
        
        # Mostrar los primeros 100 primos en la consola
        print(f"\nLos primeros 100 números primos hasta {limite}:")
        print(", ".join(primos[:100]))
        
        # Guardar todos los primos en un archivo de texto
        with open("primos.txt", "w") as archivo:
            archivo.write(", ".join(primos))
        
        print(f"\nLos números primos se han guardado en el archivo 'primos.txt' en el mismo directorio.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()