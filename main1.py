#Working with files
#Parsing genome sequence. 
#Analyzing bases in sequence
import collections
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

genome = readGenome('NC_031327.ffn.txt')
print(genome[:100])
print(len(genome))

counts = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
for base in genome:
    counts[base] += 1

print(counts)
collections.Counter(genome)

