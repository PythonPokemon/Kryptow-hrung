import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self, max_blocks):
        self.chain = []
        self.max_blocks = max_blocks
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"))
        self.chain.append(genesis_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        return hashlib.sha256((str(index) + previous_hash + str(timestamp) + data).encode()).hexdigest()

    def create_block(self, data):
        if len(self.chain) >= self.max_blocks:
            print("Max block limit reached. Cannot create more blocks.")
            return
        
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        hash = self.calculate_hash(index, previous_block.hash, timestamp, data)
        new_block = Block(index, previous_block.hash, timestamp, data, hash)
        self.chain.append(new_block)

        # Increase mining difficulty for each participant
        mining_difficulty = 1.0 + len(self.chain) * 0.1
        print(f"Mining difficulty for this block: {mining_difficulty}")

if __name__ == "__main__":
    max_blocks = 1000000  # Maximum number of blocks
    blockchain = Blockchain(max_blocks)
    
    while len(blockchain.chain) < max_blocks:
        transaction_data = f"Transaction {len(blockchain.chain) + 1}"
        blockchain.create_block(transaction_data)

    for block in blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print("=" * 20)
