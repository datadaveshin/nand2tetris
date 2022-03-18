# Ch. 6
## Unit 6.1: Assembly Languages and Assemblers
### The assembler translates symbolic machine language to binary machine language
- First layer of software above hardware
- Our computer must run in binary machine language, for the assembler, for us, it is assumed there are other computers available, therefore, we can write the assembler in any language that we want to. Meaning, we have a second computer that can write out the binary machine language for our Hack computer. This is called `cross-compiling`.
- Basic idea is to go through the symbolic code line by line and translate it to binary code.
### General assembler logic
- Read a command
- Remove blank lines and comments
- Read the instructions into an array of characters
- Break the charaters into parts or fields
- Translate each field into binary using the language specification - ie. what is the code for each command
  - For commands, use a table, i.e. for Load below
  - For register addresses, also use a table, or translate
  - For other things like data and addresses, just translate to binary
```
Load  R1 18
11001 01 000010010
```
- Then put these parts back together, basically concatenation, plus perhaps some other types of bits according to the specification, or for padding, as sometimes there may not be all the bits necessary to match the word size, like the `11` in the C-instructions.
- Then output a file for the machine that will be used, using the file format that is specified.
### Handling Symbols
- Complication is how to deal with some symbols.
  - Labels: used to have a name as opposed to hardcode the address
  - Variables: used to specify addresses
- How is this done? By building a table for mapping symbols to binary
  - If the symbol is in the table, you can just read it
  - If the symbol is not in the table, you need to add it, but according to the specification, you must locate the correct memory location for which to `allocate` it
### Handling Labels
- When the label is declared in the code, nothing is executed
- When the label is found in a command, then the value of the label address must be known.
- Use a table again
- Additional problem: `Forward references` - a label may be found in code before it is defined, and thus won't appear in the table, similar to hoisting. Solutions:
  - Leave blank in main table, put it in a side table, and fix the main table later.
  - Do one pass of the code and fill the table, then do a second pass
## Unit 6.2: The Hack Assembly Language
### A instructions: basically translate symbol to binary:
- Can be non-negative integer or symbol referring to a constant
- MSB must be one
```
Symbolic syntax    
@value -> @21

Binary syntax
0valueInBinary -> 0101101110100000
```
### C instruction:
- Break into parts and translate
- Use the various specification tables for mapping
```
Symbolic syntax
dest = comp; jump

Binary syntax
111accccccdddjjj
```
### Symbols
- Various symbol types
  - Predefined: R0, R1... R15, Screen, SP, ARG, etc.
  - Label declaration (label)
  - Variable declaration (@valiableName)

### Assembly programming elements:
- Ignored items
  - White space (lines, indentation, omment lines, in-line comments) - note he counts comments as white space
- Instructions (A and C)
- Symbols
  - References
  - Label Declarations
### Dealing with symbols
- Makes a note to deal with them later, I think he means to build the assembler without symbols first, so:
- First: Deal with white space - ignore it
- Second: Translate instructions
### The plan:
1. Develop an assembler that takes care of symbol-less code
1. Develop the ability to handle symbols
1. Morph the basic assembler into one that can translate any Hack symbolic code.

## Unit 6.3: The Assembly Process - Handling Instructions
### Translating A instructions
- If MSB is 0 (opcode), all we need to do is
1. Translate the value
1. Fill in leading zeros so you have the remaining 15 bits
1. If value is a symbol, will deal with later
### Translating C instructions
1. Again, has symbolic syntax: `dest = comp ; jump` that corresponds to `111accccccdddjjj`
1. Follow the comp, dest and jump tables
- Example: Translate symbolic code `MD=D+1`
  - `MD` is the `dest` field
  - `D+1` is the `comp` field
  - `jump` is `null`
- Here, he wants the Parser to separate the instructions into the different fields
- For translation:
  - All C instructions start with `111`, start there
  - Next 7 bits are `acccccc`, and since it's `D+1` with an `a=0` leading bit, you can find the translation in the table
  - Next 3 bits are the destination, so look at the `dest` table so for `MD`, the string is `011`
  - Last 3 bits are for the jump, which is blank in the symbolic code, so looking at the `jump` table, you see that it is `000`
  - Question from video is translate `MD=A-1;JGE`:
    `111` + `0` + `110010` + `011` + `011`
