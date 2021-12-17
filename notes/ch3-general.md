# Chapter 3 Memory
Chapter 3 focuses on building memory. In the previous chapters, the tools we built are referred to as `combinational chips`. The values that they output depending on input are done without delay (other than the time it takes for information to flow through internally).

In this chapter, we will look at chips that store their values over time, with the ability to set that value upon which time, the value can be set again upon our wishes.

The memory chips we will be building are termed `sequential chips`, as the output will depend on the input of the current time, along with input that were passed in at a previous time. Thus, you can say that combinatorial chips are time-independent, and sequential chips are time-dependent.

The "current" and "previous" time states will be controlled by a "clock", where binary changes (or not) are delivered on a continuous basis with discreet time periods called `tick` and `tock`. The time from the start of tick, and the end of tock, is termed one `cycle`. Each cycle will regulate the changes in memory for the computer.

For this chapter, we will build memory "registers", build those up to random-access memory (RAM) units, and make a counter.

We will also build a Program Counter (PC) chip, this will aid in our machine and assembly language abilities to execute programs.

Apparently, at this point, we will have all the components to build a computer.

## Memory devices
Hardware systems support the ability for memory devices to "maintain state". Simple chips do not have the concept of time or state, so this must be modeled.

To do this for this project, we will be given a clock and a time-dependent logic gate, a `Data Flip-Flop (DFF)`, that can `flip` and `flop` between 0 and 1.

To build registers, we'll start off with a one-bit register that utilize the DFF. Then move to n-bit registers, then to RAM units. Within this, we will also use an `address`, to access any single n-bit register within the RAM units, allowing the ability to set or fetch a value basically instantaneously.

The PC will orchestrate instructions later on in the course.
