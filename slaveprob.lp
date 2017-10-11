\* Slave solver *\
Minimize
OBJ: - S10 - S11 - S2 - S3 - S4 - S5 - 0.5 S6 - S7 - S9
Subject To
_C1: 6 S0 + 9 S1 + 14 S10 + 11 S11 + 16 S2 + 17 S3 + 13 S4 + 12 S5 + 10 S6
 + 15 S7 + 5 S8 + 18 S9 <= 20
Bounds
0 <= S0
0 <= S1
0 <= S10
0 <= S11
0 <= S2
0 <= S3
0 <= S4
0 <= S5
0 <= S6
0 <= S7
0 <= S8
0 <= S9
Generals
S0
S1
S10
S11
S2
S3
S4
S5
S6
S7
S8
S9
End
