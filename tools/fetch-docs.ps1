# Download the free reference PDFs into docs\pdf\ (git-ignored). Run from the repo root:
#   powershell -ExecutionPolicy Bypass -File tools\fetch-docs.ps1
$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path docs\pdf | Out-Null
$docs = [ordered]@{
  "RM0390-reference-manual.pdf"   = "https://www.st.com/resource/en/reference_manual/rm0390-stm32f446xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf"
  "STM32F446-datasheet.pdf"       = "https://www.st.com/resource/en/datasheet/stm32f446re.pdf"
  "PM0214-programming-manual.pdf" = "https://www.st.com/resource/en/programming_manual/pm0214-stm32-cortexm4-mcus-and-mpus-programming-manual-stmicroelectronics.pdf"
  "ES0298-errata.pdf"             = "https://www.st.com/resource/en/errata_sheet/es0298-stm32f446xx-device-errata-stmicroelectronics.pdf"
  "UM1724-nucleo64.pdf"           = "https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf"
  "AN2606-system-bootloader.pdf"  = "https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf"
  "UM10204-i2c-spec.pdf"          = "https://www.nxp.com/docs/en/user-guide/UM10204.pdf"
}
foreach ($name in $docs.Keys) {
  Write-Host "-> $name"
  Invoke-WebRequest -Uri $docs[$name] -OutFile "docs\pdf\$name" -UserAgent "Mozilla/5.0"
}
Write-Host "Done. ARM's DDI0403 and the Cortex-M4 TRM download from developer.arm.com (see docs/material.md)."
