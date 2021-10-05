import pprint
from tabulate import tabulate

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
        next_transaction = False
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
            if '----------' in line:
                next_transaction = True
            if 'Account_name' in line:
                account_name_array.append(line.strip("Account_name:"))
            if 'Timestamp' in line: 
                timestamp_array.append(line.strip("Timestamp:"))
            if 'Balance' in line: 
                balance_array.append(line.strip("Balance:"))
            if 'Amount' in line: 
                amount_array.append(line.strip("Amount:"))
            if 'Currency' in line: 
                currency_array.append(line.strip("Currency:"))
            if 'To' in line: 
                to_array.append(line.strip("To:"))
            if 'Notes' in line: 
                notes_array.append(line.strip("Notes:"))
            if 'Instantly_exchanged' in line: 
                instantly_exchanged_array.append(line.strip("Instantly_exchanged:"))
            if 'Transfer_total:' in line: 
                transfer_total_array.append(line.strip("Transfer_total:"))
            if 'Transfer_total_currency:' in line: 
                transfer_total_currency_array.append(line.strip("Transfer_total_currency:"))
            if 'Transfer_total_fee' in line:
                transfer_total_fee_array.append(line.strip("Transfer_total_fee:"))
            if 'Transfer_fee_currency' in line:
                transfer_fee_currency_array.append(line.strip("Transfer_fee_currency:"))
            if 'Transfer_payment_method' in line:
                transfer_payment_method_array.append(line.strip("Transfer_payment_method:"))
            if 'Transfer_id' in line: 
                transfer_id_array.append(line.strip("Transfer_id:"))
            if 'Coinbase_id' in line: 
                coinbase_id_array.append(line.strip("Coinbase_id:"))
            
            if next_transaction:
                for item in array_of_variables:
                    base_length = len(account_name_array)
                    if len(item) < base_length:
                        item.append("")
                next_transaction = False

        #removed notes and payment method to improve readability 
        #'Notes': notes_array, 'Transfer_payment_method': transfer_payment_method_array,
        transactions_table = {
            'Account_name': account_name_array,
            'Timestamp': timestamp_array,
            'Balance': balance_array,
            'Amount': amount_array,
            'Currency': currency_array,            

            'Transfer_total': transfer_total_array,
            'Transfer_total_currency': transfer_total_currency_array,
            'Transfer_total_fee': transfer_total_fee_array,
            'Transfer_fee_currency': transfer_fee_currency_array,
            
        }

        print(tabulate(transactions_table, headers='keys'))

        
        
if __name__ == "__main__":
    coinbase_data_extract = open(r"./coinbase_data.txt","r+")
    main(coinbase_data_extract)
    coinbase_data_extract.close()
