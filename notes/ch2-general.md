# Chapter 2
Chapter 2 focuses on building some Adders from our gates, an incrementer, and an Arithmetic Logic Unit (ALU). The idea is we want to be able to add binary numbers using the gates we made in chapter 1. In this case, 16 bit numbers. 

Some terminology:
For the 8-bit binary number `10101110`, the first or furthest left `1` is the most significant bit (MSB), and the last or furthest right bit is the least significant bit (LSB).

"Word size" is used to describe how many bits we will use, which is generally a power of 2.

Additionally, we have the terms
- `byte` for 8-bit word sizes
- `short` for 16-bit word sizes
- `int` for 32-bit word sizes
- `long` for 64-bit word sizes

You can have 2<sup>n</sup> combinations for a word size of n

For one byte, we can have 2<sup>8</sup> = 256 combinations. This could assign the numbers 0 to 255 (reminscent of RGB values), which is 0 to 2<sup>n</sup> - 1. 

Or, if you wanted negative numbers, you could allow say -127 to 128 (given you'd also want zero in the set).

Remember, the computer has to convert between binary (which it understands) to decimal (which we forced ourselves to understand simply because of the numbers of fingers on our hands).

## Adding Binary numbers
To add two binary numbers, you need to account for going over the limit of available numbers (in this case `1`, as opposed to `9` in decimal systems) and "carry" that to the next position immediately to the left:

```
 11 11    Carry
 10101110 1st 8 bit number x
 00101100 2nd 8 bit number y
 --------
101011010 Sum

^Ignored overflow bit
```
Moreover, since there are only 8 bits allowed, we will have to ignore or deal with the bit that "overflowed" what is termed our "word length" of 8. For this course, we will ignore it. But in the real world it will be dealt with, where there will be some form of tethering (in this case 8-bit) registers of memory.

Thus to perform our math, we will build:
- A `halfAdder` that performs the addition of only 2 1-bit numbers - outputing the Sum and the Carry
- A `fullAdder` that performs the addition of only 3 1-bit numbers the original two numbers, and the Carry)
- The we will build a `Add16` chip, that performs addition as shown above but with 16-bits
- An incrementer that adds 1 to a binary number. We can do this with the `Add16`, but apparently, having a separate chip to do this later on will save us an extra step.

Note, we also want to have the ability to deal with negative numbers in convenient fashion.

## Dealing with negative numbers
To lessen the complexity of splitting our 2<sup>n</sup> numerical values allowed for an n-bit word size, the trick we are using in this course is the "two's complement" or the "radix complement".

Here, the binary code for negative x is 2<sup>n</sup> - x. 

They provide the example that -7 in a 4-bit system can be represented with what would be "9" or `1001`. We get this via the formula above 2<sup>4</sup> - 7 = 9.

Referring to figure 2.1. in the book, you will see that what happens is that by using this system is that: 
- The MSB for the negative numbers are always 1
- The MSB for positive numbers is always 0
- The number range will be from -(2<sup>n-1</sup>) to 2<sup>n-1</sup> - 1
- The trick to get negative x from x, is to take the binary code for x, then:
  - leave all the LSB 0-bits alone
  - leave the first LSB 1-bit alone
  - flip the remaining bits (1 to 0, and 0 to 1)

## The ALU
We will then build the Arithemetic Logic Unit to manipulate 16-bit binary numbers.

The ALU will be pretty simple, it will be designed to things like add two binary integers, but skip floats. It will also perform logic operations. 

The design is such that the ALU will take in a series of binary inputs to decide which of 18 total functions to perform, including besides two complement addition: zeroing input, negating input, performing an AND operation.

It will also output two additional bits, one to tell if the output is zero, and one to tell if the output is negative.

