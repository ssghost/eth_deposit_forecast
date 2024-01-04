import vectorbt as vbt


data = vbt.YFData.pull("ETH-USD")
def find_patterns(data):
    price = data.hlc3
    pattern = price.values[-LAST_N_BARS:]
    pattern_ranges = price.vbt.find_pattern(
        pattern=pattern,
        rescale_mode="rebase",
        overlap_mode="allow",
        wrapper_kwargs=dict(freq=TIMEFRAME)
    )
    pattern_ranges = pattern_ranges.status_closed
    return pattern_ranges

pattern_ranges = find_patterns(data)