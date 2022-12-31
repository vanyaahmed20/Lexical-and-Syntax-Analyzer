import re

# Define a list of tokens that the lexical analyzer should recognize
TOKENS = [
    ('constant', r'\d+'),
    ('Operator_add', r'\+'),
    ('Operator_minus', r'-'),
    ('Operator_mul', r'\*'),
    ('Operator_div', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
]

# Create a regular expression pattern that the lexical analyzer would take and generate the tokens related to expression.
token_pattern = '|'.join('(?P<%s>%s)' % pair for pair in TOKENS)

# lexical analyzer function
def lexer(text):
    
    for match in re.finditer(token_pattern, text):
        # Extract the token type and value from the match
        token_type = match.lastgroup
        value = match.group()
        
        yield token_type, value    # Yield a tuple with the token type and value


# Give expression
for token in lexer('2 + 3 * 4'):
    print(token)
