\* 1D cutting stock *\
Minimize
OBJ: Pat0 + Pat1 + Pat10 + Pat11 + Pat13 + Pat14 + Pat15 + Pat16 + Pat17
 + Pat18 + Pat19 + Pat2 + Pat20 + Pat21 + Pat3 + Pat4 + Pat5 + Pat6 + Pat7
 + Pat8 + Pat9
Subject To
C0: Pat0 + 3 Pat14 + Pat18 + Pat19 >= 40
C1: Pat1 + 2 Pat15 + Pat17 >= 5
C10: Pat10 + Pat20 >= 18
C11: Pat11 + Pat17 + Pat18 + Pat21 >= 19
C2: Pat2 >= 64
C3: Pat3 >= 36
C4: Pat4 >= 61
C5: Pat19 + Pat5 >= 34
C6: 2 Pat16 + Pat6 >= 33
C7: Pat7 >= 46
C8: 4 Pat13 + Pat20 + Pat21 + Pat8 >= 21
C9: Pat9 >= 29
Bounds
0 <= Pat0
0 <= Pat1
0 <= Pat10
0 <= Pat11
0 <= Pat13
0 <= Pat14
0 <= Pat15
0 <= Pat16
0 <= Pat17
0 <= Pat18
0 <= Pat19
0 <= Pat2
0 <= Pat20
0 <= Pat21
0 <= Pat3
0 <= Pat4
0 <= Pat5
0 <= Pat6
0 <= Pat7
0 <= Pat8
0 <= Pat9
End
