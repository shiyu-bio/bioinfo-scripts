#!/usr/bin/env python3

import sys

def read_fasta(path):
    records = []
    name = None
    seq = ""

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    records.append((name, seq))
                name = line[1:]
                seq = ""
            else:
                seq += line

    if name is not None:
        records.append((name, seq))

    return records

def gc_content(seq):
    if len(seq) == 0:
        return 0.0
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def n50(lengths):
    if not lengths:
        return 0
    s = sorted(lengths, reverse=True)
    total = sum(s)
    half = total / 2
    acc = 0
    for length in s:
        acc += length
        if acc >= half:
            return length
    return 0

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.fasta>")
        sys.exit(1)

    path = sys.argv[1]
    records = read_fasta(path)

    lengths = [len(s) for _, s in records]
    total_len = sum(lengths)

    print(f"File: {path}")
    print(f"Sequences: {len(records)}")
    print(f"Total length: {total_len}")
    if records:
        print(f"Average length: {total_len / len(records):.2f}")
        print(f"N50: {n50(lengths)}")
        print("")
        print(f"{'Name':<10}{'Length':>8}{'GC%':>8}")
        for name, seq in records:
            short = name.split()[0]
            print(f"{short:<10}{len(seq):>8}{gc_content(seq):>8.2f}")

if __name__ == "__main__":
    main()
