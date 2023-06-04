#https://web3py.readthedocs.io/en/stable/examples.html
from web3 import Web3, EthereumTesterProvider, Account
import os
from dotenv import load_dotenv

#Uniswap Dai contract
#0x09cabEC1eAd1c0Ba254B09efb3EE13841712bE14

class NewWallet():

	def __init__(self):
		self.w3 = Web3(Web3.EthereumTesterProvider())

	def create_wallet(self):
		acc = self.w3.eth.account.create()

		return acc.address, acc._private_key.hex()

	def add_wallet_to_env(self):

		address, private_key = self.create_wallet()
		with open('.env','a') as f:
			f.write(f'{address}={private_key}\n')


#CreateWallet = NewWallet()
#CreateWallet.add_wallet_to_env()
alchemy_url = "https://eth-goerli.g.alchemy.com/v2/oRJxQFN8A4mDxE8y-g0-AiYAhxPANkeF"

class EthConnect:

	def __init__(self, address=None, contract=None):

		#self.w3 = Web3(Web3.EthereumTesterProvider())
		self.w3 = Web3(Web3.HTTPProvider(alchemy_url))
		self.address = Account.from_key('0x28e41e9e9ae0ce0dbe52bde1df8ddac701d80aa9b89a3557563cfc8cc6cc8c96')
		#self.address = Account.from_key(address)
		self.contract = contract
	#vérifier la connexion au node
	def get_balance(self):

		balance = self.w3.from_wei(self.w3.eth.get_balance(self.address.address), 'ether')
		print(balance)
		return balance





my_contract = EthConnect()
my_contract.get_balance()



