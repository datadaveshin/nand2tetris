# RAM8 Definition:
```
Memory of 8 registers, each 16 bit-wide. Out holds the value
stored at the memory location specified by address. If load==1, then
the in value is loaded into the memory location specified by address
(the loaded value will be emitted to out from the next time step onward).
```

## Discussion
So here we are going to make an 8 register RAM unit. The idea is that a 16-bit input will be sent to all registers within the RAM chip, but, you only want to set one if there is a load instruction, and that will be accompanied by an address to instruct which of the registers will receive the new input.

## Implementation
- Here, again we can use a multiplexor to set the address of the register that may or may not recieve input depending on whether the `load` is 1. Since there are 8 registers, we can use a DMux8Way chip. Where the input for `load` is load, the 3-bit address is used for `sel`, and thus the `out` will become the `load` for one of the Registers.
- All registers recieve `in`, but because of the `load` they recieve from the DMux8Way, only one will be loaded. They still all output through `out`.
- Finally, we use a Mux8Way16 for the output. You set each input to one of the registers (respectively), use the address again for `sel`, then simply take the output for the Bit `out`.
- **File** is `RAM8.hdl`

## Image
- Pictured is an 8 register RAM unit:

!["RAM8"](../img/project-03.3-Ram8.png)
