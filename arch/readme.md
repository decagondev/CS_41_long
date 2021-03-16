# Number Systems
```
base 10 (decimal)

+-----1000's place
|+----100's place
||+---10's place
|||+--1's place
||||
abcd

1234 (decimal)




base 2 (binary)

+-----8's place (0b1000's place)
|+----4's place (0b100's place)
||+---2's place (0b10's place)
|||+--1's place (0b1's place)
||||
abcd

1110 (binary)

     (decimal)

```


```

OR =>  |
AND => &
XOR => ^
NOT => ~

num    => 1001 0100
mask   => 0000 0001
anded  => 0000 0100

0110 1001 1010 1111
1111 0010 1010 1110
0110 0000 1010 1110





A    B    C    D
1000 0100 0010 0001
1111 0000 0000 0000 &
1000 0000 0000 0000 >> 12
0000 0000 0000 1000


A    B    C    D
0000 1000 0100 0010
0000 1111 0000 0000 &
0000 0100 0000 0000 >> 8
0000 0000 0000 0100

0000 0000 0000 1000

AABCDDDD
10000010 LDI
11000000 &
10000000 >> 6
opsize = 00000010 => 2


10001010 >> 6
00000010

opsize = ((cmd & 192) >> 6) + 1
if cmd == LDI:
     # do stuff

elif cmd == BOB:
     # do stuff

pc += opsize

AA
00
01
10



```