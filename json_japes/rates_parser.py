import json

class RatesParser:
    def __init__(self, filepath):
        rates = self._open_json_file(filepath)
        self.base_rate = rates["base"]
        self.date = rates["date"]
        self.gbp = rates["rates"]["GBP"]
        self.usd = rates["rates"]["USD"]
        self.jpy = rates["rates"]["JPY"]

    def _open_json_file(self, filepath: str) -> dict:
        with open(filepath) as jsonfile:
            return json.load(jsonfile)

    def to_JPY(self, amount):
        return amount * self.jpy

    def to_GBP(self, amount):
        return amount * self.gbp


if __name__ == "__main__":
    rp = RatesParser("exchange_rates.json")
    print(rp.gbp)