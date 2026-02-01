# Bitcoin Mining Simulator (Proof-of-Work)

An educational Python project that demonstrates how Bitcoin Proof-of-Work mining operates using the SHA-256 hashing algorithm.

## 🚀 Features
- Simulates nonce-based mining
- Adjustable difficulty (leading zero requirement)
- Calculates hash rate (hashes per second)
- Measures time taken to mine a block
- Graceful interrupt handling

## 🧠 How It Works
The miner continuously hashes block data combined with a nonce until the resulting SHA-256 hash satisfies the difficulty condition (leading zeros).

## 🛠 Tech Stack
- Python 3
- hashlib (SHA-256)
- time module

## ▶️ How to Run
```bash
python miner.py
