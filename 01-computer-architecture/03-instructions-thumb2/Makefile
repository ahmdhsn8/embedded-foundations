CC      = arm-none-eabi-gcc
CFLAGS  = -mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 -S -fno-asynchronous-unwind-tables
SRC     = src/examples.c

asm: build/O0.s build/O2.s
build/O0.s: $(SRC) | build
	$(CC) $(CFLAGS) -O0 $< -o $@
build/O2.s: $(SRC) | build
	$(CC) $(CFLAGS) -O2 $< -o $@
build:
	mkdir -p build
clean:
	rm -rf build
.PHONY: asm clean
