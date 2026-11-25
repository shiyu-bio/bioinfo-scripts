# bioinfo-scripts

Bioinformatics shell scripts for NGS data processing, written while learning Linux and Git.

## Scripts

| Script | Description |
|---|---|
| `count_fastq.sh` | Count FASTQ files in a directory |
| `organize.sh` | Group FASTQ files into subdirectories by sample name (before first `_`) |

## Usage

```bash
chmod +x organize.sh
./organize.sh <directory>
```

Example:

```bash
./organize.sh ./raw
# Moved 8 files into 4 directories
```

## Requirements

- bash 4+
- GNU coreutils

## Author

shiyu-bio — Undergraduate, Qingdao University
