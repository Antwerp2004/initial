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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01e2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\7\2\u0094\n")
        buf.write("\2\f\2\16\2\u0097\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\62\3\62\5\62\u014d\n\62\3")
        buf.write("\63\3\63\3\63\7\63\u0152\n\63\f\63\16\63\u0155\13\63\5")
        buf.write("\63\u0157\n\63\3\64\3\64\3\64\6\64\u015c\n\64\r\64\16")
        buf.write("\64\u015d\3\65\3\65\3\65\6\65\u0163\n\65\r\65\16\65\u0164")
        buf.write("\3\66\3\66\3\66\6\66\u016a\n\66\r\66\16\66\u016b\3\67")
        buf.write("\3\67\3\67\5\67\u0171\n\67\3\67\5\67\u0174\n\67\38\68")
        buf.write("\u0177\n8\r8\168\u0178\39\79\u017c\n9\f9\169\u017f\13")
        buf.write("9\3:\3:\5:\u0183\n:\3:\6:\u0186\n:\r:\16:\u0187\3;\3;")
        buf.write("\3;\3;\3;\6;\u018f\n;\r;\16;\u0190\3;\3;\5;\u0195\n;\3")
        buf.write(";\3;\3<\3<\5<\u019b\n<\3=\3=\3>\3>\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\5?\u01aa\n?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u01b5")
        buf.write("\n@\3A\3A\3A\3A\3B\3B\3B\5B\u01be\nB\3B\3B\3C\3C\7C\u01c4")
        buf.write("\nC\fC\16C\u01c7\13C\3D\3D\3D\3D\3E\3E\7E\u01cf\nE\fE")
        buf.write("\16E\u01d2\13E\3E\3E\3E\3F\3F\7F\u01d9\nF\fF\16F\u01dc")
        buf.write("\13F\3F\5F\u01df\nF\3G\3G\2\2H\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o\2q\2s\2u9w\2y\2{\2}\2\177")
        buf.write(":\u0081;\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\3\2")
        buf.write("\25\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4")
        buf.write("\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\6\2")
        buf.write("\f\f\17\17$$^^\3\2$$\5\2ppttvv\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\13\16\17\"\"\6\2^^ppttvv\4\3\f\f\17\17\2\u01f3")
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
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2u\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\3\u008f\3\2\2\2\5\u009a\3\2\2\2\7\u009d\3\2\2")
        buf.write("\2\t\u00a2\3\2\2\2\13\u00a6\3\2\2\2\r\u00ad\3\2\2\2\17")
        buf.write("\u00b2\3\2\2\2\21\u00b7\3\2\2\2\23\u00be\3\2\2\2\25\u00c8")
        buf.write("\3\2\2\2\27\u00cf\3\2\2\2\31\u00d3\3\2\2\2\33\u00d9\3")
        buf.write("\2\2\2\35\u00e1\3\2\2\2\37\u00e7\3\2\2\2!\u00eb\3\2\2")
        buf.write("\2#\u00f4\3\2\2\2%\u00fa\3\2\2\2\'\u0100\3\2\2\2)\u0102")
        buf.write("\3\2\2\2+\u0104\3\2\2\2-\u0106\3\2\2\2/\u0108\3\2\2\2")
        buf.write("\61\u010a\3\2\2\2\63\u010d\3\2\2\2\65\u0110\3\2\2\2\67")
        buf.write("\u0113\3\2\2\29\u0116\3\2\2\2;\u0119\3\2\2\2=\u011c\3")
        buf.write("\2\2\2?\u011f\3\2\2\2A\u0122\3\2\2\2C\u0125\3\2\2\2E\u0127")
        buf.write("\3\2\2\2G\u0129\3\2\2\2I\u012c\3\2\2\2K\u012f\3\2\2\2")
        buf.write("M\u0131\3\2\2\2O\u0134\3\2\2\2Q\u0136\3\2\2\2S\u0138\3")
        buf.write("\2\2\2U\u013a\3\2\2\2W\u013c\3\2\2\2Y\u013e\3\2\2\2[\u0140")
        buf.write("\3\2\2\2]\u0142\3\2\2\2_\u0144\3\2\2\2a\u0146\3\2\2\2")
        buf.write("c\u014c\3\2\2\2e\u0156\3\2\2\2g\u0158\3\2\2\2i\u015f\3")
        buf.write("\2\2\2k\u0166\3\2\2\2m\u016d\3\2\2\2o\u0176\3\2\2\2q\u017d")
        buf.write("\3\2\2\2s\u0180\3\2\2\2u\u0194\3\2\2\2w\u019a\3\2\2\2")
        buf.write("y\u019c\3\2\2\2{\u019e\3\2\2\2}\u01a9\3\2\2\2\177\u01b4")
        buf.write("\3\2\2\2\u0081\u01b6\3\2\2\2\u0083\u01bd\3\2\2\2\u0085")
        buf.write("\u01c1\3\2\2\2\u0087\u01c8\3\2\2\2\u0089\u01cc\3\2\2\2")
        buf.write("\u008b\u01d6\3\2\2\2\u008d\u01e0\3\2\2\2\u008f\u0090\7")
        buf.write("\61\2\2\u0090\u0091\7\61\2\2\u0091\u0095\3\2\2\2\u0092")
        buf.write("\u0094\n\2\2\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\b\2\2\2\u0099\4")
        buf.write("\3\2\2\2\u009a\u009b\7k\2\2\u009b\u009c\7h\2\2\u009c\6")
        buf.write("\3\2\2\2\u009d\u009e\7g\2\2\u009e\u009f\7n\2\2\u009f\u00a0")
        buf.write("\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\b\3\2\2\2\u00a2\u00a3")
        buf.write("\7h\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5\n")
        buf.write("\3\2\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac")
        buf.write("\7p\2\2\u00ac\f\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7w\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7e\2\2\u00b1\16")
        buf.write("\3\2\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7{\2\2\u00b4\u00b5")
        buf.write("\7r\2\2\u00b5\u00b6\7g\2\2\u00b6\20\3\2\2\2\u00b7\u00b8")
        buf.write("\7u\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7w\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7v\2\2\u00bd\22")
        buf.write("\3\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\24\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7i\2\2\u00ce\26\3\2\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\30")
        buf.write("\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7v\2\2\u00d8\32")
        buf.write("\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7p\2\2\u00e0\34\3\2\2\2\u00e1\u00e2")
        buf.write("\7e\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\u00e6\7v\2\2\u00e6\36\3\2\2\2\u00e7\u00e8")
        buf.write("\7x\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7t\2\2\u00ea \3")
        buf.write("\2\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7g\2\2\u00f3\"")
        buf.write("\3\2\2\2\u00f4\u00f5\7d\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7m\2\2\u00f9$\3")
        buf.write("\2\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7g\2\2\u00ff&\3")
        buf.write("\2\2\2\u0100\u0101\7-\2\2\u0101(\3\2\2\2\u0102\u0103\7")
        buf.write("/\2\2\u0103*\3\2\2\2\u0104\u0105\7,\2\2\u0105,\3\2\2\2")
        buf.write("\u0106\u0107\7\61\2\2\u0107.\3\2\2\2\u0108\u0109\7\'\2")
        buf.write("\2\u0109\60\3\2\2\2\u010a\u010b\7-\2\2\u010b\u010c\7?")
        buf.write("\2\2\u010c\62\3\2\2\2\u010d\u010e\7/\2\2\u010e\u010f\7")
        buf.write("?\2\2\u010f\64\3\2\2\2\u0110\u0111\7,\2\2\u0111\u0112")
        buf.write("\7?\2\2\u0112\66\3\2\2\2\u0113\u0114\7\61\2\2\u0114\u0115")
        buf.write("\7?\2\2\u01158\3\2\2\2\u0116\u0117\7\'\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118:\3\2\2\2\u0119\u011a\7?\2\2\u011a\u011b")
        buf.write("\7?\2\2\u011b<\3\2\2\2\u011c\u011d\7#\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e>\3\2\2\2\u011f\u0120\7@\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121@\3\2\2\2\u0122\u0123\7>\2\2\u0123\u0124")
        buf.write("\7?\2\2\u0124B\3\2\2\2\u0125\u0126\7@\2\2\u0126D\3\2\2")
        buf.write("\2\u0127\u0128\7>\2\2\u0128F\3\2\2\2\u0129\u012a\7(\2")
        buf.write("\2\u012a\u012b\7(\2\2\u012bH\3\2\2\2\u012c\u012d\7~\2")
        buf.write("\2\u012d\u012e\7~\2\2\u012eJ\3\2\2\2\u012f\u0130\7#\2")
        buf.write("\2\u0130L\3\2\2\2\u0131\u0132\7<\2\2\u0132\u0133\7?\2")
        buf.write("\2\u0133N\3\2\2\2\u0134\u0135\7?\2\2\u0135P\3\2\2\2\u0136")
        buf.write("\u0137\7\60\2\2\u0137R\3\2\2\2\u0138\u0139\7*\2\2\u0139")
        buf.write("T\3\2\2\2\u013a\u013b\7+\2\2\u013bV\3\2\2\2\u013c\u013d")
        buf.write("\7]\2\2\u013dX\3\2\2\2\u013e\u013f\7_\2\2\u013fZ\3\2\2")
        buf.write("\2\u0140\u0141\7}\2\2\u0141\\\3\2\2\2\u0142\u0143\7\177")
        buf.write("\2\2\u0143^\3\2\2\2\u0144\u0145\7.\2\2\u0145`\3\2\2\2")
        buf.write("\u0146\u0147\7=\2\2\u0147b\3\2\2\2\u0148\u014d\5e\63\2")
        buf.write("\u0149\u014d\5g\64\2\u014a\u014d\5i\65\2\u014b\u014d\5")
        buf.write("k\66\2\u014c\u0148\3\2\2\2\u014c\u0149\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014c\u014b\3\2\2\2\u014dd\3\2\2\2\u014e\u0157")
        buf.write("\7\62\2\2\u014f\u0153\t\3\2\2\u0150\u0152\t\4\2\2\u0151")
        buf.write("\u0150\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3")
        buf.write("\2\2\2\u0156\u014e\3\2\2\2\u0156\u014f\3\2\2\2\u0157f")
        buf.write("\3\2\2\2\u0158\u0159\7\62\2\2\u0159\u015b\t\5\2\2\u015a")
        buf.write("\u015c\t\6\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015eh\3\2\2")
        buf.write("\2\u015f\u0160\7\62\2\2\u0160\u0162\t\7\2\2\u0161\u0163")
        buf.write("\t\b\2\2\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165j\3\2\2\2\u0166")
        buf.write("\u0167\7\62\2\2\u0167\u0169\t\t\2\2\u0168\u016a\t\n\2")
        buf.write("\2\u0169\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016cl\3\2\2\2\u016d\u016e")
        buf.write("\5o8\2\u016e\u0170\7\60\2\2\u016f\u0171\5q9\2\u0170\u016f")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172")
        buf.write("\u0174\5s:\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("n\3\2\2\2\u0175\u0177\t\4\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179p\3\2\2\2\u017a\u017c\t\4\2\2\u017b\u017a\3\2\2")
        buf.write("\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017er\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182")
        buf.write("\t\13\2\2\u0181\u0183\t\f\2\2\u0182\u0181\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0186\t\4\2\2")
        buf.write("\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3")
        buf.write("\2\2\2\u0187\u0188\3\2\2\2\u0188t\3\2\2\2\u0189\u018a")
        buf.write("\5y=\2\u018a\u018b\5y=\2\u018b\u0195\3\2\2\2\u018c\u018e")
        buf.write("\5y=\2\u018d\u018f\5w<\2\u018e\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0193\5y=\2\u0193\u0195\3\2\2\2\u0194")
        buf.write("\u0189\3\2\2\2\u0194\u018c\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0197\b;\3\2\u0197v\3\2\2\2\u0198\u019b\5}?\2\u0199")
        buf.write("\u019b\n\r\2\2\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2")
        buf.write("\u019bx\3\2\2\2\u019c\u019d\t\16\2\2\u019dz\3\2\2\2\u019e")
        buf.write("\u019f\7^\2\2\u019f|\3\2\2\2\u01a0\u01a1\5{>\2\u01a1\u01a2")
        buf.write("\t\17\2\2\u01a2\u01aa\3\2\2\2\u01a3\u01a4\5{>\2\u01a4")
        buf.write("\u01a5\5y=\2\u01a5\u01aa\3\2\2\2\u01a6\u01a7\5{>\2\u01a7")
        buf.write("\u01a8\5{>\2\u01a8\u01aa\3\2\2\2\u01a9\u01a0\3\2\2\2\u01a9")
        buf.write("\u01a3\3\2\2\2\u01a9\u01a6\3\2\2\2\u01aa~\3\2\2\2\u01ab")
        buf.write("\u01ac\7v\2\2\u01ac\u01ad\7t\2\2\u01ad\u01ae\7w\2\2\u01ae")
        buf.write("\u01b5\7g\2\2\u01af\u01b0\7h\2\2\u01b0\u01b1\7c\2\2\u01b1")
        buf.write("\u01b2\7n\2\2\u01b2\u01b3\7u\2\2\u01b3\u01b5\7g\2\2\u01b4")
        buf.write("\u01ab\3\2\2\2\u01b4\u01af\3\2\2\2\u01b5\u0080\3\2\2\2")
        buf.write("\u01b6\u01b7\7p\2\2\u01b7\u01b8\7k\2\2\u01b8\u01b9\7n")
        buf.write("\2\2\u01b9\u0082\3\2\2\2\u01ba\u01bb\7\17\2\2\u01bb\u01be")
        buf.write("\7\f\2\2\u01bc\u01be\7\f\2\2\u01bd\u01ba\3\2\2\2\u01bd")
        buf.write("\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\bB\4\2")
        buf.write("\u01c0\u0084\3\2\2\2\u01c1\u01c5\t\20\2\2\u01c2\u01c4")
        buf.write("\t\21\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u0086\3\2\2\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c8\u01c9\t\22\2\2\u01c9\u01ca")
        buf.write("\3\2\2\2\u01ca\u01cb\bD\2\2\u01cb\u0088\3\2\2\2\u01cc")
        buf.write("\u01d0\5y=\2\u01cd\u01cf\5w<\2\u01ce\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\5")
        buf.write("{>\2\u01d4\u01d5\n\23\2\2\u01d5\u008a\3\2\2\2\u01d6\u01da")
        buf.write("\5y=\2\u01d7\u01d9\5w<\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01df\t\24\2")
        buf.write("\2\u01de\u01dd\3\2\2\2\u01df\u008c\3\2\2\2\u01e0\u01e1")
        buf.write("\13\2\2\2\u01e1\u008e\3\2\2\2\32\2\u0095\u014c\u0153\u0156")
        buf.write("\u015d\u0164\u016b\u0170\u0173\u0178\u017d\u0182\u0187")
        buf.write("\u0190\u0194\u019a\u01a9\u01b4\u01bd\u01c5\u01d0\u01da")
        buf.write("\u01de\5\b\2\2\3;\2\3B\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_LINE_COMMENT = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    ADD = 19
    SUB = 20
    MULTIPLY = 21
    DIVIDE = 22
    REMAIN = 23
    SHORT_ADD = 24
    SHORT_SUB = 25
    SHORT_MULTIPLY = 26
    SHORT_DIVIDE = 27
    SHORT_REMAIN = 28
    COMPARE_STR = 29
    NOT_EQ = 30
    GREATER_OR_EQ = 31
    LESS_OR_EQ = 32
    GREATER = 33
    LESS = 34
    AND = 35
    OR = 36
    NOT = 37
    DECL = 38
    EQUAL = 39
    DOT = 40
    OPEN_PARANTHESIS = 41
    CLOSE_PARANTHESIS = 42
    OPEN_SQUARE = 43
    CLOSE_SQUARE = 44
    OPEN_BRACE = 45
    CLOSE_BRACE = 46
    COMMA = 47
    SEMICOLON = 48
    INTEGER_LITERAL = 49
    DECIMAL_INT = 50
    BINARY_INT = 51
    OCTAL_INT = 52
    HEXA_INT = 53
    FLOATING_POINT_LITERAL = 54
    STRING_LITERAL = 55
    BOOLEAN_LITERAL = 56
    NIL = 57
    NEWLINE = 58
    IDENTIFIER = 59
    WHITESPACE = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'&&'", 
            "'||'", "'!'", "':='", "'='", "'.'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_COMMENT", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
            "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ADD", "SUB", 
            "MULTIPLY", "DIVIDE", "REMAIN", "SHORT_ADD", "SHORT_SUB", "SHORT_MULTIPLY", 
            "SHORT_DIVIDE", "SHORT_REMAIN", "COMPARE_STR", "NOT_EQ", "GREATER_OR_EQ", 
            "LESS_OR_EQ", "GREATER", "LESS", "AND", "OR", "NOT", "DECL", 
            "EQUAL", "DOT", "OPEN_PARANTHESIS", "CLOSE_PARANTHESIS", "OPEN_SQUARE", 
            "CLOSE_SQUARE", "OPEN_BRACE", "CLOSE_BRACE", "COMMA", "SEMICOLON", 
            "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", 
            "HEXA_INT", "FLOATING_POINT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "NIL", "NEWLINE", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "SINGLE_LINE_COMMENT", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "ADD", "SUB", "MULTIPLY", "DIVIDE", "REMAIN", 
                  "SHORT_ADD", "SHORT_SUB", "SHORT_MULTIPLY", "SHORT_DIVIDE", 
                  "SHORT_REMAIN", "COMPARE_STR", "NOT_EQ", "GREATER_OR_EQ", 
                  "LESS_OR_EQ", "GREATER", "LESS", "AND", "OR", "NOT", "DECL", 
                  "EQUAL", "DOT", "OPEN_PARANTHESIS", "CLOSE_PARANTHESIS", 
                  "OPEN_SQUARE", "CLOSE_SQUARE", "OPEN_BRACE", "CLOSE_BRACE", 
                  "COMMA", "SEMICOLON", "INTEGER_LITERAL", "DECIMAL_INT", 
                  "BINARY_INT", "OCTAL_INT", "HEXA_INT", "FLOATING_POINT_LITERAL", 
                  "INT_PART", "DECI_PART", "EXP_PART", "STRING_LITERAL", 
                  "INSIDE_STRING", "DOUBLE_QUOTE", "BACKLASH", "ESCAPE_SEQUENCE", 
                  "BOOLEAN_LITERAL", "NIL", "NEWLINE", "IDENTIFIER", "WHITESPACE", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            raise UncloseString(result.text[1:].replace("\r","").replace("\n",""));
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.STRING_LITERAL_action 
            actions[64] = self.NEWLINE_action 
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
            self.text = '\n'
     


