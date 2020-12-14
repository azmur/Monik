import pandas as pd
import os


def main():
    file2 = 'list3.xlsx'
    tbl = pd.read_excel(file2, header=0, usecols=[0], names=['Domain name'])
    for one, two in tbl.iterrows():
        print(f'{one}: {two[0]}')


if __name__ == '__main__':
    main()
