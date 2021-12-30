# Chapter 4 Machine Language
Here we focus on machine language and assembly language to gain a better understanding of the requirements for our CPU and other last parts of the computer.

The languages are machine dependent. One could say that the languages depend on the machine hardware configuration, or that the hardware configuration depends on the machine language specification.

The final parts of our hardware consist of:
1. Memory: a sequence of "cells", or "locations", or "memory registers" to handle storing data or instructions, where each part has a specific address.
1. Processor: This is normally termed the Central Processing Unit (`CPU`). It is responsible for primitive actions (simple arithmetic or logical operations), memory access, and control or "branching" operations. It draws input and output from chosen registers. Thus, it is built from an `ALU` and contains it's own set of `Registers`. It can read and execute binary instructions.
1. Registers: For speed, a built in set of registers are used to shuttle data between the memory and processor. These are located within the processor chip to increase speed. There are two types of registers:
  - Data registers for holding data
  - Address registers that can be used to interpret data or addresses, ie. for an n-bit value in the address register will select and allow the fetching of data within the register it addresses.

## Languages
The language to use for communication can be binary or symbolic. An example of an instruction for the operation `set R1 to the value of R1 + R2` is given in the text. It shows that the syntax must be agreed upon ahead of time, the 16-bit instruction is divided between the most and least significant bits in this example.

The MSBs for "addition" in the example are `101011`. However, I looked back to the ALU specification, and can see that for our ALU, it would be `000010`.

The example then shows the registers addressed for `R1` and `R2`, respectively as `00001` and `00010`. I noticed that our `RAM64` chip uses 6-bit addresses, but I'll assume here that we will use these for our internal `CPU` registers anyway, perhaps leaving the MSB for those registers to take in input from a multiplexor such that we can separate out whether we are fetching a value or it's an instruction, or we will have less registers, say from our `RAM8` chip, where the extra bits can be used for other things. Just guessing here.

You can see though, when putting these bits together, you end up with `0000100000100010`. Given many instructions, this is tough for humans to debug, so we humans turned to symbolic representations of the addresses (`R1`, `R2`, etc.) such that they could write code more easily, ie. something like `add R2,R1` as shown in their example.

At first this was done on paper only, but then why not have the computer do it, and using shorter symbols like `+`.

This requires a `translator`, another program to translate the symbolic code into binary code. Symbolic languages are therefore referred to as `assembly languages`, and the `translator` is called an `assembler`.

Additionally, say we wanted to access memory location 129, ie. through some symbolic command like Mem[129], we could substitute some word, like "index" to always refer to Mem[129] to fetch it's value, giving the ability to do commands like `add 1, index`.

Later, high-level languages were built from this foundation. Note however, these latter languages are designed to be machine independent so that they can be used on any platform, whereas machine language is machine dependent. `Compilers` provide the translation from high-level languages to machine language.


## Instructions:
### Arithmetic and logic
The book again notes that every machine language includes instructions for basic arithmetic (addition, subtraction), and logical operations, and gives a little example:
```
load R1, 17 # set register 1 to the binary value of 17
load R2, 4  # set register 2 to the binary value of 4
add R1, R1, R2 # add register 1 and register 2 values, and set the sum to Register 1
```
### Memory Access
Usually `address registers` are used to get and set values in specific memory locations, they call it `A` here. `Memory registers` that hold addresses will be called `M` and is the memory register selected by `A`

To set a value, you would do:
```
load A,17
load M,1 # Here 1 is loaded to the register with address 17
```
Sets 50 memory locations 200, 201, 202.... to 1 (though, we don't know the code for the loop yet):
```
load A,200
---- loop start # added this part for clarity
load M,1
add A,A,1
---- loop end # added this part for clarity
```
### Flow control
Under usual circumstances the program follows the next instruction using an incrementation of the binary address of the current instruction (presumably via the `PC` chip). Sometimes, you may need to `jump` to another address because of a condition, or instruction. This is called `branching`. This is done by machine language conditional and unconditional `goto` instructions.

### Symbols
Both the binary and symbolic versions of machine language perform the same instructions and can be used, however, the binary that is translated from symbolic references can be used within any available memory. Therefore, code that does not contain the specific addresses to be targeted is termed `relocatable`. This allows more freedom, giving the ability to execute code dynamically. For example, for a loop, you could say `goto 20`, but if you had a marker, say called `LOOP`, you could say `goto LOOP`.
