#!/usr/bin/env python3
"""Compute per-subdivision Market Data stats from a HomeLight/MLS CSV export.

Usage: python3 analyze_market_data.py <csv_path> <subdivision_name> [<alias> ...]

Matches the Subdivision column case-insensitively against the name and any
aliases given. Prints the same fields the page template's Market Data cards
need: sale price range, median/avg sale price, homes sold, active, pending,
median/avg DOM, median list-to-sale ratio, high/low sale, total volume.
"""
import csv
import sys
import statistics


def money(s):
    if not s:
        return None
    s = s.replace("$", "").replace(",", "").strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def num(s):
    if not s:
        return None
    s = s.strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def main():
    path = sys.argv[1]
    names = {n.strip().lower() for n in sys.argv[2:]}

    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        for row in r:
            sub = (row.get("Subdivision") or "").strip().lower()
            if sub in names:
                rows.append(row)

    print(f"Matched {len(rows)} rows for: {', '.join(sys.argv[2:])}\n")
    if not rows:
        return

    sold = [row for row in rows if row["Status"] == "Sold"]
    active = [row for row in rows if row["Status"] == "Active"]
    pending = [row for row in rows if row["Status"] in ("Offer-Show", "Offer-No Show")]

    sold_prices = [money(r["Sold Price"]) for r in sold]
    sold_prices = [p for p in sold_prices if p is not None]

    print(f"Homes Sold: {len(sold)}")
    print(f"Active Listings: {len(active)}")
    print(f"Pending: {len(pending)}")

    if sold_prices:
        print(f"Sale Price Range: ${min(sold_prices):,.0f} - ${max(sold_prices):,.0f}")
        print(f"Median Sale Price: ${statistics.median(sold_prices):,.0f}")
        print(f"Avg Sale Price: ${statistics.mean(sold_prices):,.0f}")
        print(f"Highest Sale: ${max(sold_prices):,.0f}")
        print(f"Lowest Sale: ${min(sold_prices):,.0f}")
        print(f"Total Volume: ${sum(sold_prices):,.0f}")
    else:
        print("No sold-price data found among matched sold rows.")

    doms = [num(r["Days On Market"]) for r in sold]
    doms = [d for d in doms if d is not None]
    if doms:
        print(f"Median Days on Market: {statistics.median(doms):.0f} days")
        print(f"Avg Days on Market: {statistics.mean(doms):.0f} days")

    ratios = []
    for r in sold:
        lp = money(r["List Price"])
        sp = money(r["Sold Price"])
        if lp and sp:
            ratios.append(sp / lp * 100)
    if ratios:
        print(f"Median List-to-Sale Ratio: {statistics.median(ratios):.1f}%")

    print("\n-- Addresses (sold) --")
    for r in sold:
        print(f"  {r['Address']}, {r['Listing City State Zip']} — {r['Sold Price']} — closed {r.get('Closing Date','')}")


if __name__ == "__main__":
    main()
