import sys
 
dna = 'CCTATCGTACGCTGTAGAATTTGATTTTCGGGGTCCGCCAGATGTTCATGCACCTCCGAGTAAGCCGCGTGCCTCTTTAAAGCATGCCGGTTCGAGCGTGATACGATAGCTGCTTCCTTACCATTCTCGATTCAACGTACCGCGAGAACGGGTCATCCTGGGGATGCCGGTGTCACTGTTTCCTGATGGTGTGCGGATTTTTGAACATCATTTATTTTAAGGTATGATTGCATAGAAGTTCCAATTCCTCTTGGGAGACCCACCAATGCGTAAGTGCCGTGGAGGCAACTCATCGAAACATAGCTGCCAATGCTAATGTGCGGATCCAACTAACAGAGTCTCACTAAATAGACCCTAGCCTTCCAACACCGGCCCTAACGTTTCTTATTCATATCGTCCTTTAAAACCACGCGTATTGGCCGGTTGGAATTCCATAGCCACTATACCAGGCCTTAGACGTTGGACAGATCGTTTCGTTTAAAGGATGTTTATGGAGGTTGACAACCGCGATAGCGCCCTGCAGAGGAACTCGGTCCAACGTCAGCGTAGACGACCAGAACGTGAATCCCATCCTGACAGACGTCGCCGTAGGTATCGATATCCGACCATTTTCTCCACTTTAACCGCTTCCCCACATTCTCCCCTCTGCTTCCCATTAGAAAACTTAAGGATCTGCACCCATGTATGAAGGATATTACCCTCTGTGATAGACAGCGACATGCTCACCGAGACCTCACTCCGCCACCTGTCACCTTTCATGAGCCGGACCTTGTATCGCCAGCTCTATATCAAGCGGGGGGGCCTCATGACTATTACAGCTCCGGTATAGGTCTGCCTCAATTTAGCCGCACCAATCGCGCCGAAAAAGCAAACATCCTCCTATGAGGTTCATTATGTTCAAGTTTGCACGGCAGACCGGTTAAAACCCCTGAGATTAACAGCGGGAGATTCTCGATCGATACGGGCGCGGTTATATG'
for i in 'ACGT':
    print(dna.count(i))
