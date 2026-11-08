# Genesis Chain (GNS)

An experimental, standalone Python blockchain prototype with a SHA-256 proof-of-work chain.

> **Mainnet designation is a project target, not a production-readiness claim.**
> This first release is an educational/devnet-grade reference implementation. Do not use it to hold value,
> process real payments, or expose it to untrusted peers. It has not undergone an independent security audit.

## Features in v0.1.0
- Deterministic block serialization and SHA-256 block hashes
- Proof-of-work mining with configurable difficulty
- Chain validation (hashes, links, proof of work, transaction structure)
- Basic transaction records and a genesis block
- JSON persistence and a small command-line interface
- Unit tests using only the Python standard library

## Requirements
- Python 3.11+
- No third-party runtime dependencies

## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
python -m pip install -e .
genesis-chain init --data chain.json
genesis-chain mine --data chain.json --miner genesis-miner --difficulty 3
genesis-chain status --data chain.json
genesis-chain validate --data chain.json
```

Or run from the repository without installing:
```bash
python -m genesis_chain.cli --help
```

## Project status
This is a single-node prototype. It does **not** yet implement peer discovery, a P2P protocol,
fork choice, mempool policy, account keys/signatures, replay protection, economic issuance,
or production-grade networking. The `sender` and `recipient` fields are labels, not authenticated identities.
Mining rewards are not implemented. Do not treat balances or transactions as real GNS funds.

## Roadmap
1. Cryptographic wallet keys and signed transactions
2. Nonce/accounting model and replay protection
3. Mempool and deterministic transaction ordering
4. P2P node protocol, peer authentication, and fork-choice rules
5. Testnet with multiple independently operated nodes
6. External security review, threat model, fuzzing, and load testing
7. Mainnet genesis ceremony and operational runbooks

## Security
Please do not report vulnerabilities publicly. Until a security policy and audited release process exist,
open a private security advisory with the maintainers. Never send real funds to this prototype.

## License
MIT. See [LICENSE](LICENSE).
