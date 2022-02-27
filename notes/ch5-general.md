# Chapter 5

## Section 5.1
### CPU
- Consists mainly of
  - `ALU` for operations
  - A set of `registers`, we use these instead of memory to prevent `starvation`, which is a condition where the ALU is very fast, but round trips for data further away in the computer hamper it's speed. Thus we use registers within the CPU for temporary interim values.
  - A `control unit`. Instructions are given as binary codes, so the control unit must decode the instructions then route the code to the specified hardware (ALU, registers, memory) within the CPU

## Section 5.2 Hack Specification
Hack consists of a CPU, Instruction Memory, Data Memory, Screen I/O, Keyboard I/O
- Instruction memory is a ROM chip
- CPU consists
  - ALU - The ALU from ch. 2
  - Data Register (D)
    - Basically a `Register` chip
    - It stores only Data values
  - Address Register (A)
    - A `Register` chip from ch. 3
    - It can:
      - Store Data values
      - Select an address in Instruction memory
      - Select an address in Data memory
  - Program Counter (PC) - PC chip from ch 3.

Hack must use the Hack machine language:
- `A` instructions are loaded into the `A register`
- `C` instructions are a bunch of control bits

### CPU
- Again `CPU` has the `ALU`, `A` and `D` registers, and `PC`
- CPU fetches from Instruction memory
- CPU reads/writes from Data memory
- `inM` and `outM` hold the `M` values from `C-instructions`
- `addressM` has the address that `outM` should be written to
- Flow
  - If instuctions is an `A` - then CPU loads the 16 bit value to the `A register`
  - If instruction is a `C` - then:
    - CPU causes `ALU` to perform an operation
    - `CPU` causes the value to be stored into `A`, `D`, `M` `destination registers`, depending on the instruction
    - If one of the C-instructions says to work with `M`, then `outM` is set to the `ALU` output, and `writeM` is set to `1`
    - Else, any value can appear in `outM` and `writeM` is set to `0`
  - If `reset` is `0`, the `CPU` uses the `ALU` output and the `jump` bits of the current instruction to fetch the next instruction
  - Else `CPU` sets `PC` to `0`, later, `PC` will be plugged into the instruction memory.
  - The outputs `outM` and `writeM` are combinational, the outputs `addressM` and `PC` are clocked, with caveat, they are hooked to the instruction, but new values are commited in the the next clock cycle.

  
