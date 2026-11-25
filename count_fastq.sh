#!/bin/bash
if [ $# -eq 0 ]; then
    echo "用法: $0 <目录>"
    exit 1
fi
if [ ! -d "$1" ]; then
    echo "错误: 目录不存在 -> $1"
    exit 1
fi
count=$(ls "$1"/*.fastq 2>/dev/null | wc -l)
echo "目录 $1 中有 $count 个 fastq 文件"
