import requests

def place_bet(market_id, outcome, bet_amount, key):
  # Set the request URL and headers
  url = "https://manifold.markets/api/v0/bet"
  headers = {
    "Authorization": "Key " + key
  }
  
  # Set the request body with the market ID, outcome, and bet amount
  body = {
    "marketId": market_id,
    "outcome": outcome,
    "betAmount": bet_amount
  }

  # Send the request to the API
  response = requests.post(url, headers=headers, json=body)
  
  # Assert that the request was successful
  assert response.status_code == 200
  
  # Return the response
  return response
import requests

def get_market_id(market_url, key):
  # Extract the market slug from the URL
  market_slug = market_url.split("/")[-1]

  # Set the request URL and headers
  url = "https://manifold.markets/api/v0/market/by-slug/" + market_slug
  headers = {
    "Authorization": "Key " + key
  }

  # Send the request to the API
  response = requests.get(url, headers=headers)
  
  # Parse the response to get the market ID
  market_id = response.json()["id"]

  # Return the market ID
  return market_id
