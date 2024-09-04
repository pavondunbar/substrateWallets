# Substrate Wallet Balance Checker

This Python script allows you to retrieve 10 random wallet addresses and their balances from a running Substrate blockchain using the Substrate interface. It provides a convenient way to explore and analyze wallet balances on the Substrate blockchain's network.

## Features

- Retrieve all wallet addresses on the blockchain
- Get the balance of a specific wallet address
- Randomly select a subset of wallet addresses
- Identify the wallet with the highest balance among the selected addresses

## Prerequisites

Before running this script, ensure that you have the following:

- Python 3.x installed on your machine
- `substrateinterface` library installed (`pip install substrateinterface`)

## Usage

1. Clone this repository or download the script file.

2. Open the script file in a text editor and replace the following variables with the correct values for the substrate blockchain:
   - `url`: The RPC endpoint URL for Argochain (e.g., `"wss://rpc.devolvedai.com"`)
   - `ss58_format`: The SS58 format used by Substrate (e.g., `42`)

3. Save the script file.

4. Open a terminal and navigate to the directory containing the script.

5. Run the script using the following command:
   ```
   python3 queryAddresses.py
   ```

6. The script will retrieve all wallet addresses on the blockchain and randomly select 10 addresses.

7. For each selected address, the script will fetch the balance and display it in the native token's units.

8. Finally, the script will highlight the wallet with the highest balance among the selected addresses.

## Benefits

This script provides several benefits for users and developers interested in exploring and analyzing wallet balances on the Substrate blockchain:

- **Wallet Address Retrieval**: The script allows you to easily retrieve all wallet addresses on the blockchain. This can be useful for various purposes, such as statistical analysis, data exploration, or identifying active wallets.

- **Balance Checking**: By providing a specific wallet address, you can quickly check its balance in the native token's units. This feature enables you to monitor and track the balances of individual wallets of interest.

- **Random Sampling**: The script demonstrates how to randomly select a subset of wallet addresses from the entire set. This can be helpful when you want to analyze a representative sample of wallets instead of processing the entire dataset.

- **Highest Balance Identification**: The script identifies the wallet with the highest balance among the selected addresses. This feature can be useful for various purposes, such as identifying high-value wallets or conducting further analysis on specific wallets.

- **Customization**: The script can be easily modified and extended to suit your specific needs. You can adjust the number of randomly selected addresses, add additional functionality, or integrate the script into your own projects.

## License

This script is released under the [MIT License](LICENSE).

Feel free to modify and adapt the script to fit your requirements. If you have any questions or suggestions, please open an issue or submit a pull request.
