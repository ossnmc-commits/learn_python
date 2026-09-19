Python

========================

Note:
Whitespace
In Python, whitespace is syntactically significant. Python program-
mers are especially sensitive to the effects of whitespace on code
clarity. Follow these guidelines related to whitespace:
■ Use spaces instead of tabs for indentation.
■ Use four spaces for each level of syntactically significant indenting.
■ Lines should be 79 characters in length or less.
■ Continuations of long expressions onto additional lines should
be indented by four extra spaces from their normal indentation
level.
■ In a file, functions and classes should be separated by two blank
lines.
■ In a class, methods should be separated by one blank line.
■ In a dictionary, put no whitespace between each key and colon,
and put a single space before the corresponding value if it fits on
the same line.
■ Put one—and only one—space before and after the = operator in a
variable assignment.
■ For type annotations, ensure that there is no separation between
the variable name and the colon, and use a space before the type
information.

========================

Follow these guidelines
related to naming:
■ Functions, variables, and attributes should be in lowercase_
underscore format.
■ Protected instance attributes should be in _leading_underscore
format.
	■ Private instance attributes should be in __double_leading_
	underscore format.
	■ Classes (including exceptions) should be in CapitalizedWord
	format.
		■ Module-level constants should be in ALL_CAPS format.
		■ Instance methods in classes should use self, which refers to the
		object, as the name of the first parameter.
		■ Class methods should use cls, which refers to the class, as the
		name of the first parameter.
		
		========================

		guidance for expressions and statements:
		■ Use inline negation (if a is not b) instead of negation of positive
		expressions (if not a is b).
		■ Don’t check for empty containers or sequences (like [] or '')
		by comparing the length to zero (if len(somelist) == 0). Use
		if not somelist and assume that empty values will implicitly
			evaluate to False.
			■ The same thing goes for non-empty containers or sequences (like
			[1] or 'hi'). The statement if somelist is implicitly True for non-
			empty values.
			■ Avoid single-line if statements, for and while loops, and except
			compound statements. Spread these over multiple lines for
			clarity.
			■ If you can’t fit an expression on one line, surround it with paren-
			theses and add line breaks and indentation to make it easier to
			read.
			■ Prefer surrounding multiline expressions with parentheses over
			using the \ line continuation character.
			

============

how to import modules and use
them in your code:
■ Always put import statements (including from x import y) at the
top of a file.
■ Always use absolute names for modules when importing them, not
names relative to the current module’s own path. For example, to
import the foo module from within the bar package, you should
use from bar import foo, not just import foo.
■ If you must do relative imports, use the explicit syntax
from . import foo.
■ Imports should be in sections in the following order: standard
library modules, third-party modules, your own modules. Each
subsection should have imports in alphabetical order.

====


Python is a high-level programming language known for its simple and readable syntax. It has the following features:

Allows writing clean code with fewer lines.
Supports multiple programming paradigms including object-oriented, functional and procedural programming.
Widely used in web development, automation, data analysis, artificial intelligence and many other fields.
Dynamically typed and has automatic garbage collection

Python uses indentation (spaces or tabs) to define code blocks
# (octothorpe or pound character) is used to write comments in Python. Comments are ignored during execution.

The print() function is used for output in various formats and the input() function enables interaction with users.

Python's input() function is used to take user input. By default, it returns the user input in form of a string. 

print() function allows us to display text, variables and expressions on the console.

x, y = input("Enter two numbers: ").split()
print(x , y)

i = int(input("How old are you?: "))
f = float(input("Evaluate 7/2: "))
print(i, f)

Read Input Using sys.stdin

sys.stdin is a file-like object that reads data directly from the standard input stream. It is useful when processing multiple lines of input or handling large amounts of data efficiently.

```
import sys
for line in sys.stdin:
	
	if line.rstrip() == "q":
		break
		print(f"Input: {line.rstrip()}")
		
		print("Exit")
```

Explanation:

import sys imports the sys module.
sys.stdin reads input from the standard input stream one line at a time.
for line in sys.stdin iterates over each line entered by the user.
	rstrip() removes the trailing newline character (\n).
	if line.rstrip() == "q" stops the program when the user enters q.
		

		
		import sys
		line = sys.stdin.readline()
		print("Output:", line.strip())
		
		Input
		
		GeeksforGeeks
		
		Output
		
		Output: GeeksforGeeks
		
		2. sys.stdin.readlines(): readlines() reads all input lines and returns them as a list.
		
		import sys
		lines = sys.stdin.readlines()
		print(lines)
		
		Input:
		
		Python
		Pandas
		NumPy
		
		Output
		
		['Python\n', 'Pandas\n', 'NumPy\n']
		
		Explanation: readlines() reads all available input, each line becomes an element of a list. Newline characters (\n) are preserved.
		
		3. sys.stdin.read(): read() reads the entire contents of the input stream at once and returns a single string.
		
		import sys
		data = sys.stdin.read()
		print(data)
		
		Input:
		
		Hello
		Python
		GeeksforGeeks
		
		Output
		
		Hello
		Python
		GeeksforGeeks
		
		
PEMDAS which
stands for Parentheses Exponents Multiplication Division Addition Subtraction

 PEMDAS as PE(M&D)(A&S)


 the difference between = (single-equal) and == (double-equal)? The = (single-equal) assigns
the value on the right to a variable on the left. The == (double-equal) tests whether two things
have the same value. 


from sys import argv
# read the WYSS section for how to run `this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
