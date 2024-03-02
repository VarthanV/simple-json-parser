from lexer import lex

output = lex('{"foo": [1, 2, {"bar": 2}]}')
print("tokens ",output)