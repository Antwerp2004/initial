# Generated from c://Users//HP//Downloads//Principles of Programming Language (CO3005)//Assignment//Assignment 1//initial//initial//src//main//minigo//parser//MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,65,503,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,1,0,1,0,1,0,1,0,5,0,150,8,0,10,0,12,0,153,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,5,1,162,8,1,10,1,12,1,165,9,1,1,1,1,1,1,1,1,1,1,1,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,
        1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,
        1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,33,1,33,1,33,
        1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,
        1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,
        1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,
        1,50,1,50,3,50,352,8,50,1,51,1,51,1,51,5,51,357,8,51,10,51,12,51,
        360,9,51,3,51,362,8,51,1,52,1,52,1,52,4,52,367,8,52,11,52,12,52,
        368,1,53,1,53,1,53,4,53,374,8,53,11,53,12,53,375,1,54,1,54,1,54,
        4,54,381,8,54,11,54,12,54,382,1,55,1,55,1,55,3,55,388,8,55,1,55,
        3,55,391,8,55,1,56,4,56,394,8,56,11,56,12,56,395,1,57,5,57,399,8,
        57,10,57,12,57,402,9,57,1,58,1,58,3,58,406,8,58,1,58,4,58,409,8,
        58,11,58,12,58,410,1,59,1,59,1,59,1,59,1,59,4,59,418,8,59,11,59,
        12,59,419,1,59,1,59,3,59,424,8,59,1,60,1,60,3,60,428,8,60,1,61,1,
        61,1,62,1,62,1,63,1,63,1,63,1,63,1,63,1,63,1,63,1,63,1,63,3,63,443,
        8,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,3,64,454,8,64,
        1,65,1,65,1,65,1,65,1,66,1,66,1,66,3,66,463,8,66,1,66,1,66,1,67,
        1,67,1,67,1,67,1,68,1,68,5,68,473,8,68,10,68,12,68,476,9,68,1,69,
        1,69,5,69,480,8,69,10,69,12,69,483,9,69,1,69,1,69,1,69,1,69,1,70,
        1,70,5,70,491,8,70,10,70,12,70,494,9,70,1,70,3,70,497,8,70,1,70,
        1,70,1,71,1,71,1,71,1,163,0,72,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,
        19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,
        30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,
        41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,
        103,52,105,53,107,54,109,55,111,56,113,0,115,0,117,0,119,57,121,
        0,123,0,125,0,127,0,129,58,131,59,133,60,135,61,137,62,139,63,141,
        64,143,65,1,0,19,2,0,10,10,13,13,1,0,49,57,1,0,48,57,2,0,66,66,98,
        98,1,0,48,49,2,0,79,79,111,111,1,0,48,55,2,0,88,88,120,120,3,0,48,
        57,65,70,97,102,2,0,69,69,101,101,2,0,43,43,45,45,4,0,10,10,13,13,
        34,34,92,92,1,0,34,34,3,0,110,110,114,114,116,116,3,0,9,9,12,13,
        32,32,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,4,0,92,
        92,110,110,114,114,116,116,2,1,10,10,13,13,522,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,
        0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,
        0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,
        0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,
        0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,
        0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,
        0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,
        119,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,
        0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,1,145,
        1,0,0,0,3,156,1,0,0,0,5,171,1,0,0,0,7,174,1,0,0,0,9,179,1,0,0,0,
        11,183,1,0,0,0,13,190,1,0,0,0,15,195,1,0,0,0,17,200,1,0,0,0,19,207,
        1,0,0,0,21,217,1,0,0,0,23,224,1,0,0,0,25,228,1,0,0,0,27,234,1,0,
        0,0,29,242,1,0,0,0,31,248,1,0,0,0,33,252,1,0,0,0,35,261,1,0,0,0,
        37,267,1,0,0,0,39,273,1,0,0,0,41,275,1,0,0,0,43,277,1,0,0,0,45,279,
        1,0,0,0,47,281,1,0,0,0,49,283,1,0,0,0,51,286,1,0,0,0,53,289,1,0,
        0,0,55,292,1,0,0,0,57,295,1,0,0,0,59,297,1,0,0,0,61,299,1,0,0,0,
        63,302,1,0,0,0,65,305,1,0,0,0,67,307,1,0,0,0,69,310,1,0,0,0,71,313,
        1,0,0,0,73,316,1,0,0,0,75,319,1,0,0,0,77,322,1,0,0,0,79,325,1,0,
        0,0,81,327,1,0,0,0,83,329,1,0,0,0,85,331,1,0,0,0,87,333,1,0,0,0,
        89,335,1,0,0,0,91,337,1,0,0,0,93,339,1,0,0,0,95,341,1,0,0,0,97,343,
        1,0,0,0,99,345,1,0,0,0,101,351,1,0,0,0,103,361,1,0,0,0,105,363,1,
        0,0,0,107,370,1,0,0,0,109,377,1,0,0,0,111,384,1,0,0,0,113,393,1,
        0,0,0,115,400,1,0,0,0,117,403,1,0,0,0,119,423,1,0,0,0,121,427,1,
        0,0,0,123,429,1,0,0,0,125,431,1,0,0,0,127,442,1,0,0,0,129,453,1,
        0,0,0,131,455,1,0,0,0,133,462,1,0,0,0,135,466,1,0,0,0,137,470,1,
        0,0,0,139,477,1,0,0,0,141,488,1,0,0,0,143,500,1,0,0,0,145,146,5,
        47,0,0,146,147,5,47,0,0,147,151,1,0,0,0,148,150,8,0,0,0,149,148,
        1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,
        1,0,0,0,153,151,1,0,0,0,154,155,6,0,0,0,155,2,1,0,0,0,156,157,5,
        47,0,0,157,158,5,42,0,0,158,163,1,0,0,0,159,162,3,3,1,0,160,162,
        9,0,0,0,161,159,1,0,0,0,161,160,1,0,0,0,162,165,1,0,0,0,163,164,
        1,0,0,0,163,161,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,
        5,42,0,0,167,168,5,47,0,0,168,169,1,0,0,0,169,170,6,1,0,0,170,4,
        1,0,0,0,171,172,5,105,0,0,172,173,5,102,0,0,173,6,1,0,0,0,174,175,
        5,101,0,0,175,176,5,108,0,0,176,177,5,115,0,0,177,178,5,101,0,0,
        178,8,1,0,0,0,179,180,5,102,0,0,180,181,5,111,0,0,181,182,5,114,
        0,0,182,10,1,0,0,0,183,184,5,114,0,0,184,185,5,101,0,0,185,186,5,
        116,0,0,186,187,5,117,0,0,187,188,5,114,0,0,188,189,5,110,0,0,189,
        12,1,0,0,0,190,191,5,102,0,0,191,192,5,117,0,0,192,193,5,110,0,0,
        193,194,5,99,0,0,194,14,1,0,0,0,195,196,5,116,0,0,196,197,5,121,
        0,0,197,198,5,112,0,0,198,199,5,101,0,0,199,16,1,0,0,0,200,201,5,
        115,0,0,201,202,5,116,0,0,202,203,5,114,0,0,203,204,5,117,0,0,204,
        205,5,99,0,0,205,206,5,116,0,0,206,18,1,0,0,0,207,208,5,105,0,0,
        208,209,5,110,0,0,209,210,5,116,0,0,210,211,5,101,0,0,211,212,5,
        114,0,0,212,213,5,102,0,0,213,214,5,97,0,0,214,215,5,99,0,0,215,
        216,5,101,0,0,216,20,1,0,0,0,217,218,5,115,0,0,218,219,5,116,0,0,
        219,220,5,114,0,0,220,221,5,105,0,0,221,222,5,110,0,0,222,223,5,
        103,0,0,223,22,1,0,0,0,224,225,5,105,0,0,225,226,5,110,0,0,226,227,
        5,116,0,0,227,24,1,0,0,0,228,229,5,102,0,0,229,230,5,108,0,0,230,
        231,5,111,0,0,231,232,5,97,0,0,232,233,5,116,0,0,233,26,1,0,0,0,
        234,235,5,98,0,0,235,236,5,111,0,0,236,237,5,111,0,0,237,238,5,108,
        0,0,238,239,5,101,0,0,239,240,5,97,0,0,240,241,5,110,0,0,241,28,
        1,0,0,0,242,243,5,99,0,0,243,244,5,111,0,0,244,245,5,110,0,0,245,
        246,5,115,0,0,246,247,5,116,0,0,247,30,1,0,0,0,248,249,5,118,0,0,
        249,250,5,97,0,0,250,251,5,114,0,0,251,32,1,0,0,0,252,253,5,99,0,
        0,253,254,5,111,0,0,254,255,5,110,0,0,255,256,5,116,0,0,256,257,
        5,105,0,0,257,258,5,110,0,0,258,259,5,117,0,0,259,260,5,101,0,0,
        260,34,1,0,0,0,261,262,5,98,0,0,262,263,5,114,0,0,263,264,5,101,
        0,0,264,265,5,97,0,0,265,266,5,107,0,0,266,36,1,0,0,0,267,268,5,
        114,0,0,268,269,5,97,0,0,269,270,5,110,0,0,270,271,5,103,0,0,271,
        272,5,101,0,0,272,38,1,0,0,0,273,274,5,43,0,0,274,40,1,0,0,0,275,
        276,5,45,0,0,276,42,1,0,0,0,277,278,5,42,0,0,278,44,1,0,0,0,279,
        280,5,47,0,0,280,46,1,0,0,0,281,282,5,37,0,0,282,48,1,0,0,0,283,
        284,5,61,0,0,284,285,5,61,0,0,285,50,1,0,0,0,286,287,5,33,0,0,287,
        288,5,61,0,0,288,52,1,0,0,0,289,290,5,62,0,0,290,291,5,61,0,0,291,
        54,1,0,0,0,292,293,5,60,0,0,293,294,5,61,0,0,294,56,1,0,0,0,295,
        296,5,62,0,0,296,58,1,0,0,0,297,298,5,60,0,0,298,60,1,0,0,0,299,
        300,5,38,0,0,300,301,5,38,0,0,301,62,1,0,0,0,302,303,5,124,0,0,303,
        304,5,124,0,0,304,64,1,0,0,0,305,306,5,33,0,0,306,66,1,0,0,0,307,
        308,5,58,0,0,308,309,5,61,0,0,309,68,1,0,0,0,310,311,5,43,0,0,311,
        312,5,61,0,0,312,70,1,0,0,0,313,314,5,45,0,0,314,315,5,61,0,0,315,
        72,1,0,0,0,316,317,5,42,0,0,317,318,5,61,0,0,318,74,1,0,0,0,319,
        320,5,47,0,0,320,321,5,61,0,0,321,76,1,0,0,0,322,323,5,37,0,0,323,
        324,5,61,0,0,324,78,1,0,0,0,325,326,5,61,0,0,326,80,1,0,0,0,327,
        328,5,46,0,0,328,82,1,0,0,0,329,330,5,40,0,0,330,84,1,0,0,0,331,
        332,5,41,0,0,332,86,1,0,0,0,333,334,5,91,0,0,334,88,1,0,0,0,335,
        336,5,93,0,0,336,90,1,0,0,0,337,338,5,123,0,0,338,92,1,0,0,0,339,
        340,5,125,0,0,340,94,1,0,0,0,341,342,5,44,0,0,342,96,1,0,0,0,343,
        344,5,59,0,0,344,98,1,0,0,0,345,346,5,58,0,0,346,100,1,0,0,0,347,
        352,3,103,51,0,348,352,3,105,52,0,349,352,3,107,53,0,350,352,3,109,
        54,0,351,347,1,0,0,0,351,348,1,0,0,0,351,349,1,0,0,0,351,350,1,0,
        0,0,352,102,1,0,0,0,353,362,5,48,0,0,354,358,7,1,0,0,355,357,7,2,
        0,0,356,355,1,0,0,0,357,360,1,0,0,0,358,356,1,0,0,0,358,359,1,0,
        0,0,359,362,1,0,0,0,360,358,1,0,0,0,361,353,1,0,0,0,361,354,1,0,
        0,0,362,104,1,0,0,0,363,364,5,48,0,0,364,366,7,3,0,0,365,367,7,4,
        0,0,366,365,1,0,0,0,367,368,1,0,0,0,368,366,1,0,0,0,368,369,1,0,
        0,0,369,106,1,0,0,0,370,371,5,48,0,0,371,373,7,5,0,0,372,374,7,6,
        0,0,373,372,1,0,0,0,374,375,1,0,0,0,375,373,1,0,0,0,375,376,1,0,
        0,0,376,108,1,0,0,0,377,378,5,48,0,0,378,380,7,7,0,0,379,381,7,8,
        0,0,380,379,1,0,0,0,381,382,1,0,0,0,382,380,1,0,0,0,382,383,1,0,
        0,0,383,110,1,0,0,0,384,385,3,113,56,0,385,387,5,46,0,0,386,388,
        3,115,57,0,387,386,1,0,0,0,387,388,1,0,0,0,388,390,1,0,0,0,389,391,
        3,117,58,0,390,389,1,0,0,0,390,391,1,0,0,0,391,112,1,0,0,0,392,394,
        7,2,0,0,393,392,1,0,0,0,394,395,1,0,0,0,395,393,1,0,0,0,395,396,
        1,0,0,0,396,114,1,0,0,0,397,399,7,2,0,0,398,397,1,0,0,0,399,402,
        1,0,0,0,400,398,1,0,0,0,400,401,1,0,0,0,401,116,1,0,0,0,402,400,
        1,0,0,0,403,405,7,9,0,0,404,406,7,10,0,0,405,404,1,0,0,0,405,406,
        1,0,0,0,406,408,1,0,0,0,407,409,7,2,0,0,408,407,1,0,0,0,409,410,
        1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,118,1,0,0,0,412,413,
        3,123,61,0,413,414,3,123,61,0,414,424,1,0,0,0,415,417,3,123,61,0,
        416,418,3,121,60,0,417,416,1,0,0,0,418,419,1,0,0,0,419,417,1,0,0,
        0,419,420,1,0,0,0,420,421,1,0,0,0,421,422,3,123,61,0,422,424,1,0,
        0,0,423,412,1,0,0,0,423,415,1,0,0,0,424,120,1,0,0,0,425,428,3,127,
        63,0,426,428,8,11,0,0,427,425,1,0,0,0,427,426,1,0,0,0,428,122,1,
        0,0,0,429,430,7,12,0,0,430,124,1,0,0,0,431,432,5,92,0,0,432,126,
        1,0,0,0,433,434,3,125,62,0,434,435,7,13,0,0,435,443,1,0,0,0,436,
        437,3,125,62,0,437,438,3,123,61,0,438,443,1,0,0,0,439,440,3,125,
        62,0,440,441,3,125,62,0,441,443,1,0,0,0,442,433,1,0,0,0,442,436,
        1,0,0,0,442,439,1,0,0,0,443,128,1,0,0,0,444,445,5,116,0,0,445,446,
        5,114,0,0,446,447,5,117,0,0,447,454,5,101,0,0,448,449,5,102,0,0,
        449,450,5,97,0,0,450,451,5,108,0,0,451,452,5,115,0,0,452,454,5,101,
        0,0,453,444,1,0,0,0,453,448,1,0,0,0,454,130,1,0,0,0,455,456,5,110,
        0,0,456,457,5,105,0,0,457,458,5,108,0,0,458,132,1,0,0,0,459,460,
        5,13,0,0,460,463,5,10,0,0,461,463,5,10,0,0,462,459,1,0,0,0,462,461,
        1,0,0,0,463,464,1,0,0,0,464,465,6,66,1,0,465,134,1,0,0,0,466,467,
        7,14,0,0,467,468,1,0,0,0,468,469,6,67,0,0,469,136,1,0,0,0,470,474,
        7,15,0,0,471,473,7,16,0,0,472,471,1,0,0,0,473,476,1,0,0,0,474,472,
        1,0,0,0,474,475,1,0,0,0,475,138,1,0,0,0,476,474,1,0,0,0,477,481,
        3,123,61,0,478,480,3,121,60,0,479,478,1,0,0,0,480,483,1,0,0,0,481,
        479,1,0,0,0,481,482,1,0,0,0,482,484,1,0,0,0,483,481,1,0,0,0,484,
        485,3,125,62,0,485,486,8,17,0,0,486,487,6,69,2,0,487,140,1,0,0,0,
        488,492,3,123,61,0,489,491,3,121,60,0,490,489,1,0,0,0,491,494,1,
        0,0,0,492,490,1,0,0,0,492,493,1,0,0,0,493,496,1,0,0,0,494,492,1,
        0,0,0,495,497,7,18,0,0,496,495,1,0,0,0,497,498,1,0,0,0,498,499,6,
        70,3,0,499,142,1,0,0,0,500,501,9,0,0,0,501,502,6,71,4,0,502,144,
        1,0,0,0,26,0,151,161,163,351,358,361,368,375,382,387,390,395,400,
        405,410,419,423,427,442,453,462,474,481,492,496,5,6,0,0,1,66,0,1,
        69,1,1,70,2,1,71,3
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_LINE_COMMENT = 1
    MULTI_LINE_COMMENT = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    ADD = 20
    SUB = 21
    MULTIPLY = 22
    DIVIDE = 23
    REMAIN = 24
    COMPARE_STR = 25
    NOT_EQ = 26
    GREATER_OR_EQ = 27
    LESS_OR_EQ = 28
    GREATER = 29
    LESS = 30
    AND = 31
    OR = 32
    NOT = 33
    ASSIGNMENT_SIGN = 34
    SHORT_ADD = 35
    SHORT_SUB = 36
    SHORT_MULTIPLY = 37
    SHORT_DIVIDE = 38
    SHORT_REMAIN = 39
    EQUAL = 40
    DOT = 41
    OPEN_PARENTHESIS = 42
    CLOSE_PARENTHESIS = 43
    OPEN_BRACKET = 44
    CLOSE_BRACKET = 45
    OPEN_BRACE = 46
    CLOSE_BRACE = 47
    COMMA = 48
    SEMICOLON = 49
    COLON = 50
    INTEGER_LITERAL = 51
    DECIMAL_INT = 52
    BINARY_INT = 53
    OCTAL_INT = 54
    HEXA_INT = 55
    FLOAT_LITERAL = 56
    STRING_LITERAL = 57
    BOOLEAN_LITERAL = 58
    NIL_LITERAL = 59
    NEWLINE = 60
    WHITESPACE = 61
    IDENTIFIER = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>='", "'<='", 
            "'>'", "'<'", "'&&'", "'||'", "'!'", "':='", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'='", "'.'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'", "':'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "IF", "ELSE", "FOR", 
            "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
            "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
            "ADD", "SUB", "MULTIPLY", "DIVIDE", "REMAIN", "COMPARE_STR", 
            "NOT_EQ", "GREATER_OR_EQ", "LESS_OR_EQ", "GREATER", "LESS", 
            "AND", "OR", "NOT", "ASSIGNMENT_SIGN", "SHORT_ADD", "SHORT_SUB", 
            "SHORT_MULTIPLY", "SHORT_DIVIDE", "SHORT_REMAIN", "EQUAL", "DOT", 
            "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
            "OPEN_BRACE", "CLOSE_BRACE", "COMMA", "SEMICOLON", "COLON", 
            "INTEGER_LITERAL", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", 
            "HEXA_INT", "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "NIL_LITERAL", "NEWLINE", "WHITESPACE", "IDENTIFIER", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "IF", "ELSE", 
                  "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                  "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "ADD", "SUB", "MULTIPLY", "DIVIDE", 
                  "REMAIN", "COMPARE_STR", "NOT_EQ", "GREATER_OR_EQ", "LESS_OR_EQ", 
                  "GREATER", "LESS", "AND", "OR", "NOT", "ASSIGNMENT_SIGN", 
                  "SHORT_ADD", "SHORT_SUB", "SHORT_MULTIPLY", "SHORT_DIVIDE", 
                  "SHORT_REMAIN", "EQUAL", "DOT", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                  "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                  "COMMA", "SEMICOLON", "COLON", "INTEGER_LITERAL", "DECIMAL_INT", 
                  "BINARY_INT", "OCTAL_INT", "HEXA_INT", "FLOAT_LITERAL", 
                  "INT_PART", "DECI_PART", "EXP_PART", "STRING_LITERAL", 
                  "INSIDE_STRING", "DOUBLE_QUOTE", "BACKLASH", "ESCAPE_SEQUENCE", 
                  "BOOLEAN_LITERAL", "NIL_LITERAL", "NEWLINE", "WHITESPACE", 
                  "IDENTIFIER", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input:InputStream):
        super().__init__(input)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        result = super().emit()
        self.preType = tk
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.NEWLINE_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        if self.preType in {self.IDENTIFIER, self.INTEGER_LITERAL,
                        self.FLOAT_LITERAL, self.BOOLEAN_LITERAL, self.STRING_LITERAL,
                        self.INT, self.FLOAT, self.BOOLEAN, self.STRING,
                        self.RETURN, self.CONTINUE, self.BREAK, self.NIL_LITERAL,
                        self.CLOSE_PARENTHESIS, self.CLOSE_BRACKET, self.CLOSE_BRACE}:
                            self.text = ";"
                            self.type = self.SEMICOLON
                        else:
                            self.skip()
                     
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                                if self.text[-1] in ['\r', '\n']:
                                    raise UncloseString(self.text[:-1])
                                else:
                                    raise UncloseString(self.text)
                            
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


