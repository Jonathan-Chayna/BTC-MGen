import time
from mnemonic import Mnemonic

# Initialize BIP39 mnemonic generator
mnemo = Mnemonic("english")

# Function to generate a valid BIP39 mnemonic
def generate_mnemonic():
    return mnemo.generate(strength=128)  # 128 bits of entropy, 12-word mnemonic

# Initialize the benchmark variables
start_time = time.time()
seed_count = 0

# Open file for writing
with open("wallets.txt", "a") as file:
    while True:
        # Generate a valid mnemonic and save it to the file
        mnemonic = generate_mnemonic()
        file.write(mnemonic + '\n')

        # Update count
        seed_count += 1

        # Every 10 seconds, print the rate of generation
        if time.time() - start_time >= 10:
            elapsed_time = time.time() - start_time
            rate = seed_count / elapsed_time
            print(f"Speed: {rate:.2f} M/s")

            # Reset for the next interval
            start_time = time.time()
            seed_count = 0
