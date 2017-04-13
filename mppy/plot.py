import matplotlib.pyplot as mplpy
import numpy as np

def simple_scatter_plot(matrix_2d, clusters=None):
    if clusters is None:
        clusters = np.zeros((matrix_2d.shape[0]))
    mplpy.scatter(matrix_2d[:,0], matrix_2d[:,1], c=clusters)
    mplpy.show()

def semi_interactive_scatter_plot(matrix_2d, matrix, clusters=None):
    if clusters is None:
        clusters = np.zeros((matrix_2d.shape[0]))

    if 1:  # picking on a scatter plot (matplotlib.collections.RegularPolyCollection)

        def onpick3(event):
            ind = event.ind
            print("Element: ",ind,"->", matrix[ind,:])

        fig = mplpy.figure()
        ax1 = fig.add_subplot(111)
        ax1.scatter(matrix_2d[:,0], matrix_2d[:,1], c=clusters, picker=True)
        fig.canvas.mpl_connect('pick_event', onpick3)

    mplpy.show()