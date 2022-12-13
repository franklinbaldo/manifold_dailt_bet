import requests
import os
def place_bet(market_id, outcome, bet_amount, key):
  # Set the request URL and headers
  url = "https://manifold.markets/api/v0/bet"
  headers = {"Authorization": f"Key {key}"}

  # Set the request body with the market ID, outcome, and bet amount
  body = {
    "marketId": market_id,
    "outcome": outcome,
    "betAmount": bet_amount
  }

  # Send the request to the API
  response = requests.post(url, headers=headers, json=body)

  # Assert that the request was successful
  assert response.status_code == 200, print(response.json(),response.status_code)

  # Return the response
  return response


def get_market_id(market_url, key):
  # Extract the market slug from the URL
  market_slug = market_url.split("/")[-1]

  # Set the request URL and headers
  url = f"https://manifold.markets/api/v0/slug/{market_slug}"
  headers = {"Authorization": f"Key {key}"}

  # Send the request to the API
  response = requests.get(url, headers=headers)

  return response.json()["id"]


def main():
  # Get the key from the environment
  key = os.environ["KEY"]

  # Get the market ID from the URL
  market_url = "https://manifold.markets/FranklinBaldo/brazil-election-will-brazil-have-a-b38010e4acf2"
  market_id = get_market_id(market_url, key)

  # Place the bet
  response = place_bet(market_id, "NO", 25, key)


if __name__ == "__main__":
  main()
