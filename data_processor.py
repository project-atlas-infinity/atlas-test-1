# data_processor.py - simple CSV-like processor (Python 2)
from utils import read_file, write_file, safe_json_load

def parse_rows(text, sep=','):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for row in lines:
        yield row.split(sep)

def summarize_rows(rows):
    counts = {}
    for r in rows:
        key = r[0] if r else ''
        counts[key] = counts.get(key, 0) + 1
    return counts

def load_and_summarize(path, sep=','):
    text = read_file(path)
    rows = list(parse_rows(text, sep))
    return summarize_rows(rows)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "Usage: python data_processor.py <file>"
        sys.exit(1)
