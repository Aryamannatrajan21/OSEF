#!/bin/bash
set -e

mkdir -p benchmarks/python
cd benchmarks/python

if [ ! -d "fastapi" ]; then
    git clone --depth 1 https://github.com/fastapi/fastapi.git
fi

if [ ! -d "typer" ]; then
    git clone --depth 1 https://github.com/fastapi/typer.git
fi

cd ../..
echo "=============================="
echo "Benchmarking FastAPI..."
echo "=============================="
python -m osef.cli.main analyze benchmarks/python/fastapi

echo "=============================="
echo "Benchmarking Typer..."
echo "=============================="
python -m osef.cli.main analyze benchmarks/python/typer