- Overall assembly logic
  - Parse each instruction in the input file  
  - If it's an A-instruction, translate it into a binary value
  - If it's a C-instruction, for each field in the instruction, generate the corresponding binary code
  - Assemble all codes as 16 bits
- *Note*, this solution does not deal with Symbols!
## Unit 6.4: The Assembly Process - Handling Symbols
- Examples of Hack symbols:
```
@i
@sum
@R0
@STOP
(LOOP)
@R1
@LOOP // goto LOOP
(STOP)
(END)
```
- Symbols:
  - variables: memory locations
  - labels: destinations of goto instructions
  - pre-defined: special memory locations
- Note the programmer does not care where these memory locations are, lets assembler take care of it, so great abstraction
### Predefined symbols
- R0, R1, Screen, SP etc.
- These are only found as A-Instructions
- Therefore preceded by `@`
- Translating: Since A-instruction, just translate to binary, fill in leading zeros
### Labels
- Used to label destinations
- `(xxx)` is a pseudo command - is not translated into code, therefore, it will be skipped because:
- Defines the memory location `xxx` for the following command
- In his example `(LOOP)` is on line 3, `@i` on line 4. So, in a table, `LOOP` corresponds to address `4`
- Translating: Using table, replace `@labelSymbol` with it's table value, it's similar to an A-instruction
### Variable symbols
- Any symbol `xxx` appearing in the code that is not pre-defined elsewhere using (xxx) is treated as a variable
- Variables are assigned a unique memory address starting at 16
- Translating: Again, is an A-instruction, but since it's symbolized:
  - If it hasn't been seen before, assign it an address
  - If it has, then replace `@variableSymbol` with the `variableSymbol` value
### Simplify the process
Use a Symbol Table
- Start empty
- Initialize with all pre-defined symbols
  - There are 23
  - Do this before even looking at any code
- Then go thru code, and look thru for `(` for Labels
  - While you do this, keep track of how many lines you've read that are "real" instructions
  - Add the key value pairs
  - This is the "First" pass
- Now go to variables as the "Second" pass
  - Anything that is not in the table is a variable, starting at 16
  - So if exists, do nothing, if not, add it
- This is a auxilliary table, once it's done, you can toss it
### The assembly process
- Initialization:
  - Construct an empty symbol table
  - Add the pre-defined symbols
- First pass:
  - Scan program
  - For each "instruction" `(xxx)`, which is a label:
    - Add the pair (`xxx`: `address`), where address is the instruction following `(xxx)`
- Second pass:
  - Set `n` to `16`
  - Scan program
  - If instruction is `@symbol`, check the symbol table:
     - if the key:pair exists, complete the translation
     - if not found:
       -  Add the (symbol, n) to the symbol table
       - Use `n` to complete the instructions translation
       - `n++`
  - If C-instruction, complete the instructions translation
  - Write the translated instruction to output file
- Quiz:
What will symbol table contain after:
```
(LOCATION_1)
  @LOCATION_2
  D=M
(LOCATION_2)
  @LOCATION_1
  M=D
(LOCATION_3)
  @LOCATION3
  0;JMP
```
## Unit 6.5: Developing a Hack Assembler
### Subtasks
- Read and parse commands
  - Does not need to understand anything
  - Just the format
  - And break into components
  - What it needs to do:
    - Constructor for a Parser object, accepts a string specifying filename
    - Read text file
    - Get next command
      - are we finished? boolean `hasMoreCommands()`
      - get the next command `void advance()`
      - Need to read one line at a time
      - Need to skip whitespace and comments
    - Get fields of the current commands
      - Get type of command (A-command, C-command, Label)
      - Get easy access to fields, ie. `D`, `M+1`, `JGT`, or `@sum`. ie. `dest()` etc.
