import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    lexerTest = 99
      
    # ##### String-literal testcases #####
    # def test_lexer_00(self):
    #     inp = """ "" """
    #     out = ",<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_01(self):
    #     inp = """ "\n" """
    #     out = "Unclosed string: \""
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_02(self):
    #     inp = """ "white \&Glove"? """
    #     out = "Illegal escape in string: \"white \&"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_03(self):
    #     inp = """ "Gravity\tFalls\\n,<EOF>" """
    #     out = "Gravity\tFalls\\n,<EOF>,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_04(self):
    #     inp = """ "kanji'lang\\'8" """
    #     out = "Illegal escape in string: \"kanji'lang\\'"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_05(self):
    #     inp = """ "The Thing"! """
    #     out = "The Thing,!,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_06(self):
    #     inp = """ "o.ri\\ga.mi" """
    #     out = "Illegal escape in string: \"o.ri\\g"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_07(self):
    #     inp = """ "Kaguya-Hime: '\"Love is Wrong?\"" """
    #     out = "Kaguya-Hime: ',Love,is,Wrong,ErrorToken ?"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_08(self):
    #     inp = """ "dr.Watson\\r\\b  \\n\\t\\f' " """
    #     out = "Illegal escape in string: \"dr.Watson\\r\\b"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_09(self):
    #     inp = """ "Fate/destiny: \nHeaven\'s Hell" """
    #     out = "Unclosed string: \"Fate/destiny: "
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_10(self):
    #     inp = """ "2001'" """
    #     out = "2001',<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_11(self):
    #     inp = """ "akirA\\'" who?" """
    #     out = "Illegal escape in string: \"akirA\\'"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_12(self):
    #     inp = """ Carrie" """
    #     out = "Carrie,Unclosed string: \" "
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_13(self):
    #     inp = """ "soba,no,'\\\\fried ~!@#$%^&*()_+[;]" """
    #     out = "soba,no,'\\\\fried ~!@#$%^&*()_+[;],<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_14(self):
    #     inp = """ "oishi\' no\\ko" """
    #     out = "Illegal escape in string: \"oishi\' no\\k"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_15(self):
    #     inp = """ "Dark" Age'" """
    #     out = "Dark,Age,ErrorToken '"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_16(self):
    #     inp = """ "814 + 94 + 343" """
    #     out = "814 + 94 + 343,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_17(self):
    #     inp = """ "func main() return 0" """
    #     out = "func main() return 0,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_18(self):
    #     inp = """ ""Shingeki==no" Kyojin" """
    #     out = ",Shingeki,==,no, Kyojin,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_19(self):
    #     inp = """ "Fair^Gathering """
    #     out = "Unclosed string: \"Fair^Gathering "
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_20(self):
    #     inp = """ "Wuthering |Heights\"abc\"bb" """
    #     out = """Wuthering |Heights,abc,bb,<EOF>"""
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_21(self):
    #     inp = """ "'" """
    #     out = "',<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_22(self):
    #     inp = """ "{Lord<h>`<\\\\h>of the Rings}" """
    #     out = "{Lord<h>`<\\\\h>of the Rings},<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_23(self):
    #     inp = """ "Gatsby.\''no?" """
    #     out = "Gatsby.\''no?,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_24(self):
    #     inp = """ "''Moby Dick'''\\'" """
    #     out = "Illegal escape in string: \"''Moby Dick'''\\'"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    
    # ##### Number-literal testcases #####

    # def test_lexer_25(self):
    #     inp = "16"
    #     out = "16,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_26(self):
    #     inp = "-19586345612315798513321433092845743757437573974983433412315479797797977999133"
    #     out = "-,19586345612315798513321433092845743757437573974983433412315479797797977999133,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_27(self):
    #     inp = "61.45"
    #     out = "61.45,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_28(self):
    #     inp = "-1.4598e45625"
    #     out = "-,1.4598e45625,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_29(self):
    #     inp = "0.895e-16"
    #     out = "0.895e-16,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_30(self):
    #     inp = "2E-65"
    #     out = "2,E,-,65,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_31(self):
    #     inp = "0.e222967"
    #     out = "0.e222967,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_32(self):
    #     inp = ".E9632"
    #     out = ".,E9632,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_33(self):
    #     inp = "00001e279.003"
    #     out = "0,0,0,0,1,e279,.,0,0,3,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_34(self):
    #     inp = "000.00e+081"
    #     out = "000.00e+081,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_34(self):
    #     inp = "0"
    #     out = "0,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_35(self):
    #     inp = "41e"
    #     out = "41,e,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_36(self):
    #     inp = "19f-478"
    #     out = "19,f,-,478,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_37(self):
    #     inp = "41.3E2e-6"
    #     out = "41.3E2,e,-,6,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_38(self):
    #     inp = "e3223"
    #     out = "e3223,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_39(self):
    #     inp = "15.eE-61.8"
    #     out = "15.,eE,-,61.8,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))


    # ##### Expression testcases #####

    # def test_lexer_40(self):
    #     inp = "12 + 1 = 13"
    #     out = "12,+,1,=,13,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_41(self):
    #     inp = "21 + (31 =52 - x)"
    #     out = "21,+,(,31,=,52,-,x,),<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_42(self):
    #     inp = "24*\t7 +1 && true % int"
    #     out = "24,*,7,+,1,&&,true,%,int,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_43(self):
    #     inp = "x /true/\n2"
    #     out = "x,/,true,/,2,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_44(self):
    #     inp = "main ... \"method\" == main_method"
    #     out = "main,.,.,.,method,==,main_method,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_45(self):
    #     inp = "x > \"y\" < z >= (t <= u) && v ! w"
    #     out = "x,>,y,<,z,>=,(,t,<=,u,),&&,v,!,w,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_46(self):
    #     inp = "_h*i*j+45_"
    #     out = "_h,*,i,*,j,+,45,_,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_47(self):
    #     inp = "\t\n\n<<-- ! 7"
    #     out = "<,<,-,-,!,7,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_48(self):
    #     inp = "arr = arr[0][1] + time(x,const *9)"
    #     out = "arr,=,arr,[,0,],[,1,],+,time,(,x,,,const,*,9,),<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    # def test_lexer_49(self):
    #     inp = "1 + -2(\"var'\")nil"
    #     out = "1,+,-,2,(,var',),nil,<EOF>"
    #     LexerSuite.lexerTest += 1
    #     self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

    ##### Syntax testcases #####

    def test_lexer_50(self):
        inp = \
            """ for i := 0; i < 10; i += 1 {
    if (x % i = 0) {return false;}
}
"""
        out = "for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,x,%,i,=,0,),{,return,false,;,},;,},;,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, 150))

    def test_lexer_51(self):
        inp = \
            """func main () {return 1;}

"""
        out = "func,main,(,),{,return,1,;,},;,<EOF>"
        LexerSuite.lexerTest += 1
        self.assertTrue(TestLexer.checkLexeme(inp, out, 151))

