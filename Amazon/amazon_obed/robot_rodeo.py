"""
 Robot Rodeo

During the next Amazon summit, the Amazon robotics team wants to demonstrate how easy it is to use their latest robot.

For the event, they have built a simple language to control it:

    G instructs the robot to move forward one step.
    L instructs the robot to turn left in place.
    R instructs the robot to turn right in place.

To keep the event more interactive, once the robot has completed the list of instructions, it will repeat them in
an infinite loop.
Given the time and effort in building this robot, the robotics team don't want to lose it because of a bad sequence
of instructions.

They've asked you to build a simulator based on a list of commands that will determine if it exists a circle such that
the robot always moves within the circle.

Consider the commands R and G executed infinitely. A diagram of the robot's movement looks like:
RG → RG
↑      ↓
RG ← RG

Function Description

Complete the function doesCircleExist in the editor below. The function must return an array of n strings either
YES or NO based on whether the robot is bound within a circle or not, in order of test results.
doesCircleExist has the following parameter(s):

    commands[commands[0], ... commands[n-1]]:
        An array of n commands[i] where each represents a list of commands to test.

Constraints

    1≤∣commands[i]∣≤25001≤∣commands[i]∣≤2500
    1≤n≤101≤n≤10
    Each command consists of G, L, and R only.
"""


def doesCicleExist(commands):
    results = []

    for command in commands:
        # Estado inicial
        x, y = 0, 0  # Posición inicial
        direction = 0  # Dirección inicial (0 = Arriba, 1 = Derecha, 2 = Abajo, 3 = Izquierda)

        # Mapeo de movimientos en las cuatro direcciones
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Ejecutar los comandos una vez
        for cmd in command:
            if cmd == 'G':  # Mover hacia adelante en la dirección actual
                dx, dy = moves[direction]
                x += dx
                y += dy
            elif cmd == 'L':  # Girar a la izquierda
                direction = (direction - 1) % 4
            elif cmd == 'R':  # Girar a la derecha
                direction = (direction + 1) % 4

        # Comprobar si el robot está dentro de un círculo
        if (x == 0 and y == 0) or direction != 0:
            results.append("YES")
        else:
            results.append("NO")

    return results
