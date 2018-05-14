import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules2)
text = "((14 + 6) + (2 - 7 / 9)) / 5"
#text = "5 / (3 + 4)"
ast = parser.parse(text, lexer)

print ast

#MDA