import matplotlib.pyplot as plt
import numpy as np


def visualize_transformation(vector, trans_matrix):
    """
        Method to visualize the transform operation on a vector.
    :param vector: input vector as a list or np.nd array
    :param trans_matrix: transform matrix as np.nd array
    :return: None
    """
    fig, ax = plt.subplots()
    try:
        mapped_vector = np.dot(trans_matrix, vector)
    except ValueError:
        raise ValueError("check input vector and transform matrix dimensions")
    
    for v in vector:
        ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='green')
    
    # apply transformation
    for i, i_vector in enumerate(vector):
        vector[i] = np.dot(trans_matrix, i_vector)
    
    for v1 in vector:
        ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red')
    
    # Add the grid
    ax.grid(which='major', axis='both', linestyle='-')
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_ylabel("y axis", color='red')
    ax.set_xlabel("x axis", color='red')
    ax.legend()
    plt.show()


if __name__ == "__main__":
    # construct the vector
    inp_vector = np.random.randn(2, 2)
    # construct the transformation matrix
    transform_matrix = np.array([[0, 1], [-1, 0]])
    
    # call visualization method to visualize transformation
    visualize_transformation(inp_vector, transform_matrix)
