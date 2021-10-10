# An markdown version of Table 1.2
| Func  | Var |   |   |   |  |
| ----- | --- | - | - | - |  |
|  | X | 0 | 0 | 1 | 1 |
|  | Y | 0 | 1 | 0 | 1 |
|  |  |  |  |  |  |
| Constant 0 | 0 | 0 | 0 | 0 | 0 |
| And | X And Y | 0 | 0 | 0 | 1 |
| x And Not y | Not(Y) | 0 | 1 | 0 | 0 |
| x | X | 0 | 0 | 1 | 1 |
| Not x and y | Not(X) And Y | 0 | 1 | 0 | 0 |
| y | Y | 0 | 1 | 0 | 1 |
| Xor | X And Not(Y) Or Not(X) And Y | 0 | 1 | 1 | 0 |
| Or | X Or Y | 0 | 1 | 1 | 1 |
| Nor | Not(X Or Y) | 1 | 0 | 0 | 0 |
| Equivalence | X And Y Or Not(X) And Not(Y) | 1 | 0 | 0 | 1 |
| Not y | Not(Y) | 1 | 0 | 1 | 0 |
| If y then x | X Or Not(Y) | 1 | 0 | 1 | 1 |
| Not x | Not(X) | 1 | 1 | 0 | 0 |
| If x then y | Not(X) Or Y | 1 | 1 | 0 | 1 |
| Nand | Not(X And Y) | 1 | 1 | 1 | 0 |
| Constant 1 | 1 | 1 | 1 | 1 | 1 |
