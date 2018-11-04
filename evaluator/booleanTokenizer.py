import ply.lex as lex
import re
from .exceptions import LexerInvalidToken

regex_or = r'(?i)\|\|?|or'
regex_and = r'(?i)&&?|and'
regex_true = r'(?i)si|true'
regex_false = r'(?i)no|false'
compiled_or = re.compile(regex_or)
compiled_and = re.compile(regex_and)
compiled_true = re.compile(regex_true)
compiled_false = re.compile(regex_false)

tokens = ('OR', 'AND', 'VAR', 'TRUE', 'FALSE', 'NOT', 'LPAREN', 'RPAREN')

t_OR = regex_or
t_NOT = r'~|¬'
t_AND = regex_and
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_TRUE(t):
    r'(?i)si|true'
    t.value = True
    return t


def t_FALSE(t):
    r'(?i)no|false'
    t.value = False
    return t


def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if compiled_or.fullmatch(t.value):
        t.type = 'OR'
    elif compiled_and.fullmatch(t.value):
        t.type = 'AND'
    elif compiled_true.fullmatch(t.value):
        t.type = 'TRUE'
        t.value = True
    elif compiled_false.fullmatch(t.value):
        t.type = 'FALSE'
        t.value = False
    return t


def t_error(t):
    raise LexerInvalidToken


t_ignore = ' \r\n\t'

boolean_lexer = lex.lex()
