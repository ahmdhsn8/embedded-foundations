# The loop for every sub-chunk

1. Read only the sections listed for it.
2. Predict what will happen before you run anything.
3. Write it yourself from the manual. No copy-paste, no generated code for the core pieces.
4. Verify in GDB: registers, memory, stack.
5. Break it on purpose and read the fault.
6. Explain it back in 5 lines without looking. If you can't, redo the reading.

Commit after each sub-chunk: `git commit -m "1.4 memory map: LED from GDB"`.
