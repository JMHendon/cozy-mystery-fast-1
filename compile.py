#!/usr/bin/env python3
"""Compile manuscript/chNN.md into a single reading file."""
import glob, os, sys
out = sys.argv[1] if len(sys.argv) > 1 else "Nobody-Fools-Archie-Fairweather.md"
parts = ["# Nobody Fools Archie Fairweather\n\n### An Archie Fairweather Mystery\n\n---\n"]
for f in sorted(glob.glob("manuscript/ch[0-9][0-9].md")):
    parts.append(open(f).read().strip() + "\n")
open(out, "w").write("\n\n---\n\n".join(parts) + "\n")
words = sum(len(open(f).read().split()) for f in glob.glob("manuscript/ch[0-9][0-9].md"))
print(out, words, "words")
