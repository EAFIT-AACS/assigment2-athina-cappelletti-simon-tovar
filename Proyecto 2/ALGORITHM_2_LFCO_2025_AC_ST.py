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
    results = {}
    for s in strings:
        pda = PDA()  # Se crea una nueva instancia por cada cadena
        results[s] = 'Aceptada' if pda.process_string(s) else 'Rechazada'
    return results

# Generador de cadenas válidas e inválidas
def generate_strings():
    valid_strings = []
    invalid_strings = []
    
    for _ in range(5):
        n = random.randint(1, 5)
        valid_strings.append('a' * n + 'b' * n)  # Cadena válida con igual número de 'a' y 'b'
        invalid_strings.append('a' * n + 'b' * (n - 1))  # Falta una 'b'
        invalid_strings.append('b' * n + 'a' * n)  # Orden incorrecto
    
    return valid_strings, invalid_strings

# Pruebas automáticas
valid_cases, invalid_cases = generate_strings()
print("Cadenas válidas:")
results = test_pda(valid_cases)
for s, result in results.items():
    print(f"{s}: {result}")

print("\nCadenas inválidas:")
results = test_pda(invalid_cases)
for s, result in results.items():
    print(f"{s}: {result}")
