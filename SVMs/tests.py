# Tests that the environment works correctly

import matplotlib
import sklearn
import pandas
import scipy
import numpy

from scipy.misc import imread
from sklearn.externals.six.moves import xrange

from sklearn import svm

matplotlib.use('TkAgg')
import tkinter as Tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.contour import ContourSet
from matplotlib.lines import Line2D


def test_svm():
    """Trains a SVM"""
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)  
    clf.predict([[2., 2.]])


def test_tkinter():
    """Tests that a Tk inter object can be created"""
    root = Tk.Tk()

