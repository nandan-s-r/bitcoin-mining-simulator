import hashlib
import time

# Block data (simulated)
block_data = "Hello, this is my first Bitcoin mining project"

# Difficulty = number of leading zeros required
difficulty = int(input("Enter mining difficulty (e.g. 4 or 5): "))


start_time = time.time()
nonce = 0
attempts = 0


print("Mining started")
print("Difficulty:", difficulty)

try:
    while True:
        text = block_data + str(nonce)
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        attempts += 1


        if hash_result.startswith("0" * difficulty):
            end_time = time.time()
            total_time = end_time - start_time

            print("\nBlock mined")
            print("Nonce:", nonce)
            print("Hash:", hash_result)
            print("Time taken (s):", round(total_time, 2))
            print("Hash rate (hashes/sec):", int(attempts / total_time))
            break

        nonce += 1

except KeyboardInterrupt:
    print("\nMining stopped by user")
    print("Total attempts:", attempts)




