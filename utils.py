# utils.py - small helper functions (Python 2)
import os
import json

def read_file(path):
    """Read text file and return content."""
    print "\nReading file down"
    with open(path, 'r') as f:
        return f.read()

def write_file(path, data):
    """Write text data to file."""
    with open(path, 'w') as f:
        f.write(data)

def safe_json_load(s):
    """Try to load JSON from string, return None on failure."""
    try:
        return json.loads(s)
    except Exception:
        return None

def list_py_files(directory):
    return [p for p in os.listdir(directory) if p.endswith('.py')]

# EOF
