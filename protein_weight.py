import requests
import sys

def seq_weight(sequence):
    '''
    Converts sequence to molecular weight value
    '''
    # Dict in KDa from https://web.expasy.org/protscale/pscale/Molecularweight.html
    aa_weight = {'A': 89.000,
                 'R': 174.000,
                 'N': 132.000,
                 'D': 133.000,
                 'C': 121.000,
                 'Q': 146.000,
                 'E': 147.000,
                 'G': 75.000,
                 'H': 155.000,
                 'I': 131.000,
                 'L': 131.000,
                 'K': 146.000,
                 'M': 149.000,
                 'F': 165.000,
                 'P': 115.000,
                 'S': 105.000 ,
                 'T': 119.000,
                 'W': 204.000,
                 'Y': 181.000,
                 'V': 117.000,
                 'X': "X"}
    sequence_list=list(sequence)
    weights=[]
    for aa in sequence_list:
        weights.append(aa_weight[aa])
    kilodaltons=format((sum(weights)/1000), ".2f")
    return(kilodaltons)

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
    uniprot_id=uniprot_id.strip(" ")
    uniprot_id=uniprot_id.strip("\t")
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
