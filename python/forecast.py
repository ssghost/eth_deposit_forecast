from train import *
from torch import load
import json

def forecast() -> None:
    model = load("../model.pt")
    e_data = vbt.YFData.download("ETH-USD", start="5 days ago UTC").get('Close')
    predictions = model.predict(e_data.test_dataloader())
    with open("../castdata.json", 'w') as f:
        json.dump(predictions.to_json(), f)

if __name__ == '__main__':
    forecast()
    