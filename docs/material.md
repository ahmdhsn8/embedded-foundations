# Material

Everything on the shelf, by topic, with links. **Free** marks things you can download or read for nothing; the books are paid. Section numbers move between editions, so each sub-chunk's `notes.md` records the exact sections you used.

To get all the free PDFs onto your laptop in one go, run `tools/fetch-docs.ps1` (Windows) or `tools/fetch-docs.sh` (Linux, macOS, WSL). They download into `docs/pdf/`, which git ignores. The PDFs are not stored in the repo because ST, ARM and NXP own them; the links always point to the current revision.

## Always open (free)

| Document | What it is for |
|---|---|
| [RM0390, STM32F446 reference manual](https://www.st.com/resource/en/reference_manual/rm0390-stm32f446xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) | Every peripheral and register. The main manual. |
| [STM32F446xC/E datasheet (DS10693)](https://www.st.com/resource/en/datasheet/stm32f446re.pdf) | Pins, alternate functions, clock and voltage limits, wait states per clock. |
| [PM0214, Cortex-M4 programming manual](https://www.st.com/resource/en/programming_manual/pm0214-stm32-cortexm4-mcus-and-mpus-programming-manual-stmicroelectronics.pdf) | Core registers, instruction set, exceptions, NVIC, SysTick, MPU, FPU. |
| [ES0298, STM32F446 errata](https://www.st.com/resource/en/errata_sheet/es0298-stm32f446xx-device-errata-stmicroelectronics.pdf) | Known silicon bugs. Skim once, check again when something makes no sense. |
| [UM1724, Nucleo-64 user manual](https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf) | Board wiring: LED on PA5, user button on PC13, ST-LINK virtual COM port on USART2. |

## Topic 1: Computer architecture

- Harris & Harris, [*Digital Design and Computer Architecture: ARM Edition*](https://shop.elsevier.com/books/digital-design-and-computer-architecture/harris/9780128000564) (book): architecture, microarchitecture and memory-system chapters. Main text.
- Patterson & Hennessy, [*Computer Organization and Design: ARM Edition*](https://shop.elsevier.com/books/computer-organization-and-design-arm-edition/patterson/978-0-12-801733-3) (book): the processor and memory-hierarchy chapters, for depth.
- Yiu, [*The Definitive Guide to ARM Cortex-M3 and Cortex-M4 Processors*](https://shop.elsevier.com/books/the-definitive-guide-to-arm-cortex-m3-and-cortex-m4-processors/yiu/978-0-12-408082-9) (book): registers, memory map, instruction set, stack.
- [AAPCS, Procedure Call Standard for the Arm Architecture](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst) (free): argument passing and callee-saved registers.
- [Cortex-M4 Technical Reference Manual](https://developer.arm.com/documentation/100166/0001) (free): the 3-stage pipeline, instruction timing, the DWT cycle counter.
- Memfault Interrupt, [From Zero to main(): Bare metal C](https://interrupt.memfault.com/blog/zero-to-main-1) (free): memory layout and startup.

## Topic 2: Embedded C

- Kernighan & Ritchie, *The C Programming Language* (book): the language itself, the pointers chapter above all.
- Elecia White, [*Making Embedded Systems*, 2nd edition](https://www.oreilly.com/library/view/-/9781098151539) (book): structure, state machines, fixed-point math. Free companion repo: [eleciawhite/making-embedded-systems](https://github.com/eleciawhite/making-embedded-systems).
- James Grenning, [*Test-Driven Development for Embedded C*](https://www.oreilly.com/library/view/test-driven-development/9781941222997) (book): unit testing embedded code on the PC.
- Barr Group, [*Embedded C Coding Standard*](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) (free download): a practical style and safety baseline.
- MISRA C (reference only): know what it is and why industry uses it.

## Topic 3: Microcontroller interfacing (GPIO, ADC, timers)

- RM0390: RCC (clocks), GPIO, ADC, general-purpose timers (TIM2 to TIM5), advanced timers (TIM1, TIM8).
- Datasheet: the alternate-function table and the ADC electrical characteristics.
- [cpq, *Bare Metal Programming Guide*](https://github.com/cpq/bare-metal-programming-guide) (free): register-level GPIO, UART and SysTick on a Nucleo.
- White, *Making Embedded Systems*: the peripherals and sampling chapters.

## Topic 4: Communication protocols (UART, SPI, I2C)

- RM0390: the USART, SPI and I2C chapters.
- NXP, [UM10204, *I2C-bus specification and user manual*](https://www.nxp.com/docs/en/user-guide/UM10204.pdf) (free): the real I2C spec.
- Analog Devices, [*Introduction to SPI Interface*](https://www.analog.com/en/resources/analog-dialogue/articles/introduction-to-spi-interface.html) (free): modes, clock polarity and phase.
- The datasheet of every sensor you wire up (for example an IMU such as the MPU-6050 or BMI160).

## Topic 5: Interrupts

- PM0214: exception model, exception entry and return, NVIC, priority grouping.
- RM0390: the interrupts and events chapter (vector table, EXTI).
- Yiu: the exceptions and interrupts chapters.
- Memfault Interrupt, [A Practical guide to ARM Cortex-M Exception Handling](https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic) (free).

## Topic 6: ARM architecture

- [DDI0403, ARMv7-M Architecture Reference Manual](https://developer.arm.com/documentation/ddi0403/latest/) (free, Arm account may be needed to download): the formal spec behind the Cortex-M4.
- [Cortex-M4 Technical Reference Manual](https://developer.arm.com/documentation/100166/0001) (free).
- Yiu: fault handling, MPU, SVC and the OS-support chapters.
- Memfault Interrupt, [How to debug a HardFault on an ARM Cortex-M MCU](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug) (free).
- RM0390: the embedded flash memory interface (erase and program sequence), for the bootloader.
- ST, [AN2606, system memory boot mode](https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf) (free): the chip's built-in bootloader, to compare against yours.

## Topic 7: RTOS

- Jonathan Valvano, [*Real-Time Operating Systems for ARM Cortex-M Microcontrollers*](https://users.ece.utexas.edu/~valvano/arm/outline3.htm) (book, Volume 3): building a kernel from scratch.
- Yiu: the PendSV and OS-support chapters (context switching).
- [*Mastering the FreeRTOS Real Time Kernel*](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book) (free): how a production kernel solves the same problems.
- Giorgio Buttazzo, *Hard Real-Time Computing Systems* (book, Springer): scheduling theory (rate-monotonic, EDF).
- Glenn Reeves (JPL), [What really happened on Mars](https://www.cs.unc.edu/~anderson/teach/comp790/papers/mars_pathfinder_long_version.html) (free): the Pathfinder priority-inversion bug, told by the engineer who fixed it.

## Tools

- `arm-none-eabi-gcc`, `objdump`, `nm`, `size`, `make` ([Arm GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads))
- [OpenOCD](https://openocd.org/) and `arm-none-eabi-gdb` (the Nucleo's ST-LINK is the debug probe)
- A serial terminal (PuTTY, or `screen`)
- Later: a logic analyzer or scope for protocol waveforms and timing
