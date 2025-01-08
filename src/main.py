from agents.identifier import CryptoIdentifier

def main():
    identifier = CryptoIdentifier()
    top_cryptos = identifier.identify_high_potential_cryptos()
    print("Top Cryptos Identified:")
    print(top_cryptos)

if __name__ == "__main__":
    main()