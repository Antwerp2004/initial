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
        raise UnclosedString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscapeInString(result.text[1:]);
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


// Literals
// Integer Literals
INTEGER_LITERAL: DECIMAL_INT | BINARY_INT | OCTAL_INT | HEXA_INT;
DECIMAL_INT: '0' | [1-9] [0-9]*;
BINARY_INT: '0' [bB] [01]+;
OCTAL_INT: '0' [oO] [0-7]+;
HEXA_INT: '0' [xX] [0-9a-fA-F]+;

// Floating-point Literals
FLOATING_POINT_LITERAL: INT_PART '.' DECI_PART? EXP_PART?;
fragment INT_PART: [0-9]+;
fragment DECI_PART: [0-9]*;
fragment EXP_PART: [eE] [+-]? [0-9]+;

// String Literals
STRING_LITERAL: (DOUBLE_QUOTE DOUBLE_QUOTE) | (DOUBLE_QUOTE INSIDE_STRING+ DOUBLE_QUOTE) {self.text = self.text[1:-1]};
fragment INSIDE_STRING: ESCAPE_SEQUENCE | ~["\\];
fragment DOUBLE_QUOTE: ["];
fragment BACKLASH: '\\';
fragment ESCAPE_SEQUENCE: (BACKLASH [ntr]) | (BACKLASH ["]) | (BACKLASH BACKLASH); 

// Boolean Literals
BOOLEAN_LITERAL: 'true' | 'false';

// Nil Literal
NIL: 'nil';


// Identifiers
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;

NL: '\n' -> skip; //skip newlines

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

ILLEGAL_ESCAPE: DOUBLE_QUOTE INSIDE_STRING* ~[ntr\\];
UNCLOSE_STRING: DOUBLE_QUOTE INSIDE_STRING* EOF;
ERROR_CHAR: .;