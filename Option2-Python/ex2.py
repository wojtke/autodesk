import numpy as np

if __name__ == '__main__':
    # Prompt the user for the number of points to generate
    num_points = int(input("Enter the number of points to generate: "))

    # Generate random points in the range [-100, 100] for both axes
    points = np.random.uniform(-100, 100, size=(num_points, 2))

    # Initialize variables to hold the smallest triangle found so far
    smallest_area = float('inf')
    smallest_triangle = None

    # Iterate over all combinations of three points
    for i in range(num_points):
        for j in range(i + 1, num_points):
            for k in range(j + 1, num_points):
                # Compute the area of the triangle formed by the three points
                a = points[i]
                b = points[j]
                c = points[k]
                area = 0.5 * np.abs(np.cross(b - a, c - a))

                # Update the smallest triangle found so far if necessary
                if area < smallest_area:
                    smallest_area = area
                    smallest_triangle = (a, b, c)

    # Print the smallest triangle found
    print(f"The smallest triangle has an area of {smallest_area} and is formed by the points:")
    for point in smallest_triangle:
        print(point)