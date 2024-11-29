from sklearn.datasets import load_iris, make_circles, make_moons

from matplotlib import pylab

import numpy as np

from sklearn.cluster import KMeans, DBSCAN

from mpl_toolkits.mplot3d import Axes3D

from sklearn.metrics import silhouette_score

import pandas as pd

from scipy.cluster.hierarchy import dendrogram, fcluster, linkage

from scipy.spatial.distance import pdist

from scipy.spatial.distance import euclidean

SEED = 42
