"""
Week 6: Capstone Project
Title: Simple Blockchain Transaction Simulator

Description:
This program demonstrates a simplified blockchain
implementation using Python. Each block contains
transactions and is linked using cryptographic hashes.
"""

import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}")
            print(f"Timestamp      : {block.timestamp}")
            print(f"Transactions   : {block.transactions}")
            print(f"Previous Hash  : {block.previous_hash}")
            print(f"Hash           : {block.hash}")

def main():
    blockchain = Blockchain()
    blockchain.add_block(["Alice pays Bob 50"])
    blockchain.add_block(["Bob pays Charlie 30"])
    blockchain.add_block(["Charlie pays Dave 20"])
    blockchain.display_chain()

if __name__ == "__main__":
    main()
