import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')

from matplotlib import pyplot as plt

#input data
data = [
    (8, 1, 45),
    (18, 0, 120),
    (26, 15, 210),
    (13, 16, 270),
    (0, 14, 320)
]
x_fact, y_fact = 15, 8
x_squre, y_squre = 16, 9

def prepare_system(data):
    A = np.array([[-np.tan(np.radians(row[2])), 1] for row in data])
    b = np.array([row[1] - np.tan(np.radians(row[2])) * row[0] for row in data])


    return A, b

def solve_system(A, b):
    At = np.transpose(A)
    return np.linalg.solve(np.dot(At, A), np.dot(At, b))

def visualize_data(data, ship_coordinates):
    plt.figure()
    i = 0
    for row in data:
        xi, yi, ai = row
        plt.plot(xi, yi, 'ro')
        x_end = xi + 20 * np.cos(np.radians(ai ))
        y_end = yi + 20 * np.sin(np.radians(ai ))
        plt.plot([xi, x_end], [yi, y_end])
        plt.text(xi, yi, str(i), fontsize=12, ha='right')
        i = i + 1

    plt.plot(ship_coordinates[0], ship_coordinates[1], 'bo')
    plt.plot(x_fact, y_fact, 'ro', markersize=8, label='теоретичне розташування')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Показати графік
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()

def visualize_data2(data, prev_index, ship_coordinates):
    plt.figure()
    i = 0
    for row in data:
        xi, yi, ai = row
        plt.plot(xi, yi, 'ro')
        x_end = xi + 20 * np.cos(np.radians(ai ))
        y_end = yi + 20 * np.sin(np.radians(ai ))
        plt.plot([xi, x_end], [yi, y_end])
        plt.text(xi, yi, str(prev_index[i]), fontsize=12, ha='right')
        i = i + 1

    plt.plot(ship_coordinates[0], ship_coordinates[1], 'bo')

    plt.plot(x_fact, y_fact, 'ro', markersize=8, label='теоретичне розташування')

    circle = plt.Circle((ship_coordinates[0], ship_coordinates[1]), 2, fill=False, color='b', linestyle='--')
    plt.gca().add_patch(circle)


    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()

def visualize_data3(data, prev_index, ship_coordinates):
    plt.figure()
    i = 0
    for row in data:
        xi, yi, ai = row
        plt.plot(xi, yi, 'ro')
        x_end = xi + 20 * np.cos(np.radians(ai ))
        y_end = yi + 20 * np.sin(np.radians(ai ))
        plt.plot([xi, x_end], [yi, y_end])
        plt.text(xi, yi, str(prev_index[i]), fontsize=12, ha='right')
        i = i + 1

    plt.plot(ship_coordinates[0], ship_coordinates[1], 'bo')


    square_vertices = [(x_squre, y_squre), (x_squre + 2, y_squre),
                       (x_squre + 2, y_squre + 2), (x_squre, y_squre + 2),
                       (x_squre, y_squre)]
    xs, ys = zip(*square_vertices)
    plt.plot(xs, ys, 'b-')



    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()

def angle_from_horizontal(x1, y1, x2, y2):
    angle_rad = np.arctan2( y2 - y1, x2 - x1 )
    angle_deg = np.degrees(angle_rad)


    return angle_deg%360

def angle_difference(angle1, angle2):
    diff = abs(angle1 - angle2) % 360
    return min(diff, 360 - diff)

def filter_data(data, terminal_angle):
    filtered_data = []
    prev_index = []
    i = 0
    for xi, yi, ai in data:
        if angle_difference(ai, angle_from_horizontal(xi, yi, x_fact, y_fact)) <= terminal_angle:
            filtered_row = (xi, yi, ai)
            filtered_data.append(filtered_row)
            prev_index.append(i)
            print("Датчик ", i, "відхиляється на кут ", angle_difference(ai, angle_from_horizontal(xi, yi, x_fact, y_fact)))

        else:
            print("Датчик ", i, "відхиляється на кут ", angle_difference(ai, angle_from_horizontal(xi, yi, x_fact, y_fact)),
                  "це більше ", terminal_angle)
        i = i + 1
    return filtered_data, prev_index


