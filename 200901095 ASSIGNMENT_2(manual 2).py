import ast

# Parse the expression into an AST

x = input("enter your expression\n")


code = ast.parse(x)
print(code)

# Print the AST
print(ast.dump(code))

