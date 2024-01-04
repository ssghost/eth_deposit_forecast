import vectorbt as vbt
import pandas as pd
import json

def find_patterns(data):
    pattern_ranges = data.hlc3.vbt.find_pattern(
        pattern=data.close.iloc[-10:],
        rescale_mode="rebase",
        overlap_mode="allow"
    ).status_closed
    return pattern_ranges

if __name__=='__main__':
    data = vbt.YFData.pull("ETH-USD")
    pattern_ranges = find_patterns(data)
    with open("castdata.json", 'w') as f:
        json.dump(pattern_ranges.to_json(), f)
