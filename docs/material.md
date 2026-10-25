# Material

Only free or open material. Everything here can be read or downloaded for nothing: vendor manuals, open-licensed books, and free articles. Section numbers move between revisions, so each sub-chunk's `notes.md` records the exact sections you used.

To get the vendor PDFs onto your laptop in one go, run `tools/fetch-docs.ps1` (Windows) or `tools/fetch-docs.sh` (Linux, macOS, WSL). They download into `docs/pdf/`, which git ignores. The PDFs aren't stored in the repo because ST, ARM and NXP own them; the links always point to the current revision.

## Always open

| Document | What it is for |
|---|---|
| [RM0390, STM32F446 reference manual](https://www.st.com/resource/en/reference_manual/rm0390-stm32f446xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) | Every peripheral and register. The main manual. |
| [STM32F446xC/E datasheet (DS10693)](https://www.st.com/resource/en/datasheet/stm32f446re.pdf) | Pins, alternate functions, clock and voltage limits, wait states per clock. |
| [PM0214, Cortex-M4 programming manual](https://www.st.com/resource/en/programming_manual/pm0214-stm32-cortexm4-mcus-and-mpus-programming-manual-stmicroelectronics.pdf) | Core registers, instruction set, exceptions, NVIC, SysTick, MPU, FPU. |
| [ES0298, STM32F446 errata](https://www.st.com/resource/en/errata_sheet/es0298-stm32f446xx-device-errata-stmicroelectronics.pdf) | Known silicon bugs. Skim once, check again when something makes no sense. |
| [UM1724, Nucleo-64 user manual](https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf) | Board wiring: LED on PA5, user button on PC13, ST-LINK virtual COM port on USART2. |

## Open books used across topics

| Book | License | Used for |
|---|---|---|
| [*Dive into Systems*](https://diveintosystems.org/book/) (Matthews, Newhall, Webb) | CC BY-NC-ND 4.0, free online | Architecture, pipelining, memory hierarchy, C, binary representation, OS basics |
| [*Modern C*](https://gustedt.gitlabpages.inria.fr/modern-c/) (Jens Gustedt), [free PDF](https://hal.inria.fr/hal-02383654) | CC BY-NC-ND 4.0 | The C language in depth |
| [*Beej's Guide to C Programming*](https://beej.us/guide/bgc/) | free online | A friendlier C walkthrough |
| [*Operating Systems: Three Easy Pieces*](https://pages.cs.wisc.edu/~remzi/OSTEP/) (Arpaci-Dusseau) | free online | Scheduling, concurrency, locks, semaphores |
| [*Mastering the FreeRTOS Real Time Kernel*](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book) | open source on GitHub | How a production RTOS kernel works |
| [*Computer Organization with ARM64*](https://rdw.rowan.edu/textbooks/2) (Bergmann) | CC NonCommercial | Optional: number representation, machine code, memory hierarchy (64-bit ARM, so concepts only) |

## Topic 1: Computer architecture

- *Dive into Systems*, [chapter 5, computer architecture](https://diveintosystems.org/book/C5-Arch/index.html): the von Neumann model, building a processor, instruction execution, pipelining.
- *Dive into Systems*, [chapter 11, storage and the memory hierarchy](https://diveintosystems.org/book/C11-MemHierarchy/index.html).
- *Dive into Systems*, [chapter 4, binary and data representation](https://diveintosystems.org/book/C4-Binary/index.html): endianness, two's complement.
- [DUI0553, Cortex-M4 Devices Generic User Guide](https://developer.arm.com/documentation/dui0553/latest/) (ARM): the programmer's model, memory model, instruction set.
- [Cortex-M4 Technical Reference Manual](https://developer.arm.com/documentation/100166/0001) (ARM): the 3-stage pipeline, instruction timing, the DWT cycle counter.
- [AAPCS, Procedure Call Standard for the Arm Architecture](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst): argument passing and callee-saved registers.
- Azeria Labs, [Writing ARM Assembly](https://azeria-labs.com/writing-arm-assembly-part-1/) (7-part series): 32-bit ARM assembly, registers, memory access, branches, the stack.
- Memfault Interrupt, [From Zero to main(): Bare metal C](https://interrupt.memfault.com/blog/zero-to-main-1): memory layout and startup.

## Topic 2: Embedded C

- [*Modern C*](https://gustedt.gitlabpages.inria.fr/modern-c/) and [*Beej's Guide to C*](https://beej.us/guide/bgc/): pointers, types, memory.
- *Dive into Systems*, [chapter 2, a deeper dive into C](https://diveintosystems.org/book/C2-C_depth/index.html): the stack, the heap, pointers, structs.
- Barr Group, [*Embedded C Coding Standard*](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) (free download): a practical style and safety baseline.
- Elecia White, [making-embedded-systems](https://github.com/eleciawhite/making-embedded-systems) (free companion repo): example code for state machines and embedded patterns.

## Topic 3: Microcontroller interfacing (GPIO, ADC, timers)

- RM0390: RCC (clocks), GPIO, ADC, general-purpose timers (TIM2 to TIM5), advanced timers (TIM1, TIM8).
- Datasheet: the alternate-function table and the ADC electrical characteristics.
- cpq, [*Bare Metal Programming Guide*](https://github.com/cpq/bare-metal-programming-guide): register-level GPIO, UART and SysTick on a Nucleo.

## Topic 4: Communication protocols (UART, SPI, I2C)

- RM0390: the USART, SPI and I2C chapters.
- NXP, [UM10204, *I2C-bus specification and user manual*](https://www.nxp.com/docs/en/user-guide/UM10204.pdf): the real I2C spec.
- Texas Instruments, [SLVA704, *Understanding the I2C Bus*](https://www.ti.com/lit/an/slva704/slva704.pdf): open-drain lines, addressing, read and write sequences.
- Analog Devices, [*Introduction to SPI Interface*](https://www.analog.com/en/resources/analog-dialogue/articles/introduction-to-spi-interface.html): modes, clock polarity and phase.
- The datasheet of every sensor you wire up (for example an IMU such as the MPU-6050 or BMI160).

## Topic 5: Interrupts

- PM0214 and [DUI0553](https://developer.arm.com/documentation/dui0553/latest/): exception model, entry and return, NVIC, priority grouping.
- RM0390: the interrupts and events chapter (vector table, EXTI).
- Memfault Interrupt, [A Practical guide to ARM Cortex-M Exception Handling](https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic).

## Topic 6: ARM architecture

- [DDI0403, ARMv7-M Architecture Reference Manual](https://developer.arm.com/documentation/ddi0403/latest/) (free, an Arm account may be needed to download): the formal spec behind the Cortex-M4.
- [Cortex-M4 Technical Reference Manual](https://developer.arm.com/documentation/100166/0001).
- Memfault Interrupt, [How to debug a HardFault on an ARM Cortex-M MCU](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug).
- RM0390: the embedded flash memory interface (erase and program sequence), for the bootloader.
- ST, [AN2606, system memory boot mode](https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf): the chip's built-in bootloader, to compare against yours.

## Topic 7: RTOS

- [*Operating Systems: Three Easy Pieces*](https://pages.cs.wisc.edu/~remzi/OSTEP/): CPU scheduling (chapters 7 and 8), concurrency and threads (26), locks (28), condition variables (30), semaphores (31), concurrency bugs (32).
- [*Mastering the FreeRTOS Real Time Kernel*](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book): tasks, queues, semaphores, priority inheritance, in a real kernel.
- [DUI0553](https://developer.arm.com/documentation/dui0553/latest/) and PM0214: PendSV, SysTick, the two stack pointers (MSP, PSP). This is what a context switch uses.
- Glenn Reeves (JPL), [What really happened on Mars](https://www.cs.unc.edu/~anderson/teach/comp790/papers/mars_pathfinder_long_version.html): the Pathfinder priority-inversion bug, told by the engineer who fixed it.

## Tools (all free)

- `arm-none-eabi-gcc`, `objdump`, `nm`, `size`, `make` ([Arm GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads))
- [OpenOCD](https://openocd.org/) and `arm-none-eabi-gdb` (the Nucleo's ST-LINK is the debug probe)
- A serial terminal (PuTTY, or `screen`)
- Later: a logic analyzer or scope for protocol waveforms and timing
