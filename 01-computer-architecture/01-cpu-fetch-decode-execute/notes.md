# The CPU as a machine (fetch, decode, execute)

Status: [ ] reading done   [ ] practice done   [ ] explained back

## The picture
The CPU is a clocked machine that does one loop forever: point at memory, read an instruction, work out what it means, do it, move on.

```
            clock (up to 180 MHz on the F446, one tick = 5.6 ns)
              |
   +--------+ | address  +-----------+  instruction bits  +-----------+
   |   PC   |----------->|   FLASH   |------------------->|  DECODER  |
   +--------+            | (program) |                    +-----------+
     ^    |              +-----------+                          | control signals:
     |    +--> PC + 2 or + 4 (next instruction)                 | which op, which registers
     |                                                          v
     |  branch target   +---------------+    operands     +---------+
     +------------------|   REGISTERS   |---------------->|   ALU   |--> flags N Z C V
                        | R0..R12 SP LR |<----------------|         |
                        +---------------+     result      +---------+
                                ^  load / store
                                v
                        +---------------+
                        | SRAM and      |
                        | peripherals   |
                        +---------------+
```

## Key ideas
- **Memory is a wall of numbered boxes.** An address picks a box. Code, data and peripherals all live in that one numbered space.
- **Registers are the CPU's hands.** 16 of them, 32 bits each, right next to the ALU. The ALU only works on registers; memory has to be loaded in first (load/store architecture).
- **PC (program counter, R15) is the finger on the recipe.** It holds the address of the next instruction. Three things move it: normal advance (+2 for a 16-bit instruction, +4 for a 32-bit one), a branch that writes a new address, and an exception or reset that loads an address from the vector table.
- **Fetch:** PC goes out on the instruction bus, flash sends back the instruction bits.
- **Decode:** the bits are a control word. They set the switches: which ALU operation, which registers feed it, where the result goes.
- **Execute:** the ALU computes, the result is written back to a register (or used as a memory address), and the N Z C V flags update if the instruction asks for it (the `S` in `ADDS`).
- **Flags are the memory of the last result:** N = negative, Z = zero, C = carry (for subtraction: no borrow), V = signed overflow. Conditional branches read them.
- **The very first PC comes from memory.** At reset the core reads address 0x0000_0000 into SP and 0x0000_0004 into PC. On the STM32 booting from flash, address 0 is an alias of flash at 0x0800_0000.
- **Cortex-M4 has separate buses for instructions and data** (I-Code, D-Code, System), so a fetch and a data access can happen at the same time, but there is one shared address map. This is called a modified Harvard design.
- **The M4 pipelines the loop in 3 stages** (fetch, decode, execute overlap), so simple instructions finish at about one per clock. Detail in sub-chunk 6.

### Worked trace (Thumb, all 16-bit, so PC moves by 2)

| Address | Instruction | After it runs | Flags N Z C |
|---|---|---|---|
| 0x0800_0100 | `MOVS r0, #5` | r0 = 5, PC = ..102 | 0 0 - |
| 0x0800_0102 | `MOVS r1, #3` | r1 = 3, PC = ..104 | 0 0 - |
| 0x0800_0104 | `ADDS r2, r0, r1` | r2 = 8, PC = ..106 | 0 0 0 |
| 0x0800_0106 | `SUBS r3, r1, r0` | r3 = 0xFFFF_FFFE (-2), PC = ..108 | 1 0 0 (borrow, so C = 0) |
| 0x0800_0108 | `B 0x0800_0104` | PC = 0x0800_0104, loops forever | unchanged |

### Why it matters for control work
At 180 MHz a 20 kHz control loop has 180 000 000 / 20 000 = **9 000 cycles** per period. ADC read, Clarke/Park, PI, and PWM update all have to fit inside it. "Roughly one simple instruction per cycle" is the first number you budget with; sub-chunks 7 and 8 show what makes it worse.

## Read
- Harris & Harris (ARM Edition), microarchitecture chapter: the single-cycle processor (datapath + control). Record the section numbers you used.
- Patterson & Hennessy (ARM Edition), "The Processor" chapter opening, as a second angle.
- PM0214: the processor core register summary and the xPSR (APSR flags) description.

## Practice
Paper trace, no board needed. Predict PC, r0 to r3 and N Z C after each line, then check it in GDB later with `stepi`.

```
0x0800_0200  MOVS r0, #10
0x0800_0202  MOVS r1, #10
0x0800_0204  SUBS r2, r0, r1
0x0800_0206  ADDS r3, r2, #1
0x0800_0208  B    0x0800_0204
```

| Prediction | Result | Why they differ |
|---|---|---|
| | | |

## Interview questions
1. Walk me through what the CPU does to execute one instruction.
2. What is the program counter, and what are all the things that can change it?
3. Where does the CPU get its very first instruction address after reset?
4. Harvard vs von Neumann: which is the Cortex-M4, and what does that buy you?
5. What are the N, Z, C, V flags, and how does a conditional branch use them?
6. Your control loop runs at 20 kHz on a 180 MHz MCU. How many cycles do you have, and what eats them?

## Explain it back (5 lines, no peeking)
1. _to fill_
2. _to fill_
3. _to fill_
4. _to fill_
5. _to fill_

## Still unclear
- _to fill_
