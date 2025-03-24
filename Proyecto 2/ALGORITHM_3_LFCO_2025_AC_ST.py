import random

class PDA:
    def __init__(self):
        self.stack = []  # Pila del autómata
        self.state = 'q0'  # Estado inicial

    def reset(self):
        """Reinicia la pila y el estado."""
        self.stack = []
        self.state = 'q0'

    def transition(self, symbol):
        """Procesa la transición según el símbolo de entrada."""
        if self.state == 'q0':
            if symbol == 'a':
                self.stack.append('a')  # Empujar 'a' en la pila
            elif symbol == 'b':
                if self.stack:
                    self.stack.pop()  # Sacar 'a' si hay uno en la pila
                else:
                    self.state = 'q_reject'  # Rechazar si no hay 'a' en pila
            else:
                self.state = 'q_reject'  # Cualquier otro símbolo es inválido

    def process_string(self, string):
        """Procesa la cadena símbolo por símbolo."""
        self.reset()  # Reiniciar el estado antes de procesar
        for symbol in string:
            self.transition(symbol)
            if self.state == 'q_reject':
                return False  # Se rechaza la cadena inmediatamente

        return self.state == 'q0' and not self.stack  # Acepta si pila vacía

# Función principal que recibe una lista de cadenas
def test_pda(strings):
    pda = PDA()
    results = {}
    accepted_strings = []
    for s in strings:
        if pda.process_string(s):
            results[s] = 'Aceptada'
            accepted_strings.append(s)
        else:
            results[s] = 'Rechazada'
    return results, accepted_strings

# Generador de cadenas válidas e inválidas
def generate_strings():
    valid_strings = set()
    invalid_strings = set()
    
    for _ in range(5):
        n = random.randint(1, 5)
        valid_strings.add('a' * n + 'b' * n)  # Cadena válida con igual número de 'a' y 'b'
        invalid_strings.add('a' * n + 'b' * (n - 1))  # Falta una 'b'
        invalid_strings.add('b' * n + 'a' * n)  # Orden incorrecto
    
    return list(valid_strings), list(invalid_strings)

# Construcción del Árbol de Derivación
def derivation_tree(string):
    """Construye la derivación más a la izquierda para una cadena válida."""
    derivation = ["S"]
    step = "S"
    for _ in range(string.count('a')):  # Se repite según la cantidad de 'a'
        step = f"a{step}b"
        derivation.append(step)
    derivation.append(string)  # Paso final con la cadena generada
    return derivation

# Construcción de configuraciones del PDA
def pda_configurations(string):
    """Genera las configuraciones del PDA durante el procesamiento de una cadena."""
    pda = PDA()
    pda.reset()  # Se reinicia el autómata antes de procesar la cadena
    configurations = [("q0", "", string)]  # Estado inicial con pila vacía
    remaining_input = string
    for symbol in string:
        pda.transition(symbol)
        remaining_input = remaining_input[1:]  # Eliminar el primer carácter procesado
        configurations.append((pda.state, "".join(pda.stack), remaining_input))
    return configurations

# Pruebas automáticas
valid_cases, invalid_cases = generate_strings()
results, accepted = test_pda(valid_cases + invalid_cases)

print("Cadenas procesadas:")
for s, result in results.items():
    print(f"{s}: {result}")

# Construcción de árboles de derivación
if accepted:
    print("\nÁrboles de derivación para las cadenas aceptadas:")
    for s in accepted:
        print(f"\nCadena: {s}")
        for step in derivation_tree(s):
            print(f"  {step}")

# Construcción de configuraciones del PDA
if accepted:
    print("\nConfiguraciones del PDA para las cadenas aceptadas:")
    for s in accepted:
        print(f"\nCadena: {s}")
        for config in pda_configurations(s):
            print(f"  Estado: {config[0]}, Pila: {config[1]}, Entrada restante: {config[2]}")
