from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import precision_recall_curve


def calc_auc(t, p):
    fpr, tpr, thresh = roc_curve(t, p)
    return auc(fpr, tpr)

def max_f1(t,p):
    """
        Determine the maximum F1 score
        Args:
            t: truth
            p: predictions
        Returns:
            max f1 score
    """
    precision, recall, thresholds = precision_recall_curve(t,p)
    denom = (precision + recall)
    f1 = 2.*precision*recall/(precision + recall)
    f1[denom == 0] = 0.
    return f1.max()