#     def test_lexer_52(self):
#         inp = \
#             """for i until i > x / 2 by 1
# begin
#     if (x % i = 0) return false
# end
# """
#         out = "for,i,until,i,>,x,/,2,by,1,\n,begin,\n,if,(,x,%,i,=,0,),return,false,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_53(self):
#         inp = \
#             """func main(string x, number y)  
# begin
# end
# """
#         out = "func,main,(,string,x,,,number,y,),\n,begin,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_54(self):
#         inp = \
#             """func foo(string str)
# writeString(str)
# var x <- 7 + (t - false)
# end
# """
#         out = "func,foo,(,string,str,),\n,writeString,(,str,),\n,var,x,<-,7,+,(,t,-,false,),\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_55(self):
#         inp = \
#             """func bar(number arr,,)
# begin
# x[2,8] <- [1,2,\"3\"] + [4,\"5\",6]
# end

# """
#         out = "func,bar,(,number,arr,,,,,),\n,begin,\n,x,[,2,,,8,],<-,[,1,,,2,,,3,],+,[,4,,,5,,,6,],\n,end,\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_56(self):
#         inp = \
#             """
# func min(number a, string b)
# begin  
# if (x <= false)
#     begin 
#         main(a,2,\"b\")
#     end
# for id until id >= 4 by 1 

