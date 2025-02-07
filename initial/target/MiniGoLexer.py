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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u019d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\5%\u010a\n%\3&\3&\3&\7&\u010f\n&\f&\16&\u0112\13")
        buf.write("&\5&\u0114\n&\3\'\3\'\3\'\6\'\u0119\n\'\r\'\16\'\u011a")
        buf.write("\3(\3(\3(\6(\u0120\n(\r(\16(\u0121\3)\3)\3)\6)\u0127\n")
        buf.write(")\r)\16)\u0128\3*\3*\3*\5*\u012e\n*\3*\5*\u0131\n*\3+")
        buf.write("\6+\u0134\n+\r+\16+\u0135\3,\7,\u0139\n,\f,\16,\u013c")
        buf.write("\13,\3-\3-\5-\u0140\n-\3-\6-\u0143\n-\r-\16-\u0144\3.")
        buf.write("\3.\3.\3.\3.\6.\u014c\n.\r.\16.\u014d\3.\3.\3.\3.\5.\u0154")
        buf.write("\n.\3/\3/\5/\u0158\n/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0167\n\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0172\n")
        buf.write("\63\3\64\3\64\3\64\3\64\3\65\3\65\7\65\u017a\n\65\f\65")
        buf.write("\16\65\u017d\13\65\3\66\3\66\3\66\3\66\3\67\6\67\u0184")
        buf.write("\n\67\r\67\16\67\u0185\3\67\3\67\38\38\78\u018c\n8\f8")
        buf.write("\168\u018f\138\38\38\39\39\79\u0195\n9\f9\169\u0198\13")
        buf.write("9\39\39\3:\3:\2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U\2W\2Y\2[,]\2_\2a\2c\2e-g.i/")
        buf.write("k\60m\61o\62q\63s\64\3\2\23\3\2\63;\3\2\62;\4\2DDdd\3")
        buf.write("\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4")
        buf.write("\2--//\4\2$$^^\3\2$$\5\2ppttvv\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\13\17\17\"\"\6\2^^ppttvv\2\u01ad\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2[\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5w")
        buf.write("\3\2\2\2\7y\3\2\2\2\t{\3\2\2\2\13}\3\2\2\2\r\177\3\2\2")
        buf.write("\2\17\u0081\3\2\2\2\21\u0083\3\2\2\2\23\u0085\3\2\2\2")
        buf.write("\25\u0087\3\2\2\2\27\u0089\3\2\2\2\31\u008c\3\2\2\2\33")
        buf.write("\u008f\3\2\2\2\35\u0092\3\2\2\2\37\u0095\3\2\2\2!\u0097")
        buf.write("\3\2\2\2#\u0099\3\2\2\2%\u009c\3\2\2\2\'\u009f\3\2\2\2")
        buf.write(")\u00a2\3\2\2\2+\u00a7\3\2\2\2-\u00ab\3\2\2\2/\u00b2\3")
        buf.write("\2\2\2\61\u00b7\3\2\2\2\63\u00bc\3\2\2\2\65\u00c3\3\2")
        buf.write("\2\2\67\u00cd\3\2\2\29\u00d4\3\2\2\2;\u00d8\3\2\2\2=\u00de")
        buf.write("\3\2\2\2?\u00e6\3\2\2\2A\u00ec\3\2\2\2C\u00f0\3\2\2\2")
        buf.write("E\u00f9\3\2\2\2G\u00ff\3\2\2\2I\u0109\3\2\2\2K\u0113\3")
        buf.write("\2\2\2M\u0115\3\2\2\2O\u011c\3\2\2\2Q\u0123\3\2\2\2S\u012a")
        buf.write("\3\2\2\2U\u0133\3\2\2\2W\u013a\3\2\2\2Y\u013d\3\2\2\2")
        buf.write("[\u0153\3\2\2\2]\u0157\3\2\2\2_\u0159\3\2\2\2a\u015b\3")
        buf.write("\2\2\2c\u0166\3\2\2\2e\u0171\3\2\2\2g\u0173\3\2\2\2i\u0177")
        buf.write("\3\2\2\2k\u017e\3\2\2\2m\u0183\3\2\2\2o\u0189\3\2\2\2")
        buf.write("q\u0192\3\2\2\2s\u019b\3\2\2\2uv\7=\2\2v\4\3\2\2\2wx\7")
        buf.write("*\2\2x\6\3\2\2\2yz\7+\2\2z\b\3\2\2\2{|\7}\2\2|\n\3\2\2")
        buf.write("\2}~\7\177\2\2~\f\3\2\2\2\177\u0080\7,\2\2\u0080\16\3")
        buf.write("\2\2\2\u0081\u0082\7\61\2\2\u0082\20\3\2\2\2\u0083\u0084")
        buf.write("\7\'\2\2\u0084\22\3\2\2\2\u0085\u0086\7-\2\2\u0086\24")
        buf.write("\3\2\2\2\u0087\u0088\7/\2\2\u0088\26\3\2\2\2\u0089\u008a")
        buf.write("\7?\2\2\u008a\u008b\7?\2\2\u008b\30\3\2\2\2\u008c\u008d")
        buf.write("\7#\2\2\u008d\u008e\7?\2\2\u008e\32\3\2\2\2\u008f\u0090")
        buf.write("\7@\2\2\u0090\u0091\7?\2\2\u0091\34\3\2\2\2\u0092\u0093")
        buf.write("\7>\2\2\u0093\u0094\7?\2\2\u0094\36\3\2\2\2\u0095\u0096")
        buf.write("\7@\2\2\u0096 \3\2\2\2\u0097\u0098\7>\2\2\u0098\"\3\2")
        buf.write("\2\2\u0099\u009a\7(\2\2\u009a\u009b\7(\2\2\u009b$\3\2")
        buf.write("\2\2\u009c\u009d\7~\2\2\u009d\u009e\7~\2\2\u009e&\3\2")
        buf.write("\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7h\2\2\u00a1(\3\2")
        buf.write("\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5")
        buf.write("\7u\2\2\u00a5\u00a6\7g\2\2\u00a6*\3\2\2\2\u00a7\u00a8")
        buf.write("\7h\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7t\2\2\u00aa,\3")
        buf.write("\2\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae")
        buf.write("\7v\2\2\u00ae\u00af\7w\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1.\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4")
        buf.write("\7w\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7e\2\2\u00b6\60")
        buf.write("\3\2\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7{\2\2\u00b9\u00ba")
        buf.write("\7r\2\2\u00ba\u00bb\7g\2\2\u00bb\62\3\2\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7w\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7v\2\2\u00c2\64")
        buf.write("\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7e\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\66\3\2\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7i\2\2\u00d38\3\2\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7:\3")
        buf.write("\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da\7n\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7v\2\2\u00dd<\3")
        buf.write("\2\2\2\u00de\u00df\7d\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7p\2\2\u00e5>\3\2\2\2\u00e6\u00e7")
        buf.write("\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7u\2\2\u00ea\u00eb\7v\2\2\u00eb@\3\2\2\2\u00ec\u00ed")
        buf.write("\7x\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7t\2\2\u00efB\3")
        buf.write("\2\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8\7g\2\2\u00f8D\3")
        buf.write("\2\2\2\u00f9\u00fa\7d\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7m\2\2\u00feF\3")
        buf.write("\2\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7c\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7i\2\2\u0103\u0104\7g\2\2\u0104H\3")
        buf.write("\2\2\2\u0105\u010a\5K&\2\u0106\u010a\5M\'\2\u0107\u010a")
        buf.write("\5O(\2\u0108\u010a\5Q)\2\u0109\u0105\3\2\2\2\u0109\u0106")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a")
        buf.write("J\3\2\2\2\u010b\u0114\7\62\2\2\u010c\u0110\t\2\2\2\u010d")
        buf.write("\u010f\t\3\2\2\u010e\u010d\3\2\2\2\u010f\u0112\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0114\3")
        buf.write("\2\2\2\u0112\u0110\3\2\2\2\u0113\u010b\3\2\2\2\u0113\u010c")
        buf.write("\3\2\2\2\u0114L\3\2\2\2\u0115\u0116\7\62\2\2\u0116\u0118")
        buf.write("\t\4\2\2\u0117\u0119\t\5\2\2\u0118\u0117\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2")
        buf.write("\u011bN\3\2\2\2\u011c\u011d\7\62\2\2\u011d\u011f\t\6\2")
        buf.write("\2\u011e\u0120\t\7\2\2\u011f\u011e\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122")
        buf.write("P\3\2\2\2\u0123\u0124\7\62\2\2\u0124\u0126\t\b\2\2\u0125")
        buf.write("\u0127\t\t\2\2\u0126\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129R\3\2\2")
        buf.write("\2\u012a\u012b\5U+\2\u012b\u012d\7\60\2\2\u012c\u012e")
        buf.write("\5W,\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130")
        buf.write("\3\2\2\2\u012f\u0131\5Y-\2\u0130\u012f\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131T\3\2\2\2\u0132\u0134\t\3\2\2\u0133\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136V\3\2\2\2\u0137\u0139\t\3\2\2\u0138")
        buf.write("\u0137\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013bX\3\2\2\2\u013c\u013a\3\2\2")
        buf.write("\2\u013d\u013f\t\n\2\2\u013e\u0140\t\13\2\2\u013f\u013e")
        buf.write("\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0142\3\2\2\2\u0141")
        buf.write("\u0143\t\3\2\2\u0142\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145Z\3\2\2")
        buf.write("\2\u0146\u0147\5_\60\2\u0147\u0148\5_\60\2\u0148\u0154")
        buf.write("\3\2\2\2\u0149\u014b\5_\60\2\u014a\u014c\5]/\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\5_\60\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0152\b.\2\2\u0152\u0154\3")
        buf.write("\2\2\2\u0153\u0146\3\2\2\2\u0153\u0149\3\2\2\2\u0154\\")
        buf.write("\3\2\2\2\u0155\u0158\5c\62\2\u0156\u0158\n\f\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158^\3\2\2\2\u0159")
        buf.write("\u015a\t\r\2\2\u015a`\3\2\2\2\u015b\u015c\7^\2\2\u015c")
        buf.write("b\3\2\2\2\u015d\u015e\5a\61\2\u015e\u015f\t\16\2\2\u015f")
        buf.write("\u0167\3\2\2\2\u0160\u0161\5a\61\2\u0161\u0162\t\r\2\2")
        buf.write("\u0162\u0167\3\2\2\2\u0163\u0164\5a\61\2\u0164\u0165\5")
        buf.write("a\61\2\u0165\u0167\3\2\2\2\u0166\u015d\3\2\2\2\u0166\u0160")
        buf.write("\3\2\2\2\u0166\u0163\3\2\2\2\u0167d\3\2\2\2\u0168\u0169")
        buf.write("\7v\2\2\u0169\u016a\7t\2\2\u016a\u016b\7w\2\2\u016b\u0172")
        buf.write("\7g\2\2\u016c\u016d\7h\2\2\u016d\u016e\7c\2\2\u016e\u016f")
        buf.write("\7n\2\2\u016f\u0170\7u\2\2\u0170\u0172\7g\2\2\u0171\u0168")
        buf.write("\3\2\2\2\u0171\u016c\3\2\2\2\u0172f\3\2\2\2\u0173\u0174")
        buf.write("\7p\2\2\u0174\u0175\7k\2\2\u0175\u0176\7n\2\2\u0176h\3")
        buf.write("\2\2\2\u0177\u017b\t\17\2\2\u0178\u017a\t\20\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017cj\3\2\2\2\u017d\u017b\3\2\2")
        buf.write("\2\u017e\u017f\7\f\2\2\u017f\u0180\3\2\2\2\u0180\u0181")
        buf.write("\b\66\3\2\u0181l\3\2\2\2\u0182\u0184\t\21\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\b\67\3")
        buf.write("\2\u0188n\3\2\2\2\u0189\u018d\5_\60\2\u018a\u018c\5]/")
        buf.write("\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u0190\u0191\n\22\2\2\u0191p\3\2\2\2\u0192")
        buf.write("\u0196\5_\60\2\u0193\u0195\5]/\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7")
        buf.write("\2\2\3\u019ar\3\2\2\2\u019b\u019c\13\2\2\2\u019ct\3\2")
        buf.write("\2\2\30\2\u0109\u0110\u0113\u011a\u0121\u0128\u012d\u0130")
        buf.write("\u0135\u013a\u013f\u0144\u014d\u0153\u0157\u0166\u0171")
        buf.write("\u017b\u0185\u018d\u0196\4\3.\2\b\2\2")
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
    INTEGER_LITERAL = 36
    DECIMAL_INT = 37
    BINARY_INT = 38
    OCTAL_INT = 39
    HEXA_INT = 40
    FLOATING_POINT_LITERAL = 41
    STRING_LITERAL = 42
    BOOLEAN_LITERAL = 43
    NIL = 44
    IDENTIFIER = 45
    NL = 46
    WS = 47
    ILLEGAL_ESCAPE = 48
    UNCLOSE_STRING = 49
    ERROR_CHAR = 50

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
            "BREAK", "RANGE", "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", 
            "OCTAL_INT", "HEXA_INT", "FLOATING_POINT_LITERAL", "STRING_LITERAL", 
            "BOOLEAN_LITERAL", "NIL", "IDENTIFIER", "NL", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "IF", "ELSE", "FOR", 
                  "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                  "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", 
                  "OCTAL_INT", "HEXA_INT", "FLOATING_POINT_LITERAL", "INT_PART", 
                  "DECI_PART", "EXP_PART", "STRING_LITERAL", "INSIDE_STRING", 
                  "DOUBLE_QUOTE", "BACKLASH", "ESCAPE_SEQUENCE", "BOOLEAN_LITERAL", 
                  "NIL", "IDENTIFIER", "NL", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ERROR_CHAR" ]

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
            raise UnclosedString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscapeInString(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[44] = self.STRING_LITERAL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     


