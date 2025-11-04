from statistics import mean
from .dekorator import required_columns

@required_columns({"name", "age", "city"})
def clean(rows: list[dict]) -> list[dict]:
    #boş kolonları temizkler ve age'i int yapar
    cleaned = []
    for r in rows:
        age_val = r.get("age", "").strip()
        if not age_val:
            continue
        try:
            age = int(age_val)
        except ValueError:
            continue

        cleaned.append({
            "name": r.get("name", "").strip(),
            "age": age,
            "city": r.get("city", "").strip()
        })
    return cleaned


def stats(rows: list[dict]) -> dict:
    #istatistikler 
    if not rows:
        return {"count": 0, "avg_age": 0, "by_city": {}}

    ages = [r["age"] for r in rows]
    by_city = {}
    for r in rows:
        by_city[r["city"]] = by_city.get(r["city"], 0) + 1

    return {
        "count": len(rows),
        "avg_age": round(mean(ages), 2),
        "by_city": by_city
    }


def build_report(st: dict) -> str:
   #rapor üretme 
    lines = [
        " Rapor",
        "",
        f"- Geçerli kayıt sayısı: {st['count']}",
        f"- Ortalama yaş: {st['avg_age']}",
        "",
        "Şehir dağılımı:"
    ]
    for city, count in st["by_city"].items():
        lines.append(f"  - {city}: {count}")
    return "\n".join(lines) + "\n"
