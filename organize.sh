#!/bin/bash

usage() {
    echo "Usage: $0 <dir>"
    echo "  Group *.fastq files into subdirectories by sample name (before first _)"
    exit 0
}

if [ $# -eq 0 ]; then
    usage
fi
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    usage
fi

dir="$1"

if [ ! -d "$dir" ]; then
    echo "Error: directory not found -> $dir"
    exit 1
fi

before=$(find "$dir" -maxdepth 1 -type d | wc -l)

moved=0
for f in "$dir"/*.fastq; do
    [ -e "$f" ] || continue

    name=$(basename "$f")
    sample="${name%%_*}"
    mkdir -p "$dir/$sample"
    mv "$f" "$dir/$sample/"
    moved=$((moved + 1))
done

after=$(find "$dir" -maxdepth 1 -type d | wc -l)
dirs=$((after - before))

if [ $moved -eq 0 ]; then
    echo "No fastq files found"
    exit 0
fi

echo "Moved $moved files into $dirs directories"
