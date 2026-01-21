"""
Week 5: Deployment & Testing
Description:
Basic validation tests for transaction data structure.
"""

def validate_transaction(transaction):
    required_fields = {"sender", "receiver", "amount"}
    return required_fields.issubset(transaction.keys())

def test_valid_transaction():
    transaction = {
        "sender": "Alice",
        "receiver": "Bob",
        "amount": 100
    }

    assert validate_transaction(transaction)
    print("Test Passed: Transaction structure is valid")

if __name__ == "__main__":
    test_valid_transaction()
