#!/usr/bin/env python3
import argparse, json, hashlib, pathlib

parser = argparse.ArgumentParser()
parser.add_argument("--apk", required=True)
parser.add_argument("--version", required=True)
parser.add_argument("--version-code", required=True)
args = parser.parse_args()
apk_path = pathlib.Path(args.apk)
apk_hash = hashlib.sha256(apk_path.read_bytes()).hexdigest()

data = {
    "flavors": {
        "newpipe": {
            "apk": f"https://github.com/6p6h/np_build_with_at_test/releases/download/latest/{apk_path.name}",
            "hash": apk_hash,
            "hash_type": "sha256",
            "version": args.version,
            "version_code": int(args.version_code)
        }
    },
    "stats": {}
}

with open("latest.json", "w") as f:
    json.dump(data, f, indent=2)
print("Generated latest.json")
