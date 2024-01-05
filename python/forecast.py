import vectorbt as vbt
import pandas as pd
import json

def forecast() -> None:
    data = vbt.YFData.pull("ETH-USD")
    pattern_ranges = data.hlc3.vbt.find_pattern(
        pattern=data.close.iloc[-10:],
        rescale_mode="rebase",
        overlap_mode="allow"
    ).status_closed.head(n=5)
    with open("../castdata.json", 'w') as f:
        json.dump(pattern_ranges.to_json(), f)

if __name__ == '__main__':
    forecast()
    