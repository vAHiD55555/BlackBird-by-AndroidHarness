#!/usr/bin/env python3
"""BlackBird DataBridge — Technical analysis of market JSONL."""

import json
import math
from collections import defaultdict
import sys


def load_jsonl(path):
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


def rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    gains, losses = [], []
    for i in range(len(prices) - period, len(prices)):
        delta = prices[i] - prices[i - 1]
        gains.append(max(delta, 0))
        losses.append(max(-delta, 0))
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def volatility(prices, period=24):
    if len(prices) < period + 1:
        return None
    returns = []
    for i in range(len(prices) - period, len(prices)):
        if prices[i - 1] != 0:
            returns.append((prices[i] - prices[i - 1]) / prices[i - 1])
    if not returns:
        return None
    mean = sum(returns) / len(returns)
    variance = sum((r - mean) ** 2 for r in returns) / len(returns)
    return math.sqrt(variance) * math.sqrt(24)


def trend(prices):
    if len(prices) < 5:
        return "UNKNOWN"
    sma5 = sma(prices, 5)
    sma20 = sma(prices, 20)
    if sma5 is None or sma20 is None:
        return "UNKNOWN"
    if sma5 > sma20 * 1.001:
        return "UP"
    elif sma5 < sma20 * 0.999:
        return "DOWN"
    return "SIDEWAYS"


def analyze_market(jsonl_path):
    records = load_jsonl(jsonl_path)
    assets = defaultdict(list)
    for r in records:
        assets[r["asset"]].append(r)

    results = {}
    for asset, data in assets.items():
        prices = [d["price"] for d in data if d.get("price")]
        if len(prices) < 20:
            results[asset] = {"error": "insufficient data"}
            continue

        results[asset] = {
            "asset": asset,
            "count": len(prices),
            "last_price": prices[-1],
            "sma_5": round(sma(prices, 5), 4) if sma(prices, 5) else None,
            "sma_20": round(sma(prices, 20), 4) if sma(prices, 20) else None,
            "rsi_14": round(rsi(prices, 14), 2) if rsi(prices, 14) else None,
            "volatility": round(volatility(prices, 24), 6) if volatility(prices, 24) else None,
            "trend": trend(prices),
            "change_pct": round((prices[-1] - prices[0]) / prices[0] * 100, 4),
        }

    return results


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/market_data.jsonl"
    results = analyze_market(path)
    print(json.dumps(results, indent=2, ensure_ascii=False))

    with open("analysis/output.jsonl", "w", encoding="utf-8") as f:
        for asset, data in results.items():
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
