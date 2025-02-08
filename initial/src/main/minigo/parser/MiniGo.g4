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
        raise UncloseString(result.text[1:].replace("\r","").replace("\n",""));
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
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
multiply_operator: MULTIPLY | DIVIDE | REMAIN;
add_operator: ADD | SUB;
related_operator: COMPARE_STR | NOT_EQ | GREATER_OR_EQ | LESS_OR_EQ | GREATER | LESS;
logical_operator: AND | OR;


// Comments
// Single-line Comments
SINGLE_LINE_COMMENT: '//' (~[\r\n])* -> skip;
// Multi-line Comments



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


// Operators
// Arithmetic
ADD: '+';
SUB: '-';
MULTIPLY: '*';
DIVIDE: '/';
REMAIN: '%';
SHORT_ADD: '+=';
SHORT_SUB: '-=';
SHORT_MULTIPLY: '*=';
SHORT_DIVIDE: '/=';
SHORT_REMAIN: '%=';

// Relational
COMPARE_STR: '==';
NOT_EQ: '!=';
GREATER_OR_EQ: '>=';
LESS_OR_EQ: '<=';
GREATER: '>';
LESS: '<';

// Logical
AND: '&&';
OR: '||';
NOT: '!';

// Other
DECL: ':=';
EQUAL: '=';
DOT: '.';


// Separators
OPEN_PARANTHESIS: '(';
CLOSE_PARANTHESIS: ')';
OPEN_SQUARE: '[';
CLOSE_SQUARE: ']';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';
COMMA: ',';
SEMICOLON: ';';


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
STRING_LITERAL: (DOUBLE_QUOTE DOUBLE_QUOTE | DOUBLE_QUOTE INSIDE_STRING+ DOUBLE_QUOTE) {self.text = self.text[1:-1]};
fragment INSIDE_STRING: ESCAPE_SEQUENCE | ~[\n\r"\\];
fragment DOUBLE_QUOTE: ["];
fragment BACKLASH: '\\';
fragment ESCAPE_SEQUENCE: (BACKLASH [ntr]) | (BACKLASH DOUBLE_QUOTE) | (BACKLASH BACKLASH);

// Boolean Literals
BOOLEAN_LITERAL: 'true' | 'false';

// Nil Literal
NIL: 'nil';


NEWLINE: ('\r\n' | '\n') {self.text = '\n'};

// Identifiers
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;

// Whitespace
WHITESPACE: [ \t\f\r] -> skip;


ILLEGAL_ESCAPE: DOUBLE_QUOTE INSIDE_STRING* BACKLASH ~[ntr\\];
UNCLOSE_STRING: DOUBLE_QUOTE INSIDE_STRING* ([\r\n] | EOF);
ERROR_CHAR: .;