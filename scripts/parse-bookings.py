#!/usr/bin/env python3
"""Разбор ответа Wix extended-bookings/query в читаемую таблицу.

Использование: Claude делает MCP-вызов (см. docs/ops/dashboard-bookings.md),
сохраняет ответ в файл, затем:

    python3 scripts/parse-bookings.py <файл-с-ответом>

Парсер регулярками, а не json.loads: большие ответы Wix приходят
обрезанными на 50k символов, и строгий разбор на них падает.
"""
import re
import sys
from collections import Counter

if len(sys.argv) < 2:
    sys.exit("укажи файл с ответом API")

raw = open(sys.argv[1], encoding="utf-8").read()
rows = []
for chunk in re.split(r'(?="booking":\{"id")', raw)[1:]:
    title = re.search(r'"title":"((?:[^"\\]|\\.)*)"', chunk)
    if not title:
        continue
    created = re.search(r'"createdDate":"(\d{4}-\d{2}-\d{2})', chunk)
    source = re.search(r'"platform":"(\w+)","actor":"(\w+)"', chunk)
    amount = re.search(r'"totalPrice":\{"amount":"([\d.]+)"', chunk)
    status = re.search(r'"status":"(\w+)"', chunk)
    payment = re.search(r'"paymentStatus":"(\w+)"', chunk)
    rows.append({
        "created": created.group(1) if created else "?",
        "service": title.group(1),
        "platform": source.group(1) if source else "?",
        "actor": source.group(2) if source else "?",
        "amount": amount.group(1) if amount else "-",
        "status": status.group(1) if status else "-",
        "payment": payment.group(1) if payment else "-",
    })

print(f"{'СОЗДАНА':11} {'УСЛУГА':32} {'ОТКУДА':11} {'КТО':9} {'$':>7} {'СТАТУС':10} ОПЛАТА")
for r in rows:
    print(f"{r['created']:11} {r['service'][:32]:32} {r['platform']:11} "
          f"{r['actor']:9} {r['amount']:>7} {r['status']:10} {r['payment']}")

print(f"\nвсего записей: {len(rows)}")
print("кто завёл:", dict(Counter(r["actor"] for r in rows)))

# Брошенные оформления: клиент начал запись на сайте и не дошёл до конца
abandoned = [r for r in rows if r["status"] == "CREATED"]
web = [r for r in rows if r["actor"] == "CUSTOMER"]
if web:
    print(f"через сайт: {len(web)}, из них брошено на оформлении: {len(abandoned)}")

paid = sum(float(r["amount"]) for r in rows if r["amount"] != "-")
print(f"сумма подтверждённых записей: ${paid:,.0f}")