- Translate mneumonics to code:
  - Translate each part from symbolic code to machine code
  - Again, no need to know how the fields were obtained
  - ie. how to do `dest`, use the dest table, etc
  - remember the leading `111` bits
  - Example:
```
Assume command is D=M+1;JGT
c = parser.comp() // M+1
d = parser.dest() // D
j = parser.jump() // JGT
cc = code.comp(c) // 1110111
dd = code.dest(d) // 010
jj = 001
out = "111" + cc + dd + jj
```  
- Handling symbols
  - Does not need to know what machine language is or what symbols mean
  - Just maintain associations
  - What to do
    - Create an empty table
    - Add key value pairs
    - Does the table have the symbol
    - What is the address of the symbol
  - Steps
    - Start with empty
    - Add predifined symbols
    - While reading input, add labels and new variables to table
    - When you see `@xxx`, where `xxx` is not a number, consult the table, and replace the symbol `xxx` with address
  - Adding symbols:
    - While reading input, add labels and new variables
      - Label: see `(xxx)`, add `xxx` to table with the NEXT address of the the machine language command
         - Requires maintaining a `running_address`
         - May need to be done in a first pass
  - Adding variables:
    - When you see and `@xxx`, where `xxx` is not a number and not in the table, add `xxx` to the next address for variable allocation.  
- Overall Assembler
  - Initialization
    - Parser
    - Symbol table
  - First Pass: Read all commands, only pay attention to so labels and updating symbol table
  - Restart reading and translating commands
  - Main Loop
    - Get the next command and parse
    - For A-commands, Translate symbols to binary address
    - For C-commands, get code for each part and put together
    - Output machine language to a .hack file

## Unit 6.6: Project 6 Overview: Programming Option
### Developing the Hack Assembler
- Want's to call it HackAssembler
- Source program should be text and named `Xxx.asm`
- Generated code should should be text file `Xxx.hack`
- Assumption is that Xxx.asm is error free
- Usage: `./hack_assembler.py Xxx.asm`
- If rerun, it should overwrite `Xxx.hack`
### Proposed design
- Parser: unpacks instructions into fields
- Code: translates each field to binary value
- SymbolTable: manages the symbol table
- Main: initializes the I/O files and drives the process
  - He says this one deals with getting the input file
  - He says name this one the HackAssembler
- Says to use unit tests
### Proposed Implementation
#### Staged development
- Develop the basic assembler with no symbols
- Develop the ability to handles symbols
- Morph the basic assembler to one that can translate any program
#### Supplied test programs
- Again suggests unit testing
- Have several test programs that are provided: `Add.asm` etc.
- Add.asm: Used for testing
  - white space
  - instructions
  - says can add to the program to make it more exhaustive
- `Max.asm` - no symbols
  - More complicated
- `MaxL.asm` - uses symbols
  - The `L` has symbols, so same for Rectangle and Pong files
- `Pong.asm` and `PongL.asm` - use the CPU_Emulator
  - It has it's own assembler
  - It is 27000 lines, but it was compiled from the Jack Compiler from a 200 line program
  - Can view in binary or asm (to see commands)
  - When Pong starts, there is a lot of initializing of drivers, etc. so it runs for a while.
    - So run it with `no animation` and `fast`
#### Pong
- Written in Jack to compiler to asm, so it's different in the other test programs
- 28,374 lines
- It includes the Jack OS
- Machine code
  - no white spaces
  - strange addresses: `@256`
  - strange labels: `@END_EQ`
  - strange pre-defined symbols: `SP` stack pointer
- Above comes from the virtual machine
#### Testing options
- Use the supplied programs and your assembler to make the .hack files
- Use the `Hardware Simulator` to load the .hack files you generated and execute using either the `Computer.hdl` built-in chip, or the one you wrote.
- Use the `CPU Emulator` and your .hack files
- Use the supplied `Assembler` to translate .asm files and then compare those generated by your assembler.
  - You can do the comparison in the `Assembler` there are three panes... source, compare, and your assembly code
  
