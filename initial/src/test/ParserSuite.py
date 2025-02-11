import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    parserTest = 249

    def test_parser_50(self):
        inp = \
            """ for i := 0; i < 10; i += 1 {
    if (x % i = 0) {return false;}
}
"""
        out = "Error on line 1 col 2: for"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_51(self):
        inp = \
            """func main () {return 1;}

"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_52(self):
        inp = \
            """for i; i <= x / 2; i += 1
{
    if (x % i = 0) {return false
    }
}
"""
        out = "Error on line 1 col 1: for"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_53(self):
        inp = \
            """func main(x string, y float)  {
}
"""
        out = "Error on line 2 col 1: }"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_54(self):
        inp = \
            """func foo(str string) boolean
writeString(str)
var x = 7 + (t - false)
"""
        out = "Error on line 1 col 29: ;"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_55(self):
        inp = \
            """func bar( arr int,,){
x[2][8] = [3][1,2,\"3\"] + [2][4,\"5\",6]
}"""
        out = "Error on line 1 col 19: ,"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_56(self):
        inp = \
            """
func min(int a, string b){  
if (x <= false){
        main(a,2,\"b\")
    }
for i; i <= x / 2; i += 1{ 

    loop1(arr[a(b)][b(a)])
    loop2(arr[a(b)],b[2])
}

}
"""
        out = "Error on line 2 col 10: int"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_57(self):
        inp = \
            """func min(a int, b string){ 
if (boolean) {
doSomething(a,2,\"b\");}
elif (abc > \"abc\") {doSomethingElif(b,true,foo(x,2))
}
else doSomethingElse(doSomethingElse,foo[3.2,3])
}

"""
        out = "Error on line 2 col 5: boolean"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_58(self):
        inp = \
            """//func max(a int, b number)
/* begin
## Comment 1
##if (x == 6) else {doSomething();}
## Comment 2
*/
"""
        out = "Error on line 7 col 1: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_59(self):
        inp = \
            """func bar(arr float, b boolean) {
x[2][8] := foo(1,2,\"abcd\",154/4)
var x int= readString()"""
        out = "Error on line 3 col 24: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_60(self):
        inp = \
            """const GREETING string = "Hello, World!"

var message string

func main() {
    message = GREETING
    println(message)
}
"""
        out = "Error on line 1 col 16: string"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_61(self):
        inp = \
            """var a int = 10
var b int = 5
var result int

func main() {
    result = a + b*2 - b/2
    println(result)
}
"""
        out = "Error on line 6 col 12: ="
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_62(self):
        inp = \
            """var x int = 7

func main() {
    if (x > 5) {
        println("x is greater than 5")
    } else {
        println("x is not greater than 5")
    }
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_63(self):
        inp = \
            """var numbers [5]int = [5]{1, 2, 3, 4, 5}

func main() {
    for index, value := range numbers {
        println(index, value)
    }
}
"""
        out = "Error on line 1 col 25: {"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_64(self):
        inp = \
            """type Point struct {
    x int
    y int
}

var p Point

func main() {
    p.x = 10
    p.y = 20
    println(p.x, p.y)
}"""
        out = "Error on line 3 col 5: y"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_65(self):
        inp = \
            """
type Printer interface {
    print(message string)
}

func main() {
    // No implementation here to test just declaration
}

"""
        out = "Error on line 8 col 1: }"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_66(self):
        inp = \
            """type Rectangle struct {
    width int
    height int
}

func (r Rectangle) area() int {
    return r.width * r.height
}

var rect Rectangle

func main() {
    rect.width = 5
    rect.height = 10
    println(rect.area())
}
"""
        out = "Error on line 3 col 5: height"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_67(self):
        inp = \
            """func calculate(a int, b int) (int, int) {  // Invalid: Multiple return values
    return a + b, a - b
}

func main() {
    var sum, diff int
    sum, diff = calculate(10, 5)
    println(sum, diff)
}
"""
        out = "Error on line 1 col 30: ("
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_68(self):
        inp = \
            """var age int = 25
var isStudent bool = false

func main() {
    if (age < 30) {
        if (!isStudent) {
            println("Young professional")
        } else {
            println("Young student")
        }
    } else {
        println("Experienced")
    }
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_69(self):
        inp = \
            """
func main() {
    for i := 0; i < 10; i += 1 {
        if (i % 3 == 0) {
            continue  // Skip multiples of 3
        }
        if (i > 7) {
            break     // Exit loop if i is greater than 7
        }
        println(i)
    }
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_70(self):
        inp = \
            """
type Circle struct {
    radius int
}

var circles [3]Circle

func main() {
    circles[0].radius = 5
    circles[1].radius = 7
    circles[2].radius = 9

    for _, c := range circles {
        println(c.radius)
    }
}
"""
        out = "Error on line 9 col 15: ."
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_71(self):
        inp = \
            """func main() {
    for i := 0; i < 3; i += 1 {
        for j := 0; j < 3; j += 1 {
            println(i, j)
        }
    }
}"""
        out = "Error on line 7 col 2: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_72(self):
        inp = \
            """/*
    This is a multi-line comment.
    It spans multiple lines.
*/

// This is a single-line comment.

var   x  int  =   10;  //  Declaration with extra whitespace

func main()  {
    //  More comments inside the function
    println ( x  ) ;
}"""
        out = "Error on line 13 col 2: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_73(self):
        inp = \
            """var maxInt int = 2147483647  // Maximum 32-bit integer (adjust if needed)

func main() {
    var overflow int = maxInt + 1
    println(overflow)  //  What happens when we overflow?
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_74(self):
        inp = \
            """ 
var message string = "This string contains a newline\nand a tab\t."

func main() {
    println(message)
}
"""
        out = """"This string contains a newline\n"""
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_75(self):
        inp = \
            """ 
var x int = 5@  // Invalid character @

func main() {
    println(x)
}
"""
        out = "@"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_76(self):
        inp = \
            """var message string = "This string is not terminated

func main() {
    println(message)
}
"""
        out = """"This string is not terminated\n"""
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_77(self):
        inp = \
            """ 
var x int = 5
var y int = 10 // Missing semicolon or newline here
func main() {
    println(x + y)
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_78(self):
        inp = \
            """ var x int = 5

func main() {
    var x string = "hello" // x redeclared in the same scope
    println(x)
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_79(self):
        inp = \
            """ var globalVar int = 20

func myFunction() {
    var localVar int = 10
    println(globalVar + localVar)
}

func main() {
    myFunction()
    println(globalVar) // Access global variable from main
    //println(localVar) // Error: localVar is not defined in main
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_80(self):
        inp = \
            """ 
var a int = 10
var b int = 5
var c string = "hello"

func main() {
    if ((a > 5 && b < 10) || c == "world") {
        if (a + b == 15) {
            println("Condition met")
        } else {
            println("Inner condition failed")
        }
    } else {
        println("Outer condition failed")
    }
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_81(self):
        inp = \
            """var x int
var y int
var z int

func main() {
    x, y, z = 1, 2 + 3, 4 * 5 - 1 // Note multi-assignment is illegal in MiniGo
    println(x, y, z) // Illegal because it's not a function
}"""
        out = "Error on line 6 col 6: ,"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_82(self):
        inp = \
            """func main() {
    for i := 0; i < 20; i+= 1 {
        if (i % 5 == 0) {
            continue // Skip multiples of 5
        }
        if (i > 12 && i < 15) {
            break    // Exit if between 13 and 14
        }
        println(i)
    }
}"""
        out = "Error on line 11 col 2: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_83(self):
        inp = \
            """type Person struct {
    name string
    age int
}

var p Person

func main() {
    p.name = "Alice"
    p.age = 30
    println(p.name, p.age)
    var message string = p.name + " is " + p.age + " years old" // Concatenation with integer will cause a type error

}
"""
        out = "Error on line 3 col 5: age"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_84(self):
        inp = \
            """var data [4]int = {10, 20, 30, 40}

func main() {
    for index, value := range data {
        println(index * value)
    }
    // data[index] =  // error: index not defined outside loop
}
"""
        out = "Error on line 1 col 19: {"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_85(self):
        inp = \
            """
func findValue(arr [5]int, target int) int {
    for i := 0; i < 5; i+=1 {
        if (arr[i] == target) {
            return i // Return index if found
        }
    }
    return -1  // Return -1 if not found
}

var numbers [5]int = {1, 2, 3, 4, 5}

func main() {
    var index int = findValue(numbers, 3)
    println(index)
}
"""
        out = "Error on line 11 col 22: {"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_86(self):
        inp = \
            """var x int = 10
var y string = "hello"
var z bool = true
const PI float = 3.14

func main() {
    println(x, y, z, PI)
}
"""
        out = "Error on line 4 col 10: float"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_87(self):
        inp = \
            """type Address struct {
    street string
    city string
}

type Person struct {
    name string
    address Address
}

var p Person

func main() {
    p.name = "Bob"
    p.address.street = "123 Main St"
    p.address.city = "Anytown"
    println(p.name, p.address.street, p.address.city)
}
"""
        out = "Error on line 3 col 5: city"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_88(self):
        inp = \
            """func isEven(n int) bool {
    return n % 2 == 0
}

var num int = 8

func main() {
    if (isEven(num)) {
        println("Even")
    } else {
        println("Odd")
    }
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_89(self):
        inp = \
            """var a int = 5
var b int = 10
var result bool

func main() {
    result = a + b > 12 && a * b < 60 // Will cause a type error because an int is compared to a bool
    println(result)
}
"""
        out = "Error on line 6 col 12: ="
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_90(self):
        inp = \
            """
func main() {
    for i = 0; i < 10; i++ { 
        println(i) 
    }
}
"""
        out = "Error on line 3 col 11: ="
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_91(self):
        inp = \
            """
var x int = 10

func main() {
    if (x > 5)
        println("x > 5")  // Missing braces - should cause an error
    else
        println("x <= 5")
}
"""
        out = "Error on line 5 col 15: ;"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_92(self):
        inp = \
            """func main() {
    println(undefinedVariable) // Should cause error: undefinedVariable not declared
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_93(self):
        inp = \
            """func add(x int, y int) {  // Missing return type
    return x + y  // Type error
}

func main() {
   var result int = add(5,3)
   println(result)
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_94(self):
        inp = \
            """
var a bool = true
var b bool = false
var c bool = true

func main() {
    var result bool = (a && b) || (!c && a)
    println(result)
}"""
        out = "Error on line 9 col 2: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_95(self):
        inp = \
            """


var numbers [3]int = {1, "hello", 3} // "hello" is not an int. Error expected.

func main() {
    println(numbers[0], numbers[1], numbers[2])
}
"""
        out = "Error on line 4 col 22: {"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_96(self):
        inp = \
            """var notAnArray int = 5;

func main() {
    for index, value := range notAnArray {
        println(index, value);
    }
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_97(self):
        inp = \
            """func someOtherFunction() {
    println("This program does not have a main function")
}
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_98(self):
        inp = \
            """type MyInterface interface {
	doSomething()
}
type MyType struct{}

func (m MyType) doSomething() {
	println("Hello")
}

func main() {
	var i MyInterface
	var m MyType
	i = m

	//i.doSomething()// Calling method doSomething of MyInterface

}
"""
        out = "Error on line 7 col 2: println"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

    def test_parser_99(self):
        inp = \
            """type MyType struct {
	Name string
}

func (mt MyType) someMethod() string {
	for i := 0; i < 10; i++ {
		if i == 5 {
			return "Found 5!"
		}
	}
	return "Not found"
}

func main() {
	mt := MyType{Name: "Example"}
	result := mt.someMethod()
	println(result)
}"""
        out = "Error on line 6 col 2: for"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))