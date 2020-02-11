import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
import numpy as np


def plot_image_vectors(img, scale, trans_matrix_1, trans_matrix_2):
    im = np.divide(img, 255)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for row in im[90:110]:
        for col in row[130:140]:
            ax.quiver(0, 0, 0, col[0], col[1], col[2], color='blue')
            transformed_vector_1 = np.dot(col, trans_matrix_1)
            ax.quiver(0, 0, 0, transformed_vector_1[0], transformed_vector_1[1], transformed_vector_1[2], color="red")
            transformed_vector_2 = np.dot(col, trans_matrix_2)
            ax.quiver(0, 0, 0, transformed_vector_2[0], transformed_vector_2[1], transformed_vector_2[2],
                      color="#0EFF09")
    
    ax.set_xlim(-1.3, 1.5)
    ax.set_xlabel("R channel", size='xx-large')
    ax.set_ylim(-1.3, 1.5)
    ax.set_ylabel("G channel", size='xx-large')
    ax.set_zlim(-1.3, 1.5)
    ax.set_zlabel("B channel", size='xx-large')
    plt.show()


if __name__ == "__main__":
    img = cv2.imread("color_RGB.png")
    transform_matrix_1 = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    transform_matrix_2 = np.array([[-1, .3, 0], [.4, .5, 0], [0, 0, .8]])
    plot_image_vectors(img, 2, transform_matrix_1, transform_matrix_2)
