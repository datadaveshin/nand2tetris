// File name: projects/04/Fillsandbox.asm
// SETS SCREEN JUST TO blackens

// Set the value of index to the beginning of screen register
@16384
D=A
@index
M=D
// Start the blacken screen index loop
(LOOP)
  // Set the memory location of a screen register to black
  @index
  D=M
  A=D
  M=-1
  // Increment the index value
  @index
  M=M+1
  // Determine if we are at the end of the screen memory, if so, go to end
  @24576
  D=A
  @index
  D=D-M
  @END
  D;JEQ
  // Go back to blacken screen loop if we haven't reached the end
  @LOOP
  0;JMP
// Infinite loop
(END)
@STOP
0;JMP
