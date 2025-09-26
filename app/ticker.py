import requests
import time

def get_price(symbol: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    return requests.get(url).json()[symbol]["usd"]

if __name__ == "__main__":
    interval = int(input("Refresh interval (seconds): ") or 5)
    print(f"\nStarting live crypto ticker (BTC & ETH) every {interval} sec...\n")

    try:
        while True:
            btc = get_price("bitcoin")
            eth = get_price("ethereum")
            print(f"BTC: ${btc:,.2f} | ETH: ${eth:,.2f}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nTicker stopped.")
