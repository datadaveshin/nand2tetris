// File name: projects/04/Fillsandbox4.asm
// Method: Continually check the keyboard, and set state variable to white or stripes if pressed

(START)
// Set the index to the beginning of screen
@16384
D=A
@index
M=D

// Get the keyboard input, so we can set @state to 0 or -1 depending what the KBD value is
@KBD
D=M
// Jump to set the state to white if KBD = 0
@SET_STATE_WHITE
D;JEQ
// Else, set state to stripes and jump to the color screen loop
@state
M=D
@COLOR_SCREEN_LOOP
0;JMP
// Set state to white and move on
(SET_STATE_WHITE)
@state
M=0

// Start the screen index loop
(COLOR_SCREEN_LOOP)
  // Set the memory location of a screen register to state
  @index
  D=M
  @address
  M=D
  @state
  D=M
  @address
  A=M
  M=D

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

  // Go back to colorscreen loop if we haven't reached the end
  @COLOR_SCREEN_LOOP
  0;JMP