#     loop1(arr[a(b),b(a)])
#     loop2(arr[a(b)],b[2])

# end
# """
#         out = "\n,func,min,(,number,a,,,string,b,),\n,begin,\n,if,(,x,<=,false,),\n,begin,\n,main,(,a,,,2,,,b,),\n,end,\n,for,id,until,id,>=,4,by,1,\n,\n,loop1,(,arr,[,a,(,b,),,,b,(,a,),],),\n,loop2,(,arr,[,a,(,b,),],,,b,[,2,],),\n,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_57(self):
#         inp = \
#             """func min(number a, string b)
# begin   
# if (boolean) 
# doSomething(a,2,\"b\")
# elif (abc > \"abc\") doSomethingElif(b,true,foo(x,2))
# else doSomethingElse(doSomethingElse,foo[3.2,3])
# end

# """
#         out = "func,min,(,number,a,,,string,b,),\n,begin,\n,if,(,boolean,),\n,doSomething,(,a,,,2,,,b,),\n,elif,(,abc,>,abc,),doSomethingElif,(,b,,,true,,,foo,(,x,,,2,),),\n,else,doSomethingElse,(,doSomethingElse,,,foo,[,3.2,,,3,],),\n,end,\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_58(self):
#         inp = \
#             """##func max(number a, number b)
# ## begin
# ## Comment 1
# ##if (x <- 6) else doSomething()
# ## Comment 2
# ##end
# """
#         out = "\n,\n,\n,\n,\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_59(self):
#         inp = \
#             """func bar(number arr,bool b )
# begin
# x[2,8] <- foo([1,2,\"abcd\",154/4])
# number x <- readString()"""
#         out = "func,bar,(,number,arr,,,bool,b,),\n,begin,\n,x,[,2,,,8,],<-,foo,(,[,1,,,2,,,abcd,,,154,/,4,],),\n,number,x,<-,readString,(,),<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_60(self):
#         inp = \
#             """if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"...\") 

# """
#         out = "if,(,(,x,<=,_,and,f,(,z,),),==,true,or,arr,[,1,,,2,,,3,],),if,(,[,-,2,,,3,],==,yx,...,...,),\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_61(self):
#         inp = \
#             """if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"...\") 

# """
#         out = "if,(,(,x,<=,_,and,f,(,z,),),==,true,or,arr,[,1,,,2,,,3,],),if,(,[,-,2,,,3,],==,yx,...,...,),\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_62(self):
#         inp = \
#             """func key(bool b)
# begin
# boolean b <- false
# return b and b
# end
# """
#         out = "func,key,(,bool,b,),\n,begin,\n,boolean,b,<-,false,\n,return,b,and,b,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_63(self):
#         inp = \
#             """_(___,__,_____ ) 
#     __ <- ____ * _ + __ - _(__,___)[_,[__,8],____]
# """
#         out = "_,(,___,,,__,,,_____,),\n,__,<-,____,*,_,+,__,-,_,(,__,,,___,),[,_,,,[,__,,,8,],,,____,],\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_64(self):
#         inp = \
#             """func True(number _) begin       
# if (x <= _ and f(z) == true or _) 
#         falSe(a,2,\"b\")

# end"""
#         out = "func,True,(,number,_,),begin,\n,if,(,x,<=,_,and,f,(,z,),==,true,or,_,),\n,falSe,(,a,,,2,,,b,),\n,\n,end,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_65(self):
#         inp = \
#             """func bar(number arr,bool b ) begin end
# """
#         out = "func,bar,(,number,arr,,,bool,b,),begin,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_66(self):
#         inp = \
#             """number x <- readString(i)
# number x[6] <- [1,2,3]
#     ## Comment
# """
#         out = "number,x,<-,readString,(,i,),\n,number,x,[,6,],<-,[,1,,,2,,,3,],\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_67(self):
#         inp = \
#             """if (x <= false)
#     begin 
#         main(a,2,\"b\")
#     end
# for id until id >= 4 by 1 
# """
#         out = "if,(,x,<=,false,),\n,begin,\n,main,(,a,,,2,,,b,),\n,end,\n,for,id,until,id,>=,4,by,1,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_68(self):
#         inp = \
#             """func _main_() begin
# end
# """
#         out = "func,_main_,(,),begin,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_69(self):
#         inp = \
#             """func True(number _) begin       
# if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"...\") 

