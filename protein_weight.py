import requests
import sys

def seq_weight(sequence):
    '''
    Converts sequence to molecular weight value
    '''
    # Dict in KDa from https://www.sciencegateway.org/tools/proteinmw.htm
    aa_weight = {'A': 0.09,
                 'R': 0.17,
                 'N': 0.13,
                 'D': 0.13,
                 'C': 0.12,
                 'Q': 0.15,
                 'E': 0.15,
                 'G': 0.08,
                 'H': 0.16,
                 'I': 0.13,
                 'L': 0.13,
                 'K': 0.15,
                 'M': 0.15,
                 'F': 0.17,
                 'P': 0.12,
                 'S': 0.11,
                 'T': 0.12,
                 'W': 0.2,
                 'Y': 0.18,
                 'V': 0.12,
                 'X': "X"}
    sequence_list=list(sequence)
    weights=[]
    for aa in sequence_list:
        weights.append(aa_weight[aa])
    return(format(sum(weights), ".2f"))

def parse_fasta(fasta_format):
    '''
    takes the fasta download and returns a header and sequence
    '''
    fasta_list=fasta_format.splitlines( )
    fasta_list[1::]=[''.join(fasta_list[1 ::])]
    return(fasta_list)

def download_id(uniprot_id):
    url=str(f'https://www.uniprot.org/uniprot/{uniprot_id}.fasta')
    output = requests.get(url).text
    return(output)

def process_id(uniprot_id):
    '''
    Downloads the fasta from UniProt
    '''
    uniprot_id=uniprot_id.strip("\n")
    download_output=download_id(uniprot_id)

    fasta=parse_fasta(download_output)

    print(uniprot_id,",", seq_weight(fasta[1]))

def iterate_list(filename):
    '''
    Opens the file and goes through each line as if it is a list.
    '''
    with open(filename, "r") as f:
        content = f.readlines()
    for each_id in content:
        process_id(each_id)

### Script canonically starts here! ###
print("UniProt, ","Molecular weight")
file_name = sys.argv[1]
iterate_list(file_name)
