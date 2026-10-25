# Cycle-counting lab results

Counter: DWT_CYCCNT. Subtract the empty-read overhead from every row. Predict first.

| Test | Predicted cycles | Measured | Why |
|---|---|---|---|
| empty back-to-back reads | | | |
| int multiply | | | |
| int divide | | | |
| float multiply (FPU on) | | | |
| float divide (FPU on) | | | |
| float multiply (FPU off) | | | |
| aligned word load | | | |
| unaligned word load | | | |
| loop in flash | | | |
| same loop in RAM | | | |
| wait states 0..5, cache on/off | | | |
| PID step, fixed-point | | | |
| PID step, float | | | |
| PID step jitter over 1000 calls | | | |