# xy<-    xy
#         else if ( a- n < 6) number c

#         var foo <- (54 + 1)*(4 / true)[3]
# """
#         out = "func,True,(,number,_,),begin,\n,if,(,(,x,<=,_,and,f,(,z,),),==,true,or,arr,[,1,,,2,,,3,],),if,(,[,-,2,,,3,],==,yx,...,...,),\n,\n,xy,<-,xy,\n,else,if,(,a,-,n,<,6,),number,c,\n,\n,var,foo,<-,(,54,+,1,),*,(,4,/,true,),[,3,],\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_70(self):
#         inp = \
#             """ string / >= var false dynamic true * {
# """
#         out = "string,/,>=,var,false,dynamic,true,*,Error Token {"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_71(self):
#         inp = \
#             """func main() begin ## This is comment."""
#         out = "func,main,(,),begin,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_72(self):
#         inp = \
#             """arr = arr[0,1] + foo(x,const *7)"""
#         out = "arr,=,arr,[,0,,,1,],+,foo,(,x,,,const,*,7,),<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_73(self):
#         inp = \
#             """string a<-"iP01'\"s\"
# """
#         out = "string,a,<-,iP01'\"s,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_74(self):
#         inp = \
#             """ 
# func main() begin
#     concatenatedString <- "Hello" ... " " ... "World"
#         end
# """
#         out = "\n,func,main,(,),begin,\n,concatenatedString,<-,Hello,..., ,...,World,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_75(self):
#         inp = \
#             """ 
# func main()
# func foo()
# func f()
# func main() return
# func foo() return
# func f() return
# end
# """
#         out = "\n,func,main,(,),\n,func,foo,(,),\n,func,f,(,),\n,func,main,(,),return,\n,func,foo,(,),return,\n,func,f,(,),return,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_76(self):
#         inp = \
#             """ 
# if (a=2) a<--3

