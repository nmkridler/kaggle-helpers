# kaggle-helpers
Helper functions for kaggle competitions

Currently provides helper functions for binary classification.

## Install
`python setup.py install`

## Usage
```python
from kaggle.classifier import metrics
auc = metrics.calc_auc(truth, prediction)
```