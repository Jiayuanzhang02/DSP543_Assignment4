import pandas as pd
import sys
import numpy
import matplotlib.pyplot as plt


def Count_kmers_possible(sequence,k):
    """
    Count the possible kmers
    """
    if not sequence:
        raise ValueError('Sequence is empty')
    row1=[]
    kp = min(4**k,len(sequence)-k+1)
    return kp


def Count_kmers_observed(sequence):
    """
    Count the observed kmers
    """
    df = pd.DataFrame(columns=['k','observed', 'posibility'])
    if not sequence:
        return(df)
    sequence_length =  len(sequence)
    for k in range(sequence_length):
        count_observed={}
        for i in range(sequence_length-k):
            temp = sequence[i:i+k+1]
            if temp in count_observed:
                count_observed[temp] +=1
            else:
                count_observed[temp] =1
        df.loc[k]=[k+1,len(count_observed),Count_kmers_possible(sequence,k+1)]
    return(df)


def Kmers_plot(df):
    """
    Plot the dataframe into graph
    """
    df['proportion'] = df.observed / df.posibility
    df.plot(x='k', y='proportion', kind='bar')
    plt.show()


def linguistic_complexity(df):
    """
    Calculate the linguistic complexity
    """
    return(df['observed'].sum() / df['posibility'].sum() )

if __name__ == '__main__':
    #sequence_file=str("sequence_file.txt")
    sequence_file=str(sys.argv[1:])[2:-2]
    with open(sequence_file,"r") as file1:
        sequence = file1.read()
        file1.close()
    if sequence:
        if sequence[-1]=='\n':
            sequence = sequence[:-1]

    print("Acknowledgement:This assignment can be done is under the great help of Mr.Mohsen Mosayebi. Without his help, this assignment cannot be done.")
    print(Count_kmers_possible(sequence,4))
    print(Count_kmers_observed(sequence))
    df=Count_kmers_observed(sequence)
    print('observed= ', df['observed'].sum() , ',  posibility= ', df['posibility'].sum())
    print(linguistic_complexity(df))
    print(Kmers_plot(df))
