# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3")
        buf.write("\3\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\2\2")
        buf.write("\n\2\4\6\b\n\f\16\20\2\6\3\2\27\31\3\2\25\26\3\2\37$\3")
        buf.write("\2%&\2,\2\23\3\2\2\2\4\33\3\2\2\2\6\35\3\2\2\2\b\"\3\2")
        buf.write("\2\2\n*\3\2\2\2\f,\3\2\2\2\16.\3\2\2\2\20\60\3\2\2\2\22")
        buf.write("\24\5\4\3\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2")
        buf.write("\25\26\3\2\2\2\26\27\3\2\2\2\27\30\7\2\2\3\30\3\3\2\2")
        buf.write("\2\31\34\5\b\5\2\32\34\5\6\4\2\33\31\3\2\2\2\33\32\3\2")
        buf.write("\2\2\34\5\3\2\2\2\35\36\7\21\2\2\36\37\7=\2\2\37 \7\r")
        buf.write("\2\2 !\7\62\2\2!\7\3\2\2\2\"#\7\b\2\2#$\7=\2\2$%\7+\2")
        buf.write("\2%&\7,\2\2&\'\7/\2\2\'(\7\60\2\2()\7\62\2\2)\t\3\2\2")
        buf.write("\2*+\t\2\2\2+\13\3\2\2\2,-\t\3\2\2-\r\3\2\2\2./\t\4\2")
        buf.write("\2/\17\3\2\2\2\60\61\t\5\2\2\61\21\3\2\2\2\4\25\33")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'=='", "'!='", "'>='", "'<='", "'>'", 
                     "'<'", "'&&'", "'||'", "'!'", "':='", "'='", "'.'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'nil'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_COMMENT", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "ADD", "SUB", "MULTIPLY", 
                      "DIVIDE", "REMAIN", "SHORT_ADD", "SHORT_SUB", "SHORT_MULTIPLY", 
                      "SHORT_DIVIDE", "SHORT_REMAIN", "COMPARE_STR", "NOT_EQ", 
                      "GREATER_OR_EQ", "LESS_OR_EQ", "GREATER", "LESS", 
                      "AND", "OR", "NOT", "DECL", "EQUAL", "DOT", "OPEN_PARANTHESIS", 
                      "CLOSE_PARANTHESIS", "OPEN_SQUARE", "CLOSE_SQUARE", 
                      "OPEN_BRACE", "CLOSE_BRACE", "COMMA", "SEMICOLON", 
                      "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", 
                      "HEXA_INT", "FLOATING_POINT_LITERAL", "STRING_LITERAL", 
                      "BOOLEAN_LITERAL", "NIL", "NEWLINE", "IDENTIFIER", 
                      "WHITESPACE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3
    RULE_multiply_operator = 4
    RULE_add_operator = 5
    RULE_related_operator = 6
    RULE_logical_operator = 7

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl", "multiply_operator", 
                   "add_operator", "related_operator", "logical_operator" ]

    EOF = Token.EOF
    SINGLE_LINE_COMMENT=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    CONST=14
    VAR=15
    CONTINUE=16
    BREAK=17
    RANGE=18
    ADD=19
    SUB=20
    MULTIPLY=21
    DIVIDE=22
    REMAIN=23
    SHORT_ADD=24
    SHORT_SUB=25
    SHORT_MULTIPLY=26
    SHORT_DIVIDE=27
    SHORT_REMAIN=28
    COMPARE_STR=29
    NOT_EQ=30
    GREATER_OR_EQ=31
    LESS_OR_EQ=32
    GREATER=33
    LESS=34
    AND=35
    OR=36
    NOT=37
    DECL=38
    EQUAL=39
    DOT=40
    OPEN_PARANTHESIS=41
    CLOSE_PARANTHESIS=42
    OPEN_SQUARE=43
    CLOSE_SQUARE=44
    OPEN_BRACE=45
    CLOSE_BRACE=46
    COMMA=47
    SEMICOLON=48
    INTEGER_LITERAL=49
    DECIMAL_INT=50
    BINARY_INT=51
    OCTAL_INT=52
    HEXA_INT=53
    FLOATING_POINT_LITERAL=54
    STRING_LITERAL=55
    BOOLEAN_LITERAL=56
    NIL=57
    NEWLINE=58
    IDENTIFIER=59
    WHITESPACE=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.decl()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.FUNC or _la==MiniGoParser.VAR):
                    break

            self.state = 21
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.funcdecl()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(MiniGoParser.VAR)
            self.state = 28
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 29
            self.match(MiniGoParser.INT)
            self.state = 30
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARANTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARANTHESIS, 0)

        def CLOSE_PARANTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARANTHESIS, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MiniGoParser.FUNC)
            self.state = 33
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 34
            self.match(MiniGoParser.OPEN_PARANTHESIS)
            self.state = 35
            self.match(MiniGoParser.CLOSE_PARANTHESIS)
            self.state = 36
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 37
            self.match(MiniGoParser.CLOSE_BRACE)
            self.state = 38
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiply_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(MiniGoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MiniGoParser.DIVIDE, 0)

        def REMAIN(self):
            return self.getToken(MiniGoParser.REMAIN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiply_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply_operator" ):
                return visitor.visitMultiply_operator(self)
            else:
                return visitor.visitChildren(self)




    def multiply_operator(self):

        localctx = MiniGoParser.Multiply_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multiply_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTIPLY) | (1 << MiniGoParser.DIVIDE) | (1 << MiniGoParser.REMAIN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_operator" ):
                return visitor.visitAdd_operator(self)
            else:
                return visitor.visitChildren(self)




    def add_operator(self):

        localctx = MiniGoParser.Add_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_add_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Related_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARE_STR(self):
            return self.getToken(MiniGoParser.COMPARE_STR, 0)

        def NOT_EQ(self):
            return self.getToken(MiniGoParser.NOT_EQ, 0)

        def GREATER_OR_EQ(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQ, 0)

        def LESS_OR_EQ(self):
            return self.getToken(MiniGoParser.LESS_OR_EQ, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_related_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelated_operator" ):
                return visitor.visitRelated_operator(self)
            else:
                return visitor.visitChildren(self)




    def related_operator(self):

        localctx = MiniGoParser.Related_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_related_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COMPARE_STR) | (1 << MiniGoParser.NOT_EQ) | (1 << MiniGoParser.GREATER_OR_EQ) | (1 << MiniGoParser.LESS_OR_EQ) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.LESS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logical_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_operator" ):
                return visitor.visitLogical_operator(self)
            else:
                return visitor.visitChildren(self)




    def logical_operator(self):

        localctx = MiniGoParser.Logical_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_logical_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.AND or _la==MiniGoParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





