# ALU Definition:
```
The ALU (Arithmetic Logic Unit).
Computes one of the following functions:
x+y, x-y, y-x, 0, 1, -1, x, y, -x, -y, !x, !y,
x+1, y+1, x-1, y-1, x&y, x|y on two 16-bit inputs,
according to 6 input bits denoted zx,nx,zy,ny,f,no.
In addition, the ALU computes two 1-bit outputs:
if the ALU output == 0, zr is set to 1; otherwise zr is set to 0;
if the ALU output < 0, ng is set to 1; otherwise ng is set to 0.
```

## Implementation
Here are the implementation details from the .hdl file:

The ALU logic manipulates the x and y inputs and operates on the resulting values, as follows:
```
if (zx == 1) set x = 0        // 16-bit constant
if (nx == 1) set x = !x       // bitwise not
if (zy == 1) set y = 0        // 16-bit constant
if (ny == 1) set y = !y       // bitwise not
if (f == 1)  set out = x + y  // integer 2's complement addition
if (f == 0)  set out = x & y  // bitwise and
if (no == 1) set out = !out   // bitwise not
if (out == 0) set zr = 1
if (out < 0) set ng = 1
```

So breaking it down into steps:
1. `if (zx == 1) set x = 0`: Use a `Mux16` gate with `zx` as the selector, letting `a=x` then `b=false`
2. `if (nx == 1) set x = !x`: First use `Not16` using the output from above. Then both the output from above and the flipped input from the `Not16` can then be used as an inputs into another Mux16, this time with `nx` as the selector.
3. `if (zy == 1) set y = 0` and `if (ny == 1) set y = !y`: Repeat above, but for the other original input.
4. `if (f == 1)  set out = x + y` Use `Add16` with the two outputs from steps 2 and 3 above and use the output in combination with step 5 within step 6 below.
5. `if (f == 0)  set out = x & y`: Use `And16` with the two outputs from steps 2 and 3 above and use the output in combination with step 4 within step 6 below.
6. Use outputs from steps 4 and 5 into a `Mux16` gate with `f` as the selector.
7. `if (no == 1) set out = !out`: Take the output from step 6 and feed it through a `Not16 gate`. Then use another `Mux16` gate, taking the `Not16` output as one input, along with the output of step 5 as the other. Use `no` as the selector. Here, we want to split the output in the following ways for the next steps. Make 3 sub buses `[0..7]` and `[0..8]` and `[15]` to use later, then also let the output be the output for the `ALU` chip overall.
8. `if (out == 0) set zr = 1`: Take the 2 sub buses `[0..7]` and `[0..8]` from step 7, and feed them thru `Or8Way` chips. Then take that output and put it through another `Or` chip. Only if all were zero in the beginning would we get zero at the end here. We can use that as the selector into a single `Mux1`, along with `true` and `false` as the inputs and output 1 or 0.
9. `if (out < 0) set ng = 1`: Use a `Mux` gate and the `[15]` sub bus output from the `Mux16` gate in step 7 as the selector, as this is the output for the ALU and `[15]` is the MSB, which if `true` signifies a negative number. Then we can use `true` and `false` as the inputs for this `Mux16` gate, so we can output 1 or 0.

- **Done** - File is `ALU.hdl`
