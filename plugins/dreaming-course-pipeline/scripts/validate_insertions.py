"""Validate insertion identities, original anchors and contiguous story sequences."""
import argparse
import json
from pathlib import Path


def validate(plan):
    sources = {}
    for item in plan["sources"]:
        name, count = item["source"], item["slide_count"]
        if not isinstance(name, str) or not name or name in sources:
            raise ValueError("Source identifiers must be nonempty and unique")
        if type(count) is not int or count < 1:
            raise ValueError("Source slide counts must be positive integers")
        sources[name] = count
    rows = plan["insertions"]
    if not sources or not rows:
        raise ValueError("Sources and insertions are required")
    sequences = {}
    for expected_id, row in enumerate(rows, 1):
        for key in ("id", "insert_before_slide", "sequence", "frame", "frame_count"):
            if type(row[key]) is not int or row[key] < 1:
                raise ValueError(f"{key} must be a positive integer")
        if row["id"] != expected_id:
            raise ValueError("Insertion IDs must be consecutive from 1")
        if row["source"] not in sources or row["insert_before_slide"] > sources[row["source"]]:
            raise ValueError("Insertion anchor is outside its original source")
        for key, minimum in (("story_text", 35), ("narration", 35),
                             ("concept_connection", 1), ("character_bible", 1),
                             ("visual_direction", 1)):
            if not isinstance(row.get(key), str) or len(row[key].split()) < minimum:
                raise ValueError(f"Insertion {expected_id}: incomplete {key}")
        sequences.setdefault(row["sequence"], []).append(row)
    for group in sequences.values():
        first = group[0]
        if len(group) != first["frame_count"]:
            raise ValueError("Sequence frame count does not match its actual frames")
        for index, row in enumerate(group):
            if (row["frame"] != index + 1 or row["id"] != first["id"] + index
                    or any(row[key] != first[key] for key in
                           ("source", "insert_before_slide", "frame_count", "character_bible"))):
                raise ValueError("Sequence must be contiguous with one anchor and stable character bible")
    return {"original_slides": sum(sources.values()), "insertions": len(rows),
            "final_slides": sum(sources.values()) + len(rows)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(validate(json.loads(args.plan.read_text(encoding="utf-8-sig"))), indent=2))
    except (ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Invalid insertion plan: {error}\n")
