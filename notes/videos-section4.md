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

## Video 4.4
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

## Video 4.5 Input / Output
For I/O to peripherals (keyboard / screen), the high-level approach uses a lot of software to deal with updates. The low-level approach still relies on bits:
- One approach is to use a "memory map" - a designated memory area for I/O managment.
- For example, a screen is continuously refreshed, so you manipulate the memory map for updates.
### Hack computer screen
- Black and white
- 256 x 512 columns
- Each row/column intersection is a pixel
- Assume 0 is off, 1 is on
- The memory map is a sequence of 16-bit values (or "word")
- So have 8k 16 bit words, ie. 8K * 16 gives the number (or close to it) number of pixels for our screen
- So 1 bit will refer to 1 pixel
- Therefore, for mapping, need to map which bit corresponds to which pixel, ie. one set is 8 x 1024 x 16 = 131072, the other 256 x 512 = 131072
- Problem is that every bit is bound in one word. ie. you can't just access one bit, you need to deal with the entire register of 16 bits, manipulate the bit, then give back the 16 bits.
- Map is first 32 registers corresponds to first row of screen, and so on
- To set a pixel (row,col), use `i = 32*row + col/16` (using integer division - throw away remainder), so
  - To use it directly `word = Screen[i = 32*row + col/16]`, where `Screen` is an 8K chip, and serves as a memory map
  - For the computer, `Screen` will be within the `RAM`, so need the base address also which for us is 16384, so `RAM[16384 = 32*row + col/16]`
  - Set the `(col%16)th` bit of `word` to `0` or `1`. col%16 is modular math
  - Then replace `word` in the `RAM`
- Can play around with the Screen.hdl file in tools/
### Hack keyboard
- Uses a single register `Keyboard`
- When a key is pressed, a `scan code` is sent to the keyboard memory map, ie. `A` == `65` in binary, or say `4` is `52` in binary
- When no key is being pressed, the number in the memory map is `0` in binary, this is how we can tell if it's being used.
- Thus to get the value of a keypress, check contents of `RAM[24576]`, which is the keyboard memory map register.

# Unit 4.6: Hack Programming, Part 1
Two ways to run symbolic code:
  - Translate it to binary using an assembler
  - Translate it into machine language and load it into a CPU Emulator: Therefore can use the emulator to execute and debug.

## Register and Memory:
Again:
- `D`: data register
- `A`: address or data register
- `M`: just a mneumonic for the currently selected memory register, `M=RAM[A]`
More examples:

```
// D=10
@10
D=A // Can't set D straight off the bat

// D++
D=D+1

// D=RAM[17]
@17
D=M

// RAM[17]=0
@17
M=0

// RAM[17]=10
@10
D=A  // D needs to acquire the value of A, since you can't set it directly
@17
M=D

// RAM[5] = RAM[3]
@3
D=M
@5
M=D
```

Example Add two numbers, ie. RAM[2] = RAM[1] + RAM[0]
```
@0
D=M
@1
D=M+D
@2
M=D
```
Upon translating and loading above:
- White space is ignored
- Comments are ignored
- Each command is actually "numbered" in the background, ie. the ROM registers are in sequence
- In the Simulator, you can see the commands in either symbolically and binary
- Demo's the simulator
- The program loaded into the simulator ROM is the `source code`
- The file extension is `.asm`
- Can see the code also in decimal, hex or binary
- Note, when using fast forward, the program will continue past the last line. I'm guessing then, we set the `reset` bit on the PC chip.
- Also notes that a hacker could put in downstream code with no stop, this is called `nop slide` attack. `nop` is null operation code, slide just means hide it downstream.
- So, we don't `reset`, we end our programs with an infinite loop, ie.
```
@6
0;JMP // Note here, can see the 0 prefix is the "comp" part of the C-instruction code
```
### Built-in Symbols
- R0...R15 for the internal registers, or `virtual registers`
  - Values are 0...15
  - Use them as so: `@R5` as opposed to `@5`, which is still valid but may be confusing to reader
 - Hack is case sensitive, therefore use `@R5` over `@r5`
- `SCREEN` and `KBD`, where latter is for keyboard. Respective values are `16384` and `24576`, and serve as the base addresses.
- Others are `SP`, `LCL`, `ARG`, `THIS`, `THAT`, with values 0...4. These are used for implementing the virtual machine in part 2.

## Unit 4.7: Hack Programming, Part 2
### Branching
- Example of if else statement:

```
// if R0>0
//    R1 = 1
// else
//    R1 = 0

@R0
D=M    // D=RAM[0]

@8
D;JGT  // If R0>0 Jump to 8

@R1
M=0    // RAM[1]=0
@10    // Start infinite loop
0;JMP  // END

@R1    // This would be line 8
M=1    // RAM[1]=1

@10    // Start infinite loop
0;JMP  // END
```

- To make it less cryptic, use an `@LABEL` declaration:
  - Label declarations are not translated
  - The references is passed to the instruction `@n` that follows the declaration