# """
#         out = "\n,if,(,a,=,2,),a,<-,-,3,\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_77(self):
#         inp = \
#             """ func main() begin
#     var a<-2 dynamic b<-3
# end
# """
#         out = "func,main,(,),begin,\n,var,a,<-,2,dynamic,b,<-,3,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_78(self):
#         inp = \
#             """ 
# for	until + end	false not	"abcd"
# > for / + ,	* true 20E-3364 ( <= break
# """
#         out = "\n,for,until,+,end,false,not,abcd,\n,>,for,/,+,,,*,true,20E-3364,(,<=,break,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_79(self):
#         inp = \
#             """ 
# [	>= bool	else	func * 82 [ %	return true	break	break begin and
# ]	<=	dynamic
# """
#         out = "\n,[,>=,bool,else,func,*,82,[,%,return,true,break,break,begin,and,\n,],<=,dynamic,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_80(self):
#         inp = \
#             """ 
# foo <- foo[7,[1,[2,[3,[4,5,\"\\n\"],[]]]]] + 7
# return True(true) + i*falSe[]
# """
#         out = "\n,foo,<-,foo,[,7,,,[,1,,,[,2,,,[,3,,,[,4,,,5,,,\\n,],,,[,],],],],],+,7,\n,return,True,(,true,),+,i,*,falSe,[,],\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_81(self):
#         inp = \
#             """\t\n\t\n\t\n\t\n\t"""
#         out = "\n,\n,\n,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_81(self):
#         inp = \
#             """ (-_-) zzZ """
#         out = "(,-,_,-,),zzZ,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_82(self):
#         inp = \
#             """if
# bool	-
# / begin
# not [	if <= begin	if
# != else <
# elif if else <= return and not begin and continue"""
#         out = "if,\n,bool,-,\n,/,begin,\n,not,[,if,<=,begin,if,\n,!=,else,<,\n,elif,if,else,<=,return,and,not,begin,and,continue,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_83(self):
#         inp = \
#             """var fAlse <- (10.89e-1*8..."ahihi")%7"""
#         out = "var,fAlse,<-,(,10.89e-1,*,8.,Error Token ."
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_84(self):
#         inp = \
#             """func main()
#     begin
#     dynamic a <- [-1<3,foo(4),[1,2,3]]
#     end
# """
#         out = "func,main,(,),\n,begin,\n,dynamic,a,<-,[,-,1,<,3,,,foo,(,4,),,,[,1,,,2,,,3,],],\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_85(self):
#         inp = \
#             """
# begin
# number r
# number s
# r <- 2.0
# s <- r * r * 3.14
# """
#         out = "\n,begin,\n,number,r,\n,number,s,\n,r,<-,2.0,\n,s,<-,r,*,r,*,3.14,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_86(self):
#         inp = \
#             """func fOXkhQ6(pW88PnG) \n begin \nstring vZrJM5E <--1774\n end
# """
#         out = "func,fOXkhQ6,(,pW88PnG,),\n,begin,\n,string,vZrJM5E,<-,-,1774,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_87(self):
#         inp = \
#             """var tRue <- true func ahihi() return if (IF) else fALse <- true"""
#         out = "var,tRue,<-,true,func,ahihi,(,),return,if,(,IF,),else,fALse,<-,true,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_88(self):
#         inp = \
#             """
# a = 5
# b = 5%6
# c = x + 5 / 2 / 3
# """
#         out = "\n,a,=,5,\n,b,=,5,%,6,\n,c,=,x,+,5,/,2,/,3,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_89(self):
#         inp = \
#             """var tRue <- true func ahihi() return if (IF) else fALse <- true"""
#         out = "var,tRue,<-,true,func,ahihi,(,),return,if,(,IF,),else,fALse,<-,true,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_90(self):
#         inp = \
#             """
# a[3 + foo(2)] <- a[b[2, 3]] + 4
# """
#         out = "\n,a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_91(self):
#         inp = \
#             """
# a <- 5555
# number b <- -5678
# string c <- "PTMD"
# bool d <- true 
# """
#         out = "\n,a,<-,5555,\n,number,b,<-,-,5678,\n,string,c,<-,PTMD,\n,bool,d,<-,true,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_92(self):
#         inp = \
#             """_variable = 42.5;
# """
#         out = "_variable,=,42.5,Error Token ;"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_93(self):
#         inp = \
#             """boolean isTrue = true()
# """
#         out = "boolean,isTrue,=,true,(,),\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_94(self):
#         inp = \
#             """
# func main()
# begin 
#     ## assign
#     ahihi <- 8989
# end
# """
#         out = "\n,func,main,(,),\n,begin,\n,\n,ahihi,<-,8989,\n,end,\n,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_95(self):
#         inp = \
#             """
# func main() begin number a[5] <- [1, 2, 3, 4, 5] number b[2, 3] <- [[1, 2, 3], [4, 5, 6]] end"""
#         out = "\n,func,main,(,),begin,number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],end,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_96(self):
#         inp = \
#             """dynamic begin end % - [ ( ] ( 09090 ) ) ] |"""
#         out = "dynamic,begin,end,%,-,[,(,],(,09090,),),],Error Token |"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_97(self):
#         inp = \
#             """I wanted to protect everything. But I failed, and that's the sin I bare. So this time, I can't fail to protect them!"""
#         out = "I,wanted,to,protect,everything,Error Token ."
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_98(self):
#         inp = \
#             """\"If the villain doesn't show their evil, it's a problem. To turn knights into heroes, villains are required.\" - Escanor"""
#         out = "If the villain doesn't show their evil, it's a problem. To turn knights into heroes, villains are required.,-,Escanor,<EOF>"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))

#     def test_lexer_99(self):
#         inp = \
#             "'isn''t'"
#         out = "ID,Error Token :"
#         LexerSuite.lexerTest += 1
#         self.assertTrue(TestLexer.checkLexeme(inp, out, LexerSuite.lexerTest))