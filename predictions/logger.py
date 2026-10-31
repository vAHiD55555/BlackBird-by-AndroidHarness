#!/usr/bin/env python3
"""Log predictions from models for later comparison."""

import json
from datetime import datetime, timezone


def log_prediction(asset, model, prediction, confidence, reasoning):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "asset": asset,
        "model": model,
        "prediction": prediction,
        "confidence": confidence,
        "reasoning": reasoning,
        "actual_result": None,
    }
    with open("predictions/predictions.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def update_outcome(index, actual_result):
    with open("predictions/predictions.jsonl", "r", encoding="utf-8") as f:
        lines = f.readlines()
    if 0 <= index < len(lines):
        entry = json.loads(lines[index])
        entry["actual_result"] = actual_result
        lines[index] = json.dumps(entry, ensure_ascii=False)
        with open("predictions/predictions.jsonl", "w", encoding="utf-8") as f:
            f.writelines(lines)
