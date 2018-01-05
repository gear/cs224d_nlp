#!/usr/bin/env python

import numpy as np

def _sigmoid(x):
    if x > 0:
        s = 1.0 / (1.0 + np.exp(-x))
    else:
        s = np.exp(x) / (1.0 + np.exp(x))
    return s

sigmoid = np.vectorize(_sigmoid)

def sigmoid_grad(f):
    return f * (1 - f)

def test_sigmoid_basic():
    print "Running basic tests..."
    x = np.array([[1, 2], [-1, -2]])
    f = sigmoid(x)
    g = sigmoid_grad(f)
    print f
    f_ans = np.array([
        [0.73105858, 0.88079708],
        [0.26894142, 0.11920292]])
    assert np.allclose(f, f_ans, rtol=1e-05, atol=1e-06)
    print g
    g_ans = np.array([
        [0.19661193, 0.10499359],
        [0.19661193, 0.10499359]])
    assert np.allclose(g, g_ans, rtol=1e-05, atol=1e-06)
    print "You should verify these results by hand!\n"


def test_sigmoid():
    print "Running your tests..."


if __name__ == "__main__":
    test_sigmoid_basic();
    test_sigmoid()
