# Primos

Cálculo de números primos basado en la criba de Eratóstenes.

## Descripción

Este proyecto implementa un algoritmo eficiente para calcular números primos utilizando la **Criba de Eratóstenes**. El programa permite encontrar todos los números primos hasta un límite especificado (máximo 1,000,000) y guarda los resultados en un archivo.

## Características

- ⚡ **Algoritmo eficiente**: Utiliza la Criba de Eratóstenes para un cálculo rápido.
- 📄 **Exportación de resultados**: Guarda todos los números primos en un archivo `primos.txt`.
- 🖥️ **Interfaz interactiva**: Solicita el límite superior al usuario.
- ✅ **Validación de entrada**: Verifica que el valor sea válido (entre 2 y 1,000,000).
- 📊 **Visualización en consola**: Muestra los primeros 100 números primos encontrados.

## Algoritmo: Criba de Eratóstenes

La Criba de Eratóstenes es un método clásico que funciona así:

1. Crear una lista de números desde 2 hasta el límite.
2. Comenzar con el primer número no marcado (2).
3. Marcar todos sus múltiplos como compuestos.
4. Repetir el proceso con el siguiente número no marcado.
5. Los números que permanecen sin marcar son primos.

**Complejidad**: O(n log log n)

## Requisitos

- Python 3.x

## Ejecución

1. Clona este repositorio:

```bash
git clone https://github.com/jemenendezs/primos.git
cd primos
```

2. Ejecuta el script:

```bash
python numeros_primos.py
```

3. Ingresa el límite superior (máximo 1,000,000):

```
Ingrese el valor máximo para calcular números primos (máximo 1,000,000): 100
```

## Ejemplo de salida

**Entrada:**
```
100
```

**Salida en consola:**
```
Calculando números primos hasta 100...

Los primeros 100 números primos hasta 100:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

Los números primos se han guardado en el archivo 'primos.txt' en el mismo directorio.
```

**Archivo generado:** `primos.txt`
```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
```

## Estructura del proyecto

```text
primos/
├── README.md
├── LICENSE
├── numeros_primos.py
└── primos.txt (generado al ejecutar)
```

## Detalles técnicos

### Función principal: `calcular_primos_eratostenes(limite)`

- **Parámetro**: `limite` (int) - valor máximo para buscar primos.
- **Retorna**: Lista de strings con los números primos encontrados.
- **Funcionamiento**:
  - Crea una lista booleana del tamaño de `limite + 1`.
  - Marca 0 y 1 como no primos.
  - Itera desde 2 hasta √limite, marcando múltiplos de cada primo.
  - Utiliza slicing de listas para optimizar el marcado de múltiplos.

### Función `main()`

- Solicita al usuario el límite superior.
- Valida que el valor sea válido (entre 2 y 1,000,000).
- Calcula los primos.
- Muestra los primeros 100 primos en la consola.
- Guarda todos los primos en el archivo `primos.txt`.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor

Proyecto desarrollado con Python para practicar algoritmos matemáticos y programación eficiente.
