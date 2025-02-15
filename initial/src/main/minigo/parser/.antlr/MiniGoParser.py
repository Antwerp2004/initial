# Generated from c://Users//HP//Downloads//Principles of Programming Language (CO3005)//Assignment//Assignment 1//initial//initial//src//main//minigo//parser//MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,65,592,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,4,0,128,8,0,11,0,12,0,129,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,140,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,152,8,2,1,3,1,3,4,3,156,8,3,11,3,12,3,157,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,171,8,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,184,8,6,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,3,8,194,8,8,1,9,1,9,1,9,3,9,199,8,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        216,8,11,10,11,12,11,219,9,11,1,12,1,12,1,12,1,13,1,13,1,13,3,13,
        227,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,3,17,257,8,17,1,17,1,17,3,17,261,8,17,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,3,22,285,8,22,1,22,1,22,1,
        23,1,23,3,23,291,8,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,299,8,24,
        1,24,1,24,3,24,303,8,24,1,24,1,24,1,24,1,25,1,25,1,25,3,25,311,8,
        25,1,25,1,25,1,26,1,26,1,26,5,26,318,8,26,10,26,12,26,321,9,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,331,8,27,1,27,1,27,3,
        27,335,8,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,30,1,
        30,1,30,3,30,349,8,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,357,8,31,
        10,31,12,31,360,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,368,8,32,
        10,32,12,32,371,9,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,380,
        8,33,10,33,12,33,383,9,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,5,34,
        392,8,34,10,34,12,34,395,9,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        5,35,404,8,35,10,35,12,35,407,9,35,1,36,1,36,1,36,3,36,412,8,36,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,5,37,425,
        8,37,10,37,12,37,428,9,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,39,1,39,1,39,3,39,444,8,39,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,3,40,453,8,40,3,40,455,8,40,1,41,1,41,1,41,1,41,1,
        42,1,42,1,42,1,42,1,43,1,43,1,43,4,43,468,8,43,11,43,12,43,469,1,
        43,1,43,1,44,1,44,1,44,5,44,477,8,44,10,44,12,44,480,9,44,1,45,1,
        45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,490,8,45,1,46,1,46,1,46,1,
        46,1,47,1,47,4,47,498,8,47,11,47,12,47,499,1,48,1,48,1,48,1,48,1,
        48,4,48,507,8,48,11,48,12,48,508,1,48,1,48,1,48,1,49,1,49,1,49,1,
        49,1,50,1,50,1,50,3,50,521,8,50,1,50,1,50,1,51,1,51,1,51,5,51,528,
        8,51,10,51,12,51,531,9,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,
        1,54,1,54,1,54,1,54,1,54,4,54,546,8,54,11,54,12,54,547,1,54,1,54,
        1,54,1,55,1,55,1,55,3,55,556,8,55,1,55,1,55,3,55,560,8,55,1,55,1,
        55,1,56,1,56,1,56,5,56,567,8,56,10,56,12,56,570,9,56,1,57,1,57,1,
        57,5,57,575,8,57,10,57,12,57,578,9,57,1,57,1,57,1,58,1,58,1,59,1,
        59,1,60,1,60,1,61,1,61,1,62,1,62,1,62,0,6,62,64,66,68,70,74,63,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,
        92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,
        0,8,1,0,11,14,2,0,21,21,33,33,2,0,51,51,62,62,1,0,22,24,1,0,20,21,
        1,0,25,30,1,0,34,39,1,0,1,2,604,0,127,1,0,0,0,2,139,1,0,0,0,4,151,
        1,0,0,0,6,153,1,0,0,0,8,161,1,0,0,0,10,174,1,0,0,0,12,183,1,0,0,
        0,14,185,1,0,0,0,16,193,1,0,0,0,18,195,1,0,0,0,20,202,1,0,0,0,22,
        217,1,0,0,0,24,220,1,0,0,0,26,226,1,0,0,0,28,228,1,0,0,0,30,233,
        1,0,0,0,32,235,1,0,0,0,34,260,1,0,0,0,36,262,1,0,0,0,38,266,1,0,
        0,0,40,276,1,0,0,0,42,279,1,0,0,0,44,284,1,0,0,0,46,288,1,0,0,0,
        48,294,1,0,0,0,50,307,1,0,0,0,52,314,1,0,0,0,54,322,1,0,0,0,56,339,
        1,0,0,0,58,343,1,0,0,0,60,348,1,0,0,0,62,350,1,0,0,0,64,361,1,0,
        0,0,66,372,1,0,0,0,68,384,1,0,0,0,70,396,1,0,0,0,72,411,1,0,0,0,
        74,413,1,0,0,0,76,429,1,0,0,0,78,443,1,0,0,0,80,454,1,0,0,0,82,456,
        1,0,0,0,84,460,1,0,0,0,86,464,1,0,0,0,88,473,1,0,0,0,90,489,1,0,
        0,0,92,491,1,0,0,0,94,495,1,0,0,0,96,501,1,0,0,0,98,513,1,0,0,0,
        100,517,1,0,0,0,102,524,1,0,0,0,104,532,1,0,0,0,106,536,1,0,0,0,
        108,540,1,0,0,0,110,552,1,0,0,0,112,563,1,0,0,0,114,571,1,0,0,0,
        116,581,1,0,0,0,118,583,1,0,0,0,120,585,1,0,0,0,122,587,1,0,0,0,
        124,589,1,0,0,0,126,128,3,2,1,0,127,126,1,0,0,0,128,129,1,0,0,0,
        129,127,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,5,0,0,1,
        132,1,1,0,0,0,133,140,3,8,4,0,134,140,3,10,5,0,135,140,3,96,48,0,
        136,140,3,108,54,0,137,140,3,48,24,0,138,140,3,54,27,0,139,133,1,
        0,0,0,139,134,1,0,0,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,
        0,0,0,139,138,1,0,0,0,140,3,1,0,0,0,141,152,3,8,4,0,142,152,3,10,
        5,0,143,152,3,14,7,0,144,152,3,18,9,0,145,152,3,26,13,0,146,152,
        3,40,20,0,147,152,3,42,21,0,148,152,3,44,22,0,149,152,3,46,23,0,
        150,152,3,124,62,0,151,141,1,0,0,0,151,142,1,0,0,0,151,143,1,0,0,
        0,151,144,1,0,0,0,151,145,1,0,0,0,151,146,1,0,0,0,151,147,1,0,0,
        0,151,148,1,0,0,0,151,149,1,0,0,0,151,150,1,0,0,0,152,5,1,0,0,0,
        153,155,5,46,0,0,154,156,3,4,2,0,155,154,1,0,0,0,156,157,1,0,0,0,
        157,155,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,47,0,0,
        160,7,1,0,0,0,161,162,5,16,0,0,162,170,5,62,0,0,163,171,3,12,6,0,
        164,165,5,40,0,0,165,171,3,62,31,0,166,167,3,12,6,0,167,168,5,40,
        0,0,168,169,3,62,31,0,169,171,1,0,0,0,170,163,1,0,0,0,170,164,1,
        0,0,0,170,166,1,0,0,0,171,172,1,0,0,0,172,173,5,49,0,0,173,9,1,0,
        0,0,174,175,5,15,0,0,175,176,5,62,0,0,176,177,5,40,0,0,177,178,3,
        62,31,0,178,179,5,49,0,0,179,11,1,0,0,0,180,184,3,58,29,0,181,184,
        5,62,0,0,182,184,3,80,40,0,183,180,1,0,0,0,183,181,1,0,0,0,183,182,
        1,0,0,0,184,13,1,0,0,0,185,186,3,16,8,0,186,187,3,122,61,0,187,188,
        3,62,31,0,188,189,5,49,0,0,189,15,1,0,0,0,190,194,5,62,0,0,191,194,
        3,106,53,0,192,194,3,94,47,0,193,190,1,0,0,0,193,191,1,0,0,0,193,
        192,1,0,0,0,194,17,1,0,0,0,195,196,3,20,10,0,196,198,3,22,11,0,197,
        199,3,24,12,0,198,197,1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,0,200,
        201,5,49,0,0,201,19,1,0,0,0,202,203,5,3,0,0,203,204,5,42,0,0,204,
        205,3,62,31,0,205,206,5,43,0,0,206,207,3,6,3,0,207,21,1,0,0,0,208,
        209,5,4,0,0,209,210,5,3,0,0,210,211,5,42,0,0,211,212,3,62,31,0,212,
        213,5,43,0,0,213,214,3,6,3,0,214,216,1,0,0,0,215,208,1,0,0,0,216,
        219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,23,1,0,0,0,219,217,
        1,0,0,0,220,221,5,4,0,0,221,222,3,6,3,0,222,25,1,0,0,0,223,227,3,
        28,14,0,224,227,3,32,16,0,225,227,3,38,19,0,226,223,1,0,0,0,226,
        224,1,0,0,0,226,225,1,0,0,0,227,27,1,0,0,0,228,229,5,5,0,0,229,230,
        3,30,15,0,230,231,3,6,3,0,231,232,5,49,0,0,232,29,1,0,0,0,233,234,
        3,62,31,0,234,31,1,0,0,0,235,236,5,5,0,0,236,237,3,34,17,0,237,238,
        3,30,15,0,238,239,5,49,0,0,239,240,3,36,18,0,240,241,3,6,3,0,241,
        242,5,49,0,0,242,33,1,0,0,0,243,244,5,62,0,0,244,245,3,122,61,0,
        245,246,3,62,31,0,246,247,5,49,0,0,247,261,1,0,0,0,248,249,5,16,
        0,0,249,256,5,62,0,0,250,251,5,40,0,0,251,257,3,62,31,0,252,253,
        3,12,6,0,253,254,5,40,0,0,254,255,3,62,31,0,255,257,1,0,0,0,256,
        250,1,0,0,0,256,252,1,0,0,0,257,258,1,0,0,0,258,259,5,49,0,0,259,
        261,1,0,0,0,260,243,1,0,0,0,260,248,1,0,0,0,261,35,1,0,0,0,262,263,
        5,62,0,0,263,264,3,122,61,0,264,265,3,62,31,0,265,37,1,0,0,0,266,
        267,5,5,0,0,267,268,5,62,0,0,268,269,5,48,0,0,269,270,5,62,0,0,270,
        271,5,34,0,0,271,272,5,19,0,0,272,273,3,62,31,0,273,274,3,6,3,0,
        274,275,5,49,0,0,275,39,1,0,0,0,276,277,5,18,0,0,277,278,5,49,0,
        0,278,41,1,0,0,0,279,280,5,17,0,0,280,281,5,49,0,0,281,43,1,0,0,
        0,282,285,3,50,25,0,283,285,3,56,28,0,284,282,1,0,0,0,284,283,1,
        0,0,0,285,286,1,0,0,0,286,287,5,49,0,0,287,45,1,0,0,0,288,290,5,
        6,0,0,289,291,3,62,31,0,290,289,1,0,0,0,290,291,1,0,0,0,291,292,
        1,0,0,0,292,293,5,49,0,0,293,47,1,0,0,0,294,295,5,7,0,0,295,296,
        5,62,0,0,296,298,5,42,0,0,297,299,3,112,56,0,298,297,1,0,0,0,298,
        299,1,0,0,0,299,300,1,0,0,0,300,302,5,43,0,0,301,303,3,60,30,0,302,
        301,1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,3,6,3,0,305,
        306,5,49,0,0,306,49,1,0,0,0,307,308,5,62,0,0,308,310,5,42,0,0,309,
        311,3,52,26,0,310,309,1,0,0,0,310,311,1,0,0,0,311,312,1,0,0,0,312,
        313,5,43,0,0,313,51,1,0,0,0,314,319,3,62,31,0,315,316,5,48,0,0,316,
        318,3,62,31,0,317,315,1,0,0,0,318,321,1,0,0,0,319,317,1,0,0,0,319,
        320,1,0,0,0,320,53,1,0,0,0,321,319,1,0,0,0,322,323,5,7,0,0,323,324,
        5,42,0,0,324,325,5,62,0,0,325,326,5,62,0,0,326,327,5,43,0,0,327,
        328,5,62,0,0,328,330,5,42,0,0,329,331,3,112,56,0,330,329,1,0,0,0,
        330,331,1,0,0,0,331,332,1,0,0,0,332,334,5,43,0,0,333,335,3,60,30,
        0,334,333,1,0,0,0,334,335,1,0,0,0,335,336,1,0,0,0,336,337,3,6,3,
        0,337,338,5,49,0,0,338,55,1,0,0,0,339,340,3,74,37,0,340,341,5,41,
        0,0,341,342,3,50,25,0,342,57,1,0,0,0,343,344,7,0,0,0,344,59,1,0,
        0,0,345,349,3,58,29,0,346,349,5,62,0,0,347,349,3,80,40,0,348,345,
        1,0,0,0,348,346,1,0,0,0,348,347,1,0,0,0,349,61,1,0,0,0,350,351,6,
        31,-1,0,351,352,3,64,32,0,352,358,1,0,0,0,353,354,10,2,0,0,354,355,
        5,32,0,0,355,357,3,64,32,0,356,353,1,0,0,0,357,360,1,0,0,0,358,356,
        1,0,0,0,358,359,1,0,0,0,359,63,1,0,0,0,360,358,1,0,0,0,361,362,6,
        32,-1,0,362,363,3,66,33,0,363,369,1,0,0,0,364,365,10,2,0,0,365,366,
        5,31,0,0,366,368,3,66,33,0,367,364,1,0,0,0,368,371,1,0,0,0,369,367,
        1,0,0,0,369,370,1,0,0,0,370,65,1,0,0,0,371,369,1,0,0,0,372,373,6,
        33,-1,0,373,374,3,68,34,0,374,381,1,0,0,0,375,376,10,2,0,0,376,377,
        3,120,60,0,377,378,3,68,34,0,378,380,1,0,0,0,379,375,1,0,0,0,380,
        383,1,0,0,0,381,379,1,0,0,0,381,382,1,0,0,0,382,67,1,0,0,0,383,381,
        1,0,0,0,384,385,6,34,-1,0,385,386,3,70,35,0,386,393,1,0,0,0,387,
        388,10,2,0,0,388,389,3,118,59,0,389,390,3,70,35,0,390,392,1,0,0,
        0,391,387,1,0,0,0,392,395,1,0,0,0,393,391,1,0,0,0,393,394,1,0,0,
        0,394,69,1,0,0,0,395,393,1,0,0,0,396,397,6,35,-1,0,397,398,3,72,
        36,0,398,405,1,0,0,0,399,400,10,2,0,0,400,401,3,116,58,0,401,402,
        3,72,36,0,402,404,1,0,0,0,403,399,1,0,0,0,404,407,1,0,0,0,405,403,
        1,0,0,0,405,406,1,0,0,0,406,71,1,0,0,0,407,405,1,0,0,0,408,409,7,
        1,0,0,409,412,3,72,36,0,410,412,3,74,37,0,411,408,1,0,0,0,411,410,
        1,0,0,0,412,73,1,0,0,0,413,414,6,37,-1,0,414,415,3,78,39,0,415,426,
        1,0,0,0,416,417,10,3,0,0,417,418,5,41,0,0,418,425,3,78,39,0,419,
        420,10,2,0,0,420,421,5,44,0,0,421,422,3,62,31,0,422,423,5,45,0,0,
        423,425,1,0,0,0,424,416,1,0,0,0,424,419,1,0,0,0,425,428,1,0,0,0,
        426,424,1,0,0,0,426,427,1,0,0,0,427,75,1,0,0,0,428,426,1,0,0,0,429,
        430,5,42,0,0,430,431,3,62,31,0,431,432,5,43,0,0,432,77,1,0,0,0,433,
        444,5,51,0,0,434,444,5,56,0,0,435,444,5,57,0,0,436,444,5,58,0,0,
        437,444,5,59,0,0,438,444,3,86,43,0,439,444,3,100,50,0,440,444,5,
        62,0,0,441,444,3,50,25,0,442,444,3,76,38,0,443,433,1,0,0,0,443,434,
        1,0,0,0,443,435,1,0,0,0,443,436,1,0,0,0,443,437,1,0,0,0,443,438,
        1,0,0,0,443,439,1,0,0,0,443,440,1,0,0,0,443,441,1,0,0,0,443,442,
        1,0,0,0,444,79,1,0,0,0,445,446,3,82,41,0,446,447,3,80,40,0,447,455,
        1,0,0,0,448,452,3,82,41,0,449,453,3,58,29,0,450,453,5,62,0,0,451,
        453,3,80,40,0,452,449,1,0,0,0,452,450,1,0,0,0,452,451,1,0,0,0,453,
        455,1,0,0,0,454,445,1,0,0,0,454,448,1,0,0,0,455,81,1,0,0,0,456,457,
        5,44,0,0,457,458,7,2,0,0,458,459,5,45,0,0,459,83,1,0,0,0,460,461,
        5,44,0,0,461,462,3,62,31,0,462,463,5,45,0,0,463,85,1,0,0,0,464,465,
        3,80,40,0,465,467,5,46,0,0,466,468,3,88,44,0,467,466,1,0,0,0,468,
        469,1,0,0,0,469,467,1,0,0,0,469,470,1,0,0,0,470,471,1,0,0,0,471,
        472,5,47,0,0,472,87,1,0,0,0,473,478,3,90,45,0,474,475,5,48,0,0,475,
        477,3,90,45,0,476,474,1,0,0,0,477,480,1,0,0,0,478,476,1,0,0,0,478,
        479,1,0,0,0,479,89,1,0,0,0,480,478,1,0,0,0,481,490,5,51,0,0,482,
        490,5,56,0,0,483,490,5,58,0,0,484,490,5,57,0,0,485,490,5,59,0,0,
        486,490,5,62,0,0,487,490,3,100,50,0,488,490,3,92,46,0,489,481,1,
        0,0,0,489,482,1,0,0,0,489,483,1,0,0,0,489,484,1,0,0,0,489,485,1,
        0,0,0,489,486,1,0,0,0,489,487,1,0,0,0,489,488,1,0,0,0,490,91,1,0,
        0,0,491,492,5,46,0,0,492,493,3,88,44,0,493,494,5,47,0,0,494,93,1,
        0,0,0,495,497,3,74,37,0,496,498,3,84,42,0,497,496,1,0,0,0,498,499,
        1,0,0,0,499,497,1,0,0,0,499,500,1,0,0,0,500,95,1,0,0,0,501,502,5,
        8,0,0,502,503,5,62,0,0,503,504,5,9,0,0,504,506,5,46,0,0,505,507,
        3,98,49,0,506,505,1,0,0,0,507,508,1,0,0,0,508,506,1,0,0,0,508,509,
        1,0,0,0,509,510,1,0,0,0,510,511,5,47,0,0,511,512,5,49,0,0,512,97,
        1,0,0,0,513,514,5,62,0,0,514,515,3,60,30,0,515,516,5,49,0,0,516,
        99,1,0,0,0,517,518,5,62,0,0,518,520,5,46,0,0,519,521,3,102,51,0,
        520,519,1,0,0,0,520,521,1,0,0,0,521,522,1,0,0,0,522,523,5,47,0,0,
        523,101,1,0,0,0,524,529,3,104,52,0,525,526,5,48,0,0,526,528,3,104,
        52,0,527,525,1,0,0,0,528,531,1,0,0,0,529,527,1,0,0,0,529,530,1,0,
        0,0,530,103,1,0,0,0,531,529,1,0,0,0,532,533,5,62,0,0,533,534,5,50,
        0,0,534,535,3,62,31,0,535,105,1,0,0,0,536,537,3,74,37,0,537,538,
        5,41,0,0,538,539,5,62,0,0,539,107,1,0,0,0,540,541,5,8,0,0,541,542,
        5,62,0,0,542,543,5,10,0,0,543,545,5,46,0,0,544,546,3,110,55,0,545,
        544,1,0,0,0,546,547,1,0,0,0,547,545,1,0,0,0,547,548,1,0,0,0,548,
        549,1,0,0,0,549,550,5,47,0,0,550,551,5,49,0,0,551,109,1,0,0,0,552,
        553,5,62,0,0,553,555,5,42,0,0,554,556,3,112,56,0,555,554,1,0,0,0,
        555,556,1,0,0,0,556,557,1,0,0,0,557,559,5,43,0,0,558,560,3,60,30,
        0,559,558,1,0,0,0,559,560,1,0,0,0,560,561,1,0,0,0,561,562,5,49,0,
        0,562,111,1,0,0,0,563,568,3,114,57,0,564,565,5,48,0,0,565,567,3,
        114,57,0,566,564,1,0,0,0,567,570,1,0,0,0,568,566,1,0,0,0,568,569,
        1,0,0,0,569,113,1,0,0,0,570,568,1,0,0,0,571,576,5,62,0,0,572,573,
        5,48,0,0,573,575,5,62,0,0,574,572,1,0,0,0,575,578,1,0,0,0,576,574,
        1,0,0,0,576,577,1,0,0,0,577,579,1,0,0,0,578,576,1,0,0,0,579,580,
        3,60,30,0,580,115,1,0,0,0,581,582,7,3,0,0,582,117,1,0,0,0,583,584,
        7,4,0,0,584,119,1,0,0,0,585,586,7,5,0,0,586,121,1,0,0,0,587,588,
        7,6,0,0,588,123,1,0,0,0,589,590,7,7,0,0,590,125,1,0,0,0,44,129,139,
        151,157,170,183,193,198,217,226,256,260,284,290,298,302,310,319,
        330,334,348,358,369,381,393,405,411,424,426,443,452,454,469,478,
        489,499,508,520,529,547,555,559,568,576
    ]

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
        self.checkVersion("4.13.1")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 98688) != 0)):
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5694823719043039342) != 0)):
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




    def decl_typ(self):

        localctx = MiniGoParser.Decl_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_typ)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.primitive_type()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [44]:
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
            if _la==4:
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




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_initialization)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
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
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(MiniGoParser.VAR)
                self.state = 249
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 256
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 250
                    self.match(MiniGoParser.EQUAL)
                    self.state = 251
                    self.expr(0)
                    pass
                elif token in [11, 12, 13, 14, 44, 62]:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5694823727634579456) != 0):
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
            if _la==62:
                self.state = 297
                self.param_list()


            self.state = 300
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611703610613463040) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5694823727634579456) != 0):
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
            while _la==48:
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
            if _la==62:
                self.state = 329
                self.param_list()


            self.state = 332
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611703610613463040) != 0):
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




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
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




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_typ)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.primitive_type()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [44]:
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




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                _la = self._input.LA(1)
                if not(_la==21 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 409
                self.expr5()
                pass
            elif token in [42, 44, 51, 56, 57, 58, 59, 62]:
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
                if token in [11, 12, 13, 14]:
                    self.state = 449
                    self.primitive_type()
                    pass
                elif token in [62]:
                    self.state = 450
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                elif token in [44]:
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
            if not(_la==51 or _la==62):
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5694872097554169856) != 0)):
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
            while _la==48:
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
                if not (_la==44):
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
                if not (_la==62):
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
            if _la==62:
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
            while _la==48:
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
                if not (_la==62):
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
            if _la==62:
                self.state = 554
                self.param_list()


            self.state = 557
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 559
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611703610613463040) != 0):
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
            while _la==48:
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
            while _la==48:
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




    def arith_high_operator(self):

        localctx = MiniGoParser.Arith_high_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arith_high_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
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




    def arith_low_operator(self):

        localctx = MiniGoParser.Arith_low_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arith_low_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
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




    def relational_operator(self):

        localctx = MiniGoParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
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




    def assign_operator(self):

        localctx = MiniGoParser.Assign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_assign_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
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




    def comment(self):

        localctx = MiniGoParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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
         




