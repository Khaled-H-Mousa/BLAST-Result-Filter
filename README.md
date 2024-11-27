# BLAST Result Filter

This Python script filters BLAST results based on specified criteria for **percent identity** and **alignment length**. It processes a tabular BLAST output file (`-outfmt 6`) and extracts entries that meet the thresholds. 

## Features
- Reads a BLAST output file in tab-delimited format.
- Filters results where:
  - **Percent Identity** > 50
  - **Alignment Length** > 200
- Prints the filtered results to the console.

## Requirements
- Python 3.x
- Tabular BLAST output file generated using the `-outfmt 6` option.

