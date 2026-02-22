from matplotlib import pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
    plt.savefig('artifacts/foo.png')               # Export the figure.               

if __name__ == "__main__":
    main()
