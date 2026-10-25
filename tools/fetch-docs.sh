#!/usr/bin/env sh
# Download the free reference PDFs into docs/pdf/ (git-ignored). Run from the repo root.
set -e
mkdir -p docs/pdf
get() { echo "-> $1"; curl -fL --retry 2 -A "Mozilla/5.0" -o "docs/pdf/$1" "$2"; }
get RM0390-reference-manual.pdf  https://www.st.com/resource/en/reference_manual/rm0390-stm32f446xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf
get STM32F446-datasheet.pdf      https://www.st.com/resource/en/datasheet/stm32f446re.pdf
get PM0214-programming-manual.pdf https://www.st.com/resource/en/programming_manual/pm0214-stm32-cortexm4-mcus-and-mpus-programming-manual-stmicroelectronics.pdf
get ES0298-errata.pdf            https://www.st.com/resource/en/errata_sheet/es0298-stm32f446xx-device-errata-stmicroelectronics.pdf
get UM1724-nucleo64.pdf          https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf
get AN2606-system-bootloader.pdf https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf
get UM10204-i2c-spec.pdf         https://www.nxp.com/docs/en/user-guide/UM10204.pdf
echo "Done. ARM's DDI0403 and the Cortex-M4 TRM download from developer.arm.com (see docs/material.md)."
