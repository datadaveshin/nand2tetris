## Notes on Videos
### Unit 5.3: Central Processing Unit
- 12:00 Instruction handling - The A-register can be fed from the
  - incoming instruction
  - the ALU output
  - Use the Mux16 to control this
  - Says of it's an A instruction, then load the A register from the incoming instruction
  - Says if it's a C instruction, we want to load the input of A from the ALU
  - Notes to use the op code
- 14:00 ALU input
  - Input x? comes from the D register
  - Input y? comes from the A or M registers
  - Above is controlled by the second Mux16
  - The Mux16 inputs comes from one of the control bits.
- 15:00 ALU Control
  - ALU needs to know what to do with the input, that comes from bits 6-11 of the instruction coming from the second Mux16.
  - Appears, zx would be 11, then down to no would be bit 6
- 16:00 ALU Output
  - ALU output is fanned out to 3 places:
    - A register via first Mux16
    - D register
    - M register via outM then inM
  - However, certain combinations are used from the Destination bits 3-5 of the instruction.
  - From the diagram, it appears that
    - A register uses the Destination bit 5 for it's load
    - D register uses the Destination bit 4 for it's load
    - M register use the Destination bit 3 via writeM, ie. assume, 0 to not write, 1 to write.
  - ALU also does 2 control outputs zr and ng.

- 18:00 Conrol logic of CPU itself
  - talks about the reset and PC
  - 21:00 focus on Jump bits 0-2 of the C-instruction
    - If all 3 are zero, it's a no jump situation, so set the PC trigger the inc
    - If all 3 are 1, then it's an unconditional jump situation, so then trigger the PC load to A
    - Any other combination is a conditional goto. If it is true, then PC=A, if false, then PC++.
    - Need to decide based on the jump bits, and the ALU output, if you want to load or not. This is the f() function in his slide.
  - The PC must always must emit the next instruction.


## Notes on PARTS
1. Mux16
```
* 16-bit multiplexor:
* for i = 0..15 out[i] = a[i] if sel == 0
*                        b[i] if sel == 1
*/

CHIP Mux16 {
   IN a[16], b[16], sel;
   OUT out[16];
```
1. Register
```
* 16-bit register:
* If load[t] == 1 then out[t+1] = in[t]
* else out does not change
*/

CHIP Register {
   IN in[16], load;
   OUT out[16];
```
1. ALU
```
* The ALU (Arithmetic Logic Unit).
* Computes one of the following functions:
* x+y, x-y, y-x, 0, 1, -1, x, y, -x, -y, !x, !y,
* x+1, y+1, x-1, y-1, x&y, x|y on two 16-bit inputs,
* according to 6 input bits denoted zx,nx,zy,ny,f,no.
* In addition, the ALU computes two 1-bit outputs:
* if the ALU output == 0, zr is set to 1; otherwise zr is set to 0;
* if the ALU output < 0, ng is set to 1; otherwise ng is set to 0.
*/

// Implementation: the ALU logic manipulates the x and y inputs
// and operates on the resulting values, as follows:
// if (zx == 1) set x = 0        // 16-bit constant
// if (nx == 1) set x = !x       // bitwise not
// if (zy == 1) set y = 0        // 16-bit constant
// if (ny == 1) set y = !y       // bitwise not
// if (f == 1)  set out = x + y  // integer 2's complement addition
// if (f == 0)  set out = x & y  // bitwise and
// if (no == 1) set out = !out   // bitwise not
// if (out == 0) set zr = 1
// if (out < 0) set ng = 1

IN
    x[16], y[16],  // 16-bit inputs
    zx, // zero the x input?
    nx, // negate the x input?
    zy, // zero the y input?
    ny, // negate the y input?
    f,  // compute out = x + y (if 1) or x & y (if 0)
    no; // negate the out output?

OUT
    out[16], // 16-bit output
    zr, // 1 if (out == 0), 0 otherwise
    ng; // 1 if (out < 0),  0 otherwise
```
### PC
```
/**
 * A 16-bit counter with load and reset control bits.
 * if      (reset[t] == 1) out[t+1] = 0
 * else if (load[t] == 1)  out[t+1] = in[t]
 * else if (inc[t] == 1)   out[t+1] = out[t] + 1  (integer addition)
 * else                    out[t+1] = out[t]
 */

CHIP PC {
    IN in[16],load,inc,reset;
    OUT out[16];
```
