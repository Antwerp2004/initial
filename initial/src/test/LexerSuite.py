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
        inp = """ "black \\&Clover"? """
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
        out = "one_Piece,ErrorToken !"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_06(self):
        inp = """ "no.ra\\ga.mi" """
        out = "Illegal escape in string: no.ra\\g"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_07(self):
        inp = """ "Kaguya-sama: '\"Love is War'\"" """
        out = "Kaguya-sama: '\"Love is War'\",<EOF>"
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
        inp = """ "rurouni |kenshin\\" """
        out = """Unclosed string: rurouni |kenshin\" """
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