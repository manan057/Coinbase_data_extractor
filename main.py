import pprint

"""
Account_name: XRP Wallet
Timestamp: 2021-08-30 14:15:18 UTC
Balance: 30.80125124
Amount: 2580.125124000000
Currency: XRP
To: 12345abc
Notes: Converted 1.78387608 ETH to 2,580.125124 XRP.
Instantly_exchanged: False
Transfer_total: 25801251.24
Transfer_total_currency: XRP
Transfer_total_fee: 0.0
Transfer_fee_currency: XRP
Transfer_id: 12345abc
Coinbase_id: 1234565abc
"""
def main(file):
    contents = [] 
    with file as data_file:
        contents = data_file.readlines()
        count = 0
        account_name_array = []
        timestamp_array = []
        balance_array = []
        amount_array = []
        currency_array = []
        to_array = []
        notes_array = []
        instantly_exchanged_array = []
        transfer_total_array = []
        transfer_total_currency_array = []
        transfer_total_fee_array = []
        transfer_fee_currency_array = []
        transfer_payment_method_array = []
        transfer_id_array = []
        coinbase_id_array = []
        array_of_variables = [account_name_array, timestamp_array, balance_array, amount_array, 
            currency_array, to_array, notes_array, instantly_exchanged_array, transfer_total_array, 
            transfer_total_currency_array, transfer_total_fee_array, transfer_fee_currency_array,
            transfer_payment_method_array, transfer_id_array, coinbase_id_array]
        for line in contents:
            if 'Account_name' in line:
                account_name_array.append(line.strip(":"))
            if 'Timestamp' in line: 
                timestamp_array.append(line.strip(":"))
            if 'Balance' in line: 
                balance_array.append(line.strip(":"))
            if 'Amount' in line: 
                amount_array.append(line.strip(":"))
            if 'Currency' in line: 
                currency_array.append(line.strip(":"))
            if 'To' in line: 
                to_array.append(line.strip(":"))
            if 'Notes' in line: 
                notes_array.append(line.strip(":"))
            if 'Instantly_exchanged' in line: 
                instantly_exchanged_array.append(line.strip(":"))
            if 'Transfer_total' in line: 
                transfer_total_array.append(line.strip(":"))
            if 'Transfer_total_currency' in line: 
                transfer_total_currency_array.append(line.strip(":"))
            if 'Transfer_total_fee' in line:
                transfer_total_fee_array.append(line.strip(":"))
            if 'Transfer_fee_currency' in line:
                transfer_total_fee_array.append(line.strip(":"))
            if 'Transfer_payment_method' in line:
                transfer_payment_method_array.append(line.strip(":"))
            if 'Transfer_id' in line: 
                transfer_id_array.append(line.strip(":"))
            if 'Coinbase_id' in line: 
                coinbase_id_array.append(line.strip(":"))
            
            for item in array_of_variables:
                base_length = len(account_name_array)
                if len(item) < base_length:
                    item.append("")

        for a, b, c, d, e, f, g in zip(account_name_array, timestamp_array, amount_array, currency_array, notes_array,
            transfer_total_array, transfer_total_fee_array):
            print(a, b, c, d, e, f, g)

        print()    
        
if __name__ == "__main__":
    coinbase_data_extract = open(r"./coinbase_data.txt","r+")
    main(coinbase_data_extract)
    coinbase_data_extract.close()
