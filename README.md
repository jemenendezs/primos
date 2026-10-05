# Primos

Proyecto en Python para calcular números primos utilizando la criba de Eratóstenes.

## Descripción

Este repositorio contiene una implementación simple y eficiente del algoritmo de la criba de Eratóstenes para identificar números primos dentro de un rango determinado.

La criba de Eratóstenes es un método clásico para encontrar todos los números primos menores o iguales a un valor `n`. Funciona marcando múltiplos de cada primo encontrado y dejando únicamente los números no marcados.

## Características

- Cálculo de números primos en un rango especificado.
- Implementación sencilla y fácil de entender.
- Enfoque educativo para practicar lógica y algoritmos en Python.
- Ideal para aprender cómo funcionan los números primos y la eficiencia de la criba.

## Requisitos

- Python 3.x

## Uso

1. Clona este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el script principal:

```bash
python main.py
```

4. Ingresa el límite superior para encontrar los números primos.

## Ejemplo

Si el usuario ingresa:

```bash
50
```

La salida esperada será:

```text
Números primos hasta 50:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

## Algoritmo utilizado

La idea principal es:

1. Crear una lista con todos los números desde 2 hasta `n`.
2. Marcar como compuestos los múltiplos de cada número primo.
3. Los números que no fueron marcados son primos.

## Estructura del proyecto

```text
primos/
├── README.md
├── LICENSE
├── main.py
```

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor

Proyecto desarrollado con Python para practicar algoritmos matemáticos y programación.
