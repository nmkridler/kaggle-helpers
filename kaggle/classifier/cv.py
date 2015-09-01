from sklearn.cross_validation import KFold
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.cross_validation import train_test_split

from .metrics import calc_auc

def run_folds(algo, X, y, folds):
    """
    """
    y_ = np.empty(y.size)
    for train, test in kf:
        algo.fit(X[train, :], y[train])
        y_[test] = algo.predict_proba(X[test, :])[:,1]
    return y_

def kfold(algo, X, y, n_folds=4, seed=1337):
    """
    """
    kf = KFold(X.shape[0],
               n_folds=n_folds,
               indices=False,
               shuffle=True,
               random_state=seed)

    return run_folds(algo, X, y, kf)


def stratified_kfold(algo, X, y, n_folds=4, seed=1337):
    """
    """
    kf = StratifiedKFold(y,
                         n_iter=n_folds,
                         indices=False,
                         random_state=seed)

    return run_folds(algo, X, y, kf)

def holdout(algo, X, y, test_size=0.3, n_iter=10, seed=1337,
    metric=calc_auc, verbose=False):
    mean_score = 0.
    for i in xrange(n_iter):
        x_tr, x_cv, y_tr, y_cv = train_test_split(X, y,
            test_size=test_size, random_state=i*seed)
        algo.fit(x_tr, y_tr)
        y_ = algo.predict_proba(x_cv)[:,1]
        _score = metric(y_cv, y_)
        mean_score += _score
        if verbose:
            print "AUC: %f (fold %d of %d)"%(_score, i, n_iter)

    return mean_score / n_iter

def stratified_holdout(algo, X, y, n_iter=10, seed=1337, test_size=0.3,
    metric=calc_auc, verbose=False):
    mean_score = 0.
    sss = StratifiedShuffleSplit(y, n_iter=n_iter,
        test_size=test_size, random_state=seed)
    for train, test in sss:
        algo.fit(X[train,:],yTarget[train])
        y_ = algo.predict_proba(X[test, :])[:, 1]
        _score = metric(y[test], y_)
        if verbose:
            print "AUC: %f (fold %d of %d)"%(_score, i, n_iter)
        mean_score += _score

    return mean_score / n_iter