#!/bin/bash

# Compare unique lines in two files. Print lines that occur in file a but not file b, and lines that occur in file b but not file a.

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <a_tables.sql> <b_tables.sql>"
  exit 1
fi

FILE_A="$1"
FILE_B="$2"

echo "Lines in A but not B:"
comm -23 <(sort -u $FILE_A) <(sort -u $FILE_B)

echo ""
echo "Lines in B but not A:"
comm -13 <(sort -u $FILE_A) <(sort -u $FILE_B)g 