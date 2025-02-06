import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abc""","""abc,<EOF>""",101))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("""ab?sVN""","""ab,ErrorToken ?""",102))

    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("""var abc int ;""","""var,abc,int,;,<EOF>""",103))

    def test104(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    


    def test201(self):
        self.assertTrue(TestLexer.checkLexeme("""func main() {};""","""func,main,(,),{,},;,<EOF>""",201))

    def test202(self):
        self.assertTrue(TestLexer.checkLexeme("""func foo () {};""","""func,foo,(,),{,},;,<EOF>""",202))

    def test203(self):
        self.assertTrue(TestLexer.checkLexeme("""func main({};""","""func,main,(,UncloseString (""",203))

    def test204(self):
        self.assertTrue(TestLexer.checkLexeme("""var int;""","""var,int,;,<EOF>""",204))
    
    def test205(self):
        self.assertTrue(TestLexer.checkLexeme("""var i ;""","""var,i,;,<EOF>""",205))