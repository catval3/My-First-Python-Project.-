

import re 
from codons import aa_codons_dict 

def main():

    #prompting user for FASTA file:
    while True:
        file = input("Enter the FASTA file that you want to analyze: ").strip().lower()
        if not re.search(r"^\w+\.fasta$", file, re.IGNORECASE):
            print("Invalid file format")
        else:
            break

    sequence = get_sequence(file)
    gene_name = name(file)
    
    #analyze the sequence in file:
    if validate(sequence): 
        print("This is a valid gene.")
    else:
        print("This is an invalid gene.")

    #count the occurance of each letter. 
    A, T, G, C = count(sequence)
    print(f"Nucelotide count-> A:{A}, T:{T}, G:{G}, C:{C}")

    #give me percentages of their occurance. 
    GC, AT = percentages(sequence)
    print(f"GC%: {GC:.2f}, AT%: {AT:.2f}")

    #find a specific 3 letters "motif" given by user:
    while True:
        motif = input(f"Enter a motif to search for, in {gene_name} sequence: ").strip().upper()
        result = find_motif(sequence, motif)

        if result is not None:
            if result > 0:
                print(f"Motif {motif} appeared {result} times.")
            else:
                print("Motif does not exist")
            break
        print("Please enter a valid input of exactly 3 nucleotides (A, T, C, or G).")


    #turn sequence ino protein
    translate(sequence, gene_name)
    print("Protein sequence has been successfullt created, check your folder.")

    #turn DNA sequence to mRNA sequence
    RNA(sequence)
    print("RNA file has been successfully created, check your folder.")




def get_sequence(FASTA_file):
    sequence = ""

    with open(FASTA_file, "r") as file:
        for line in file:
            if line.startswith(">"):
                continue 

            sequence += line.strip()

    return sequence


def validate(sequence): 
    for nucleotide in sequence:
        if nucleotide not in "ATCG":
            return False

    return True



def name(FASTA_file):
    with open(FASTA_file, "r") as file:
        for line in file:
            if line.startswith(">"):
                match = re.search(r"\(([A-Za-z0-9.-]+)\)", line)

                if match:
                    gene_name = match.group(1)
                    print(f"The gene's name is ({gene_name})")

    return gene_name 



def count(sequence):

    A = 0
    T = 0
    G = 0
    C = 0

    for nucleotide in sequence: 
        if nucleotide == "A":
            A += 1
        elif nucleotide == "T":
            T += 1
        elif nucleotide == "G":
            G += 1
        elif nucleotide == "C":
            C += 1

    return A, T, G, C


def percentages(sequence):
    A, T, G, C = count(sequence)

    total = A + T + G + C

    # preventing zerodivision error if sequence was empty. 
    if total == 0:
        return 0.0, 0.0

    GC_percentage = (G + C) / total * 100
    AT_percentage = (A + T) / total * 100

    return GC_percentage, AT_percentage


def RNA(sequence):
    sequence = sequence.replace("T", "U")
    with open("RNAseq.txt", "w") as RNA_file:
        RNA_file.write(sequence)

def find_motif(sequence, motif):
    if not re.fullmatch("([ATCG]){3}", motif):
        return None
    return sequence.count(motif)

def translate(sequence, gene_name):
    codon_table = {} 

    for amino_acid_key in aa_codons_dict: 
        for codon_value in aa_codons_dict[amino_acid_key]: 
            codon_table[codon_value] = amino_acid_key 

    protein = []

    # Go through the DNA 3 nucleotides at a time
    for i in range(0, len(sequence) - 2, 3): 
        codon = sequence[i:i + 3]

        if codon in codon_table: 
            protein.append(codon_table[codon])

    with open(f"protein_{gene_name}.txt", "w") as file:
        file.write(" ".join(protein))

    return protein

if __name__ == "__main__":
    main()