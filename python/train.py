import vectorbt as vbt
from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer
import lightning.pytorch as pl
from typing import Any

def train() -> Any:
    data = vbt.YFData.download("ETH-USD", start="5 years ago UTC").get('Close')
    t_data = TimeSeriesDataSet(data, target='Close', time_idx='Date', group_ids= ['Date'])
    t_data.prepare_training(split_into_train_val_test=[0.8, 0.1, 0.1])
    model = TemporalFusionTransformer.from_dataset(t_data)
    trainer = pl.Trainer()
    trainer.fit(model, t_data.train_dataloader())
    return model

if __name__ == '__main':
    train()