```
  // if R0>0
  //    R1 = 1
  // else
  //    R1 = 0

  @R0
  D=M    // D=RAM[0]

  @POSITIVE
  D;JGT  // If R0>0 Jump to 8, which is now under POSITIVE

  @R1
  M=0    // RAM[1]=0
  @END   
  0;JMP  // JUMP to 10 which is @END

(POSITIVE)
  @R1    // This would be line 8
  M=1    // RAM[1]=1

(END)
  @END
  0;JMP  // END
```
### Variables
- A container that holds a value
- For Hack, only one way to do it, setting a register
Example, a swap program:

```
// Swap RAM[0] and RAM[1]

// temp = R1
// R1 = R0
// R0 = temp

@R1
D=M
@temp
M=D   // temp = R1

@R0
D=M
@R1
M=D  // R1 = R0

@temp
D=M
@R0
M=D  // R0 = temp

(END)
@END
0;JMP
```

So here `@temp` means... find an available register (n), use it to represent `@temp`. Then any time you see `@temp` in the program, translated it to `@n`. How does this happen:
- A reference to a symbol with no label declaration is treated as a reference to a variable
- Variables are allocated to the `RAM` (in Hack) from RAM `address` `16` onward.
Benefits:
- This is easier to read than using typical memory addresses
- This is also `relocatable`, you don't have to load into `ROM` at `address` `0`, and need not worry about whether the addresses for `RAM` are available, as they are dynamically set. A `loader` takes care of these issues.

### Iterative processing
- Goes over the Sum 1 to n example in book.
- Goes over importance of psuedocode
- Even mentions debugging your psuedocode before coding
- Mentions using a `variable-value` `trace table` on paper, where you write the variables and values, and step your way though.

## Unit 4.8: Hack Programming, Part 3
### Pointers
- Starts with example of a simple program
```
for (i=0; i<n; i++)
  arr[i] = -1
}
```
- Notes that when writing a translator/compiler for this code that "arrays" get lost in translation when going to machine language, all you get are some memory locations for the base, and say the length of the array.
- Next is setting the registers for the values.
- ie. for setting up an array where values start at RAM[100], you'd have something like this:


| Var | Line | RAM |
| -- | --- | --- |
| | 0 | |
| arr | 16 | 100 |
|...|...|...|
|...|100|-1|
|...|101|-1|
|...|102|-1|
|...|103|-1|
|...|104|-1|
|...|...|...|

- Shows code around 4:00 in video
- Shows the arithmetic operation to increment the memory address by using `A=D+M`, where in the code you have:

```
// RAM[arr+i] = -1

@arr
D=M
@i
A=D+M // Here you are adding the array memory address and i
M=-1
```

- Variables that store memory addresses like `arr` and `i`, are called `pointers`
- Hack pointer logic: When we need to use a pointer to access memory, need an `A=M` instruction.
- Pointer semantics: "set the address register to the contents of some memory register"


### Input / Output
Hack RAM overview:

| RAM | Function | Bits | LABEL |
| -- | --- | --- |--- |
| 0 | Data Memory | 16K | ... |
| 16384 | Screen Memory Map | 8K | SCREEN |
| 24576 | Keyboard | 16 | KBD |

### Screen
- Note we have labels for screen and keyboard to make access easy
- Task at 11:30 - Make a rectangle on screen in upper left, 16 pixels wide, and let user choose width via `RAM[0]`
- Program is in tools/ called Rectangle.asm, and goes using the CPU emulator
- 20:00 or so, goes over the pseudocode, then code.

### Keyboard
- Mentions to get the key symbol, can `@24576`, then `D=M`, but can use the shortcut `@KBD`
- Notes that while when no key is pressed and then register contains 0, to do something more complex like take in a password, have to keep storing until you get the code for the "enter" key.

### Compilation
- The `compiler` allows you to translate high-level code to machine language. Example, going from the for loop to machine language.

## Unit 4.9: Project 4 Overview
Projects:
- Make a mulitplier, so use one of the numbers as a stopping point for loop.
- Make the screen go black if key is hit... so, set up an infinit loop, fetch KBD for 0 or 1, if 1, iterate through all registers for screen and set to 1.
  - Notes that need to address the memory using pointers
  - For testing, he says to select 'no animation' in the emulator, and to test manually, there's not test script.
  - Says for fun, instead of going row by row, can do col by col, or a swirl or something.
- Save files with `.asm` and convention is to have name of program to start with a capital letter... `Program.asm`
- Must use symbolic variables and labels
- Variables are `lowercase`
- Labels are `UPPERCASE`
- Can use indentation, white space is ignored

# Unit 4.10: Perspectives
- Question was, do you have to use two lines of code to do things in machine language for more powerful computers, answer was no, but the reason why we do it is we only have 16-bits to work with. Other machines have larger word lengths, or can combine them dynamically. Also, other machines can remember the current register that's being worked on and do more steps.
- Question, do people often write machine language... no, they use compilers to generate machine language. Caveat is for high-performance, but they often still use C first, then inspect the machine language
