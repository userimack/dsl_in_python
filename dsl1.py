#!/usr/bin/env python3
import sys
import importlib

sys.path.insert(0, './modules/')

# source file as first argument
if len(sys.argv) != 2:
    print("usage: %s <src.dsl>" % sys.argv[1])
    sys.exit(1)

with open(sys.argv[1], 'r') as file_obj:
    for line in file_obj:
        line = line.strip()
        if not line or line[0] == "#":
            continue
        parts = line.split()
        print(parts)

        mod = importlib.import_module(parts[0])
        print(mod)
