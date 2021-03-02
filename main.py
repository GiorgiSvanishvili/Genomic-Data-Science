#with this loops we can find undefined bases in sequence
'''dna = input('Enter you DNA: ')

if 'n' in dna:
    nbases = dna.count('n')

    print('DNA sequence has %d undefined bases ' %nbases)
else:
    print('DNA sequence has no undefined bases')

pos = dna.find('gt',0)

while pos>-1:
    print("Donor splice site candidate at position %d" %pos)
    pos = dna.find('gt', pos + 1)'''

#this algorithm tells us invalid amino acids with theirs' positions in protein and deletes them.
protein = 'BHGHKHNMIJUMJQRCACZVDOSLMIASBQBTBZB' #<--random letters
corrected_protein = ''
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTWYZ' : #<--amino acids
        continue
    corrected_protein=corrected_protein+protein[i]
print('Corrected protein sequence is: %s' %corrected_protein)
        #print('protein contains invalid amino acid %s at position %d' %(protein[i], i))
    
    
