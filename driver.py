from lexer import lex
from json_parser import parse


def json_to_object(string):
    tokens = lex(string)
    return parse(tokens, is_root=True)[0]

