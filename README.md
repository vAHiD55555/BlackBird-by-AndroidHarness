# BlackBird by AndroidHarness

Market data pipeline for trading model practice — BlackBird Core v0.4.

## Structure

| Directory | Purpose |
|-----------|---------|
| `data/` | Raw market JSONL from your servers |
| `analysis/` | Technical analysis script |
| `predictions/` | Model prediction logging & comparison |
| `docs/` | Architecture, models, trading rules |

## Run

### 1. Place data
Put your server JSONL in `data/market_data.jsonl`

### 2. Analyze
```bash
python3 analysis/analyze.py data/market_data.jsonl
```

### 3. Compare predictions (after actual results known)
```bash
python3 predictions/compare.py
```

## Models Used
- Gemini 3 Flash (Analysis)
- Claude Haiku 5.5 (Critical Review)
- Nemotron 3 Ultra (Strategic Prediction)
- Claude Sonnet 4.6 (Code & Integration)

## License
MIT
