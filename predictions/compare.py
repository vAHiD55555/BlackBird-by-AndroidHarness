#!/usr/bin/env python3
"""Compare model prediction accuracy."""

import json
import sys


def compare(path="predictions/predictions.jsonl"):
    preds = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                preds.append(json.loads(line))

    by_model = {}
    for p in preds:
        by_model.setdefault(p["model"], []).append(p)

    print(f"{'Model':20} {'Total':8} {'Correct':8} {'Accuracy'}")
    print("-" * 46)
    for model, plist in by_model.items():
        total = len(plist)
        correct = sum(1 for p in plist if p.get("actual_result") == p["prediction"])
        acc = (correct / total * 100) if total > 0 else 0
        print(f"{model:20} {total:8} {correct:8} {acc:.1f}%")


if __name__ == "__main__":
    compare(sys.argv[1] if len(sys.argv) > 1 else None)
