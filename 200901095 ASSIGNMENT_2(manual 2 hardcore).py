import ast

# Parse the expression into an AST

code = ast.parse("print(1000*(8*9))")
print(code)

# Print the AST
print(ast.dump(code))

