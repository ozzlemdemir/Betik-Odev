from pathlib import Path
import csv, json
from .dekorator import timer

@timer
def read_csv(path):
    #dosyadan CSV okur
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

@timer
def write_json(path, obj):
    #JSON dosyasına yazar
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)#dump ile yazdırır

@timer
def write_text(path, text):
    #TXT dosyasına yazar
    Path(path).write_text(text, encoding="utf-8")
