# DNA Sequence Analyzer

#### Video Demo: https://youtu.be/gY5_RqRfeQU

#### Description:

DNA Sequence Analyzer is a Python program that analyzes DNA sequences stored in FASTA files. I created this project to practice Python programming while applying it to a topic related to my background in biochemistry. The program allows the user to provide a FASTA file and perform several analyses on the DNA sequence, including nucleotide counting, nucleotide percentage calculation, motif searching, and translation into RNA and protein sequences.

FASTA is a common file format used to store biological sequences. It contains a header that provides information about the sequence, followed by the actual nucleotide sequence. In this project, the program reads the FASTA file, separates the header from the DNA sequence, and extracts the gene name from the header. The extracted gene name is then used when creating the protein output file.

The program first asks the user to enter the name of a FASTA file. I used a regular expression to check that the entered filename follows the expected format and ends with `.fasta`. After reading the file, the program validates the DNA sequence by checking whether all its characters are valid DNA nucleotides: A, T, C, or G.

The program then counts the occurrences of each nucleotide in the sequence. It also calculates the GC percentage and AT percentage. These percentages are useful for describing the nucleotide composition of a DNA sequence. The user can also enter a three-nucleotide motif, and the program searches for that motif and reports how many times it appears in the sequence.

Another feature of the project is DNA transcription. The program converts the DNA sequence into an RNA sequence by replacing thymine (T) with uracil (U). The resulting RNA sequence is saved in a file called `RNAseq.txt`.

The project also includes a translation feature. The program uses a codon dictionary stored in a separate file called `codons.py`. This dictionary contains codons and their corresponding amino acids. The DNA sequence is read three nucleotides at a time, and the codons are converted into amino acids. The resulting protein sequence is saved in a file named using the gene name, such as `protein_TP53.txt`.

I decided to separate the codon dictionary from the main program to keep `project.py` organized and make the codon information easier to manage. I also separated the testing code into `test_project.py`, where I use pytest to test the functions that perform DNA validation, nucleotide counting, and motif searching.

## Features

1. Identify the gene name from the FASTA header.
2. Validate the DNA sequence.
3. Count each nucleotide in the sequence.
4. Calculate GC% and AT%.
5. Search for a user-defined three-nucleotide motif.
6. Count motif occurrences in the sequence.
7. Transcribe DNA into RNA and save it to a file.
8. Translate DNA into a protein sequence and save it to a file.

## Files

* `project.py` - Contains the main program and the functions used to analyze DNA sequences.
* `test_project.py` - Contains unit tests for the project functions.
* `codons.py` - Contains the codon and amino acid dictionary used for translation.
* `requirements.txt` - Contains the required libraries, if any.
* `tp53.fasta` - An example FASTA file containing a human TP53 sequence.

## Output Files

After running the program, the following files are created:

* `RNAseq.txt` - Contains the RNA sequence.
* `protein_TP53.txt` - Contains the translated protein sequence.

## How to Run

Make sure that `project.py`, `codons.py`, and the FASTA file are located in the same folder.

Run the program using:

```
python project.py
```

Then enter the name of the FASTA file when prompted.

FASTA files can be downloaded from biological sequence databases such as NCBI.

## How to Test

Install pytest if necessary, then run:

pytest test_project.py

The tests check for all functions in the project.py file, whether they return the expected results or not.

## Design Choices

I used functions to divide the program into smaller tasks, making the code easier to understand and test. I used regular expressions to validate the FASTA filename and motif input. I also used a separate codon dictionary because it keeps the biological information separate from the main program logic.

The project was created as a way to combine programming practice with my interest in biology and bioinformatics.
