import numpy as np
import pandas as pd

from transformers import moving_average


def test_moving_average():
    df = pd.DataFrame(
            {"time_s": np.arange(5) / 1000.0, "ch0": [0.0, 0.0, 3.0, 0.0, 0.0]}
        )
    df.attrs = {"x": "time_s", "sample_rate": 1000.0}
    out = moving_average(df, window_ms=3.0)
    np.testing.assert_allclose(out["ch0"], [0.0, 1.0, 1.0, 1.0, 0.0])
