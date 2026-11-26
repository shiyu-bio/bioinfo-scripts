#!/usr/bin/env python3

def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq) * 100

seq1 = "ATGCGTACGTAGCTAGCTAGCTAGC"
seq2 = "GGGCCCTTTAAAGGGCCCTTTAAA"

print(f"seq1 GC: {gc_content(seq1):.2f}%")
print(f"seq2 GC: {gc_content(seq2):.2f}%")
