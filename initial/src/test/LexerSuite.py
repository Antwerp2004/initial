import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    lexerTest = 99
      
    ##### String-literal testcases #####
    def test_lexer_00(self):
        inp = "\"\""
        out = ",<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_01(self):
        inp = "\"\n\""
        out = ",<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_02(self):
        inp = "\"black \\&Clover\"?"
        out = "Illegal Escape In String: black \&"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_03(self):
        inp = "\"Tokyo\tGhoul\\n,<EOF>\""
        out = "Tokyo\tGhoul\\n,<EOF>,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_04(self):
        inp = "\"kaiju'no\\'8\""
        out = "kaiju'no\\'8,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_05(self):
        inp = "\"one_Piece\"!"
        out = "one_Piece,Error Token !"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_06(self):
        inp = "\"no.ra\\ga.mi\""
        out = "Illegal Escape In String: no.ra\\g"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_07(self):
        inp = "\"Kaguya-sama: '\"Love is War'\"\""
        out = "Kaguya-sama: '\"Love is War'\",<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_08(self):
        inp = "\"dr.Stone\\r\\b  \\n\\t\\f' \""
        out = "dr.Stone\\r\\b  \\n\\t\\f' ,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_09(self):
        inp = "\"Fate/stay night: \nHeaven\'s Feel\""
        out = "Unclosed String: Fate/stay night: "
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_10(self):
        inp = "\"gintama'\""
        out = "Unclosed String: gintama'\""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_11(self):
        inp = "\"spy\\'\"x family\""
        out = "spy\\',x,family,Unclosed String: "
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_12(self):
        inp = "Magi\""
        out = "Magi,Unclosed String: "
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_13(self):
        inp = "\"sousou,no,'\\\\frieren ~!@#$%^&*()_+[;]\""
        out = "sousou,no,'\\\\frieren ~!@#$%^&*()_+[;],<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_14(self):
        inp = "\"oshi\' no\\ko\""
        out = "Illegal Escape In String: oshi\' no\\k"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_15(self):
        inp = "\"sakamoto\" days'\""
        out = "sakamoto,days,Error Token '"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_16(self):
        inp = "\"81194 + 63194 + 22194\""
        out = "81194 + 63194 + 22194,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_17(self):
        inp = "\"func main() return 1\""
        out = "func main() return 1,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_18(self):
        inp = "\"\"Kimetsu=no\" yaiba\""
        out = ",Kimetsu,=,no, yaiba,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_19(self):
        inp = "\"Dark^Gathering"
        out = "Unclosed String: Dark^Gathering"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_20(self):
        inp = "\"rurouni |kenshin\\\""
        out = "Illegal Escape In String: rurouni |kenshin\\\""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_21(self):
        inp = "\"'\""
        out = "Unclosed String: '\""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_22(self):
        inp = "\"{Kusuriya<h>no`<\\\\h>hitorigoto}\""
        out = "{Kusuriya<h>no`<\\\\h>hitorigoto},<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_23(self):
        inp = "\"nanatsu.\''no?taizai\""
        out = "nanatsu.\''no?taizai,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    def test_lexer_24(self):
        inp = "\"''bleach'''\\'\""
        out = "''bleach'''\\',<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))