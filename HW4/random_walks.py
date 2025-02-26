import numpy as np
import matplotlib.pyplot as plt

def oneHundredRandomWalks():
    def random_walk_2d(steps):
        # Initialize arrays to store the coordinates
        x = np.zeros(steps)
        y = np.zeros(steps)
        
        for i in range(1, steps):
            # Randomly choose a direction: up, down, left, or right
            direction = np.random.choice(['up', 'down', 'left', 'right'])
            
            if direction == 'up':
                y[i] = y[i-1] + 1
                x[i] = x[i-1]
            elif direction == 'down':
                y[i] = y[i-1] - 1
                x[i] = x[i-1]
            elif direction == 'left':
                x[i] = x[i-1] - 1
                y[i] = y[i-1]
            elif direction == 'right':
                x[i] = x[i-1] + 1
                y[i] = y[i-1]
        
        return x, y

    # Parameters
    steps = 1000
    num_walks = 100

    # Plot all random walks
    plt.figure(figsize=(10, 10))

    for _ in range(num_walks):
        x, y = random_walk_2d(steps)
        plt.plot(x, y, marker='.', markersize=1, alpha=0.5)  # Adjust markersize and alpha for better visibility

    plt.title('100 2D Random Walks')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def random_walk_spatial():
    def random_walk_2d(steps, start_pos=(0, 0)):
        x, y = start_pos
        positions = np.zeros((steps, 2))
        positions[0] = [x, y]

        for i in range(1, steps):
            direction = np.random.choice(['up', 'down', 'left', 'right'])
            
            if direction == 'up':
                y += 1
            elif direction == 'down':
                y -= 1
            elif direction == 'left':
                x -= 1
            elif direction == 'right':
                x += 1

            positions[i] = [x, y]
        
        return positions

    # Parameters
    steps = 1000
    num_walks = 5  # Number of random walks to simulate
    start_positions = [(0, 0), (50, 50), (-50, -50), (100, -100), (-100, 100)]  # Different starting positions

    # Plot all random walks
    plt.figure(figsize=(10, 10))

    for start_pos in start_positions:
        walk = random_walk_2d(steps, start_pos=start_pos)
        plt.plot(walk[:, 0], walk[:, 1], marker='.', markersize=1, alpha=0.7, label=f'Start: {start_pos}')

    plt.title('Spatial Homogeneity in 2D Random Walks')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


def random_walk_temporal():
    def random_walk_2d(steps, start_time=0):
        x, y = 0, 0
        positions = np.zeros((steps, 2))
        positions[start_time] = [x, y]

        for i in range(start_time + 1, steps + start_time):
            direction = np.random.choice(['up', 'down', 'left', 'right'])
            
            if direction == 'up':
                y += 1
            elif direction == 'down':
                y -= 1
            elif direction == 'left':
                x -= 1
            elif direction == 'right':
                x += 1

            positions[i - start_time] = [x, y]
        
        return positions

    # Parameters
    steps = 1000
    num_walks = 5  # Number of random walks to simulate
    start_times = [0, 200, 400, 600, 800]  # Different start times

    # Plot all random walks
    plt.figure(figsize=(10, 10))

    for start_time in start_times:
        walk = random_walk_2d(steps, start_time=start_time)
        plt.plot(walk[:, 0], walk[:, 1], marker='.', markersize=1, alpha=0.7, label=f'Start Time: {start_time}')

    plt.title('Temporal Homogeneity in 2D Random Walks')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


def random_walks_var_expected_val():

    def random_walk_1d(steps):
        steps = np.random.choice([-1, 1], size=steps)
        return np.cumsum(steps)

    # Parameters
    steps = 1000
    num_walks = 1000

    # Simulate multiple random walks
    end_positions = np.zeros(num_walks)
    for i in range(num_walks):
        walk = random_walk_1d(steps)
        end_positions[i] = walk[-1]

    # Expected value should be close to 0
    expected_value = np.mean(end_positions)
    # Variance should increase with the number of steps
    variance = np.var(end_positions)

    print(f"Expected Value: {expected_value}")
    print(f"Variance: {variance}")

    # Plot the histogram of end positions
    plt.hist(end_positions, bins=50, alpha=0.75)
    plt.title('Histogram of End Positions of Random Walks')
    plt.xlabel('End Position')
    plt.ylabel('Frequency')
    plt.show()


def variance_is_Linear():
    def random_walk_1d(steps):
        steps = np.random.choice([-1, 1], size=steps)
        return np.cumsum(steps)

    # Parameters
    max_steps = 1000
    num_walks = 500  # Number of random walks to simulate
    step_intervals = np.arange(50, max_steps + 1, 50)  # Different step intervals

    variances = []

    # Calculate variance for each step interval
    for steps in step_intervals:
        end_positions = np.zeros(num_walks)
        for i in range(num_walks):
            walk = random_walk_1d(steps)
            end_positions[i] = walk[-1]
        
        variance = np.var(end_positions)
        variances.append(variance)

    # Plot variance against the number of steps
    plt.figure(figsize=(10, 6))
    plt.plot(step_intervals, variances, marker='o')
    plt.title('Variance of Random Walks vs. Number of Steps')
    plt.xlabel('Number of Steps')
    plt.ylabel('Variance')
    plt.grid(True)
    plt.show()