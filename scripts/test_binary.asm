// File accompanies test_binary.hack
// Just wanted to try to program in machine language
// This is a translation of test_binary.hack

// Sets RAM[99] to 17
// Sets RAM[100] to RAM[99] + 1
// Loops and increments RAM[100] by 1
@17
D=A
@99
M=D
@100
M=D+1
@100
M=M+1
@6
0;JMP
