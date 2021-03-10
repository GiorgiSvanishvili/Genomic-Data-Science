#with this loops we can find undefined bases in sequence
'''dna = input('Enter your DNA: ')

if 'n' in dna:
    nbases = dna.count('n')

    print('DNA sequence has %d undefined bases ' %nbases)
else:
    print('DNA sequence has no undefined bases')

pos = dna.find('gt',0)

while pos>-1:
    print("Donor splice site candidate at position %d" %pos)
    pos = dna.find('gt', pos + 1)

#this algorithm tells us invalid amino acids with theirs' positions in protein and deletes them.
protein = 'BHGHKHNMIJUMJQRCACZVDOSLMIASBQBTBZB' #<--random letters
corrected_protein = ''
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTWYZ' : #<--amino acids
        continue
    corrected_protein=corrected_protein+protein[i]
print('Corrected protein sequence is: %s' %corrected_protein)
        #print('protein contains invalid amino acid %s at position %d' %(protein[i], i))


#This algorithm computes GC percentage
#In molecular biology and genetics, GC-content is the percentage of nitrogenous bases in a DNA or RNA molecule that are either guanine or cytosine. 
def gc(dna):
    nbases = dna.count('n')
    gc_percentage = float(dna.count('c') + dna.count('g')) * 100/(len(dna)-nbases)
    return gc_percentage

gc('ctttggtttctactcgccggcagcgtcccatctgtgcacttgccatcgaa')

#checking stop codons in dna sequence
def has_stop_codon(dna):
    stop_codon_found = False
    stop_codons=['tga', 'tag', 'taa']
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found

has_stop_codon('acgacctatgatgtggacagtcaacaaggcttctcagaaggctattcaat')

#complementing DNA sequence
def complement(dna):
    basecomplement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
    letters = list(dna)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)
dna('ctttggtttctactcgccggcagcgtcccatctgtgcacttgccatcgaa')'''

def recursion(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *=i
        return fact
print(recursion(3))



    

    
    
