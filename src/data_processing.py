
### `src/data_processing.py`
```python
import pandas as pd
import numpy as np

def load_data(filepath):
    """Load the dataset from the specified file path."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Preprocess the data by handling missing values, encoding categorical features, etc."""
    # Example preprocessing steps
    df = df.dropna()
    df = pd.get_dummies(df, columns=['team', 'driver'])
    return df
