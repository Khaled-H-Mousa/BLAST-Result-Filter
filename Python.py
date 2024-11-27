# Script to filter BLAST results based on percent identity and alignment length

# Define input file: Path to the BLAST output file in tabular format (-outfmt 6)
FileBlast = "/home/khaled/Documents/Out_Blast/Out_Blast.txt"

# Initialize a list to store filtered results
filtered_results = []

# Open and process the file line by line
with open(FileBlast, "r") as file:
    for line in file:
        # Split each line into columns based on tab delimiter
        line = line.strip().split("\t")
        
        # Extract percent identity (column 3) and alignment length (column 4)
        identity = float(line[2])
        alignment_length = int(line[3])
        
        # Filter results: Only keep entries with identity > 50 and alignment length > 200
        if identity > 50 and alignment_length > 200:
            filtered_results.append(line)

# Print filtered results to the console
for result in filtered_results:
    print(result)

