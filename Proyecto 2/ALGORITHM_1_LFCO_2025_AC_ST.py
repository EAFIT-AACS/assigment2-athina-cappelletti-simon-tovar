import random

def generar_cadena_valida(n):
    """Genera una cadena válida con n pares de 'a' y 'b'."""
    return 'a' * n + 'b' * n

def generar_cadena_invalida(n):
    """Genera una cadena inválida con el mismo alfabeto pero que no pertenece a la gramática."""
    opciones = [
        'b' * n + 'a' * n,  # Orden incorrecto
        'a' * (n + 1) + 'b' * n,  # Más 'a' que 'b'
        'a' * n + 'b' * (n + 1),  # Más 'b' que 'a'
        ''.join(random.choice('ab') for _ in range(2 * n))  # Orden aleatorio
    ]
    return random.choice(opciones)

def es_valida(cadena):
    """Verifica si la cadena pertenece al lenguaje de la gramática S → aSb | ε."""
    while cadena:
        if cadena[0] == 'a' and cadena[-1] == 'b':
            cadena = cadena[1:-1]  # Elimina un par 'a' y 'b'
        else:
            return False
    return True

# Pruebas con múltiples valores de n
test_cases = [1, 2, 3, 4, 5]
print("Cadenas válidas y su validación:")
for n in test_cases:
    cadena = generar_cadena_valida(n)
    print(f"{cadena} -> {'Válida' if es_valida(cadena) else 'Inválida'}")

print("\nCadenas inválidas y su validación:")
for n in test_cases:
    cadena = generar_cadena_invalida(n)
    print(f"{cadena} -> {'Válida' if es_valida(cadena) else 'Inválida'}")
