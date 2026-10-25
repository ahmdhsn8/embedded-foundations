# Sub-chunk 1.4: toggle the Nucleo LED (PA5) with raw memory writes. No program needed.
# Load in GDB:  source tools/led_toggle.gdb   then run:  led_init   led_toggle
#
#  RCC_AHB1ENR  0x40023830   bit 0  = GPIOA clock enable
#  GPIOA_MODER  0x40020000   bits 11:10 = mode of PA5 (01 = output)
#  GPIOA_ODR    0x40020014   bit 5   = PA5 output level
define led_init
  set *(unsigned int *)0x40023830 = *(unsigned int *)0x40023830 | 1
  set *(unsigned int *)0x40020000 = (*(unsigned int *)0x40020000 & ~(3 << 10)) | (1 << 10)
end
define led_toggle
  set *(unsigned int *)0x40020014 = *(unsigned int *)0x40020014 ^ (1 << 5)
end
