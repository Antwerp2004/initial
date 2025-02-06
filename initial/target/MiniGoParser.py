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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3")
        buf.write("\3\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\2\2")
        buf.write("\n\2\4\6\b\n\f\16\20\2\6\3\2\b\n\3\2\13\f\3\2\r\22\3\2")
        buf.write("\23\24\2,\2\23\3\2\2\2\4\33\3\2\2\2\6\35\3\2\2\2\b\"\3")
        buf.write("\2\2\2\n*\3\2\2\2\f,\3\2\2\2\16.\3\2\2\2\20\60\3\2\2\2")
        buf.write("\22\24\5\4\3\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2")
        buf.write("\2\25\26\3\2\2\2\26\27\3\2\2\2\27\30\7\2\2\3\30\3\3\2")
        buf.write("\2\2\31\34\5\b\5\2\32\34\5\6\4\2\33\31\3\2\2\2\33\32\3")
        buf.write("\2\2\2\34\5\3\2\2\2\35\36\7\"\2\2\36\37\7)\2\2\37 \7\36")
        buf.write("\2\2 !\7\3\2\2!\7\3\2\2\2\"#\7\31\2\2#$\7)\2\2$%\7\4\2")
        buf.write("\2%&\7\5\2\2&\'\7\6\2\2\'(\7\7\2\2()\7\3\2\2)\t\3\2\2")
        buf.write("\2*+\t\2\2\2+\13\3\2\2\2,-\t\3\2\2-\r\3\2\2\2./\t\4\2")
        buf.write("\2/\17\3\2\2\2\60\61\t\5\2\2\61\21\3\2\2\2\4\25\33")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'{'", "'}'", "'*'", 
                     "'/'", "'%'", "'+'", "'-'", "'=='", "'!='", "'>='", 
                     "'<='", "'>'", "'<'", "'&&'", "'||'", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'nil'", "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "NIL", "BOOLEAN_LITERAL", 
                      "FLOATING_POINT_LITERAL", "IDENTIFIER", "NL", "WS", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    IF=19
    ELSE=20
    FOR=21
    RETURN=22
    FUNC=23
    TYPE=24
    STRUCT=25
    INTERFACE=26
    STRING=27
    INT=28
    FLOAT=29
    BOOLEAN=30
    CONST=31
    VAR=32
    CONTINUE=33
    BREAK=34
    RANGE=35
    NIL=36
    BOOLEAN_LITERAL=37
    FLOATING_POINT_LITERAL=38
    IDENTIFIER=39
    NL=40
    WS=41
    ERROR_CHAR=42
    ILLEGAL_ESCAPE=43
    UNCLOSE_STRING=44

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
            self.match(MiniGoParser.T__0)
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
            self.match(MiniGoParser.T__1)
            self.state = 35
            self.match(MiniGoParser.T__2)
            self.state = 36
            self.match(MiniGoParser.T__3)
            self.state = 37
            self.match(MiniGoParser.T__4)
            self.state = 38
            self.match(MiniGoParser.T__0)
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__5) | (1 << MiniGoParser.T__6) | (1 << MiniGoParser.T__7))) != 0)):
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
            if not(_la==MiniGoParser.T__8 or _la==MiniGoParser.T__9):
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__12) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15))) != 0)):
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
            if not(_la==MiniGoParser.T__16 or _la==MiniGoParser.T__17):
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





