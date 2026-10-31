# Architecture — BlackBird by AndroidHarness

## Data Flow

```
سرور (Market Data)
     │ JSONL
     ▼
 data/market_data.jsonl
     │ analysis/analyze.py
     ▼
 analysis/output.jsonl
     │ predictions/logger.py / predictions/compare.py
     ▼
 predictions/predictions.jsonl
     └──> models comparison
```

## Components

| Component | Responsibility |
|-----------|----------------|
| `analysis/analyze.py` | RSI, SMA, Volatility, Trend per asset |
| `predictions/logger.py` | Log model predictions (asset, model, prediction, confidence) |
| `predictions/compare.py` | Compare model accuracy after outcomes known |
| `data/` | Raw JSONL input from market data server |
