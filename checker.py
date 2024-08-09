import requests
import bip32utils
from mnemonic import Mnemonic

def check_btc_balance(address):
    url = f'https://chain.api.btc.com/v3/address/{address}'
    response = requests.get(url)
    data = response.json()
    
    # Extract balance from the response
    if data.get('status') == 'success' and 'data' in data and 'balance' in data['data']:
        balance_satoshis = data['data']['balance']
        balance_btc = balance_satoshis / 1e8  # Convert satoshis to BTC
        return balance_btc
    else:
        raise ValueError(f"Unexpected API response: {data}")

def mnemonic_to_btc_address(mnemonic):
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic)
    
    # Create BIP32 root key from seed
    bip32_root_key = bip32utils.BIP32Key.fromEntropy(seed)
    
    # Derive the first Bitcoin address (m/44'/0'/0'/0/0 path)
    bip32_child_key = bip32_root_key.ChildKey(0).ChildKey(0).ChildKey(0).ChildKey(0).ChildKey(0)
    address = bip32_child_key.Address()
    
    return address

def check_mnemonics(file_path):
    with open(file_path, 'r') as file:
        mnemonics = file.readlines()
    
    for mnemonic in mnemonics:
        mnemonic = mnemonic.strip()
        if not mnemonic:
            continue
        
        try:
            btc_address = mnemonic_to_btc_address(mnemonic)
            btc_balance = check_btc_balance(btc_address)
            print(f"Mnemonic: {mnemonic} |\n BTC Address: {btc_address} | Balance: {btc_balance:.8f} BTC")
        
        except Exception as e:
            print(f"Error processing mnemonic: {mnemonic}\n{e}")

# Example usage
file_path = 'wallets.txt'
check_mnemonics(file_path)

