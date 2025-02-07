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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\7\24\u00a8\n\24\f\24\16\24\u00ab\13\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\7\25\u00b3\n\25\f\25\16\25\u00b6\13\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00c1")
        buf.write("\n\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\5\'\u012d\n\'\3(\3(\3(\7(\u0132\n(\f(\16")
        buf.write("(\u0135\13(\5(\u0137\n(\3)\3)\3)\6)\u013c\n)\r)\16)\u013d")
        buf.write("\3*\3*\3*\6*\u0143\n*\r*\16*\u0144\3+\3+\3+\6+\u014a\n")
        buf.write("+\r+\16+\u014b\3,\3,\3,\5,\u0151\n,\3,\5,\u0154\n,\3-")
        buf.write("\6-\u0157\n-\r-\16-\u0158\3.\7.\u015c\n.\f.\16.\u015f")
        buf.write("\13.\3/\3/\5/\u0163\n/\3/\6/\u0166\n/\r/\16/\u0167\3\60")
        buf.write("\3\60\3\60\3\60\3\60\6\60\u016f\n\60\r\60\16\60\u0170")
        buf.write("\3\60\3\60\5\60\u0175\n\60\3\60\3\60\3\61\3\61\5\61\u017b")
        buf.write("\n\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u018a\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\5\65\u0195\n\65\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\5\67\u019e\n\67\3\67\3\67\38\38\7")
        buf.write("8\u01a4\n8\f8\168\u01a7\138\39\39\39\39\3:\3:\7:\u01af")
        buf.write("\n:\f:\16:\u01b2\13:\3:\3:\3:\3;\3;\7;\u01b9\n;\f;\16")
        buf.write(";\u01bc\13;\3;\5;\u01bf\n;\3<\3<\2\2=\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2")
        buf.write("]\2_.a\2c\2e\2g\2i/k\60m\61o\62q\63s\64u\65w\66\3\2\25")
        buf.write("\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2Q")
        buf.write("Qqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\6\2\f")
        buf.write("\f\17\17$$^^\3\2$$\5\2ppttvv\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\5\2\13\13\16\17\"\"\6\2^^ppttvv\4\3\f\f\17\17\2\u01d5")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2_\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5{\3\2\2\2\7}\3\2\2\2\t\177")
        buf.write("\3\2\2\2\13\u0081\3\2\2\2\r\u0083\3\2\2\2\17\u0085\3\2")
        buf.write("\2\2\21\u0087\3\2\2\2\23\u0089\3\2\2\2\25\u008b\3\2\2")
        buf.write("\2\27\u008d\3\2\2\2\31\u0090\3\2\2\2\33\u0093\3\2\2\2")
        buf.write("\35\u0096\3\2\2\2\37\u0099\3\2\2\2!\u009b\3\2\2\2#\u009d")
        buf.write("\3\2\2\2%\u00a0\3\2\2\2\'\u00a3\3\2\2\2)\u00c0\3\2\2\2")
        buf.write("+\u00c2\3\2\2\2-\u00c5\3\2\2\2/\u00ca\3\2\2\2\61\u00ce")
        buf.write("\3\2\2\2\63\u00d5\3\2\2\2\65\u00da\3\2\2\2\67\u00df\3")
        buf.write("\2\2\29\u00e6\3\2\2\2;\u00f0\3\2\2\2=\u00f7\3\2\2\2?\u00fb")
        buf.write("\3\2\2\2A\u0101\3\2\2\2C\u0109\3\2\2\2E\u010f\3\2\2\2")
        buf.write("G\u0113\3\2\2\2I\u011c\3\2\2\2K\u0122\3\2\2\2M\u012c\3")
        buf.write("\2\2\2O\u0136\3\2\2\2Q\u0138\3\2\2\2S\u013f\3\2\2\2U\u0146")
        buf.write("\3\2\2\2W\u014d\3\2\2\2Y\u0156\3\2\2\2[\u015d\3\2\2\2")
        buf.write("]\u0160\3\2\2\2_\u0174\3\2\2\2a\u017a\3\2\2\2c\u017c\3")
        buf.write("\2\2\2e\u017e\3\2\2\2g\u0189\3\2\2\2i\u0194\3\2\2\2k\u0196")
        buf.write("\3\2\2\2m\u019d\3\2\2\2o\u01a1\3\2\2\2q\u01a8\3\2\2\2")
        buf.write("s\u01ac\3\2\2\2u\u01b6\3\2\2\2w\u01c0\3\2\2\2yz\7=\2\2")
        buf.write("z\4\3\2\2\2{|\7*\2\2|\6\3\2\2\2}~\7+\2\2~\b\3\2\2\2\177")
        buf.write("\u0080\7}\2\2\u0080\n\3\2\2\2\u0081\u0082\7\177\2\2\u0082")
        buf.write("\f\3\2\2\2\u0083\u0084\7,\2\2\u0084\16\3\2\2\2\u0085\u0086")
        buf.write("\7\61\2\2\u0086\20\3\2\2\2\u0087\u0088\7\'\2\2\u0088\22")
        buf.write("\3\2\2\2\u0089\u008a\7-\2\2\u008a\24\3\2\2\2\u008b\u008c")
        buf.write("\7/\2\2\u008c\26\3\2\2\2\u008d\u008e\7?\2\2\u008e\u008f")
        buf.write("\7?\2\2\u008f\30\3\2\2\2\u0090\u0091\7#\2\2\u0091\u0092")
        buf.write("\7?\2\2\u0092\32\3\2\2\2\u0093\u0094\7@\2\2\u0094\u0095")
        buf.write("\7?\2\2\u0095\34\3\2\2\2\u0096\u0097\7>\2\2\u0097\u0098")
        buf.write("\7?\2\2\u0098\36\3\2\2\2\u0099\u009a\7@\2\2\u009a \3\2")
        buf.write("\2\2\u009b\u009c\7>\2\2\u009c\"\3\2\2\2\u009d\u009e\7")
        buf.write("(\2\2\u009e\u009f\7(\2\2\u009f$\3\2\2\2\u00a0\u00a1\7")
        buf.write("~\2\2\u00a1\u00a2\7~\2\2\u00a2&\3\2\2\2\u00a3\u00a4\7")
        buf.write("\61\2\2\u00a4\u00a5\7\61\2\2\u00a5\u00a9\3\2\2\2\u00a6")
        buf.write("\u00a8\n\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\b\24\2\2\u00ad")
        buf.write("(\3\2\2\2\u00ae\u00af\7\61\2\2\u00af\u00b0\7,\2\2\u00b0")
        buf.write("\u00b4\3\2\2\2\u00b1\u00b3\13\2\2\2\u00b2\u00b1\3\2\2")
        buf.write("\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7")
        buf.write("\u00b8\7,\2\2\u00b8\u00c1\7\61\2\2\u00b9\u00ba\7\61\2")
        buf.write("\2\u00ba\u00bb\7,\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd")
        buf.write("\5)\25\2\u00bd\u00be\7,\2\2\u00be\u00bf\7\61\2\2\u00bf")
        buf.write("\u00c1\3\2\2\2\u00c0\u00ae\3\2\2\2\u00c0\u00b9\3\2\2\2")
        buf.write("\u00c1*\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7h\2\2")
        buf.write("\u00c4,\3\2\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7n\2\2")
        buf.write("\u00c7\u00c8\7u\2\2\u00c8\u00c9\7g\2\2\u00c9.\3\2\2\2")
        buf.write("\u00ca\u00cb\7h\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7t")
        buf.write("\2\2\u00cd\60\3\2\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7")
        buf.write("g\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7p\2\2\u00d4\62\3\2\2\2\u00d5\u00d6")
        buf.write("\7h\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7e\2\2\u00d9\64\3\2\2\2\u00da\u00db\7v\2\2\u00db\u00dc")
        buf.write("\7{\2\2\u00dc\u00dd\7r\2\2\u00dd\u00de\7g\2\2\u00de\66")
        buf.write("\3\2\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e58\3\2\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7e\2\2\u00ee\u00ef\7g\2\2\u00ef:\3\2\2\2\u00f0\u00f1")
        buf.write("\7u\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7i\2\2\u00f6<\3")
        buf.write("\2\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa>\3\2\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd")
        buf.write("\7n\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100@\3\2\2\2\u0101\u0102\7d\2\2\u0102\u0103")
        buf.write("\7q\2\2\u0103\u0104\7q\2\2\u0104\u0105\7n\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7c\2\2\u0107\u0108\7p\2\2\u0108B\3")
        buf.write("\2\2\2\u0109\u010a\7e\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\u010d\7u\2\2\u010d\u010e\7v\2\2\u010eD\3")
        buf.write("\2\2\2\u010f\u0110\7x\2\2\u0110\u0111\7c\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112F\3\2\2\2\u0113\u0114\7e\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7p\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a\7w\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011bH\3\2\2\2\u011c\u011d\7d\2\2\u011d\u011e")
        buf.write("\7t\2\2\u011e\u011f\7g\2\2\u011f\u0120\7c\2\2\u0120\u0121")
        buf.write("\7m\2\2\u0121J\3\2\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7p\2\2\u0125\u0126\7i\2\2\u0126\u0127")
        buf.write("\7g\2\2\u0127L\3\2\2\2\u0128\u012d\5O(\2\u0129\u012d\5")
        buf.write("Q)\2\u012a\u012d\5S*\2\u012b\u012d\5U+\2\u012c\u0128\3")
        buf.write("\2\2\2\u012c\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012dN\3\2\2\2\u012e\u0137\7\62\2\2\u012f\u0133")
        buf.write("\t\3\2\2\u0130\u0132\t\4\2\2\u0131\u0130\3\2\2\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u012e\3")
        buf.write("\2\2\2\u0136\u012f\3\2\2\2\u0137P\3\2\2\2\u0138\u0139")
        buf.write("\7\62\2\2\u0139\u013b\t\5\2\2\u013a\u013c\t\6\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013eR\3\2\2\2\u013f\u0140\7\62\2")
        buf.write("\2\u0140\u0142\t\7\2\2\u0141\u0143\t\b\2\2\u0142\u0141")
        buf.write("\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0142\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145T\3\2\2\2\u0146\u0147\7\62\2\2\u0147")
        buf.write("\u0149\t\t\2\2\u0148\u014a\t\n\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014cV\3\2\2\2\u014d\u014e\5Y-\2\u014e\u0150\7")
        buf.write("\60\2\2\u014f\u0151\5[.\2\u0150\u014f\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0154\5]/\2\u0153\u0152")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154X\3\2\2\2\u0155\u0157")
        buf.write("\t\4\2\2\u0156\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159Z\3\2\2\2\u015a")
        buf.write("\u015c\t\4\2\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\\\3\2\2")
        buf.write("\2\u015f\u015d\3\2\2\2\u0160\u0162\t\13\2\2\u0161\u0163")
        buf.write("\t\f\2\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0166\t\4\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168^\3\2\2\2\u0169\u016a\5c\62\2\u016a\u016b")
        buf.write("\5c\62\2\u016b\u0175\3\2\2\2\u016c\u016e\5c\62\2\u016d")
        buf.write("\u016f\5a\61\2\u016e\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0173\5c\62\2\u0173\u0175\3\2\2\2\u0174\u0169")
        buf.write("\3\2\2\2\u0174\u016c\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0177\b\60\3\2\u0177`\3\2\2\2\u0178\u017b\5g\64\2\u0179")
        buf.write("\u017b\n\r\2\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017bb\3\2\2\2\u017c\u017d\t\16\2\2\u017dd\3\2\2\2\u017e")
        buf.write("\u017f\7^\2\2\u017ff\3\2\2\2\u0180\u0181\5e\63\2\u0181")
        buf.write("\u0182\t\17\2\2\u0182\u018a\3\2\2\2\u0183\u0184\5e\63")
        buf.write("\2\u0184\u0185\5c\62\2\u0185\u018a\3\2\2\2\u0186\u0187")
        buf.write("\5e\63\2\u0187\u0188\5e\63\2\u0188\u018a\3\2\2\2\u0189")
        buf.write("\u0180\3\2\2\2\u0189\u0183\3\2\2\2\u0189\u0186\3\2\2\2")
        buf.write("\u018ah\3\2\2\2\u018b\u018c\7v\2\2\u018c\u018d\7t\2\2")
        buf.write("\u018d\u018e\7w\2\2\u018e\u0195\7g\2\2\u018f\u0190\7h")
        buf.write("\2\2\u0190\u0191\7c\2\2\u0191\u0192\7n\2\2\u0192\u0193")
        buf.write("\7u\2\2\u0193\u0195\7g\2\2\u0194\u018b\3\2\2\2\u0194\u018f")
        buf.write("\3\2\2\2\u0195j\3\2\2\2\u0196\u0197\7p\2\2\u0197\u0198")
        buf.write("\7k\2\2\u0198\u0199\7n\2\2\u0199l\3\2\2\2\u019a\u019b")
        buf.write("\7\17\2\2\u019b\u019e\7\f\2\2\u019c\u019e\7\f\2\2\u019d")
        buf.write("\u019a\3\2\2\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a0\b\67\4\2\u01a0n\3\2\2\2\u01a1\u01a5\t\20")
        buf.write("\2\2\u01a2\u01a4\t\21\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("p\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9\t\22\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ab\b9\2\2\u01abr\3\2\2\2\u01ac")
        buf.write("\u01b0\5c\62\2\u01ad\u01af\5a\61\2\u01ae\u01ad\3\2\2\2")
        buf.write("\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3")
        buf.write("\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4")
        buf.write("\5e\63\2\u01b4\u01b5\n\23\2\2\u01b5t\3\2\2\2\u01b6\u01ba")
        buf.write("\5c\62\2\u01b7\u01b9\5a\61\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01bf\t")
        buf.write("\24\2\2\u01be\u01bd\3\2\2\2\u01bfv\3\2\2\2\u01c0\u01c1")
        buf.write("\13\2\2\2\u01c1x\3\2\2\2\34\2\u00a9\u00b4\u00c0\u012c")
        buf.write("\u0133\u0136\u013d\u0144\u014b\u0150\u0153\u0158\u015d")
        buf.write("\u0162\u0167\u0170\u0174\u017a\u0189\u0194\u019d\u01a5")
        buf.write("\u01b0\u01ba\u01be\5\b\2\2\3\60\2\3\67\3")
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
    SINGLE_LINE_COMMENT = 19
    MULTI_LINE_COMMENT = 20
    IF = 21
    ELSE = 22
    FOR = 23
    RETURN = 24
    FUNC = 25
    TYPE = 26
    STRUCT = 27
    INTERFACE = 28
    STRING = 29
    INT = 30
    FLOAT = 31
    BOOLEAN = 32
    CONST = 33
    VAR = 34
    CONTINUE = 35
    BREAK = 36
    RANGE = 37
    INTEGER_LITERAL = 38
    DECIMAL_INT = 39
    BINARY_INT = 40
    OCTAL_INT = 41
    HEXA_INT = 42
    FLOATING_POINT_LITERAL = 43
    STRING_LITERAL = 44
    BOOLEAN_LITERAL = 45
    NIL = 46
    NEWLINE = 47
    IDENTIFIER = 48
    WHITESPACE = 49
    ILLEGAL_ESCAPE = 50
    UNCLOSE_STRING = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'", "'{'", "'}'", "'*'", "'/'", "'%'", "'+'", 
            "'-'", "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'&&'", 
            "'||'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "IF", "ELSE", "FOR", 
            "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
            "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
            "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", 
            "HEXA_INT", "FLOATING_POINT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "NIL", "NEWLINE", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                  "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                  "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                  "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", 
                  "HEXA_INT", "FLOATING_POINT_LITERAL", "INT_PART", "DECI_PART", 
                  "EXP_PART", "STRING_LITERAL", "INSIDE_STRING", "DOUBLE_QUOTE", 
                  "BACKLASH", "ESCAPE_SEQUENCE", "BOOLEAN_LITERAL", "NIL", 
                  "NEWLINE", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[46] = self.STRING_LITERAL_action 
            actions[53] = self.NEWLINE_action 
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
     


