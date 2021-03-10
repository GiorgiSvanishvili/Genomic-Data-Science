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

#calculating GC in genome
def findGCByPos(reads):
    gc = [0] * 100
    totals = [0] * 100

    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read == 'G':
                gc[i] += 1
            totals[i] += 1
    
    for i in range(len(gc)):
        if totals[i] > 0:
            gc[i] /= float(totals[i])
    return gc

gc = findGCByPos('NC_031327.ffn.txt')
print(gc)

#Finding bases matches in sequence
def matches(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False 
                break 
        if match:
            occurrences.append(i)
    return occurrences 

occurrences = matches(t = 'AGCTTAGATAGCTAG', p= 'AG')
print(occurrences)


#This algorithm takes random substrings and matching genome 
import random 
def generateReads(genome, numReads, readLen):

    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome) - readLen) - 1
        reads.append(genome[start: start + readLen])
    return reads 

reads = generateReads(genome, 100, 100)

numMatched = 0
for r in reads:
    exacts = matches(r, genome)
    if len(exacts)>0:
        numMatched += 1

print('%d / %d reads matched exactly!' %(numMatched, len(reads)))
