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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01e6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\7\2\u0096")
        buf.write("\n\2\f\2\16\2\u0099\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\63\5")
        buf.write("\63\u0151\n\63\3\64\3\64\3\64\7\64\u0156\n\64\f\64\16")
        buf.write("\64\u0159\13\64\5\64\u015b\n\64\3\65\3\65\3\65\6\65\u0160")
        buf.write("\n\65\r\65\16\65\u0161\3\66\3\66\3\66\6\66\u0167\n\66")
        buf.write("\r\66\16\66\u0168\3\67\3\67\3\67\6\67\u016e\n\67\r\67")
        buf.write("\16\67\u016f\38\38\38\58\u0175\n8\38\58\u0178\n8\39\6")
        buf.write("9\u017b\n9\r9\169\u017c\3:\7:\u0180\n:\f:\16:\u0183\13")
        buf.write(":\3;\3;\5;\u0187\n;\3;\6;\u018a\n;\r;\16;\u018b\3<\3<")
        buf.write("\3<\3<\3<\6<\u0193\n<\r<\16<\u0194\3<\3<\5<\u0199\n<\3")
        buf.write("<\3<\3=\3=\5=\u019f\n=\3>\3>\3?\3?\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\5@\u01ae\n@\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u01b9")
        buf.write("\nA\3B\3B\3B\3B\3C\3C\3C\5C\u01c2\nC\3C\3C\3D\3D\7D\u01c8")
        buf.write("\nD\fD\16D\u01cb\13D\3E\3E\3E\3E\3F\3F\7F\u01d3\nF\fF")
        buf.write("\16F\u01d6\13F\3F\3F\3F\3G\3G\7G\u01dd\nG\fG\16G\u01e0")
        buf.write("\13G\3G\5G\u01e3\nG\3H\3H\2\2I\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w:y\2{\2}\2\177\2")
        buf.write("\u0081;\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\u008f")
        buf.write("B\3\2\25\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2DDdd\3\2\62")
        buf.write("\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--")
        buf.write("//\6\2\f\f\17\17$$^^\3\2$$\5\2ppttvv\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\13\16\17\"\"\6\2^^ppttvv\4\3\f\f\17\17")
        buf.write("\2\u01f7\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2w\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2")
        buf.write("\2\5\u009c\3\2\2\2\7\u009f\3\2\2\2\t\u00a4\3\2\2\2\13")
        buf.write("\u00a8\3\2\2\2\r\u00af\3\2\2\2\17\u00b4\3\2\2\2\21\u00b9")
        buf.write("\3\2\2\2\23\u00c0\3\2\2\2\25\u00ca\3\2\2\2\27\u00d1\3")
        buf.write("\2\2\2\31\u00d5\3\2\2\2\33\u00db\3\2\2\2\35\u00e3\3\2")
        buf.write("\2\2\37\u00e9\3\2\2\2!\u00ed\3\2\2\2#\u00f6\3\2\2\2%\u00fc")
        buf.write("\3\2\2\2\'\u0102\3\2\2\2)\u0104\3\2\2\2+\u0106\3\2\2\2")
        buf.write("-\u0108\3\2\2\2/\u010a\3\2\2\2\61\u010c\3\2\2\2\63\u010f")
        buf.write("\3\2\2\2\65\u0112\3\2\2\2\67\u0115\3\2\2\29\u0118\3\2")
        buf.write("\2\2;\u011b\3\2\2\2=\u011e\3\2\2\2?\u0121\3\2\2\2A\u0124")
        buf.write("\3\2\2\2C\u0127\3\2\2\2E\u0129\3\2\2\2G\u012b\3\2\2\2")
        buf.write("I\u012e\3\2\2\2K\u0131\3\2\2\2M\u0133\3\2\2\2O\u0136\3")
        buf.write("\2\2\2Q\u0138\3\2\2\2S\u013a\3\2\2\2U\u013c\3\2\2\2W\u013e")
        buf.write("\3\2\2\2Y\u0140\3\2\2\2[\u0142\3\2\2\2]\u0144\3\2\2\2")
        buf.write("_\u0146\3\2\2\2a\u0148\3\2\2\2c\u014a\3\2\2\2e\u0150\3")
        buf.write("\2\2\2g\u015a\3\2\2\2i\u015c\3\2\2\2k\u0163\3\2\2\2m\u016a")
        buf.write("\3\2\2\2o\u0171\3\2\2\2q\u017a\3\2\2\2s\u0181\3\2\2\2")
        buf.write("u\u0184\3\2\2\2w\u0198\3\2\2\2y\u019e\3\2\2\2{\u01a0\3")
        buf.write("\2\2\2}\u01a2\3\2\2\2\177\u01ad\3\2\2\2\u0081\u01b8\3")
        buf.write("\2\2\2\u0083\u01ba\3\2\2\2\u0085\u01c1\3\2\2\2\u0087\u01c5")
        buf.write("\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u01d0\3\2\2\2\u008d")
        buf.write("\u01da\3\2\2\2\u008f\u01e4\3\2\2\2\u0091\u0092\7\61\2")
        buf.write("\2\u0092\u0093\7\61\2\2\u0093\u0097\3\2\2\2\u0094\u0096")
        buf.write("\n\2\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u009a\u009b\b\2\2\2\u009b\4\3\2\2")
        buf.write("\2\u009c\u009d\7k\2\2\u009d\u009e\7h\2\2\u009e\6\3\2\2")
        buf.write("\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7")
        buf.write("u\2\2\u00a2\u00a3\7g\2\2\u00a3\b\3\2\2\2\u00a4\u00a5\7")
        buf.write("h\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7t\2\2\u00a7\n\3")
        buf.write("\2\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae")
        buf.write("\7p\2\2\u00ae\f\3\2\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1")
        buf.write("\7w\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7e\2\2\u00b3\16")
        buf.write("\3\2\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7{\2\2\u00b6\u00b7")
        buf.write("\7r\2\2\u00b7\u00b8\7g\2\2\u00b8\20\3\2\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7w\2\2\u00bd\u00be\7e\2\2\u00be\u00bf\7v\2\2\u00bf\22")
        buf.write("\3\2\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\24\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7i\2\2\u00d0\26\3\2\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\30")
        buf.write("\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7v\2\2\u00da\32")
        buf.write("\3\2\2\2\u00db\u00dc\7d\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7p\2\2\u00e2\34\3\2\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e8\7v\2\2\u00e8\36\3\2\2\2\u00e9\u00ea")
        buf.write("\7x\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7t\2\2\u00ec \3")
        buf.write("\2\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7g\2\2\u00f5\"")
        buf.write("\3\2\2\2\u00f6\u00f7\7d\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7g\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7m\2\2\u00fb$\3")
        buf.write("\2\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7i\2\2\u0100\u0101\7g\2\2\u0101&\3")
        buf.write("\2\2\2\u0102\u0103\7-\2\2\u0103(\3\2\2\2\u0104\u0105\7")
        buf.write("/\2\2\u0105*\3\2\2\2\u0106\u0107\7,\2\2\u0107,\3\2\2\2")
        buf.write("\u0108\u0109\7\61\2\2\u0109.\3\2\2\2\u010a\u010b\7\'\2")
        buf.write("\2\u010b\60\3\2\2\2\u010c\u010d\7-\2\2\u010d\u010e\7?")
        buf.write("\2\2\u010e\62\3\2\2\2\u010f\u0110\7/\2\2\u0110\u0111\7")
        buf.write("?\2\2\u0111\64\3\2\2\2\u0112\u0113\7,\2\2\u0113\u0114")
        buf.write("\7?\2\2\u0114\66\3\2\2\2\u0115\u0116\7\61\2\2\u0116\u0117")
        buf.write("\7?\2\2\u01178\3\2\2\2\u0118\u0119\7\'\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a:\3\2\2\2\u011b\u011c\7?\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011d<\3\2\2\2\u011e\u011f\7#\2\2\u011f\u0120")
        buf.write("\7?\2\2\u0120>\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123")
        buf.write("\7?\2\2\u0123@\3\2\2\2\u0124\u0125\7>\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126B\3\2\2\2\u0127\u0128\7@\2\2\u0128D\3\2\2")
        buf.write("\2\u0129\u012a\7>\2\2\u012aF\3\2\2\2\u012b\u012c\7(\2")
        buf.write("\2\u012c\u012d\7(\2\2\u012dH\3\2\2\2\u012e\u012f\7~\2")
        buf.write("\2\u012f\u0130\7~\2\2\u0130J\3\2\2\2\u0131\u0132\7#\2")
        buf.write("\2\u0132L\3\2\2\2\u0133\u0134\7<\2\2\u0134\u0135\7?\2")
        buf.write("\2\u0135N\3\2\2\2\u0136\u0137\7?\2\2\u0137P\3\2\2\2\u0138")
        buf.write("\u0139\7\60\2\2\u0139R\3\2\2\2\u013a\u013b\7*\2\2\u013b")
        buf.write("T\3\2\2\2\u013c\u013d\7+\2\2\u013dV\3\2\2\2\u013e\u013f")
        buf.write("\7]\2\2\u013fX\3\2\2\2\u0140\u0141\7_\2\2\u0141Z\3\2\2")
        buf.write("\2\u0142\u0143\7}\2\2\u0143\\\3\2\2\2\u0144\u0145\7\177")
        buf.write("\2\2\u0145^\3\2\2\2\u0146\u0147\7.\2\2\u0147`\3\2\2\2")
        buf.write("\u0148\u0149\7=\2\2\u0149b\3\2\2\2\u014a\u014b\7<\2\2")
        buf.write("\u014bd\3\2\2\2\u014c\u0151\5g\64\2\u014d\u0151\5i\65")
        buf.write("\2\u014e\u0151\5k\66\2\u014f\u0151\5m\67\2\u0150\u014c")
        buf.write("\3\2\2\2\u0150\u014d\3\2\2\2\u0150\u014e\3\2\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151f\3\2\2\2\u0152\u015b\7\62\2\2\u0153")
        buf.write("\u0157\t\3\2\2\u0154\u0156\t\4\2\2\u0155\u0154\3\2\2\2")
        buf.write("\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u0152")
        buf.write("\3\2\2\2\u015a\u0153\3\2\2\2\u015bh\3\2\2\2\u015c\u015d")
        buf.write("\7\62\2\2\u015d\u015f\t\5\2\2\u015e\u0160\t\6\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162j\3\2\2\2\u0163\u0164\7\62\2")
        buf.write("\2\u0164\u0166\t\7\2\2\u0165\u0167\t\b\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169l\3\2\2\2\u016a\u016b\7\62\2\2\u016b")
        buf.write("\u016d\t\t\2\2\u016c\u016e\t\n\2\2\u016d\u016c\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170n\3\2\2\2\u0171\u0172\5q9\2\u0172\u0174\7")
        buf.write("\60\2\2\u0173\u0175\5s:\2\u0174\u0173\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0178\5u;\2\u0177\u0176")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178p\3\2\2\2\u0179\u017b")
        buf.write("\t\4\2\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017dr\3\2\2\2\u017e")
        buf.write("\u0180\t\4\2\2\u017f\u017e\3\2\2\2\u0180\u0183\3\2\2\2")
        buf.write("\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182t\3\2\2")
        buf.write("\2\u0183\u0181\3\2\2\2\u0184\u0186\t\13\2\2\u0185\u0187")
        buf.write("\t\f\2\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u018a\t\4\2\2\u0189\u0188\3\2\2\2")
        buf.write("\u018a\u018b\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018cv\3\2\2\2\u018d\u018e\5{>\2\u018e\u018f\5")
        buf.write("{>\2\u018f\u0199\3\2\2\2\u0190\u0192\5{>\2\u0191\u0193")
        buf.write("\5y=\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0197\5{>\2\u0197\u0199\3\2\2\2\u0198\u018d\3\2\2\2\u0198")
        buf.write("\u0190\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\b<\3\2")
        buf.write("\u019bx\3\2\2\2\u019c\u019f\5\177@\2\u019d\u019f\n\r\2")
        buf.write("\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019fz\3\2")
        buf.write("\2\2\u01a0\u01a1\t\16\2\2\u01a1|\3\2\2\2\u01a2\u01a3\7")
        buf.write("^\2\2\u01a3~\3\2\2\2\u01a4\u01a5\5}?\2\u01a5\u01a6\t\17")
        buf.write("\2\2\u01a6\u01ae\3\2\2\2\u01a7\u01a8\5}?\2\u01a8\u01a9")
        buf.write("\5{>\2\u01a9\u01ae\3\2\2\2\u01aa\u01ab\5}?\2\u01ab\u01ac")
        buf.write("\5}?\2\u01ac\u01ae\3\2\2\2\u01ad\u01a4\3\2\2\2\u01ad\u01a7")
        buf.write("\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ae\u0080\3\2\2\2\u01af")
        buf.write("\u01b0\7v\2\2\u01b0\u01b1\7t\2\2\u01b1\u01b2\7w\2\2\u01b2")
        buf.write("\u01b9\7g\2\2\u01b3\u01b4\7h\2\2\u01b4\u01b5\7c\2\2\u01b5")
        buf.write("\u01b6\7n\2\2\u01b6\u01b7\7u\2\2\u01b7\u01b9\7g\2\2\u01b8")
        buf.write("\u01af\3\2\2\2\u01b8\u01b3\3\2\2\2\u01b9\u0082\3\2\2\2")
        buf.write("\u01ba\u01bb\7p\2\2\u01bb\u01bc\7k\2\2\u01bc\u01bd\7n")
        buf.write("\2\2\u01bd\u0084\3\2\2\2\u01be\u01bf\7\17\2\2\u01bf\u01c2")
        buf.write("\7\f\2\2\u01c0\u01c2\7\f\2\2\u01c1\u01be\3\2\2\2\u01c1")
        buf.write("\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4\bC\4\2")
        buf.write("\u01c4\u0086\3\2\2\2\u01c5\u01c9\t\20\2\2\u01c6\u01c8")
        buf.write("\t\21\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u0088\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cc\u01cd\t\22\2\2\u01cd\u01ce")
        buf.write("\3\2\2\2\u01ce\u01cf\bE\2\2\u01cf\u008a\3\2\2\2\u01d0")
        buf.write("\u01d4\5{>\2\u01d1\u01d3\5y=\2\u01d2\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\5")
        buf.write("}?\2\u01d8\u01d9\n\23\2\2\u01d9\u008c\3\2\2\2\u01da\u01de")
        buf.write("\5{>\2\u01db\u01dd\5y=\2\u01dc\u01db\3\2\2\2\u01dd\u01e0")
        buf.write("\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e3\t\24\2")
        buf.write("\2\u01e2\u01e1\3\2\2\2\u01e3\u008e\3\2\2\2\u01e4\u01e5")
        buf.write("\13\2\2\2\u01e5\u0090\3\2\2\2\32\2\u0097\u0150\u0157\u015a")
        buf.write("\u0161\u0168\u016f\u0174\u0177\u017c\u0181\u0186\u018b")
        buf.write("\u0194\u0198\u019e\u01ad\u01b8\u01c1\u01c9\u01d4\u01de")
        buf.write("\u01e2\5\b\2\2\3<\2\3C\3")
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
    OPEN_PARENTHESIS = 41
    CLOSE_PARENTHESIS = 42
    OPEN_BRACKET = 43
    CLOSE_BRACKET = 44
    OPEN_BRACE = 45
    CLOSE_BRACE = 46
    COMMA = 47
    SEMICOLON = 48
    COLON = 49
    INTEGER_LITERAL = 50
    DECIMAL_INT = 51
    BINARY_INT = 52
    OCTAL_INT = 53
    HEXA_INT = 54
    FLOATING_POINT_LITERAL = 55
    STRING_LITERAL = 56
    BOOLEAN_LITERAL = 57
    NIL_LITERAL = 58
    NEWLINE = 59
    IDENTIFIER = 60
    WHITESPACE = 61
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'&&'", 
            "'||'", "'!'", "':='", "'='", "'.'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'", "':'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_COMMENT", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
            "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ADD", "SUB", 
            "MULTIPLY", "DIVIDE", "REMAIN", "SHORT_ADD", "SHORT_SUB", "SHORT_MULTIPLY", 
            "SHORT_DIVIDE", "SHORT_REMAIN", "COMPARE_STR", "NOT_EQ", "GREATER_OR_EQ", 
            "LESS_OR_EQ", "GREATER", "LESS", "AND", "OR", "NOT", "DECL", 
            "EQUAL", "DOT", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", 
            "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", "COMMA", "SEMICOLON", 
            "COLON", "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", 
            "HEXA_INT", "FLOATING_POINT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "NIL_LITERAL", "NEWLINE", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "SINGLE_LINE_COMMENT", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "ADD", "SUB", "MULTIPLY", "DIVIDE", "REMAIN", 
                  "SHORT_ADD", "SHORT_SUB", "SHORT_MULTIPLY", "SHORT_DIVIDE", 
                  "SHORT_REMAIN", "COMPARE_STR", "NOT_EQ", "GREATER_OR_EQ", 
                  "LESS_OR_EQ", "GREATER", "LESS", "AND", "OR", "NOT", "DECL", 
                  "EQUAL", "DOT", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                  "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                  "COMMA", "SEMICOLON", "COLON", "INTEGER_LITERAL", "DECIMAL_INT", 
                  "BINARY_INT", "OCTAL_INT", "HEXA_INT", "FLOATING_POINT_LITERAL", 
                  "INT_PART", "DECI_PART", "EXP_PART", "STRING_LITERAL", 
                  "INSIDE_STRING", "DOUBLE_QUOTE", "BACKLASH", "ESCAPE_SEQUENCE", 
                  "BOOLEAN_LITERAL", "NIL_LITERAL", "NEWLINE", "IDENTIFIER", 
                  "WHITESPACE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[58] = self.STRING_LITERAL_action 
            actions[65] = self.NEWLINE_action 
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
     


