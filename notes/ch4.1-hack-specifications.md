# Hack Machine Language
## Background
The Hack platform has 2 memory units (`data memory` and `instruction memory`)
- Each is 16 bits
- Each uses 15-bit addresses therefore have 2<sup>15</sup> addresses
- Think of them as linear sequences of addresses indexed from `0 ` to `32K - 1`, where 1 K is 2<sup>10</sup> or 1024.
- There are a series of buses that connect to the CPU (instruction bus, data bus, address bus)
### Memory:
#### Data Memory
- `Data memory` will be called `RAM`
- Data memory is a `read/write` device
- Each `register` is selected via the `address`
- The data memory's address input will always have ONE value, so a `register` is ALWAYS selected
- The selected `register` is referred to as `M`
- The Hack instruction `M=0` sets the selected `register` to `0`
#### Instruction Memory
- `Instruction memory` will be called `ROM`
- Instruction memory is a `read only` device
- Instructions are loaded exogenously
- Instruction's memory's address will always have ONE value, so a `register` is ALWAYS selected, and it's value is termed `current instruction`
### Registers:
- Hack instructions maniupulate 3 * 16-bit registers:
  - a `data register` denoted as `D`
  - an `address register` denoted as `A`
  - a selected data `memory register` denoted as `M`
- `D` stores a 16-bit value
- `A` works as both a data and address register.
- Instruction `@17` stores value `17` into the `A` register
- To set `D` to 17, we must peform:
```
@17
D=A
```
### Addressing:
- Hack Instruction `@xxx` sets `A` to `xxx`, with side effects:
  - makes register `xxx` the selected memory register `M`
  - makes register `xxx`in ROM the selected instruction
- Setting A thus stages either the ability to manipulate a the selected memory register or do something with the selected instruction
- Example: `Set value of RAM[100] to 17`
```
@17   # A serves as data register
D=A   
@100  # A serves as address register
M=D
```
- Example: `Set RAM[100] to RAM[200] value`
```
@200
D=M
@100
M=D
```
- Both examples, A did select instruction memory, but these were ignored
### Branching:
#### Unconditional Branching
To jump to an instruction that is out of sequence do (in this case jump to register 29):
```
@29     # Selects ROM[29]
@0;JMP  # GOTO ROM[29]
```
- Step `@29` also selects `RAM[29]`, but we don't do anything with it. `@0;JMP `
- Step `0;JMP` executes instruction in `A` register, which will be from `ROM[29]`
- The '0' prefix will be explained later, but we are assuming here that the program started at `ROM[0]`
#### Conditional Branching
For the equivalent of:
```
if D==0
    GOTO 52
```
Use:
```
@52
D;JEQ
```
- First you are setting `A` to `ROM[52]`
- Then "evaluate `D`", if it is `0`, then jump to address stored in `A`
#### Recap
- The `A` register through the command `@xxx`. We use it to focus on data memory register `M` and ignore the instruction, or focus on the selected instruction and ignore the data memory register.
### Variables:
- `xxx` in `@xxx` can be a constant (`17`) or symbol (`HERE`), where `HERE` is bound to some value (`18`). Regardless, `A` will be set to 17 or 18 depending what xxx was. The latter allows the use of `symbols` as `variables` over limiting to physical memory addresses.
- To do `let x = 17`:
```
@17
D=A
@x
M=D
```
- Need an agent to do the binding for `x` above, that's the assembler.
- Importance... if we want to increment a value with `@30,M=M+1`, we must use register `RAM30`. If we do `@count,M=M+1`, then we can have the assembler use any open RAM address. Just need to implement this for the assembler.
#### Hack built-in symbols
- Have 16 built in symbols: `R0`...`R15`, and are sometimes referred to as virtual registers.
- These are bound to `RAM[0]`...`RAM[15]`, respectively by the assembler
- `R3,M=0` will set `RAM[3]` to `0`
### Programming Examples
- Notes that all operations involving a memory location takes two steps:
  - `@addr` selects the target memory address
  - second instruction tells what to do with that address
- There are two generic instructions:
  - `A-instruction`, or "address instruction", which start with `@`
  - `C-instruction`, or "compute instruction", which is any non-A-instruction.
