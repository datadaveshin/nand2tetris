// File name: projects/04/Fillsandbox2.asm
// Method: Continually check the keyboard, and go to black or white loop depending if pressed

(START)
// Set the index to the beginning of screen
@16384
D=A
@index
M=D

// Get the keyboard input, and go to corresponding loop
@KBD
D=M
@WHITELOOP
D;JEQ
@BLACKLOOP
0;JMP

// Start the white screen loop
(WHITELOOP)
  // Set the memory location of a screen register to white
  @index
  D=M
  A=D
  M=0
  // Increment the index value
  @index
  M=M+1
  // Determine if we are at the end of the screen memory, if so, go to back to start
  @24576
  D=A
  @index
  D=D-M
  @START
  D;JEQ
  // Go back to white screen loop if we haven't reached the end
  @WHITELOOP
  0;JMP

// Start the black screen loop
(BLACKLOOP)
  // Set the memory location of a screen register to black
  @index
  D=M
  A=D
  M=-1
  // Increment the index value
  @index
  M=M+1
  // Determine if we are at the end of the screen memory, if so, go to back to start
  @24576
  D=A
  @index
  D=D-M
  @START
  D;JEQ
  // Go back to black screen loop if we haven't reached the end
  @BLACKLOOP
  0;JMP
