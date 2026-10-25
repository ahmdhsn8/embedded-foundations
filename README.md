# Embedded Foundations

Self-study repo for NUCLEO-F446RE (STM32F446RE, Cortex-M4F). Seven topics, one project each, in order.
Method and loop: `docs/study-loop.md`.

| # | Topic | Project | Done |
|---|---|---|---|
| 1 | [Computer architecture](01-computer-architecture) | cycle-counting lab | [ ] |
| 2 | [Embedded C](02-embedded-c) | portable core library | [ ] |
| 3 | [MCU interfacing](03-mcu-interfacing) | PID on an RC filter | [ ] |
| 4 | [Communication protocols](04-communication-protocols) | sensor hub | [ ] |
| 5 | [Interrupts](05-interrupts) | real-time sampler | [ ] |
| 6 | [ARM architecture](06-arm-architecture) | fault analyzer and bootloader | [ ] |
| 7 | [RTOS](07-rtos) | own kernel | [ ] |

## Tools
`arm-none-eabi-gcc`, `make`, OpenOCD, `arm-none-eabi-gdb`. Debug setup lives in `tools/`.

## Quick start
```
openocd -f tools/openocd.cfg
arm-none-eabi-gdb -x tools/gdbinit
```
