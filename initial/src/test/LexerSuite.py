import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    lexerTest = 99
      
    def test100(self):
        input = """abcd"""
        output = """abcd,<EOF>"""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(input,output,LexerSuite.lexerTest))

    def test101(self):
        input = """ab?sVN"""
        output = """ab,ErrorToken ?"""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(input,output,LexerSuite.lexerTest))

    def test102(self):
        input = """var abc int ;"""
        output = """var,abc,int,;,<EOF>"""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(input,output,LexerSuite.lexerTest))

    def test103(self):
        input = """func abc ( ) """
        output = """func,abc,(,),<EOF>"""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(input,output,LexerSuite.lexerTest))

    def test104(self):
        input = """4.E-6"""
        output = """4.E-6,<EOF>"""
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(input,output,LexerSuite.lexerTest))


    # def test201(self):
    #     self.assertTrue(TestLexer.checkLexeme("""func main() {};""","""func,main,(,),{,},;,<EOF>""",201))

    # def test202(self):
    #     self.assertTrue(TestLexer.checkLexeme("""func foo () {};""","""func,foo,(,),{,},;,<EOF>""",202))

    # def test203(self):
    #     self.assertTrue(TestLexer.checkLexeme("""func main({};""","""func,main,(,UncloseString (""",203))

    # def test204(self):
    #     self.assertTrue(TestLexer.checkLexeme("""var int;""","""var,int,;,<EOF>""",204))
    
    # def test205(self):
    #     self.assertTrue(TestLexer.checkLexeme("""var i ;""","""var,i,;,<EOF>""",205))