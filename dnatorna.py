def dna_to_rna(seq):
    """Converts DNA sequence to RNA"""
    rna_seq = seq[::-1]
    rna_seq = rna_seq.upper()
    rna_seq = rna_seq.replace('T', 'U')
    return rna_seq

def reverse_rna_complement(seq):
    """Computes a reverse complement RNA sequence of a DNA sequence"""
    new_seq = seq[::-1]
    new_seq = new_seq.upper()
    new_seq = new_seq.replace('A', 'u')
    new_seq = new_seq.replace('T', 'a')
    new_seq = new_seq.replace('G', 'c')
    new_seq = new_seq.replace('C', 'g')

    return new_seq.upper()
