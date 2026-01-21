"""
Week 2: Core Concepts
Description:
Demonstrates structured data handling using
lists and dictionaries to simulate transactions.
"""

def get_transactions():
    return [
        {"sender": "Alice", "receiver": "Bob", "amount": 50},
        {"sender": "Bob", "receiver": "Charlie", "amount": 30},
        {"sender": "Charlie", "receiver": "Dave", "amount": 20}
    ]

def display_transactions(transactions):
    for index, tx in enumerate(transactions, start=1):
        print(f"Transaction {index}")
        print(f"  Sender   : {tx['sender']}")
        print(f"  Receiver : {tx['receiver']}")
        print(f"  Amount   : {tx['amount']}")
        print("-" * 30)

def main():
    transactions = get_transactions()
    display_transactions(transactions)

if __name__ == "__main__":
    main()
