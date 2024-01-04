import vectorbt as vbt
vbt.settings.set_theme("dark")
SYMBOL = "BTC-USD"
TIMEFRAME = "1 hour"
START = "one year ago"

LAST_N_BARS = 66
PRED_N_BARS = 12

GIF_FNAME = "projections.gif"
GIF_N_BARS = 72
GIF_FPS = 4
GIF_PAD = 0.01

data = vbt.YFData.pull(SYMBOL, timeframe=TIMEFRAME, start=START)
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