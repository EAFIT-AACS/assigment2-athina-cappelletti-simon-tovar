Athina Cappelletti Simón Tovar

Wednesday Classes SI2002-2 (7309)

Operating System: Windows

Programming Language: Python

Execution Instructions:

Open your code editor (preferably VSCode). Go to the options to run the Python file. The console will open, where you can see the results, as the test cases are implemented in the code to facilitate execution.

Explanation of the Algorithms:

Algorithm 1 (String Processing with PDA): This algorithm receives a list of strings and processes them using a stack automaton (PDA). It verifies that the number of symbols 'a' and 'b' are equal and that they are in the correct order. If the string meets these rules, it is accepted; otherwise, it is rejected. Finally, it returns a list of the accepted and rejected strings.

Algorithm_2 (Filtering accepted strings): From the result of Algorithm_1, this algorithm extracts only the accepted strings. Its function is to select the strings that comply with the established grammar and can be used in the next tree building phase.

Algorithm_3 (Building trees or configurations): It receives the accepted strings from Algorithm_2 and generates one of two possible structures: (1) the leftmost derivation tree, which shows the step-by-step transformation of the grammar until the final string is formed, or (2) the configurations of the stack automaton, recording its state, the stack contents, and the remaining input at each processing step.

References:

https://pypi.org/project/automata-lib/5.0.0/

https://www.chegg.com/homework-help/questions-and-answers/write-python-program-implement-pda-accepts-one-languages-l-anb2n-n-1-bl-aibj-jj-1-design-q86636643

https://caleb531.github.io/automata/api/pda/class-npda/
