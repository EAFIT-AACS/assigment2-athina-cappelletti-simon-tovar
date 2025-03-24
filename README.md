Athina Cappelletti Simón Tovar

Clases de los miércoles SI2002-2 (7309)

Sistema operativo: Windows

Lenguaje de programación: Python

Instrucciones de ejecución:

Abra su editor de código (preferiblemente VSCode).
Vaya a las opciones para ejecutar el archivo Python.
Se abrirá la consola, donde podrá ver los resultados, ya que tiene implementados los casos de pruebas en el código para facilitar la ejecución.

Explicación de los algoritmos:

Algoritmo_1 (Procesamiento de cadenas con PDA): Este algoritmo recibe una lista de cadenas y las procesa mediante un autómata de pila (PDA). Verifica que la cantidad de símbolos 'a' y 'b' sea igual y estén en el orden correcto. Si la cadena cumple con estas reglas, se acepta; de lo contrario, se rechaza. Al final, devuelve un listado de las cadenas aceptadas y rechazadas.

Algoritmo_2 (Filtrado de cadenas aceptadas): A partir del resultado del Algoritmo_1, este algoritmo extrae únicamente las cadenas que fueron aceptadas. Su función es seleccionar las cadenas que cumplen con la gramática establecida y que pueden ser utilizadas en la siguiente fase de construcción de árboles.

Algoritmo_3 (Construcción de árboles o configuraciones): Recibe las cadenas aceptadas del Algoritmo_2 y genera una de dos posibles estructuras: (1) el árbol de derivación más a la izquierda, donde se muestra paso a paso la transformación de la gramática hasta formar la cadena final, o (2) las configuraciones del autómata de pila, registrando su estado, el contenido de la pila y la entrada restante en cada paso del procesamiento.

Bibliografía:

https://pypi.org/project/automata-lib/5.0.0/

https://www.chegg.com/homework-help/questions-and-answers/write-python-program-implement-pda-accepts-one-languages-l-anb2n-n-1-b-l-aibj-j-j-1-design-q86636643

https://caleb531.github.io/automata/api/pda/class-npda/



[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gjhNPQOm)
