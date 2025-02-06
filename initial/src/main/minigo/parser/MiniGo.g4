// Student's ID: 2212779

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : decl+ EOF ;

decl: funcdecl | vardecl  ;

vardecl: 'var' IDENTIFIER 'int' ';' ;

funcdecl: 'func' IDENTIFIER '(' ')' '{' '}' ';' ;

// Operators
multiply_operator: '*' | '/' | '%';
add_operator: '+' | '-';
related_operator: '==' | '!=' | '>=' | '<=' | '>' | '<';
logical_operator: '&&' | '||';

// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
BOOLEAN_LITERAL: 'true' | 'false';

// Literals
// Floating-point Literals
FLOATING_POINT_LITERAL: INT_PART '.' DECI_PART? EXP_PART?;
fragment INT_PART: [0-9]+;
fragment DECI_PART: [0-9]*;
fragment EXP_PART: [eE] [+-]? [0-9]+;

// Identifiers
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;

NL: '\n' -> skip; //skip newlines

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;