import numpy

from mpPy.Model.Matrix import Matrix


class ForceScheme(Matrix):
    """
    Force Scheme Projection

    """

    def __init__(self, matrix,
                 max_iterations=50,
                 tolerance=0.0,
                 fraction_of_delta=8.0,
                 epsilon=1e-6):
        super().__init__(matrix)
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.fraction_of_delta = fraction_of_delta
        self.epsilon = epsilon

class LSP(Matrix):
    """

    Least Square Projeciton

    """

    def __init__(self, matrix,
                 subsample_indices = None,
                 initial_subsample=None,
                 num_neighbors = 15,
                 dimensionality = 2):

        super().__init__(matrix)
        self.subsample_indices = subsample_indices
        self.initial_subsample = initial_subsample
        self.num_neighbors = num_neighbors
        self.dimensionality = dimensionality

class Pekalska(Matrix):
    """

    Pekalska Approximation

    """
    def __init__(self, matrix,
                 subsample_indices = None,
                 subsample_mapping = None):
        super().__init__(matrix)
        self.subsample_indices = subsample_indices
        self.subsample_mapping = subsample_mapping

class PLMP(Matrix):
    """

    Part-Linear Multidimensional Projection

    """
    def __init__(self, matrix,
                 subsample_indices = None,
                 subsample_control_points = None,
                 dimensionality = 2):
        super().__init__(matrix)
        self.subsample_indices = subsample_indices
        self.subsample_control_points = subsample_control_points
        self.dimensionality = dimensionality

class LAMP(Matrix):
    """

    Local Affine Multidimensional Projection

    """

    def __init__(self, matrix,
                 proportion = 1,
                 subsample_indices = None,
                 initial_sample = None):
        super().__init__(matrix)
        self.subsample_indices = subsample_indices
        self.initial_sample = initial_sample
        self.proportion = proportion