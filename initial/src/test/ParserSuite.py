import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    parserTest = 199

    def test_parser_00(self):
        input = """ [2][3]int{{1, 2, 3}, {4, 5, 6}} """
        expect = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(input,expect,ParserSuite.parserTest))

    # def test_parser_01(self):
    #     input = """func foo () {
    #     };"""
    #     expect = "successful"
    #     ParserSuite.parserTest += 1
    #     self.assertTrue(TestParser.checkParser(input,expect,ParserSuite.parserTest))
    
    # def test_parser_02(self):
    #     input = """func main({};"""
    #     expect = "Error on line 1 col 11: {"
    #     ParserSuite.parserTest += 1
    #     self.assertTrue(TestParser.checkParser(input,expect,ParserSuite.parserTest))

    # def test_parser_03(self):
    #     input = """var int;"""
    #     expect = "Error on line 1 col 5: int"
    #     ParserSuite.parserTest += 1
    #     self.assertTrue(TestParser.checkParser(input,expect,ParserSuite.parserTest))

    # def test_parser_04(self):
    #     input = """var i ;"""
    #     expect = "Error on line 1 col 7: ;"
    #     ParserSuite.parserTest += 1
    #     self.assertTrue(TestParser.checkParser(input,expect,ParserSuite.parserTest))
    