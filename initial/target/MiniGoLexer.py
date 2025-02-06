# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.")
        buf.write("\u0134\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u00ff")
        buf.write("\n&\3\'\3\'\3\'\5\'\u0104\n\'\3\'\5\'\u0107\n\'\3(\6(")
        buf.write("\u010a\n(\r(\16(\u010b\3)\7)\u010f\n)\f)\16)\u0112\13")
        buf.write(")\3*\3*\5*\u0116\n*\3*\6*\u0119\n*\r*\16*\u011a\3+\3+")
        buf.write("\7+\u011f\n+\f+\16+\u0122\13+\3,\3,\3,\3,\3-\6-\u0129")
        buf.write("\n-\r-\16-\u012a\3-\3-\3.\3.\3/\3/\3\60\3\60\2\2\61\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O\2Q")
        buf.write("\2S\2U)W*Y+[,]-_.\3\2\b\3\2\62;\4\2GGgg\4\2--//\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\13\13\17\17\"\"\2\u0139\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\3a\3\2\2\2\5c\3\2\2\2")
        buf.write("\7e\3\2\2\2\tg\3\2\2\2\13i\3\2\2\2\rk\3\2\2\2\17m\3\2")
        buf.write("\2\2\21o\3\2\2\2\23q\3\2\2\2\25s\3\2\2\2\27u\3\2\2\2\31")
        buf.write("x\3\2\2\2\33{\3\2\2\2\35~\3\2\2\2\37\u0081\3\2\2\2!\u0083")
        buf.write("\3\2\2\2#\u0085\3\2\2\2%\u0088\3\2\2\2\'\u008b\3\2\2\2")
        buf.write(")\u008e\3\2\2\2+\u0093\3\2\2\2-\u0097\3\2\2\2/\u009e\3")
        buf.write("\2\2\2\61\u00a3\3\2\2\2\63\u00a8\3\2\2\2\65\u00af\3\2")
        buf.write("\2\2\67\u00b9\3\2\2\29\u00c0\3\2\2\2;\u00c4\3\2\2\2=\u00ca")
        buf.write("\3\2\2\2?\u00d2\3\2\2\2A\u00d8\3\2\2\2C\u00dc\3\2\2\2")
        buf.write("E\u00e5\3\2\2\2G\u00eb\3\2\2\2I\u00f1\3\2\2\2K\u00fe\3")
        buf.write("\2\2\2M\u0100\3\2\2\2O\u0109\3\2\2\2Q\u0110\3\2\2\2S\u0113")
        buf.write("\3\2\2\2U\u011c\3\2\2\2W\u0123\3\2\2\2Y\u0128\3\2\2\2")
        buf.write("[\u012e\3\2\2\2]\u0130\3\2\2\2_\u0132\3\2\2\2ab\7=\2\2")
        buf.write("b\4\3\2\2\2cd\7*\2\2d\6\3\2\2\2ef\7+\2\2f\b\3\2\2\2gh")
        buf.write("\7}\2\2h\n\3\2\2\2ij\7\177\2\2j\f\3\2\2\2kl\7,\2\2l\16")
        buf.write("\3\2\2\2mn\7\61\2\2n\20\3\2\2\2op\7\'\2\2p\22\3\2\2\2")
        buf.write("qr\7-\2\2r\24\3\2\2\2st\7/\2\2t\26\3\2\2\2uv\7?\2\2vw")
        buf.write("\7?\2\2w\30\3\2\2\2xy\7#\2\2yz\7?\2\2z\32\3\2\2\2{|\7")
        buf.write("@\2\2|}\7?\2\2}\34\3\2\2\2~\177\7>\2\2\177\u0080\7?\2")
        buf.write("\2\u0080\36\3\2\2\2\u0081\u0082\7@\2\2\u0082 \3\2\2\2")
        buf.write("\u0083\u0084\7>\2\2\u0084\"\3\2\2\2\u0085\u0086\7(\2\2")
        buf.write("\u0086\u0087\7(\2\2\u0087$\3\2\2\2\u0088\u0089\7~\2\2")
        buf.write("\u0089\u008a\7~\2\2\u008a&\3\2\2\2\u008b\u008c\7k\2\2")
        buf.write("\u008c\u008d\7h\2\2\u008d(\3\2\2\2\u008e\u008f\7g\2\2")
        buf.write("\u008f\u0090\7n\2\2\u0090\u0091\7u\2\2\u0091\u0092\7g")
        buf.write("\2\2\u0092*\3\2\2\2\u0093\u0094\7h\2\2\u0094\u0095\7q")
        buf.write("\2\2\u0095\u0096\7t\2\2\u0096,\3\2\2\2\u0097\u0098\7t")
        buf.write("\2\2\u0098\u0099\7g\2\2\u0099\u009a\7v\2\2\u009a\u009b")
        buf.write("\7w\2\2\u009b\u009c\7t\2\2\u009c\u009d\7p\2\2\u009d.\3")
        buf.write("\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1")
        buf.write("\7p\2\2\u00a1\u00a2\7e\2\2\u00a2\60\3\2\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7{\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\62\3\2\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7e\2\2\u00ad\u00ae\7v\2\2\u00ae\64\3\2\2\2\u00af\u00b0")
        buf.write("\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6")
        buf.write("\7c\2\2\u00b6\u00b7\7e\2\2\u00b7\u00b8\7g\2\2\u00b8\66")
        buf.write("\3\2\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7i\2\2\u00bf8\3\2\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7v\2\2\u00c3:\3\2\2\2\u00c4\u00c5")
        buf.write("\7h\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7c\2\2\u00c8\u00c9\7v\2\2\u00c9<\3\2\2\2\u00ca\u00cb")
        buf.write("\7d\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1>\3\2\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7u\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7@\3\2\2\2\u00d8\u00d9\7x\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7t\2\2\u00dbB\3\2\2\2\u00dc\u00dd")
        buf.write("\7e\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7w\2\2\u00e3\u00e4\7g\2\2\u00e4D\3\2\2\2\u00e5\u00e6")
        buf.write("\7d\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7c\2\2\u00e9\u00ea\7m\2\2\u00eaF\3\2\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7i\2\2\u00ef\u00f0\7g\2\2\u00f0H\3\2\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7n\2\2\u00f4J\3")
        buf.write("\2\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00ff\7g\2\2\u00f9\u00fa\7h\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7u\2\2\u00fd\u00ff")
        buf.write("\7g\2\2\u00fe\u00f5\3\2\2\2\u00fe\u00f9\3\2\2\2\u00ff")
        buf.write("L\3\2\2\2\u0100\u0101\5O(\2\u0101\u0103\7\60\2\2\u0102")
        buf.write("\u0104\5Q)\2\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u0106\3\2\2\2\u0105\u0107\5S*\2\u0106\u0105\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107N\3\2\2\2\u0108\u010a\t\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0109\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010cP\3\2\2\2\u010d\u010f\t\2\2")
        buf.write("\2\u010e\u010d\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111R\3\2\2\2\u0112\u0110")
        buf.write("\3\2\2\2\u0113\u0115\t\3\2\2\u0114\u0116\t\4\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0118\3\2\2\2")
        buf.write("\u0117\u0119\t\2\2\2\u0118\u0117\3\2\2\2\u0119\u011a\3")
        buf.write("\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011bT")
        buf.write("\3\2\2\2\u011c\u0120\t\5\2\2\u011d\u011f\t\6\2\2\u011e")
        buf.write("\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121V\3\2\2\2\u0122\u0120\3\2\2")
        buf.write("\2\u0123\u0124\7\f\2\2\u0124\u0125\3\2\2\2\u0125\u0126")
        buf.write("\b,\2\2\u0126X\3\2\2\2\u0127\u0129\t\7\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\b-\2\2")
        buf.write("\u012dZ\3\2\2\2\u012e\u012f\13\2\2\2\u012f\\\3\2\2\2\u0130")
        buf.write("\u0131\13\2\2\2\u0131^\3\2\2\2\u0132\u0133\13\2\2\2\u0133")
        buf.write("`\3\2\2\2\f\2\u00fe\u0103\u0106\u010b\u0110\u0115\u011a")
        buf.write("\u0120\u012a\3\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    IF = 19
    ELSE = 20
    FOR = 21
    RETURN = 22
    FUNC = 23
    TYPE = 24
    STRUCT = 25
    INTERFACE = 26
    STRING = 27
    INT = 28
    FLOAT = 29
    BOOLEAN = 30
    CONST = 31
    VAR = 32
    CONTINUE = 33
    BREAK = 34
    RANGE = 35
    NIL = 36
    BOOLEAN_LITERAL = 37
    FLOATING_POINT_LITERAL = 38
    IDENTIFIER = 39
    NL = 40
    WS = 41
    ERROR_CHAR = 42
    ILLEGAL_ESCAPE = 43
    UNCLOSE_STRING = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'", "'{'", "'}'", "'*'", "'/'", "'%'", "'+'", 
            "'-'", "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'&&'", 
            "'||'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "BOOLEAN_LITERAL", "FLOATING_POINT_LITERAL", 
            "IDENTIFIER", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "IF", "ELSE", "FOR", 
                  "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                  "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "BOOLEAN_LITERAL", "FLOATING_POINT_LITERAL", 
                  "INT_PART", "DECI_PART", "EXP_PART", "IDENTIFIER", "NL", 
                  "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