def filter_data_square(detectors, xs, ys):
    filtered_detectors = []
    prev_index = []
    i = 0
    for x, y, angle in detectors:
        # Calculate the coordinates of the top-right corner of the square

        slope = np.tan(np.radians(angle))

        # Calculate intersection with left edge
        intersection_x_left = xs
        intersection_y_left = y + (xs - x) * slope

        # Calculate intersection with right edge
        intersection_x_right = xs + 2
        intersection_y_right = y + (xs + 2 - x) * slope

        # Calculate intersection with top edge
        intersection_x_top = x + (ys + 2 - y) / slope
        intersection_y_top = ys + 2

        # Calculate intersection with bottom edge
        intersection_x_bottom = x + (ys - y) / slope
        intersection_y_bottom = ys



        # Check if any of the intersections are inside the square
        if ((xs <= intersection_x_left <= xs + 2 and ys <= intersection_y_left <= ys + 2) or
                (xs <= intersection_x_right <= xs + 2 and ys <= intersection_y_right <= ys + 2) or
                (xs <= intersection_x_top <= xs + 2 and ys <= intersection_y_top <= ys + 2) or
                (xs <= intersection_x_bottom <= xs + 2 and ys <= intersection_y_bottom <= ys + 2)):
            filtered_detectors.append((x, y, angle))
            prev_index.append(i)
            print("Датчик ", i, "не перетинає квадрат")
        else:
            print("Датчик ", i, "перетинає квадрат")

        i = i + 1

    return filtered_detectors, prev_index


def accuracy_evaluation(detectors, x, y):
    total_error = 0

    for x1, y1, angle in detectors:
        k = np.tan(np.radians(angle))
        error = (y1 - k * x1 + k * x - y)**2
        total_error += error

    return total_error

def main():
    #Завдання 1
    A, b =  prepare_system(data)

    ship_coordinates = solve_system(A, b)

    print("Координати коробля: ", ship_coordinates)
    print("Похибка: ", accuracy_evaluation(data, ship_coordinates[0], ship_coordinates[1]))
    visualize_data(data, ship_coordinates)

    # Завдання 2
    distance = np.sqrt((x_fact - ship_coordinates[0]) ** 2 + (y_fact - ship_coordinates[1]) ** 2)
    print("Передані координати: ", x_fact, y_fact)
    print("Відстань до даних з датчиків: ", distance)
    terminal_angle = 10
    #print (np.degrees(np.arctan2((y_fact-data[0][1]),(x_fact-data[0][0]))))
    filtered_data, prev_index = filter_data(data, terminal_angle)

    A2, b2 = prepare_system(filtered_data)
    print("Координати коробля після фільтрування датчиків: ", solve_system(A2,b2))
    ship_coordinates2 = solve_system(A2, b2)
    visualize_data2(filtered_data,prev_index, ship_coordinates2)
    print("Похибка: ", accuracy_evaluation(filtered_data, ship_coordinates2[0], ship_coordinates2[1]))

    # Завдання 3
    filtered_data2, prev_index2 = filter_data_square(data , x_squre, y_squre)
    A3, b3 = prepare_system(filtered_data2)
    print("Координати коробля після фільтрування датчиків по квадрату: ", solve_system(A3, b3))
    ship_coordinates3 =  solve_system(A3, b3)
    visualize_data3(filtered_data2, prev_index2, ship_coordinates3)
    print("Похибка: ", accuracy_evaluation(filtered_data2, ship_coordinates3[0], ship_coordinates3[1]))






#np.degrees((y_fact - data [0][1])/(x_fact - data[0][0]))

if __name__ == "__main__":
    main()

