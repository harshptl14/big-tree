#!/usr/bin/env python3
import sys
for line in sys.stdin:
    fields = line.strip().split(',')
    if fields[0] != 'outlook':  # Skip header
        class_label = fields[-1]
        for i, value in enumerate(fields[:-1]):
            print(f"{i}\t{value}\t{class_label}\t1")