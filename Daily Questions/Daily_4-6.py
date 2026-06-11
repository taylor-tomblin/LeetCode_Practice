"""
874. Walking Robot Simulation
(Medium)

A robot on an infinite XY-plane starts at (0, 0) facing north. The robot recieves an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can recieve:
- -2: Turn left 90 degrees.
- -1: Turn right 90 degrees.
- 1 <= x <= 9: Move forward x units, one unit at a time.

Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (x_i, y_i). If the robot runs into an obstacle, it will stay in its current locationo (on the block adjacent to the obstacle) and move onto the next command.
Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

Note: 
    - There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to (0, 0) due to the obstacle.
    - North means +Y direction
    - East means +X direction
    - South means -Y direction
    - West means -X direction

"""

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x = 0
        y = 0
        direction = 0
        max_distance = 0
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                for _ in range(command):
                    next_x = x + (direction == 1) - (direction == 3)
                    next_y = y + (direction == 0) - (direction == 2)

                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_distance = max(max_distance, x**2 + y**2)
                    else:
                        break

        return max_distance