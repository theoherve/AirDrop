from web3 import Web3, EthereumTesterProvider

w3 = Web3(Web3.EthereumTesterProvider())
account = w3.eth.accounts[0]

print(w3.eth.get_balance(account, 'ether'))



