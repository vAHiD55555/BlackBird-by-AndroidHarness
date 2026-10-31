# Market Data — JSONL Input

Here you put your server's market data files (JSONL format).

## Format
Each line is one JSON record:
{
  "asset": "BTC-USD",
  "price": 81500.0,
  "source_time": "2026-10-20T01:06:47.101352047Z",
  "timestamp": "2026-10-20 03:06:49"
}

## Files
- `market_data.jsonl` — raw market data from your server
