import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np


def visualize_transformation(vector, trans_matrix):
    """
    :param vector:
    :param trans_matrix:
    :return:
    """
    fig, ax = plt.subplots()
    mapped_vector = np.dot(trans_matrix, vector)
    
    ax.quiver(0, 0, vector[0], vector[1], color='blue', angles='xy', scale_units='xy', scale=1, label="input vector")
    
    ax.quiver(0, 0,
              mapped_vector[0], mapped_vector[1],
              angles='xy',
              scale_units='xy',
              color='green',
              scale=1,
              label="transformed vector")
    
    # Add the grid
    ax.grid(which='major', axis='both', linestyle='-')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_ylabel("y axis", color='red')
    ax.set_xlabel("x axis", color='red')
    ax.legend()
    plt.show()


if __name__ == "__main__":
    # construct the vector
    inp_vector = np.array([1, 1])
    # construct the transformation matrix
    transform_matrix = np.array([[-1, 0], [0, 1]])
    
    # call visualization method to visualize transformation
    visualize_transformation(inp_vector, transform_matrix)
