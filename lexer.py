
from constants import *

def lex_string(string:str):
     json_string = ''

     if string[0] == JSON_QUOTE:
            string = string[1:]
     else:
            return None, string

     for c in string:
            if c == JSON_QUOTE:
                return json_string, string[len(json_string)+1:]
            else:
                json_string += c

     raise Exception('Expected end-of-string quote')

def lex_number(num_str:str):
    json_num = ''
    number_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', 'e', '.']

    for c in num_str:
        if c in number_chars:
            json_num += c
        else:
            break

    if not len(json_num):
        return None,num_str
    
    rest = num_str[len(json_num):]

    if '.' in json_num:
        return float(json_num),rest

    return int(json_num),rest

def lex_bool(bool_str:str):
    str_len = len(bool_str)
    if str_len >= TRUE_LEN and \
        bool_str[:TRUE_LEN] == 'true':
        return True , bool_str[:TRUE_LEN]

    if str_len >= FALSE_LEN and \
        bool_str[:FALSE_LEN] == 'false':
        return False, bool_str[:FALSE_LEN]
    return None,bool_str

def lex_null(null_str:str):
    string_len = len(null_str)
    if string_len >= NULL_LEN and \
       null_str[:NULL_LEN] == 'null':
        return None, null_str[:NULL_LEN]
    return None,null_str

def lex(string:str):
    tokens = []
    while len(string):
        json_str,string = lex_string(string)
        if json_str is not None:
            # We are able to lex it as string
            tokens.append(json_str)
            continue

        json_num , string = lex_number(string)
        if json_num is not None:
            tokens.append(json_num)
            continue

        json_bool,string = lex_bool(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue

        json_none , string = lex_bool(string)
        if json_bool is not None:
            tokens.append(json_none)
            continue

        c = string[0]

        if c in JSON_WHITESPACE:
            # Ignore whitespace
            string = string[1:]
        elif c in JSON_SYNTAX:
            tokens.append(c)
            string = string[1:]

        else:
            raise Exception('Unexpected character: {}'.format(c))
    return tokens