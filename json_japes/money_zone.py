from rates_parser import RatesParser

rp = RatesParser("exchange_rates.json")

print(f"{rp.date}: {rp.base_rate} to GBP - {rp.gbp}")

wallet = 142
print(rp.to_GBP(wallet))
print(rp.to_JPY(wallet))