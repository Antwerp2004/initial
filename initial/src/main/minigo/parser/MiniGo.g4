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

program  : (stmt | decl)+ EOF ;

decl: var_decl | const_decl
    | array_decl
    | struct_decl | interface_decl
    | func_decl | method_decl ;

// Statements
stmt: var_decl | const_decl
    | assign_stmt
    | if_stmt
    | for_stmt
    | break_stmt | continue_stmt
    | call_stmt | return_stmt 
    | comment ;
// Block
block: OPEN_BRACE statement+ CLOSE_BRACE

// Variable, Constant declaration Statement
var_decl: VAR IDENTIFIER (typ | EQUAL expr | typ EQUAL expr) SEMICOLON;
const_decl: CONST IDENTIFIER ASSIGNMENT_SIGN expr SEMICOLON;

// Assignment Statement
assign_stmt: lhs assign_operator expr SEMICOLON;
lhs: IDENTIFIER | array_access | struct_access;

// If Statement
if_stmt: only_if_stmt else_if_list else_stmt? SEMICOLON;
only_if_stmt: IF OPEN_PARENTHESIS expr CLOSE_PARENTHESIS block;
else_if_list: (ELSE IF OPEN_PARENTHESIS expr CLOSE_PARENTHESIS block)*;
else_stmt: ELSE block;

// For Statement
for_stmt: basic_for_loop | for_loop_initial | for_loop_range;
// Basic For Loop
basic_for_loop: FOR condition block SEMICOLON;
condition: expr;
// For Loop with Initialization, Condition, and Update
for_loop_initial: FOR initialization condition SEMICOLON update block SEMICOLON;
initialization: IDENTIFIER assign_operator expr SEMICOLON | var_decl;
update: IDENTIFIER assign_operator expr;
// For Loop with Range
for_loop_range: FOR IDENTIFIER COMMA IDENTIFIER ASSIGNMENT_SIGN RANGE IDENTIFIER block SEMICOLON;

// Break Statement
break_stmt: BREAK SEMICOLON;
// Continue Statement
continue_stmt: CONTINUE SEMICOLON;

// Call Statement
call_stmt: (func_call | method_call) SEMICOLON;
// Return Statement
return_stmt: RETURN expr? SEMICOLON;


// Function
// Function declaration
func_decl: FUNC IDENTIFIER OPEN_PARENTHESIS param_list? CLOSE_PARENTHESIS typ? block SEMICOLON;
// Function call
func_call: IDENTIFIER OPEN_PARENTHESIS argument_list? CLOSE_PARENTHESIS;
argument_list: expr (COMMA expr)*;


// Method
// Method declaration
method_decl: FUNC OPEN_PARENTHESIS IDENTIFIER IDENTIFIER CLOSE_PARENTHESIS 
        IDENTIFIER OPEN_PARENTHESIS param_list? CLOSE_PARENTHESIS typ? OPEN_BRACE block CLOSE_BRACE SEMICOLON;
// Method call
method_call: IDENTIFIER DOT func_call;


// Type
primitive_type: INT | FLOAT | STRING | BOOLEAN;
typ: primitive_type | IDENTIFIER | array_type;


// Expression
expr: expr OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2;
expr2: expr2 relational_operator expr3 | expr3;
expr3: expr3 arith_low_operator expr4 | expr4;
expr4: expr4 arith_high_operator expr5 | expr5;
expr5: (NOT | SUB) expr5 | operand;
// Sub-expression
sub_expr: OPEN_PARENTHESIS expr CLOSE_PARENTHESIS;


// Operand
operand: INTEGER_LITERAL
        | FLOATING_POINT_LITERAL
        | STRING_LITERAL
        | BOOLEAN_LITERAL
        | array_literal
        | struct_literal
        | array_access
        | struct_access
        | IDENTIFIER
        | func_call
        | method_call
        | sub_expr;


// Array
// Array declaration
array_decl: VAR IDENTIFIER (OPEN_BRACKET (INTEGER_LITERAL | IDENTIFIER) CLOSE_BRACKET)+ (primitive_type | IDENTIFIER) SEMICOLON;
// Array type
array_type: array_size_box array_type | array_size_box (primitive_type | IDENTIFIER);
array_size_box: OPEN_BRACKET expr CLOSE_BRACKET;

// Array Literal
array_literal: array_type OPEN_BRACE array_ele_list* CLOSE_BRACE;
array_ele_list: expr (COMMA expr)*
            | OPEN_BRACE array_ele_list CLOSE_BRACE;
// Array access
array_access: array_access array_size_box | IDENTIFIER array_size_box;


// Struct
// Struct declaration
struct_decl: TYPE IDENTIFIER STRUCT OPEN_BRACE field_list? CLOSE_BRACE SEMICOLON;
field_list: IDENTIFIER (typ | array_type) SEMICOLON;

// Struct Literal
struct_literal: IDENTIFIER OPEN_BRACE struct_ele_list? CLOSE_BRACE;
struct_ele_list: struct_ele (COMMA struct_ele)*;
struct_ele: IDENTIFIER COLON expr;
// Struct access
struct_access: struct_access DOT IDENTIFIER | IDENTIFIER DOT IDENTIFIER;


// Interface
// Interface declaration
interface_decl: TYPE IDENTIFIER INTERFACE OPEN_BRACE interface_method* CLOSE_BRACE SEMICOLON;
interface_method: IDENTIFIER OPEN_PARENTHESIS param_list? CLOSE_PARENTHESIS typ? SEMICOLON;
param_list: param_decl (COMMA param_decl)*;
param_decl: IDENTIFIER (COMMA IDENTIFIER)* typ;


// Operators
arith_high_operator: MULTIPLY | DIVIDE | REMAIN;
arith_low_operator: ADD | SUB;
relational_operator: COMPARE_STR | NOT_EQ | GREATER_OR_EQ | LESS_OR_EQ | GREATER | LESS;
assign_operator: ASSIGNMENT_SIGN | SHORT_ADD | SHORT_SUB | SHORT_MULTIPLY | SHORT_DIVIDE | SHORT_REMAIN;


// Comments
comment: SINGLE_LINE_COMMENT;
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

// Assignment
ASSIGNMENT_SIGN: ':=';
SHORT_ADD: '+=';
SHORT_SUB: '-=';
SHORT_MULTIPLY: '*=';
SHORT_DIVIDE: '/=';
SHORT_REMAIN: '%=';

// Other
EQUAL: '=';
DOT: '.';


// Separators
OPEN_PARENTHESIS: '(';
CLOSE_PARENTHESIS: ')';
OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';


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
NIL_LITERAL: 'nil';


NEWLINE: ('\r\n' | '\n') {self.text = '\n'};

// Identifiers
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;

// Whitespace
WHITESPACE: [ \t\f\r] -> skip;


ILLEGAL_ESCAPE: DOUBLE_QUOTE INSIDE_STRING* BACKLASH ~[ntr\\];
UNCLOSE_STRING: DOUBLE_QUOTE INSIDE_STRING* ([\r\n] | EOF);
ERROR_CHAR: .;