import random
from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException

# Initialize the Substrate interface for Argochain
substrate = SubstrateInterface(
    url="wss://your-rpc-endpoint-url",  # Replace with the correct RPC endpoint 
    ss58_format=42,                     # Replace with the correct SS58 format
    type_registry_preset='substrate-node-template'
)

# Function to get all wallet addresses on the chain
def get_all_wallet_addresses():
    wallet_addresses = []
    for key, _ in substrate.query_map("System", "Account"):
        wallet_addresses.append(key.value)
    return wallet_addresses

# Function to get the balance of a given wallet address
def get_wallet_balance(address):
    try:
        result = substrate.query("System", "Account", [address])
        if result:
            # Convert the U128 balance to an integer
            balance = result['data']['free'].value / 10**18  # Assuming the balance is in pico units
            return balance
    except SubstrateRequestException as e:
        print(f"Failed to fetch balance for {address}: {str(e)}")
    return None

# Get all wallet addresses
wallet_addresses = get_all_wallet_addresses()

# Randomly select 10 wallet addresses
selected_addresses = random.sample(wallet_addresses, 10)

# Track the wallet with the highest balance
highest_balance = 0
highest_balance_address = None

# Print the selected wallet addresses and their balances
print("Randomly selected wallet addresses and their balances in AGC:\n") # Replce AGC with the symbol of the native token
for address in selected_addresses:
    balance = get_wallet_balance(address)
    if balance is not None:
        print(f"Address: {address}, Balance: {balance:.6f} AGC") # Replce AGC with the symbol of the native token
        if balance > highest_balance:
            highest_balance = balance
            highest_balance_address = address
    else:
        print(f"Address: {address}, Balance: Unable to retrieve")

# Highlight the wallet with the highest balance
if highest_balance_address:
    print("\n\033[1;32mWallet with the highest balance:\033[0m")
    print(f"\033[1;33mAddress: {highest_balance_address}, Balance: {highest_balance:.6f} AGC\033[0m") # Replce AGC with the symbol of the native token
