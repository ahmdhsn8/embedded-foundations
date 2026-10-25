Use `tools/led_toggle.gdb` from the repo root. No source code needed for this one.

1. `openocd -f tools/openocd.cfg`
2. `arm-none-eabi-gdb -x tools/gdbinit`
3. `source tools/led_toggle.gdb`, then `led_init`, then `led_toggle` repeatedly.
