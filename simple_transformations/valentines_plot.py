import matplotlib.pyplot as plt

# v of the heart
plt.quiver(5, 4, -5, -4, angles='xy', scale=1, scale_units='xy', color='red', label="Love is in the grid!")
plt.quiver(-5, 4, 5, - 4, angles='xy', scale=1, scale_units='xy', color='red')

plt.quiver(0, 4, 2, 2, angles='xy', scale=1, scale_units='xy', color='red')
plt.quiver(0, 4, -2, 2, angles='xy', scale=1, scale_units='xy', color='red')

plt.quiver(2, 6, 2, 0, angles='xy', scale=1, scale_units='xy', color='red')
plt.quiver(-2, 6, -2, 0, angles='xy', scale=1, scale_units='xy', color='red')

plt.quiver(-4, 6, -1, -2, angles='xy', scale=1, scale_units='xy', color='red')
plt.quiver(4, 6, 1, -2, angles='xy', scale=1, scale_units='xy', color='red')

plt.grid(True)
plt.legend()
plt.title("Happy valentines day!")
plt.xlabel("atrium")
plt.ylabel("ventricle")
plt.xlim(-10, 10)
plt.ylim(-1, 10)
plt.savefig("valentines_day.png")
plt.show()
