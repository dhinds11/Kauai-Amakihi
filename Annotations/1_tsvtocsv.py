# Down and dirty method of swapping from Audacity generated TSV annotations to CSV format and file

import pandas as pd
import os

def tsv_to_csv_pandas(tsv_file, csv_file):
    df = pd.read_csv(tsv_file, sep='\t')
    df.to_csv(csv_file, index=False) # index=False prevents writing the DataFrame index as a column




path = "Kauai-Amakihi/Annotations/macaulay/tsv files"
dir_list = os.listdir(path)

for item in dir_list:
    tsv_to_csv_pandas(f'Kauai-Amakihi/Annotations/macaulay/tsv files/{item}', f'Kauai-Amakihi/Annotations/macaulay/csv files/{item[:-4]}.csv')
    print(f"Conversion complete: {item} converted to {item[:-4]}.csv using pandas")