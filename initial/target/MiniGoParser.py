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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0252\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0082\n\2\r\2")
        buf.write("\16\2\u0083\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008e")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u009a")
        buf.write("\n\4\3\5\3\5\6\5\u009e\n\5\r\5\16\5\u009f\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ad\n\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\5\b\u00ba\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00c4\n\n\3\13\3\13\3")
        buf.write("\13\5\13\u00c9\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00da\n\r\f\r\16\r\u00dd")
        buf.write("\13\r\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u00e5\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0103\n\23\3\23\3")
        buf.write("\23\5\23\u0107\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\5\30\u011f\n\30\3\30\3\30\3\31\3")
        buf.write("\31\5\31\u0125\n\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u012d\n\32\3\32\3\32\5\32\u0131\n\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\5\33\u0139\n\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\7\34\u0140\n\34\f\34\16\34\u0143\13\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u014d\n\35\3\35\3\35\5")
        buf.write("\35\u0151\n\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \5 \u015f\n \3!\3!\3!\3!\3!\3!\7!\u0167")
        buf.write("\n!\f!\16!\u016a\13!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0172")
        buf.write("\n\"\f\"\16\"\u0175\13\"\3#\3#\3#\3#\3#\3#\3#\7#\u017e")
        buf.write("\n#\f#\16#\u0181\13#\3$\3$\3$\3$\3$\3$\3$\7$\u018a\n$")
        buf.write("\f$\16$\u018d\13$\3%\3%\3%\3%\3%\3%\3%\7%\u0196\n%\f%")
        buf.write("\16%\u0199\13%\3&\3&\3&\5&\u019e\n&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01ab\n\'\f\'\16\'\u01ae")
        buf.write("\13\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01be")
        buf.write("\n)\3*\3*\3*\3*\3*\3*\3*\5*\u01c7\n*\5*\u01c9\n*\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3-\3-\3-\6-\u01d6\n-\r-\16-\u01d7")
        buf.write("\3-\3-\3.\3.\3.\7.\u01df\n.\f.\16.\u01e2\13.\3/\3/\3/")
        buf.write("\3/\3/\3/\3/\3/\5/\u01ec\n/\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\6\61\u01f4\n\61\r\61\16\61\u01f5\3\62\3\62\3\62\3")
        buf.write("\62\3\62\6\62\u01fd\n\62\r\62\16\62\u01fe\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\5\64\u020b\n\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\7\65\u0212\n\65\f\65\16\65\u0215")
        buf.write("\13\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\68\u0224\n8\r8\168\u0225\38\38\38\39\39\39\59")
        buf.write("\u022e\n9\39\39\59\u0232\n9\39\39\3:\3:\3:\7:\u0239\n")
        buf.write(":\f:\16:\u023c\13:\3;\3;\3;\7;\u0241\n;\f;\16;\u0244\13")
        buf.write(";\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\2\b@BDFHLA\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2\n\3\2\r\20")
        buf.write("\4\2\27\27##\4\2\65\65@@\3\2\30\32\3\2\26\27\3\2\33 \3")
        buf.write("\2$)\3\2\3\4\2\u025e\2\u0081\3\2\2\2\4\u008d\3\2\2\2\6")
        buf.write("\u0099\3\2\2\2\b\u009b\3\2\2\2\n\u00a3\3\2\2\2\f\u00b0")
        buf.write("\3\2\2\2\16\u00b9\3\2\2\2\20\u00bb\3\2\2\2\22\u00c3\3")
        buf.write("\2\2\2\24\u00c5\3\2\2\2\26\u00cc\3\2\2\2\30\u00db\3\2")
        buf.write("\2\2\32\u00de\3\2\2\2\34\u00e4\3\2\2\2\36\u00e6\3\2\2")
        buf.write("\2 \u00eb\3\2\2\2\"\u00ed\3\2\2\2$\u0106\3\2\2\2&\u0108")
        buf.write("\3\2\2\2(\u010c\3\2\2\2*\u0116\3\2\2\2,\u0119\3\2\2\2")
        buf.write(".\u011e\3\2\2\2\60\u0122\3\2\2\2\62\u0128\3\2\2\2\64\u0135")
        buf.write("\3\2\2\2\66\u013c\3\2\2\28\u0144\3\2\2\2:\u0155\3\2\2")
        buf.write("\2<\u0159\3\2\2\2>\u015e\3\2\2\2@\u0160\3\2\2\2B\u016b")
        buf.write("\3\2\2\2D\u0176\3\2\2\2F\u0182\3\2\2\2H\u018e\3\2\2\2")
        buf.write("J\u019d\3\2\2\2L\u019f\3\2\2\2N\u01af\3\2\2\2P\u01bd\3")
        buf.write("\2\2\2R\u01c8\3\2\2\2T\u01ca\3\2\2\2V\u01ce\3\2\2\2X\u01d2")
        buf.write("\3\2\2\2Z\u01db\3\2\2\2\\\u01eb\3\2\2\2^\u01ed\3\2\2\2")
        buf.write("`\u01f1\3\2\2\2b\u01f7\3\2\2\2d\u0203\3\2\2\2f\u0207\3")
        buf.write("\2\2\2h\u020e\3\2\2\2j\u0216\3\2\2\2l\u021a\3\2\2\2n\u021e")
        buf.write("\3\2\2\2p\u022a\3\2\2\2r\u0235\3\2\2\2t\u023d\3\2\2\2")
        buf.write("v\u0247\3\2\2\2x\u0249\3\2\2\2z\u024b\3\2\2\2|\u024d\3")
        buf.write("\2\2\2~\u024f\3\2\2\2\u0080\u0082\5\4\3\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\7\2\2\3")
        buf.write("\u0086\3\3\2\2\2\u0087\u008e\5\n\6\2\u0088\u008e\5\f\7")
        buf.write("\2\u0089\u008e\5b\62\2\u008a\u008e\5n8\2\u008b\u008e\5")
        buf.write("\62\32\2\u008c\u008e\58\35\2\u008d\u0087\3\2\2\2\u008d")
        buf.write("\u0088\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008a\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\5\3\2\2")
        buf.write("\2\u008f\u009a\5\n\6\2\u0090\u009a\5\f\7\2\u0091\u009a")
        buf.write("\5\20\t\2\u0092\u009a\5\24\13\2\u0093\u009a\5\34\17\2")
        buf.write("\u0094\u009a\5*\26\2\u0095\u009a\5,\27\2\u0096\u009a\5")
        buf.write(".\30\2\u0097\u009a\5\60\31\2\u0098\u009a\5~@\2\u0099\u008f")
        buf.write("\3\2\2\2\u0099\u0090\3\2\2\2\u0099\u0091\3\2\2\2\u0099")
        buf.write("\u0092\3\2\2\2\u0099\u0093\3\2\2\2\u0099\u0094\3\2\2\2")
        buf.write("\u0099\u0095\3\2\2\2\u0099\u0096\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u0099\u0098\3\2\2\2\u009a\7\3\2\2\2\u009b\u009d")
        buf.write("\7\60\2\2\u009c\u009e\5\6\4\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7\61\2\2\u00a2\t\3\2")
        buf.write("\2\2\u00a3\u00a4\7\22\2\2\u00a4\u00ac\7@\2\2\u00a5\u00ad")
        buf.write("\5\16\b\2\u00a6\u00a7\7*\2\2\u00a7\u00ad\5@!\2\u00a8\u00a9")
        buf.write("\5\16\b\2\u00a9\u00aa\7*\2\2\u00aa\u00ab\5@!\2\u00ab\u00ad")
        buf.write("\3\2\2\2\u00ac\u00a5\3\2\2\2\u00ac\u00a6\3\2\2\2\u00ac")
        buf.write("\u00a8\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\7\63\2")
        buf.write("\2\u00af\13\3\2\2\2\u00b0\u00b1\7\21\2\2\u00b1\u00b2\7")
        buf.write("@\2\2\u00b2\u00b3\7*\2\2\u00b3\u00b4\5@!\2\u00b4\u00b5")
        buf.write("\7\63\2\2\u00b5\r\3\2\2\2\u00b6\u00ba\5<\37\2\u00b7\u00ba")
        buf.write("\7@\2\2\u00b8\u00ba\5R*\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\17\3\2\2\2\u00bb\u00bc")
        buf.write("\5\22\n\2\u00bc\u00bd\5|?\2\u00bd\u00be\5@!\2\u00be\u00bf")
        buf.write("\7\63\2\2\u00bf\21\3\2\2\2\u00c0\u00c4\7@\2\2\u00c1\u00c4")
        buf.write("\5l\67\2\u00c2\u00c4\5`\61\2\u00c3\u00c0\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\23\3\2\2\2\u00c5")
        buf.write("\u00c6\5\26\f\2\u00c6\u00c8\5\30\r\2\u00c7\u00c9\5\32")
        buf.write("\16\2\u00c8\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cb\7\63\2\2\u00cb\25\3\2\2\2\u00cc\u00cd")
        buf.write("\7\5\2\2\u00cd\u00ce\7,\2\2\u00ce\u00cf\5@!\2\u00cf\u00d0")
        buf.write("\7-\2\2\u00d0\u00d1\5\b\5\2\u00d1\27\3\2\2\2\u00d2\u00d3")
        buf.write("\7\6\2\2\u00d3\u00d4\7\5\2\2\u00d4\u00d5\7,\2\2\u00d5")
        buf.write("\u00d6\5@!\2\u00d6\u00d7\7-\2\2\u00d7\u00d8\5\b\5\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00d2\3\2\2\2\u00da\u00dd\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\31\3\2")
        buf.write("\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\7\6\2\2\u00df\u00e0")
        buf.write("\5\b\5\2\u00e0\33\3\2\2\2\u00e1\u00e5\5\36\20\2\u00e2")
        buf.write("\u00e5\5\"\22\2\u00e3\u00e5\5(\25\2\u00e4\u00e1\3\2\2")
        buf.write("\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\35\3")
        buf.write("\2\2\2\u00e6\u00e7\7\7\2\2\u00e7\u00e8\5 \21\2\u00e8\u00e9")
        buf.write("\5\b\5\2\u00e9\u00ea\7\63\2\2\u00ea\37\3\2\2\2\u00eb\u00ec")
        buf.write("\5@!\2\u00ec!\3\2\2\2\u00ed\u00ee\7\7\2\2\u00ee\u00ef")
        buf.write("\5$\23\2\u00ef\u00f0\5 \21\2\u00f0\u00f1\7\63\2\2\u00f1")
        buf.write("\u00f2\5&\24\2\u00f2\u00f3\5\b\5\2\u00f3\u00f4\7\63\2")
        buf.write("\2\u00f4#\3\2\2\2\u00f5\u00f6\7@\2\2\u00f6\u00f7\5|?\2")
        buf.write("\u00f7\u00f8\5@!\2\u00f8\u00f9\7\63\2\2\u00f9\u0107\3")
        buf.write("\2\2\2\u00fa\u00fb\7\22\2\2\u00fb\u0102\7@\2\2\u00fc\u00fd")
        buf.write("\7*\2\2\u00fd\u0103\5@!\2\u00fe\u00ff\5\16\b\2\u00ff\u0100")
        buf.write("\7*\2\2\u0100\u0101\5@!\2\u0101\u0103\3\2\2\2\u0102\u00fc")
        buf.write("\3\2\2\2\u0102\u00fe\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u0105\7\63\2\2\u0105\u0107\3\2\2\2\u0106\u00f5\3\2\2")
        buf.write("\2\u0106\u00fa\3\2\2\2\u0107%\3\2\2\2\u0108\u0109\7@\2")
        buf.write("\2\u0109\u010a\5|?\2\u010a\u010b\5@!\2\u010b\'\3\2\2\2")
        buf.write("\u010c\u010d\7\7\2\2\u010d\u010e\7@\2\2\u010e\u010f\7")
        buf.write("\62\2\2\u010f\u0110\7@\2\2\u0110\u0111\7$\2\2\u0111\u0112")
        buf.write("\7\25\2\2\u0112\u0113\5@!\2\u0113\u0114\5\b\5\2\u0114")
        buf.write("\u0115\7\63\2\2\u0115)\3\2\2\2\u0116\u0117\7\24\2\2\u0117")
        buf.write("\u0118\7\63\2\2\u0118+\3\2\2\2\u0119\u011a\7\23\2\2\u011a")
        buf.write("\u011b\7\63\2\2\u011b-\3\2\2\2\u011c\u011f\5\64\33\2\u011d")
        buf.write("\u011f\5:\36\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u0121\7\63\2\2\u0121/\3\2\2")
        buf.write("\2\u0122\u0124\7\b\2\2\u0123\u0125\5@!\2\u0124\u0123\3")
        buf.write("\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127")
        buf.write("\7\63\2\2\u0127\61\3\2\2\2\u0128\u0129\7\t\2\2\u0129\u012a")
        buf.write("\7@\2\2\u012a\u012c\7,\2\2\u012b\u012d\5r:\2\u012c\u012b")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u0130\7-\2\2\u012f\u0131\5> \2\u0130\u012f\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\5\b\5\2")
        buf.write("\u0133\u0134\7\63\2\2\u0134\63\3\2\2\2\u0135\u0136\7@")
        buf.write("\2\2\u0136\u0138\7,\2\2\u0137\u0139\5\66\34\2\u0138\u0137")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\7-\2\2\u013b\65\3\2\2\2\u013c\u0141\5@!\2\u013d")
        buf.write("\u013e\7\62\2\2\u013e\u0140\5@!\2\u013f\u013d\3\2\2\2")
        buf.write("\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3")
        buf.write("\2\2\2\u0142\67\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145")
        buf.write("\7\t\2\2\u0145\u0146\7,\2\2\u0146\u0147\7@\2\2\u0147\u0148")
        buf.write("\7@\2\2\u0148\u0149\7-\2\2\u0149\u014a\7@\2\2\u014a\u014c")
        buf.write("\7,\2\2\u014b\u014d\5r:\2\u014c\u014b\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\7-\2\2\u014f")
        buf.write("\u0151\5> \2\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0153\5\b\5\2\u0153\u0154\7\63\2")
        buf.write("\2\u01549\3\2\2\2\u0155\u0156\5L\'\2\u0156\u0157\7+\2")
        buf.write("\2\u0157\u0158\5\64\33\2\u0158;\3\2\2\2\u0159\u015a\t")
        buf.write("\2\2\2\u015a=\3\2\2\2\u015b\u015f\5<\37\2\u015c\u015f")
        buf.write("\7@\2\2\u015d\u015f\5R*\2\u015e\u015b\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015d\3\2\2\2\u015f?\3\2\2\2\u0160\u0161")
        buf.write("\b!\1\2\u0161\u0162\5B\"\2\u0162\u0168\3\2\2\2\u0163\u0164")
        buf.write("\f\4\2\2\u0164\u0165\7\"\2\2\u0165\u0167\5B\"\2\u0166")
        buf.write("\u0163\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169A\3\2\2\2\u016a\u0168\3\2\2")
        buf.write("\2\u016b\u016c\b\"\1\2\u016c\u016d\5D#\2\u016d\u0173\3")
        buf.write("\2\2\2\u016e\u016f\f\4\2\2\u016f\u0170\7!\2\2\u0170\u0172")
        buf.write("\5D#\2\u0171\u016e\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174C\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0176\u0177\b#\1\2\u0177\u0178\5F$\2\u0178\u017f")
        buf.write("\3\2\2\2\u0179\u017a\f\4\2\2\u017a\u017b\5z>\2\u017b\u017c")
        buf.write("\5F$\2\u017c\u017e\3\2\2\2\u017d\u0179\3\2\2\2\u017e\u0181")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("E\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\b$\1\2\u0183")
        buf.write("\u0184\5H%\2\u0184\u018b\3\2\2\2\u0185\u0186\f\4\2\2\u0186")
        buf.write("\u0187\5x=\2\u0187\u0188\5H%\2\u0188\u018a\3\2\2\2\u0189")
        buf.write("\u0185\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018cG\3\2\2\2\u018d\u018b\3\2\2")
        buf.write("\2\u018e\u018f\b%\1\2\u018f\u0190\5J&\2\u0190\u0197\3")
        buf.write("\2\2\2\u0191\u0192\f\4\2\2\u0192\u0193\5v<\2\u0193\u0194")
        buf.write("\5J&\2\u0194\u0196\3\2\2\2\u0195\u0191\3\2\2\2\u0196\u0199")
        buf.write("\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("I\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\t\3\2\2\u019b")
        buf.write("\u019e\5J&\2\u019c\u019e\5L\'\2\u019d\u019a\3\2\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019eK\3\2\2\2\u019f\u01a0\b\'\1\2\u01a0")
        buf.write("\u01a1\5P)\2\u01a1\u01ac\3\2\2\2\u01a2\u01a3\f\5\2\2\u01a3")
        buf.write("\u01a4\7+\2\2\u01a4\u01ab\5P)\2\u01a5\u01a6\f\4\2\2\u01a6")
        buf.write("\u01a7\7.\2\2\u01a7\u01a8\5@!\2\u01a8\u01a9\7/\2\2\u01a9")
        buf.write("\u01ab\3\2\2\2\u01aa\u01a2\3\2\2\2\u01aa\u01a5\3\2\2\2")
        buf.write("\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01adM\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0")
        buf.write("\7,\2\2\u01b0\u01b1\5@!\2\u01b1\u01b2\7-\2\2\u01b2O\3")
        buf.write("\2\2\2\u01b3\u01be\7\65\2\2\u01b4\u01be\7:\2\2\u01b5\u01be")
        buf.write("\7;\2\2\u01b6\u01be\7<\2\2\u01b7\u01be\7=\2\2\u01b8\u01be")
        buf.write("\5X-\2\u01b9\u01be\5f\64\2\u01ba\u01be\7@\2\2\u01bb\u01be")
        buf.write("\5\64\33\2\u01bc\u01be\5N(\2\u01bd\u01b3\3\2\2\2\u01bd")
        buf.write("\u01b4\3\2\2\2\u01bd\u01b5\3\2\2\2\u01bd\u01b6\3\2\2\2")
        buf.write("\u01bd\u01b7\3\2\2\2\u01bd\u01b8\3\2\2\2\u01bd\u01b9\3")
        buf.write("\2\2\2\u01bd\u01ba\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01beQ\3\2\2\2\u01bf\u01c0\5T+\2\u01c0\u01c1")
        buf.write("\5R*\2\u01c1\u01c9\3\2\2\2\u01c2\u01c6\5T+\2\u01c3\u01c7")
        buf.write("\5<\37\2\u01c4\u01c7\7@\2\2\u01c5\u01c7\5R*\2\u01c6\u01c3")
        buf.write("\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("\u01c9\3\2\2\2\u01c8\u01bf\3\2\2\2\u01c8\u01c2\3\2\2\2")
        buf.write("\u01c9S\3\2\2\2\u01ca\u01cb\7.\2\2\u01cb\u01cc\t\4\2\2")
        buf.write("\u01cc\u01cd\7/\2\2\u01cdU\3\2\2\2\u01ce\u01cf\7.\2\2")
        buf.write("\u01cf\u01d0\5@!\2\u01d0\u01d1\7/\2\2\u01d1W\3\2\2\2\u01d2")
        buf.write("\u01d3\5R*\2\u01d3\u01d5\7\60\2\2\u01d4\u01d6\5Z.\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\7")
        buf.write("\61\2\2\u01daY\3\2\2\2\u01db\u01e0\5\\/\2\u01dc\u01dd")
        buf.write("\7\62\2\2\u01dd\u01df\5\\/\2\u01de\u01dc\3\2\2\2\u01df")
        buf.write("\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1[\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01ec\7\65\2")
        buf.write("\2\u01e4\u01ec\7:\2\2\u01e5\u01ec\7<\2\2\u01e6\u01ec\7")
        buf.write(";\2\2\u01e7\u01ec\7=\2\2\u01e8\u01ec\7@\2\2\u01e9\u01ec")
        buf.write("\5f\64\2\u01ea\u01ec\5^\60\2\u01eb\u01e3\3\2\2\2\u01eb")
        buf.write("\u01e4\3\2\2\2\u01eb\u01e5\3\2\2\2\u01eb\u01e6\3\2\2\2")
        buf.write("\u01eb\u01e7\3\2\2\2\u01eb\u01e8\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01eb\u01ea\3\2\2\2\u01ec]\3\2\2\2\u01ed\u01ee")
        buf.write("\7\60\2\2\u01ee\u01ef\5Z.\2\u01ef\u01f0\7\61\2\2\u01f0")
        buf.write("_\3\2\2\2\u01f1\u01f3\5L\'\2\u01f2\u01f4\5V,\2\u01f3\u01f2")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f6\3\2\2\2\u01f6a\3\2\2\2\u01f7\u01f8\7\n\2\2\u01f8")
        buf.write("\u01f9\7@\2\2\u01f9\u01fa\7\13\2\2\u01fa\u01fc\7\60\2")
        buf.write("\2\u01fb\u01fd\5d\63\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0201\7\61\2\2\u0201\u0202\7\63\2")
        buf.write("\2\u0202c\3\2\2\2\u0203\u0204\7@\2\2\u0204\u0205\5> \2")
        buf.write("\u0205\u0206\7\63\2\2\u0206e\3\2\2\2\u0207\u0208\7@\2")
        buf.write("\2\u0208\u020a\7\60\2\2\u0209\u020b\5h\65\2\u020a\u0209")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("\u020d\7\61\2\2\u020dg\3\2\2\2\u020e\u0213\5j\66\2\u020f")
        buf.write("\u0210\7\62\2\2\u0210\u0212\5j\66\2\u0211\u020f\3\2\2")
        buf.write("\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214i\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0217")
        buf.write("\7@\2\2\u0217\u0218\7\64\2\2\u0218\u0219\5@!\2\u0219k")
        buf.write("\3\2\2\2\u021a\u021b\5L\'\2\u021b\u021c\7+\2\2\u021c\u021d")
        buf.write("\7@\2\2\u021dm\3\2\2\2\u021e\u021f\7\n\2\2\u021f\u0220")
        buf.write("\7@\2\2\u0220\u0221\7\f\2\2\u0221\u0223\7\60\2\2\u0222")
        buf.write("\u0224\5p9\2\u0223\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\3\2\2\2")
        buf.write("\u0227\u0228\7\61\2\2\u0228\u0229\7\63\2\2\u0229o\3\2")
        buf.write("\2\2\u022a\u022b\7@\2\2\u022b\u022d\7,\2\2\u022c\u022e")
        buf.write("\5r:\2\u022d\u022c\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f")
        buf.write("\3\2\2\2\u022f\u0231\7-\2\2\u0230\u0232\5> \2\u0231\u0230")
        buf.write("\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("\u0234\7\63\2\2\u0234q\3\2\2\2\u0235\u023a\5t;\2\u0236")
        buf.write("\u0237\7\62\2\2\u0237\u0239\5t;\2\u0238\u0236\3\2\2\2")
        buf.write("\u0239\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u023b\3")
        buf.write("\2\2\2\u023bs\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u0242")
        buf.write("\7@\2\2\u023e\u023f\7\62\2\2\u023f\u0241\7@\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0245\3\2\2\2\u0244\u0242\3")
        buf.write("\2\2\2\u0245\u0246\5> \2\u0246u\3\2\2\2\u0247\u0248\t")
        buf.write("\5\2\2\u0248w\3\2\2\2\u0249\u024a\t\6\2\2\u024ay\3\2\2")
        buf.write("\2\u024b\u024c\t\7\2\2\u024c{\3\2\2\2\u024d\u024e\t\b")
        buf.write("\2\2\u024e}\3\2\2\2\u024f\u0250\t\t\2\2\u0250\177\3\2")
        buf.write("\2\2.\u0083\u008d\u0099\u009f\u00ac\u00b9\u00c3\u00c8")
        buf.write("\u00db\u00e4\u0102\u0106\u011e\u0124\u012c\u0130\u0138")
        buf.write("\u0141\u014c\u0150\u015e\u0168\u0173\u017f\u018b\u0197")
        buf.write("\u019d\u01aa\u01ac\u01bd\u01c6\u01c8\u01d7\u01e0\u01eb")
        buf.write("\u01f5\u01fe\u020a\u0213\u0225\u022d\u0231\u023a\u0242")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>='", "'<='", "'>'", "'<'", "'&&'", "'||'", "'!'", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", 
                     "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
                     "';'", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ADD", 
                      "SUB", "MULTIPLY", "DIVIDE", "REMAIN", "COMPARE_STR", 
                      "NOT_EQ", "GREATER_OR_EQ", "LESS_OR_EQ", "GREATER", 
                      "LESS", "AND", "OR", "NOT", "ASSIGNMENT_SIGN", "SHORT_ADD", 
                      "SHORT_SUB", "SHORT_MULTIPLY", "SHORT_DIVIDE", "SHORT_REMAIN", 
                      "EQUAL", "DOT", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                      "COMMA", "SEMICOLON", "COLON", "INTEGER_LITERAL", 
                      "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", "HEXA_INT", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "NIL_LITERAL", "NEWLINE", "WHITESPACE", "IDENTIFIER", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_stmt = 2
    RULE_block = 3
    RULE_var_decl = 4
    RULE_const_decl = 5
    RULE_decl_typ = 6
    RULE_assign_stmt = 7
    RULE_lhs = 8
    RULE_if_stmt = 9
    RULE_only_if_stmt = 10
    RULE_else_if_list = 11
    RULE_else_stmt = 12
    RULE_for_stmt = 13
    RULE_basic_for_loop = 14
    RULE_condition = 15
    RULE_for_loop_initial = 16
    RULE_initialization = 17
    RULE_update = 18
    RULE_for_loop_range = 19
    RULE_break_stmt = 20
    RULE_continue_stmt = 21
    RULE_call_stmt = 22
    RULE_return_stmt = 23
    RULE_func_decl = 24
    RULE_func_call = 25
    RULE_argument_list = 26
    RULE_method_decl = 27
    RULE_method_call = 28
    RULE_primitive_type = 29
    RULE_typ = 30
    RULE_expr = 31
    RULE_expr1 = 32
    RULE_expr2 = 33
    RULE_expr3 = 34
    RULE_expr4 = 35
    RULE_expr5 = 36
    RULE_expr6 = 37
    RULE_sub_expr = 38
    RULE_operand = 39
    RULE_array_type = 40
    RULE_array_literal_box = 41
    RULE_array_access_box = 42
    RULE_array_literal = 43
    RULE_array_ele_list = 44
    RULE_array_ele = 45
    RULE_short_array_literal = 46
    RULE_array_access = 47
    RULE_struct_decl = 48
    RULE_struct_field = 49
    RULE_struct_literal = 50
    RULE_struct_ele_list = 51
    RULE_struct_ele = 52
    RULE_struct_access = 53
    RULE_interface_decl = 54
    RULE_interface_method = 55
    RULE_param_list = 56
    RULE_param_decl = 57
    RULE_arith_high_operator = 58
    RULE_arith_low_operator = 59
    RULE_relational_operator = 60
    RULE_assign_operator = 61
    RULE_comment = 62

    ruleNames =  [ "program", "decl", "stmt", "block", "var_decl", "const_decl", 
                   "decl_typ", "assign_stmt", "lhs", "if_stmt", "only_if_stmt", 
                   "else_if_list", "else_stmt", "for_stmt", "basic_for_loop", 
                   "condition", "for_loop_initial", "initialization", "update", 
                   "for_loop_range", "break_stmt", "continue_stmt", "call_stmt", 
                   "return_stmt", "func_decl", "func_call", "argument_list", 
                   "method_decl", "method_call", "primitive_type", "typ", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "sub_expr", "operand", "array_type", "array_literal_box", 
                   "array_access_box", "array_literal", "array_ele_list", 
                   "array_ele", "short_array_literal", "array_access", "struct_decl", 
                   "struct_field", "struct_literal", "struct_ele_list", 
                   "struct_ele", "struct_access", "interface_decl", "interface_method", 
                   "param_list", "param_decl", "arith_high_operator", "arith_low_operator", 
                   "relational_operator", "assign_operator", "comment" ]

    EOF = Token.EOF
    SINGLE_LINE_COMMENT=1
    MULTI_LINE_COMMENT=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    ADD=20
    SUB=21
    MULTIPLY=22
    DIVIDE=23
    REMAIN=24
    COMPARE_STR=25
    NOT_EQ=26
    GREATER_OR_EQ=27
    LESS_OR_EQ=28
    GREATER=29
    LESS=30
    AND=31
    OR=32
    NOT=33
    ASSIGNMENT_SIGN=34
    SHORT_ADD=35
    SHORT_SUB=36
    SHORT_MULTIPLY=37
    SHORT_DIVIDE=38
    SHORT_REMAIN=39
    EQUAL=40
    DOT=41
    OPEN_PARENTHESIS=42
    CLOSE_PARENTHESIS=43
    OPEN_BRACKET=44
    CLOSE_BRACKET=45
    OPEN_BRACE=46
    CLOSE_BRACE=47
    COMMA=48
    SEMICOLON=49
    COLON=50
    INTEGER_LITERAL=51
    DECIMAL_INT=52
    BINARY_INT=53
    OCTAL_INT=54
    HEXA_INT=55
    FLOAT_LITERAL=56
    STRING_LITERAL=57
    BOOLEAN_LITERAL=58
    NIL_LITERAL=59
    NEWLINE=60
    WHITESPACE=61
    IDENTIFIER=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    ERROR_CHAR=65

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
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.decl()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 131
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

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.struct_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.interface_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.func_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def comment(self):
            return self.getTypedRuleContext(MiniGoParser.CommentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 148
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 149
                self.return_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 150
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 155 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 154
                self.stmt()
                self.state = 157 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SINGLE_LINE_COMMENT) | (1 << MiniGoParser.MULTI_LINE_COMMENT) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.OPEN_PARENTHESIS) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.INTEGER_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 159
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def decl_typ(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_typContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MiniGoParser.VAR)
            self.state = 162
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 163
                self.decl_typ()
                pass

            elif la_ == 2:
                self.state = 164
                self.match(MiniGoParser.EQUAL)
                self.state = 165
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 166
                self.decl_typ()
                self.state = 167
                self.match(MiniGoParser.EQUAL)
                self.state = 168
                self.expr(0)
                pass


            self.state = 172
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MiniGoParser.CONST)
            self.state = 175
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 176
            self.match(MiniGoParser.EQUAL)
            self.state = 177
            self.expr(0)
            self.state = 178
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_typ" ):
                return visitor.visitDecl_typ(self)
            else:
                return visitor.visitChildren(self)




    def decl_typ(self):

        localctx = MiniGoParser.Decl_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_typ)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.array_type()
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


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.lhs()
            self.state = 186
            self.assign_operator()
            self.state = 187
            self.expr(0)
            self.state = 188
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lhs)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.struct_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def only_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Only_if_stmtContext,0)


        def else_if_list(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_listContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.only_if_stmt()
            self.state = 196
            self.else_if_list()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 197
                self.else_stmt()


            self.state = 200
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Only_if_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_only_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOnly_if_stmt" ):
                return visitor.visitOnly_if_stmt(self)
            else:
                return visitor.visitChildren(self)




    def only_if_stmt(self):

        localctx = MiniGoParser.Only_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_only_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MiniGoParser.IF)
            self.state = 203
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 204
            self.expr(0)
            self.state = 205
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 206
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IF)
            else:
                return self.getToken(MiniGoParser.IF, i)

        def OPEN_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.OPEN_PARENTHESIS, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def CLOSE_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_list" ):
                return visitor.visitElse_if_list(self)
            else:
                return visitor.visitChildren(self)




    def else_if_list(self):

        localctx = MiniGoParser.Else_if_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_else_if_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 208
                    self.match(MiniGoParser.ELSE)
                    self.state = 209
                    self.match(MiniGoParser.IF)
                    self.state = 210
                    self.match(MiniGoParser.OPEN_PARENTHESIS)
                    self.state = 211
                    self.expr(0)
                    self.state = 212
                    self.match(MiniGoParser.CLOSE_PARENTHESIS)
                    self.state = 213
                    self.block() 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MiniGoParser.ELSE)
            self.state = 221
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_for_loopContext,0)


        def for_loop_initial(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_initialContext,0)


        def for_loop_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_stmt)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.basic_for_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.for_loop_initial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.for_loop_range()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for_loop" ):
                return visitor.visitBasic_for_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_for_loop(self):

        localctx = MiniGoParser.Basic_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_basic_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MiniGoParser.FOR)
            self.state = 229
            self.condition()
            self.state = 230
            self.block()
            self.state = 231
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_initialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def initialization(self):
            return self.getTypedRuleContext(MiniGoParser.InitializationContext,0)


        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_initial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_initial" ):
                return visitor.visitFor_loop_initial(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_initial(self):

        localctx = MiniGoParser.For_loop_initialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_loop_initial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(MiniGoParser.FOR)
            self.state = 236
            self.initialization()
            self.state = 237
            self.condition()
            self.state = 238
            self.match(MiniGoParser.SEMICOLON)
            self.state = 239
            self.update()
            self.state = 240
            self.block()
            self.state = 241
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def decl_typ(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_typContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_initialization)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 244
                self.assign_operator()
                self.state = 245
                self.expr(0)
                self.state = 246
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(MiniGoParser.VAR)
                self.state = 249
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 256
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.EQUAL]:
                    self.state = 250
                    self.match(MiniGoParser.EQUAL)
                    self.state = 251
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.OPEN_BRACKET, MiniGoParser.IDENTIFIER]:
                    self.state = 252
                    self.decl_typ()
                    self.state = 253
                    self.match(MiniGoParser.EQUAL)
                    self.state = 254
                    self.expr(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 258
                self.match(MiniGoParser.SEMICOLON)
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


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 263
            self.assign_operator()
            self.state = 264
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGNMENT_SIGN(self):
            return self.getToken(MiniGoParser.ASSIGNMENT_SIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_range" ):
                return visitor.visitFor_loop_range(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_range(self):

        localctx = MiniGoParser.For_loop_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_loop_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.FOR)
            self.state = 267
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 268
            self.match(MiniGoParser.COMMA)
            self.state = 269
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 270
            self.match(MiniGoParser.ASSIGNMENT_SIGN)
            self.state = 271
            self.match(MiniGoParser.RANGE)
            self.state = 272
            self.expr(0)
            self.state = 273
            self.block()
            self.state = 274
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MiniGoParser.BREAK)
            self.state = 277
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MiniGoParser.CONTINUE)
            self.state = 280
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 282
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 283
                self.method_call()
                pass


            self.state = 286
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(MiniGoParser.RETURN)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.OPEN_PARENTHESIS) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.INTEGER_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 289
                self.expr(0)


            self.state = 292
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MiniGoParser.FUNC)
            self.state = 295
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 296
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 297
                self.param_list()


            self.state = 300
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 301
                self.typ()


            self.state = 304
            self.block()
            self.state = 305
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 308
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.OPEN_PARENTHESIS) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.INTEGER_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 309
                self.argument_list()


            self.state = 312
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = MiniGoParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.expr(0)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 315
                self.match(MiniGoParser.COMMA)
                self.state = 316
                self.expr(0)
                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def OPEN_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.OPEN_PARENTHESIS, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def CLOSE_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(MiniGoParser.FUNC)
            self.state = 323
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 324
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 325
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 326
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 327
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 328
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 329
                self.param_list()


            self.state = 332
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 333
                self.typ()


            self.state = 336
            self.block()
            self.state = 337
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr6(0)
            self.state = 340
            self.match(MiniGoParser.DOT)
            self.state = 341
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
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


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_typ)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.array_type()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    self.match(MiniGoParser.OR)
                    self.state = 355
                    self.expr1(0) 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    self.match(MiniGoParser.AND)
                    self.state = 366
                    self.expr2(0) 
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def relational_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 375
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 376
                    self.relational_operator()
                    self.state = 377
                    self.expr3(0) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def arith_low_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Arith_low_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    self.arith_low_operator()
                    self.state = 389
                    self.expr4(0) 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def arith_high_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Arith_high_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 399
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 400
                    self.arith_high_operator()
                    self.state = 401
                    self.expr5() 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 409
                self.expr5()
                pass
            elif token in [MiniGoParser.OPEN_PARENTHESIS, MiniGoParser.OPEN_BRACKET, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.expr6(0)
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def OPEN_BRACKET(self):
            return self.getToken(MiniGoParser.OPEN_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MiniGoParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 426
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 424
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 416
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 417
                        self.match(MiniGoParser.DOT)
                        self.state = 418
                        self.operand()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 419
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 420
                        self.match(MiniGoParser.OPEN_BRACKET)
                        self.state = 421
                        self.expr(0)
                        self.state = 422
                        self.match(MiniGoParser.CLOSE_BRACKET)
                        pass

             
                self.state = 428
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = MiniGoParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 430
            self.expr(0)
            self.state = 431
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Sub_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_operand)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 435
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 437
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 438
                self.array_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 439
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 440
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 441
                self.func_call()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 442
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_box(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_boxContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_type)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.array_literal_box()
                self.state = 446
                self.array_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.array_literal_box()
                self.state = 452
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 449
                    self.primitive_type()
                    pass
                elif token in [MiniGoParser.IDENTIFIER]:
                    self.state = 450
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                elif token in [MiniGoParser.OPEN_BRACKET]:
                    self.state = 451
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_boxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(MiniGoParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(MiniGoParser.CLOSE_BRACKET, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal_box

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_box" ):
                return visitor.visitArray_literal_box(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_box(self):

        localctx = MiniGoParser.Array_literal_boxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_literal_box)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(MiniGoParser.OPEN_BRACKET)
            self.state = 457
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.INTEGER_LITERAL or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 458
            self.match(MiniGoParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_access_boxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(MiniGoParser.OPEN_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MiniGoParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access_box

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access_box" ):
                return visitor.visitArray_access_box(self)
            else:
                return visitor.visitChildren(self)




    def array_access_box(self):

        localctx = MiniGoParser.Array_access_boxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_access_box)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.OPEN_BRACKET)
            self.state = 461
            self.expr(0)
            self.state = 462
            self.match(MiniGoParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def array_ele_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_ele_listContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_ele_listContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.array_type()
            self.state = 465
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 467 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 466
                self.array_ele_list()
                self.state = 469 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.OPEN_BRACE) | (1 << MiniGoParser.INTEGER_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 471
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_eleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_eleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_ele_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_ele_list" ):
                return visitor.visitArray_ele_list(self)
            else:
                return visitor.visitChildren(self)




    def array_ele_list(self):

        localctx = MiniGoParser.Array_ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.array_ele()
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 474
                self.match(MiniGoParser.COMMA)
                self.state = 475
                self.array_ele()
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def short_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Short_array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_ele" ):
                return visitor.visitArray_ele(self)
            else:
                return visitor.visitChildren(self)




    def array_ele(self):

        localctx = MiniGoParser.Array_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array_ele)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 485
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 486
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 487
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 488
                self.short_array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def array_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_ele_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_short_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShort_array_literal" ):
                return visitor.visitShort_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def short_array_literal(self):

        localctx = MiniGoParser.Short_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_short_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 492
            self.array_ele_list()
            self.state = 493
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def array_access_box(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_access_boxContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_access_boxContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.expr6(0)
            self.state = 497 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 496
                self.array_access_box()
                self.state = 499 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.OPEN_BRACKET):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_struct_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.TYPE)
            self.state = 502
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 503
            self.match(MiniGoParser.STRUCT)
            self.state = 504
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 506 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 505
                self.struct_field()
                self.state = 508 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

            self.state = 510
            self.match(MiniGoParser.CLOSE_BRACE)
            self.state = 511
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 514
            self.typ()
            self.state = 515
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def struct_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_ele_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 518
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 519
                self.struct_ele_list()


            self.state = 522
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_eleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_eleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ele_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ele_list" ):
                return visitor.visitStruct_ele_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_ele_list(self):

        localctx = MiniGoParser.Struct_ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_struct_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.struct_ele()
            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 525
                self.match(MiniGoParser.COMMA)
                self.state = 526
                self.struct_ele()
                self.state = 531
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ele" ):
                return visitor.visitStruct_ele(self)
            else:
                return visitor.visitChildren(self)




    def struct_ele(self):

        localctx = MiniGoParser.Struct_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_struct_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 533
            self.match(MiniGoParser.COLON)
            self.state = 534
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.expr6(0)
            self.state = 537
            self.match(MiniGoParser.DOT)
            self.state = 538
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def interface_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_methodContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(MiniGoParser.TYPE)
            self.state = 541
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 542
            self.match(MiniGoParser.INTERFACE)
            self.state = 543
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 545 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 544
                self.interface_method()
                self.state = 547 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

            self.state = 549
            self.match(MiniGoParser.CLOSE_BRACE)
            self.state = 550
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 553
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 555
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 554
                self.param_list()


            self.state = 557
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 559
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 558
                self.typ()


            self.state = 561
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Param_declContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Param_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.param_decl()
            self.state = 568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 564
                self.match(MiniGoParser.COMMA)
                self.state = 565
                self.param_decl()
                self.state = 570
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = MiniGoParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 572
                self.match(MiniGoParser.COMMA)
                self.state = 573
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 579
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_high_operatorContext(ParserRuleContext):
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
            return MiniGoParser.RULE_arith_high_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_high_operator" ):
                return visitor.visitArith_high_operator(self)
            else:
                return visitor.visitChildren(self)




    def arith_high_operator(self):

        localctx = MiniGoParser.Arith_high_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arith_high_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
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


    class Arith_low_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arith_low_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_low_operator" ):
                return visitor.visitArith_low_operator(self)
            else:
                return visitor.visitChildren(self)




    def arith_low_operator(self):

        localctx = MiniGoParser.Arith_low_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arith_low_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
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


    class Relational_operatorContext(ParserRuleContext):
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
            return MiniGoParser.RULE_relational_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = MiniGoParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
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


    class Assign_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT_SIGN(self):
            return self.getToken(MiniGoParser.ASSIGNMENT_SIGN, 0)

        def SHORT_ADD(self):
            return self.getToken(MiniGoParser.SHORT_ADD, 0)

        def SHORT_SUB(self):
            return self.getToken(MiniGoParser.SHORT_SUB, 0)

        def SHORT_MULTIPLY(self):
            return self.getToken(MiniGoParser.SHORT_MULTIPLY, 0)

        def SHORT_DIVIDE(self):
            return self.getToken(MiniGoParser.SHORT_DIVIDE, 0)

        def SHORT_REMAIN(self):
            return self.getToken(MiniGoParser.SHORT_REMAIN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_operator" ):
                return visitor.visitAssign_operator(self)
            else:
                return visitor.visitChildren(self)




    def assign_operator(self):

        localctx = MiniGoParser.Assign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_assign_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGNMENT_SIGN) | (1 << MiniGoParser.SHORT_ADD) | (1 << MiniGoParser.SHORT_SUB) | (1 << MiniGoParser.SHORT_MULTIPLY) | (1 << MiniGoParser.SHORT_DIVIDE) | (1 << MiniGoParser.SHORT_REMAIN))) != 0)):
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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(MiniGoParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(MiniGoParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_comment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = MiniGoParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SINGLE_LINE_COMMENT or _la==MiniGoParser.MULTI_LINE_COMMENT):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr_sempred
        self._predicates[32] = self.expr1_sempred
        self._predicates[33] = self.expr2_sempred
        self._predicates[34] = self.expr3_sempred
        self._predicates[35] = self.expr4_sempred
        self._predicates[37] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




