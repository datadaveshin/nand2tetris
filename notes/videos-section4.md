## Video 4.2
### Addressing Modes:
- Register
```
Add R1,R2      # R2 <- R2 + R1
```
- Direct
```
Add R1, M[200] # Mem[200] < Mem[200] + Mem[100]
```
- Indirect
```
Add R1,@A      # Mem[A] < Mem[A] + R1
```
- Immediate
```
Add 73, R1     # R1 <- R1 + 73
```

### I/O
- Additional input and output come from different devices (mouse, sensor, screen)
- CPU needs a protocol for these. Software `drivers` know the protocols.
- Can use "memory mapping" for interactions, ie. location 500234 holds the last mouse coordinates.

## Video 4.3
### Hack computer control:
- `ROM` is loaded with a program
- The `reset` button is pushed (presumably on the PC chip)
- The program starts running

### The Hack machine language
- Hack recognizes 3 registers:
  - `D` holds a 16-bit `data` value
  - `A` holds a 16-bit `address` or `data` value
  - `M` represents the 16-bit "selected memory register" selected by A, so even if you have 1 billion memory registers, only one is selected, and it is denoted by `M`. The rest are irrelevant.

### The A-instruction:
syntax: `@value`, where value is
- a non-negative decimal constant
- a symbol
semantics:
- sets the `A` register to value
- side effect: `RAM[A]` becomes the selected RAM register
- Thus `@21`:
  - Sets `A` to `21`
  - RAM[21] becomes the selected `M` RAM register
- Set RAM[100] to -1
```
@100 // A = 100, but also sets RAM[100] as M
M=-1 // RAM[100] = -1
```  

### The C-instruction:
Has three parts: `dest  = comp ; jump` (both `dest` and `jump` are optional)
  - `dest` is destination (null, M, D, MD, A, AM, AD, AMD)
  - `comp` is computation (0, 1, -1, D, A and M, !D, !A and !M, D+1, A+1 and M+1, D-1, A-1 and M-1, D+A and D+M, D-A and D-M, A-D and M-D, D&A and D&M, D|A and D|M): M refers to RAM[A]. Guessing these are what we can do with the ALU
  - `jump` is jump directive (null, JGT, JEQ, JGE, JLT, JNE, JLE, JMP): Comparisons are always against 0.
Here you can do 2 things:
- store a computation in some destination
- jump to another instruction in the program
Sematics:
- Compute the value of comp
- Stores result in dest;
- If the Boolean expression (comp jump 0) is true, jumps to execute the instruction ROM[A].
- For examples see last 3rd of video

## Video 4.
Goes over symbolic vs binary syntax
## A-instruction:
- symbolic syntax: `@value`, where value can be 0 to 2<sup>15</sup>-1 or symbol, example `@21`
- binary syntax: `0value`, where value is a 15-bit binary number, example `0000000000010101`, note the MSB is an "operation code" or `op code`

## C-instruction:
- symbolic syntax: `dest = comp ; jump`
- binary syntax: `1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3`:
  - MSB is the `op code`, since we have two instructions, `1` in this position would mean a C instruction.
  - Next 2 bits are unused
  - Next 6 are comp bits, what do you want to achieve with the ALU, as these are the control bits.
  - Next 3 are the destination bits
  - Last 3 the jump bits 
