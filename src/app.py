from src.dosya_islemleri import read_csv, write_json, write_text
from src.processing import clean, stats, build_report

def main():
    read_doc = "data/people.csv"
    json_cleaned = "data/people_clean.json"
    json_stats = "data/stats.json"
    report_txt = "data/report.txt"

    # 1. CSV oku
    rows = read_csv(read_doc)

    # 2. Temizle
    valid = clean(rows)

    # 3. İstatistikleri hesapla
    st = stats(valid)

    # 4. Çıktıları yaz
    write_json(json_cleaned, valid)
    write_json(json_stats, st)
    write_text(report_txt, build_report(st))

    print("İşlem tamamlandı")

if __name__ == "__main__":
    main()
