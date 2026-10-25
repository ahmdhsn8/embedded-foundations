# Material

Everything on the shelf, by topic. Explanatory reading builds the picture; the manuals are the ground truth. Free ST and ARM PDFs: search the document number on st.com or developer.arm.com. Section numbers move between editions, so each sub-chunk's `notes.md` records the exact sections you used.

## Always open

| Document | What it is for |
|---|---|
| **RM0390** (STM32F446 reference manual) | Every peripheral and register. The main manual. |
| **STM32F446xC/E datasheet** | Pins, alternate functions, clock and voltage limits, wait states per clock. |
| **PM0214** (Cortex-M4 programming manual) | Core registers, instruction set, exceptions, NVIC, SysTick, MPU, FPU. |
| **STM32F446 errata sheet** | Known silicon bugs. Skim once, check again when something makes no sense. |
| **UM1724** (Nucleo-64 user manual) | Board wiring: LED on PA5, user button on PC13, ST-LINK virtual COM port on USART2. |

## Topic 1: Computer architecture

- Harris & Harris, *Digital Design and Computer Architecture: ARM Edition*: architecture, microarchitecture and memory-system chapters.
- Patterson & Hennessy, *Computer Organization and Design: ARM Edition*: the processor (pipelining) and memory hierarchy chapters, for depth.
- Yiu, *The Definitive Guide to ARM Cortex-M3/M4*: registers, memory map, instruction set, stack.
- AAPCS (ARM Procedure Call Standard): argument passing and callee-saved registers.
- Cortex-M4 Technical Reference Manual: the 3-stage pipeline, instruction timing, the DWT cycle counter.
- Memfault Interrupt blog, "From Zero to main()" series: memory layout and startup.

## Topic 2: Embedded C

- Kernighan & Ritchie, *The C Programming Language*: the language itself, pointers chapter above all.
- Elecia White, *Making Embedded Systems*: structure, state machines, fixed-point math, real-world habits.
- James Grenning, *Test-Driven Development for Embedded C*: unit testing embedded code on the PC.
- Barr Group, *Embedded C Coding Standard* (free PDF): a practical style and safety baseline.
- MISRA C (reference only): know what it is and why industry uses it.

## Topic 3: Microcontroller interfacing (GPIO, ADC, timers)

- RM0390: RCC (clocks), GPIO, ADC, general-purpose timers (TIM2 to TIM5), advanced timers (TIM1, TIM8).
- Datasheet: alternate-function table and ADC electrical characteristics.
- *Bare Metal Programming Guide* (cpq, free on GitHub): register-level GPIO, UART and SysTick on a Nucleo.
- White, *Making Embedded Systems*: the peripherals and the sampling chapters.

## Topic 4: Communication protocols (UART, SPI, I2C)

- RM0390: USART, SPI and I2C chapters.
- NXP **UM10204**, *I2C-bus specification and user manual* (free): the real I2C spec.
- Analog Devices, "Introduction to SPI Interface" (free article): modes, clock polarity and phase.
- The datasheet of every sensor you wire up (for example an IMU such as the MPU-6050 or BMI160).

## Topic 5: Interrupts

- PM0214: exception model, exception entry and return, NVIC, priority grouping.
- RM0390: interrupts and events chapter (vector table, EXTI).
- Yiu: the exceptions and interrupts chapters.
- Memfault Interrupt, "A Practical guide to ARM Cortex-M Exception Handling".

## Topic 6: ARM architecture

- ARM **DDI0403**, *ARMv7-M Architecture Reference Manual*: the formal spec behind the Cortex-M4.
- Cortex-M4 Technical Reference Manual.
- Yiu: fault handling, MPU, SVC and the OS-support chapters.
- Memfault Interrupt, "How to debug a HardFault on an ARM Cortex-M MCU".
- RM0390: embedded flash memory interface (erase and program sequence) for the bootloader.
- ST **AN2606**: the chip's built-in system-memory bootloader, to compare against yours.

## Topic 7: RTOS

- Jonathan Valvano, *Real-Time Operating Systems for ARM Cortex-M Microcontrollers*: building a kernel from scratch.
- Yiu: the PendSV and OS-support chapters (context switching).
- *Mastering the FreeRTOS Real Time Kernel* (free PDF): how a production kernel solves the same problems.
- Giorgio Buttazzo, *Hard Real-Time Computing Systems*: scheduling theory (rate-monotonic, EDF).
- The Mars Pathfinder priority-inversion write-ups: the classic real-world failure.

## Tools

- `arm-none-eabi-gcc`, `objdump`, `nm`, `size`, `make`
- OpenOCD and `arm-none-eabi-gdb` (the Nucleo's ST-LINK is the debug probe)
- A serial terminal (PuTTY, or `screen`)
- Later: a logic analyzer or scope for protocol waveforms and timing
