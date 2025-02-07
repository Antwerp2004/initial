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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0196\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\5")
        buf.write("%\u0108\n%\3&\3&\3&\7&\u010d\n&\f&\16&\u0110\13&\5&\u0112")
        buf.write("\n&\3\'\3\'\3\'\6\'\u0117\n\'\r\'\16\'\u0118\3(\3(\3(")
        buf.write("\6(\u011e\n(\r(\16(\u011f\3)\3)\3)\6)\u0125\n)\r)\16)")
        buf.write("\u0126\3*\3*\3*\5*\u012c\n*\3*\5*\u012f\n*\3+\6+\u0132")
        buf.write("\n+\r+\16+\u0133\3,\7,\u0137\n,\f,\16,\u013a\13,\3-\3")
        buf.write("-\5-\u013e\n-\3-\6-\u0141\n-\r-\16-\u0142\3.\3.\3.\3.")
        buf.write("\3.\6.\u014a\n.\r.\16.\u014b\3.\3.\3.\3.\5.\u0152\n.\3")
        buf.write("/\3/\5/\u0156\n/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\5\62\u0165\n\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0170\n\63\3")
        buf.write("\64\3\64\3\64\3\64\3\65\3\65\7\65\u0178\n\65\f\65\16\65")
        buf.write("\u017b\13\65\3\66\3\66\3\66\3\66\3\67\3\67\7\67\u0183")
        buf.write("\n\67\f\67\16\67\u0186\13\67\3\67\3\67\3\67\38\38\78\u018d")
        buf.write("\n8\f8\168\u0190\138\38\58\u0193\n8\39\39\2\2:\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U\2W")
        buf.write("\2Y\2[,]\2_\2a\2c\2e-g.i/k\60m\61o\62q\63\3\2\24\3\2\63")
        buf.write(";\3\2\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5")
        buf.write("\2\62;CHch\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\3\2$$\5\2")
        buf.write("ppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\13\16\17\"\"\6")
        buf.write("\2^^ppttvv\4\3\f\f\17\17\2\u01a5\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2[\3\2\2\2\2e\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3")
        buf.write("\2\2\2\2q\3\2\2\2\3s\3\2\2\2\5u\3\2\2\2\7w\3\2\2\2\ty")
        buf.write("\3\2\2\2\13{\3\2\2\2\r}\3\2\2\2\17\177\3\2\2\2\21\u0081")
        buf.write("\3\2\2\2\23\u0083\3\2\2\2\25\u0085\3\2\2\2\27\u0087\3")
        buf.write("\2\2\2\31\u008a\3\2\2\2\33\u008d\3\2\2\2\35\u0090\3\2")
        buf.write("\2\2\37\u0093\3\2\2\2!\u0095\3\2\2\2#\u0097\3\2\2\2%\u009a")
        buf.write("\3\2\2\2\'\u009d\3\2\2\2)\u00a0\3\2\2\2+\u00a5\3\2\2\2")
        buf.write("-\u00a9\3\2\2\2/\u00b0\3\2\2\2\61\u00b5\3\2\2\2\63\u00ba")
        buf.write("\3\2\2\2\65\u00c1\3\2\2\2\67\u00cb\3\2\2\29\u00d2\3\2")
        buf.write("\2\2;\u00d6\3\2\2\2=\u00dc\3\2\2\2?\u00e4\3\2\2\2A\u00ea")
        buf.write("\3\2\2\2C\u00ee\3\2\2\2E\u00f7\3\2\2\2G\u00fd\3\2\2\2")
        buf.write("I\u0107\3\2\2\2K\u0111\3\2\2\2M\u0113\3\2\2\2O\u011a\3")
        buf.write("\2\2\2Q\u0121\3\2\2\2S\u0128\3\2\2\2U\u0131\3\2\2\2W\u0138")
        buf.write("\3\2\2\2Y\u013b\3\2\2\2[\u0151\3\2\2\2]\u0155\3\2\2\2")
        buf.write("_\u0157\3\2\2\2a\u0159\3\2\2\2c\u0164\3\2\2\2e\u016f\3")
        buf.write("\2\2\2g\u0171\3\2\2\2i\u0175\3\2\2\2k\u017c\3\2\2\2m\u0180")
        buf.write("\3\2\2\2o\u018a\3\2\2\2q\u0194\3\2\2\2st\7=\2\2t\4\3\2")
        buf.write("\2\2uv\7*\2\2v\6\3\2\2\2wx\7+\2\2x\b\3\2\2\2yz\7}\2\2")
        buf.write("z\n\3\2\2\2{|\7\177\2\2|\f\3\2\2\2}~\7,\2\2~\16\3\2\2")
        buf.write("\2\177\u0080\7\61\2\2\u0080\20\3\2\2\2\u0081\u0082\7\'")
        buf.write("\2\2\u0082\22\3\2\2\2\u0083\u0084\7-\2\2\u0084\24\3\2")
        buf.write("\2\2\u0085\u0086\7/\2\2\u0086\26\3\2\2\2\u0087\u0088\7")
        buf.write("?\2\2\u0088\u0089\7?\2\2\u0089\30\3\2\2\2\u008a\u008b")
        buf.write("\7#\2\2\u008b\u008c\7?\2\2\u008c\32\3\2\2\2\u008d\u008e")
        buf.write("\7@\2\2\u008e\u008f\7?\2\2\u008f\34\3\2\2\2\u0090\u0091")
        buf.write("\7>\2\2\u0091\u0092\7?\2\2\u0092\36\3\2\2\2\u0093\u0094")
        buf.write("\7@\2\2\u0094 \3\2\2\2\u0095\u0096\7>\2\2\u0096\"\3\2")
        buf.write("\2\2\u0097\u0098\7(\2\2\u0098\u0099\7(\2\2\u0099$\3\2")
        buf.write("\2\2\u009a\u009b\7~\2\2\u009b\u009c\7~\2\2\u009c&\3\2")
        buf.write("\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f(\3\2")
        buf.write("\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a4\7g\2\2\u00a4*\3\2\2\2\u00a5\u00a6")
        buf.write("\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8,\3")
        buf.write("\2\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af.\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7e\2\2\u00b4\60")
        buf.write("\3\2\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7{\2\2\u00b7\u00b8")
        buf.write("\7r\2\2\u00b8\u00b9\7g\2\2\u00b9\62\3\2\2\2\u00ba\u00bb")
        buf.write("\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7w\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7v\2\2\u00c0\64")
        buf.write("\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\66\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7i\2\2\u00d18\3\2\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5:\3")
        buf.write("\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7v\2\2\u00db<\3")
        buf.write("\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7p\2\2\u00e3>\3\2\2\2\u00e4\u00e5")
        buf.write("\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7u\2\2\u00e8\u00e9\7v\2\2\u00e9@\3\2\2\2\u00ea\u00eb")
        buf.write("\7x\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7t\2\2\u00edB\3")
        buf.write("\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7g\2\2\u00f6D\3")
        buf.write("\2\2\2\u00f7\u00f8\7d\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7m\2\2\u00fcF\3")
        buf.write("\2\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7i\2\2\u0101\u0102\7g\2\2\u0102H\3")
        buf.write("\2\2\2\u0103\u0108\5K&\2\u0104\u0108\5M\'\2\u0105\u0108")
        buf.write("\5O(\2\u0106\u0108\5Q)\2\u0107\u0103\3\2\2\2\u0107\u0104")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108")
        buf.write("J\3\2\2\2\u0109\u0112\7\62\2\2\u010a\u010e\t\2\2\2\u010b")
        buf.write("\u010d\t\3\2\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0112\3")
        buf.write("\2\2\2\u0110\u010e\3\2\2\2\u0111\u0109\3\2\2\2\u0111\u010a")
        buf.write("\3\2\2\2\u0112L\3\2\2\2\u0113\u0114\7\62\2\2\u0114\u0116")
        buf.write("\t\4\2\2\u0115\u0117\t\5\2\2\u0116\u0115\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119N\3\2\2\2\u011a\u011b\7\62\2\2\u011b\u011d\t\6\2")
        buf.write("\2\u011c\u011e\t\7\2\2\u011d\u011c\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120")
        buf.write("P\3\2\2\2\u0121\u0122\7\62\2\2\u0122\u0124\t\b\2\2\u0123")
        buf.write("\u0125\t\t\2\2\u0124\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127R\3\2\2")
        buf.write("\2\u0128\u0129\5U+\2\u0129\u012b\7\60\2\2\u012a\u012c")
        buf.write("\5W,\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e")
        buf.write("\3\2\2\2\u012d\u012f\5Y-\2\u012e\u012d\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012fT\3\2\2\2\u0130\u0132\t\3\2\2\u0131\u0130")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134V\3\2\2\2\u0135\u0137\t\3\2\2\u0136")
        buf.write("\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139X\3\2\2\2\u013a\u0138\3\2\2")
        buf.write("\2\u013b\u013d\t\n\2\2\u013c\u013e\t\13\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f")
        buf.write("\u0141\t\3\2\2\u0140\u013f\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143Z\3\2\2")
        buf.write("\2\u0144\u0145\5_\60\2\u0145\u0146\5_\60\2\u0146\u0152")
        buf.write("\3\2\2\2\u0147\u0149\5_\60\2\u0148\u014a\5]/\2\u0149\u0148")
        buf.write("\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\5_\60\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0150\b.\2\2\u0150\u0152\3")
        buf.write("\2\2\2\u0151\u0144\3\2\2\2\u0151\u0147\3\2\2\2\u0152\\")
        buf.write("\3\2\2\2\u0153\u0156\5c\62\2\u0154\u0156\n\f\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156^\3\2\2\2\u0157")
        buf.write("\u0158\t\r\2\2\u0158`\3\2\2\2\u0159\u015a\7^\2\2\u015a")
        buf.write("b\3\2\2\2\u015b\u015c\5a\61\2\u015c\u015d\t\16\2\2\u015d")
        buf.write("\u0165\3\2\2\2\u015e\u015f\5a\61\2\u015f\u0160\5_\60\2")
        buf.write("\u0160\u0165\3\2\2\2\u0161\u0162\5a\61\2\u0162\u0163\5")
        buf.write("a\61\2\u0163\u0165\3\2\2\2\u0164\u015b\3\2\2\2\u0164\u015e")
        buf.write("\3\2\2\2\u0164\u0161\3\2\2\2\u0165d\3\2\2\2\u0166\u0167")
        buf.write("\7v\2\2\u0167\u0168\7t\2\2\u0168\u0169\7w\2\2\u0169\u0170")
        buf.write("\7g\2\2\u016a\u016b\7h\2\2\u016b\u016c\7c\2\2\u016c\u016d")
        buf.write("\7n\2\2\u016d\u016e\7u\2\2\u016e\u0170\7g\2\2\u016f\u0166")
        buf.write("\3\2\2\2\u016f\u016a\3\2\2\2\u0170f\3\2\2\2\u0171\u0172")
        buf.write("\7p\2\2\u0172\u0173\7k\2\2\u0173\u0174\7n\2\2\u0174h\3")
        buf.write("\2\2\2\u0175\u0179\t\17\2\2\u0176\u0178\t\20\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017aj\3\2\2\2\u017b\u0179\3\2\2")
        buf.write("\2\u017c\u017d\t\21\2\2\u017d\u017e\3\2\2\2\u017e\u017f")
        buf.write("\b\66\3\2\u017fl\3\2\2\2\u0180\u0184\5_\60\2\u0181\u0183")
        buf.write("\5]/\2\u0182\u0181\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0187\u0188\5a\61\2\u0188\u0189\n\22\2")
        buf.write("\2\u0189n\3\2\2\2\u018a\u018e\5_\60\2\u018b\u018d\5]/")
        buf.write("\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0192\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0191\u0193\t\23\2\2\u0192\u0191\3\2\2")
        buf.write("\2\u0193p\3\2\2\2\u0194\u0195\13\2\2\2\u0195r\3\2\2\2")
        buf.write("\30\2\u0107\u010e\u0111\u0118\u011f\u0126\u012b\u012e")
        buf.write("\u0133\u0138\u013d\u0142\u014b\u0151\u0155\u0164\u016f")
        buf.write("\u0179\u0184\u018e\u0192\4\3.\2\b\2\2")
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
    WHITESPACE = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'", "'{'", "'}'", "'*'", "'/'", "'%'", "'+'", 
            "'-'", "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'&&'", 
            "'||'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", 
            "OCTAL_INT", "HEXA_INT", "FLOATING_POINT_LITERAL", "STRING_LITERAL", 
            "BOOLEAN_LITERAL", "NIL", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", 
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
                  "NIL", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
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
     


