
import numpy as np

def rouwenhorst(n, mu, rho, sigma):
    """
    Code to approximate an AR(1) process using the Rouwenhorst method as in
    Kopecky & Suen, Review of Economic Dynamics (2010), Vol 13, pp. 701-714
    Adapted from Matlab code by Martin Floden.

    Parameters
    ----------
    n : int
        Number of states for discretized Markov process
    mu : float
        Unconditional mean or AR(1) process
    rho : float
        Autocorrelation of AR(1) process
    sigma : float
        Conditional standard deviation of AR(1) innovations

    Returns
    -------
    z : numpy.ndarray
        Discretized state space
    Pi : numpy.ndarray
        Transition matrix of discretized process where
            Pi[i,j] = Prob[z'=z_j | z=z_i]
    """

    if n < 1:
        msg = 'Invalid number of states'
        raise ValueError(msg)
    if sigma < 0.0:
        msg = 'Argument sigma must be non-negative'
        raise ValueError(msg)
    if abs(rho) >= 1.0:
        msg = 'Cannot create stationary process with abs(rho) >= 1.0'
        raise ValueError(msg)

    if n == 1:
        # Degenerate process on a single state: disregard variance and
        # autocorrelation
        z = np.array([mu])
        Pi = np.ones((1, 1))
        return z, Pi

    p = (1+rho)/2
    Pi = np.array([[p, 1-p], [1-p, p]])

    for i in range(Pi.shape[0], n):
        tmp = np.pad(Pi, 1, mode='constant', constant_values=0)
        Pi = p * tmp[1:, 1:] + (1-p) * tmp[1:, :-1] + \
             (1-p) * tmp[:-1, 1:] + p * tmp[:-1, :-1]
        Pi[1:-1, :] /= 2

    fi = np.sqrt(n-1) * sigma / np.sqrt(1 - rho ** 2)
    z = np.linspace(-fi, fi, n) + mu

    return z, Pi


def markov_ergodic_dist(transm):
    """
    Compute the ergodic distribution implied by a given Markov chain transition
    matrix.

    Parameters
    ----------
    transm : numpy.ndarray
        Markov chain transition matrix where the element at position (i,j)
        represents the transition probability from i to j.

    Returns
    -------
    mu : numpy.ndarray
        Ergodic distribution
    """

    # Check that this is a transition matrix
    assert np.all(np.abs(transm.sum(axis=0) - 1) < 1e-12)
    assert np.all(transm >= 0.0)

    m = transm - np.identity(transm.shape[0])
    m[-1] = 1
    m = np.linalg.inv(m)
    mu = np.ascontiguousarray(m[:, -1])
    assert np.abs(np.sum(mu) - 1) < 1e-9
    mu /= np.sum(mu)

    return mu
