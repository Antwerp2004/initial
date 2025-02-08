import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    lexerTest = 99
      
    ##### String-literal testcases #####
    def test_lexer_00(self):
        inp = """ "" """
        out = ",<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_01(self):
        inp = """ "\n" """
        out = "Unclosed string: "
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_02(self):
        inp = """ "black \&Clover"? """
        out = "Illegal escape in string: black \&"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_03(self):
        inp = """ "Tokyo\tGhoul\\n,<EOF>" """
        out = "Tokyo\tGhoul\\n,<EOF>,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_04(self):
        inp = """ "kaiju'no\\'8" """
        out = "Illegal escape in string: kaiju'no\\'"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_05(self):
        inp = """ "one_Piece"! """
        out = "one_Piece,!,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_06(self):
        inp = """ "no.ra\\ga.mi" """
        out = "Illegal escape in string: no.ra\\g"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_07(self):
        inp = """ "Kaguya-sama: '\"Love is War'\"" """
        out = "Kaguya-sama: ',Love,is,War,ErrorToken '"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_08(self):
        inp = """ "dr.Stone\\r\\b  \\n\\t\\f' " """
        out = "Illegal escape in string: dr.Stone\\r\\b"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_09(self):
        inp = """ "Fate/stay night: \nHeaven\'s Feel" """
        out = "Unclosed string: Fate/stay night: "
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_10(self):
        inp = """ "gintama'" """
        out = "gintama',<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_11(self):
        inp = """ "spy\\'"x family" """
        out = "Illegal escape in string: spy\\'"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_12(self):
        inp = """ Magi" """
        out = "Magi,Unclosed string:  "
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_13(self):
        inp = """ "sousou,no,'\\\\frieren ~!@#$%^&*()_+[;]" """
        out = "sousou,no,'\\\\frieren ~!@#$%^&*()_+[;],<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_14(self):
        inp = """ "oshi\' no\\ko" """
        out = "Illegal escape in string: oshi\' no\\k"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_15(self):
        inp = """ "sakamoto" days'" """
        out = "sakamoto,days,ErrorToken '"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_16(self):
        inp = """ "81194 + 63194 + 22194" """
        out = "81194 + 63194 + 22194,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_17(self):
        inp = """ "func main() return 1" """
        out = "func main() return 1,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_18(self):
        inp = """ ""Kimetsu=no" yaiba" """
        out = ",Kimetsu,=,no, yaiba,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_19(self):
        inp = """ "Dark^Gathering """
        out = "Unclosed string: Dark^Gathering "
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_20(self):
        inp = """ "rurouni |kenshin\"abc\"bb" """
        out = """rurouni |kenshin,abc,bb,<EOF>"""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_21(self):
        inp = """ "'" """
        out = "',<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_22(self):
        inp = """ "{Kusuriya<h>no`<\\\\h>hitorigoto}" """
        out = "{Kusuriya<h>no`<\\\\h>hitorigoto},<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_23(self):
        inp = """ "nanatsu.\''no?taizai" """
        out = "nanatsu.\''no?taizai,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_24(self):
        inp = """ "''bleach'''\\'" """
        out = "Illegal escape in string: ''bleach'''\\'"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    
    ##### Number-literal testcases #####

    def test_lexer_25(self):
        inp = "16"
        out = "16,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_26(self):
        inp = "-195863456123157985133216654899513121564679878562133156467913412315479797797977999133"
        out = "-,195863456123157985133216654899513121564679878562133156467913412315479797797977999133,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_27(self):
        inp = "61.4598"
        out = "61.4598,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_28(self):
        inp = "-61.4598e4566331125"
        out = "-,61.4598e4566331125,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_29(self):
        inp = "0.895e-1246"
        out = "0.895e-1246,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_30(self):
        inp = "3E-4165"
        out = "3,E,-,4165,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_31(self):
        inp = "0.e213967"
        out = "0.e213967,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_32(self):
        inp = ".E9631892"
        out = ".,E9631892,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_33(self):
        inp = "00001e136.003"
        out = "0,0,0,0,1,e136,.,0,0,3,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_34(self):
        inp = "000.00e+00781"
        out = "000.00e+00781,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_34(self):
        inp = "0"
        out = "0,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_35(self):
        inp = "23e"
        out = "23,e,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_36(self):
        inp = "1549f-478"
        out = "1549,f,-,478,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_37(self):
        inp = "41.83E2e+657"
        out = "41.83E2,e,+,657,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_38(self):
        inp = "e4159"
        out = "e4159,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_39(self):
        inp = "1235.eE-61.248"
        out = "1235.,eE,-,61.248,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))


    ##### Syntax testcases #####
    def test_lexer_40(self):
        inp = \
            """[2][3]int{{1, 2, 3}, {4, 5, 6}}"""
        out = "<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))