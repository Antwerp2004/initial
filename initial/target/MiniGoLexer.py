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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01fb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\7\2\u0098\n\2\f\2\16\2\u009b\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\7\3\u00a4\n\3\f\3\16\3\u00a7\13\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\5\64\u0162\n\64\3\65\3\65\3")
        buf.write("\65\7\65\u0167\n\65\f\65\16\65\u016a\13\65\5\65\u016c")
        buf.write("\n\65\3\66\3\66\3\66\6\66\u0171\n\66\r\66\16\66\u0172")
        buf.write("\3\67\3\67\3\67\6\67\u0178\n\67\r\67\16\67\u0179\38\3")
        buf.write("8\38\68\u017f\n8\r8\168\u0180\39\39\39\59\u0186\n9\39")
        buf.write("\59\u0189\n9\3:\6:\u018c\n:\r:\16:\u018d\3;\7;\u0191\n")
        buf.write(";\f;\16;\u0194\13;\3<\3<\5<\u0198\n<\3<\6<\u019b\n<\r")
        buf.write("<\16<\u019c\3=\3=\3=\3=\3=\6=\u01a4\n=\r=\16=\u01a5\3")
        buf.write("=\3=\5=\u01aa\n=\3=\3=\3>\3>\5>\u01b0\n>\3?\3?\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u01bf\nA\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\5B\u01ca\nB\3C\3C\3C\3C\3D\3D\3D\5D\u01d3\n")
        buf.write("D\3D\3D\3E\3E\3E\3E\3F\3F\7F\u01dd\nF\fF\16F\u01e0\13")
        buf.write("F\3G\3G\7G\u01e4\nG\fG\16G\u01e7\13G\3G\3G\3G\3G\3H\3")
        buf.write("H\7H\u01ef\nH\fH\16H\u01f2\13H\3H\5H\u01f5\nH\3H\3H\3")
        buf.write("I\3I\3I\3\u00a5\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q:s\2u\2w\2y;{\2}\2\177\2\u0081\2\u0083")
        buf.write("<\u0085=\u0087>\u0089?\u008b@\u008dA\u008fB\u0091C\3\2")
        buf.write("\25\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4")
        buf.write("\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\6\2")
        buf.write("\f\f\17\17$$^^\3\2$$\5\2ppttvv\5\2\13\13\16\17\"\"\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\6\2^^ppttvv\4\3\f\f\17\17\2\u020e")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2y\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2")
        buf.write("\2\5\u009e\3\2\2\2\7\u00ad\3\2\2\2\t\u00b0\3\2\2\2\13")
        buf.write("\u00b5\3\2\2\2\r\u00b9\3\2\2\2\17\u00c0\3\2\2\2\21\u00c5")
        buf.write("\3\2\2\2\23\u00ca\3\2\2\2\25\u00d1\3\2\2\2\27\u00db\3")
        buf.write("\2\2\2\31\u00e2\3\2\2\2\33\u00e6\3\2\2\2\35\u00ec\3\2")
        buf.write("\2\2\37\u00f4\3\2\2\2!\u00fa\3\2\2\2#\u00fe\3\2\2\2%\u0107")
        buf.write("\3\2\2\2\'\u010d\3\2\2\2)\u0113\3\2\2\2+\u0115\3\2\2\2")
        buf.write("-\u0117\3\2\2\2/\u0119\3\2\2\2\61\u011b\3\2\2\2\63\u011d")
        buf.write("\3\2\2\2\65\u0120\3\2\2\2\67\u0123\3\2\2\29\u0126\3\2")
        buf.write("\2\2;\u0129\3\2\2\2=\u012b\3\2\2\2?\u012d\3\2\2\2A\u0130")
        buf.write("\3\2\2\2C\u0133\3\2\2\2E\u0135\3\2\2\2G\u0138\3\2\2\2")
        buf.write("I\u013b\3\2\2\2K\u013e\3\2\2\2M\u0141\3\2\2\2O\u0144\3")
        buf.write("\2\2\2Q\u0147\3\2\2\2S\u0149\3\2\2\2U\u014b\3\2\2\2W\u014d")
        buf.write("\3\2\2\2Y\u014f\3\2\2\2[\u0151\3\2\2\2]\u0153\3\2\2\2")
        buf.write("_\u0155\3\2\2\2a\u0157\3\2\2\2c\u0159\3\2\2\2e\u015b\3")
        buf.write("\2\2\2g\u0161\3\2\2\2i\u016b\3\2\2\2k\u016d\3\2\2\2m\u0174")
        buf.write("\3\2\2\2o\u017b\3\2\2\2q\u0182\3\2\2\2s\u018b\3\2\2\2")
        buf.write("u\u0192\3\2\2\2w\u0195\3\2\2\2y\u01a9\3\2\2\2{\u01af\3")
        buf.write("\2\2\2}\u01b1\3\2\2\2\177\u01b3\3\2\2\2\u0081\u01be\3")
        buf.write("\2\2\2\u0083\u01c9\3\2\2\2\u0085\u01cb\3\2\2\2\u0087\u01d2")
        buf.write("\3\2\2\2\u0089\u01d6\3\2\2\2\u008b\u01da\3\2\2\2\u008d")
        buf.write("\u01e1\3\2\2\2\u008f\u01ec\3\2\2\2\u0091\u01f8\3\2\2\2")
        buf.write("\u0093\u0094\7\61\2\2\u0094\u0095\7\61\2\2\u0095\u0099")
        buf.write("\3\2\2\2\u0096\u0098\n\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\b")
        buf.write("\2\2\2\u009d\4\3\2\2\2\u009e\u009f\7\61\2\2\u009f\u00a0")
        buf.write("\7,\2\2\u00a0\u00a5\3\2\2\2\u00a1\u00a4\5\5\3\2\u00a2")
        buf.write("\u00a4\13\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2")
        buf.write("\2\u00a4\u00a7\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8")
        buf.write("\u00a9\7,\2\2\u00a9\u00aa\7\61\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\b\3\2\2\u00ac\6\3\2\2\2\u00ad\u00ae\7k\2")
        buf.write("\2\u00ae\u00af\7h\2\2\u00af\b\3\2\2\2\u00b0\u00b1\7g\2")
        buf.write("\2\u00b1\u00b2\7n\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4\7")
        buf.write("g\2\2\u00b4\n\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7")
        buf.write("q\2\2\u00b7\u00b8\7t\2\2\u00b8\f\3\2\2\2\u00b9\u00ba\7")
        buf.write("t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd")
        buf.write("\7w\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7p\2\2\u00bf\16")
        buf.write("\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7e\2\2\u00c4\20\3\2\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7{\2\2\u00c7\u00c8\7r\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\22\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7e\2\2\u00cf\u00d0\7v\2\2\u00d0\24\3\2\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7g\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8")
        buf.write("\7c\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7g\2\2\u00da\26")
        buf.write("\3\2\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7i\2\2\u00e1\30\3\2\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\u00e5\7v\2\2\u00e5\32\3\2\2\2\u00e6\u00e7")
        buf.write("\7h\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7c\2\2\u00ea\u00eb\7v\2\2\u00eb\34\3\2\2\2\u00ec\u00ed")
        buf.write("\7d\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\36\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6")
        buf.write("\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9 \3\2\2\2\u00fa\u00fb\7x\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7t\2\2\u00fd\"\3\2\2\2\u00fe\u00ff")
        buf.write("\7e\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7k\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7w\2\2\u0105\u0106\7g\2\2\u0106$\3\2\2\2\u0107\u0108")
        buf.write("\7d\2\2\u0108\u0109\7t\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7m\2\2\u010c&\3\2\2\2\u010d\u010e")
        buf.write("\7t\2\2\u010e\u010f\7c\2\2\u010f\u0110\7p\2\2\u0110\u0111")
        buf.write("\7i\2\2\u0111\u0112\7g\2\2\u0112(\3\2\2\2\u0113\u0114")
        buf.write("\7-\2\2\u0114*\3\2\2\2\u0115\u0116\7/\2\2\u0116,\3\2\2")
        buf.write("\2\u0117\u0118\7,\2\2\u0118.\3\2\2\2\u0119\u011a\7\61")
        buf.write("\2\2\u011a\60\3\2\2\2\u011b\u011c\7\'\2\2\u011c\62\3\2")
        buf.write("\2\2\u011d\u011e\7?\2\2\u011e\u011f\7?\2\2\u011f\64\3")
        buf.write("\2\2\2\u0120\u0121\7#\2\2\u0121\u0122\7?\2\2\u0122\66")
        buf.write("\3\2\2\2\u0123\u0124\7@\2\2\u0124\u0125\7?\2\2\u01258")
        buf.write("\3\2\2\2\u0126\u0127\7>\2\2\u0127\u0128\7?\2\2\u0128:")
        buf.write("\3\2\2\2\u0129\u012a\7@\2\2\u012a<\3\2\2\2\u012b\u012c")
        buf.write("\7>\2\2\u012c>\3\2\2\2\u012d\u012e\7(\2\2\u012e\u012f")
        buf.write("\7(\2\2\u012f@\3\2\2\2\u0130\u0131\7~\2\2\u0131\u0132")
        buf.write("\7~\2\2\u0132B\3\2\2\2\u0133\u0134\7#\2\2\u0134D\3\2\2")
        buf.write("\2\u0135\u0136\7<\2\2\u0136\u0137\7?\2\2\u0137F\3\2\2")
        buf.write("\2\u0138\u0139\7-\2\2\u0139\u013a\7?\2\2\u013aH\3\2\2")
        buf.write("\2\u013b\u013c\7/\2\2\u013c\u013d\7?\2\2\u013dJ\3\2\2")
        buf.write("\2\u013e\u013f\7,\2\2\u013f\u0140\7?\2\2\u0140L\3\2\2")
        buf.write("\2\u0141\u0142\7\61\2\2\u0142\u0143\7?\2\2\u0143N\3\2")
        buf.write("\2\2\u0144\u0145\7\'\2\2\u0145\u0146\7?\2\2\u0146P\3\2")
        buf.write("\2\2\u0147\u0148\7?\2\2\u0148R\3\2\2\2\u0149\u014a\7\60")
        buf.write("\2\2\u014aT\3\2\2\2\u014b\u014c\7*\2\2\u014cV\3\2\2\2")
        buf.write("\u014d\u014e\7+\2\2\u014eX\3\2\2\2\u014f\u0150\7]\2\2")
        buf.write("\u0150Z\3\2\2\2\u0151\u0152\7_\2\2\u0152\\\3\2\2\2\u0153")
        buf.write("\u0154\7}\2\2\u0154^\3\2\2\2\u0155\u0156\7\177\2\2\u0156")
        buf.write("`\3\2\2\2\u0157\u0158\7.\2\2\u0158b\3\2\2\2\u0159\u015a")
        buf.write("\7=\2\2\u015ad\3\2\2\2\u015b\u015c\7<\2\2\u015cf\3\2\2")
        buf.write("\2\u015d\u0162\5i\65\2\u015e\u0162\5k\66\2\u015f\u0162")
        buf.write("\5m\67\2\u0160\u0162\5o8\2\u0161\u015d\3\2\2\2\u0161\u015e")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("h\3\2\2\2\u0163\u016c\7\62\2\2\u0164\u0168\t\3\2\2\u0165")
        buf.write("\u0167\t\4\2\2\u0166\u0165\3\2\2\2\u0167\u016a\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016c\3")
        buf.write("\2\2\2\u016a\u0168\3\2\2\2\u016b\u0163\3\2\2\2\u016b\u0164")
        buf.write("\3\2\2\2\u016cj\3\2\2\2\u016d\u016e\7\62\2\2\u016e\u0170")
        buf.write("\t\5\2\2\u016f\u0171\t\6\2\2\u0170\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173l\3\2\2\2\u0174\u0175\7\62\2\2\u0175\u0177\t\7\2")
        buf.write("\2\u0176\u0178\t\b\2\2\u0177\u0176\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("n\3\2\2\2\u017b\u017c\7\62\2\2\u017c\u017e\t\t\2\2\u017d")
        buf.write("\u017f\t\n\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181p\3\2\2")
        buf.write("\2\u0182\u0183\5s:\2\u0183\u0185\7\60\2\2\u0184\u0186")
        buf.write("\5u;\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188")
        buf.write("\3\2\2\2\u0187\u0189\5w<\2\u0188\u0187\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189r\3\2\2\2\u018a\u018c\t\4\2\2\u018b\u018a")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018et\3\2\2\2\u018f\u0191\t\4\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193v\3\2\2\2\u0194\u0192\3\2\2")
        buf.write("\2\u0195\u0197\t\13\2\2\u0196\u0198\t\f\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019a\3\2\2\2\u0199")
        buf.write("\u019b\t\4\2\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019dx\3\2\2")
        buf.write("\2\u019e\u019f\5}?\2\u019f\u01a0\5}?\2\u01a0\u01aa\3\2")
        buf.write("\2\2\u01a1\u01a3\5}?\2\u01a2\u01a4\5{>\2\u01a3\u01a2\3")
        buf.write("\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\5}?\2\u01a8\u01aa")
        buf.write("\3\2\2\2\u01a9\u019e\3\2\2\2\u01a9\u01a1\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ac\b=\3\2\u01acz\3\2\2\2\u01ad")
        buf.write("\u01b0\5\u0081A\2\u01ae\u01b0\n\r\2\2\u01af\u01ad\3\2")
        buf.write("\2\2\u01af\u01ae\3\2\2\2\u01b0|\3\2\2\2\u01b1\u01b2\t")
        buf.write("\16\2\2\u01b2~\3\2\2\2\u01b3\u01b4\7^\2\2\u01b4\u0080")
        buf.write("\3\2\2\2\u01b5\u01b6\5\177@\2\u01b6\u01b7\t\17\2\2\u01b7")
        buf.write("\u01bf\3\2\2\2\u01b8\u01b9\5\177@\2\u01b9\u01ba\5}?\2")
        buf.write("\u01ba\u01bf\3\2\2\2\u01bb\u01bc\5\177@\2\u01bc\u01bd")
        buf.write("\5\177@\2\u01bd\u01bf\3\2\2\2\u01be\u01b5\3\2\2\2\u01be")
        buf.write("\u01b8\3\2\2\2\u01be\u01bb\3\2\2\2\u01bf\u0082\3\2\2\2")
        buf.write("\u01c0\u01c1\7v\2\2\u01c1\u01c2\7t\2\2\u01c2\u01c3\7w")
        buf.write("\2\2\u01c3\u01ca\7g\2\2\u01c4\u01c5\7h\2\2\u01c5\u01c6")
        buf.write("\7c\2\2\u01c6\u01c7\7n\2\2\u01c7\u01c8\7u\2\2\u01c8\u01ca")
        buf.write("\7g\2\2\u01c9\u01c0\3\2\2\2\u01c9\u01c4\3\2\2\2\u01ca")
        buf.write("\u0084\3\2\2\2\u01cb\u01cc\7p\2\2\u01cc\u01cd\7k\2\2\u01cd")
        buf.write("\u01ce\7n\2\2\u01ce\u0086\3\2\2\2\u01cf\u01d0\7\17\2\2")
        buf.write("\u01d0\u01d3\7\f\2\2\u01d1\u01d3\7\f\2\2\u01d2\u01cf\3")
        buf.write("\2\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5")
        buf.write("\bD\4\2\u01d5\u0088\3\2\2\2\u01d6\u01d7\t\20\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01d9\bE\2\2\u01d9\u008a\3\2\2\2")
        buf.write("\u01da\u01de\t\21\2\2\u01db\u01dd\t\22\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u008c\3\2\2\2\u01e0\u01de\3\2\2\2")
        buf.write("\u01e1\u01e5\5}?\2\u01e2\u01e4\5{>\2\u01e3\u01e2\3\2\2")
        buf.write("\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8")
        buf.write("\u01e9\5\177@\2\u01e9\u01ea\n\23\2\2\u01ea\u01eb\bG\5")
        buf.write("\2\u01eb\u008e\3\2\2\2\u01ec\u01f0\5}?\2\u01ed\u01ef\5")
        buf.write("{>\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f3\u01f5\t\24\2\2\u01f4\u01f3\3\2\2")
        buf.write("\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\bH\6\2\u01f7\u0090")
        buf.write("\3\2\2\2\u01f8\u01f9\13\2\2\2\u01f9\u01fa\bI\7\2\u01fa")
        buf.write("\u0092\3\2\2\2\34\2\u0099\u00a3\u00a5\u0161\u0168\u016b")
        buf.write("\u0172\u0179\u0180\u0185\u0188\u018d\u0192\u0197\u019c")
        buf.write("\u01a5\u01a9\u01af\u01be\u01c9\u01d2\u01de\u01e5\u01f0")
        buf.write("\u01f4\b\b\2\2\3=\2\3D\3\3G\4\3H\5\3I\6")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_LINE_COMMENT = 1
    MULTI_LINE_COMMENT = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    ADD = 20
    SUB = 21
    MULTIPLY = 22
    DIVIDE = 23
    REMAIN = 24
    COMPARE_STR = 25
    NOT_EQ = 26
    GREATER_OR_EQ = 27
    LESS_OR_EQ = 28
    GREATER = 29
    LESS = 30
    AND = 31
    OR = 32
    NOT = 33
    ASSIGNMENT_SIGN = 34
    SHORT_ADD = 35
    SHORT_SUB = 36
    SHORT_MULTIPLY = 37
    SHORT_DIVIDE = 38
    SHORT_REMAIN = 39
    EQUAL = 40
    DOT = 41
    OPEN_PARENTHESIS = 42
    CLOSE_PARENTHESIS = 43
    OPEN_BRACKET = 44
    CLOSE_BRACKET = 45
    OPEN_BRACE = 46
    CLOSE_BRACE = 47
    COMMA = 48
    SEMICOLON = 49
    COLON = 50
    INTEGER_LITERAL = 51
    DECIMAL_INT = 52
    BINARY_INT = 53
    OCTAL_INT = 54
    HEXA_INT = 55
    FLOAT_LITERAL = 56
    STRING_LITERAL = 57
    BOOLEAN_LITERAL = 58
    NIL_LITERAL = 59
    NEWLINE = 60
    WHITESPACE = 61
    IDENTIFIER = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>='", "'<='", 
            "'>'", "'<'", "'&&'", "'||'", "'!'", "':='", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'='", "'.'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'", "':'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "IF", "ELSE", "FOR", 
            "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
            "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
            "ADD", "SUB", "MULTIPLY", "DIVIDE", "REMAIN", "COMPARE_STR", 
            "NOT_EQ", "GREATER_OR_EQ", "LESS_OR_EQ", "GREATER", "LESS", 
            "AND", "OR", "NOT", "ASSIGNMENT_SIGN", "SHORT_ADD", "SHORT_SUB", 
            "SHORT_MULTIPLY", "SHORT_DIVIDE", "SHORT_REMAIN", "EQUAL", "DOT", 
            "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
            "OPEN_BRACE", "CLOSE_BRACE", "COMMA", "SEMICOLON", "COLON", 
            "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", 
            "HEXA_INT", "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "NIL_LITERAL", "NEWLINE", "WHITESPACE", "IDENTIFIER", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "IF", "ELSE", 
                  "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                  "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "ADD", "SUB", "MULTIPLY", "DIVIDE", 
                  "REMAIN", "COMPARE_STR", "NOT_EQ", "GREATER_OR_EQ", "LESS_OR_EQ", 
                  "GREATER", "LESS", "AND", "OR", "NOT", "ASSIGNMENT_SIGN", 
                  "SHORT_ADD", "SHORT_SUB", "SHORT_MULTIPLY", "SHORT_DIVIDE", 
                  "SHORT_REMAIN", "EQUAL", "DOT", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                  "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                  "COMMA", "SEMICOLON", "COLON", "INTEGER_LITERAL", "DECIMAL_INT", 
                  "BINARY_INT", "OCTAL_INT", "HEXA_INT", "FLOAT_LITERAL", 
                  "INT_PART", "DECI_PART", "EXP_PART", "STRING_LITERAL", 
                  "INSIDE_STRING", "DOUBLE_QUOTE", "BACKLASH", "ESCAPE_SEQUENCE", 
                  "BOOLEAN_LITERAL", "NIL_LITERAL", "NEWLINE", "WHITESPACE", 
                  "IDENTIFIER", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input:InputStream):
        super().__init__(input)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        result = super().emit()
        self.preType = tk
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.STRING_LITERAL_action 
            actions[66] = self.NEWLINE_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                        if self.preType in {self.IDENTIFIER, self.INTEGER_LITERAL,
                        self.FLOAT_LITERAL, self.BOOLEAN_LITERAL, self.STRING_LITERAL,
                        self.INT, self.FLOAT, self.BOOLEAN, self.STRING,
                        self.RETURN, self.CONTINUE, self.BREAK, self.NIL_LITERAL,
                        self.CLOSE_PARENTHESIS, self.CLOSE_BRACKET, self.CLOSE_BRACE}:
                            self.text = ";"
                            self.type = self.SEMICOLON
                        else:
                            self.skip()
                     
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


