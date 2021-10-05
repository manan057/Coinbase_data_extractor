import pprint

def main(file):
    contents = [] 
    with file as data_file:
        contents = data_file.readlines()
        count = 0
        for line in contents:
            count += 1
            print(f'line {count}: {line}')    

if __name__ == "__main__":
    coinbase_data_extract = open(r"./coinbase_data.txt","r+")
    main(coinbase_data_extract)
    coinbase_data_extract.close()
