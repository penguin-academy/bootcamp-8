# Créditos: código del equipo "Happy Feet", ganador del torneo de robot-sumo (RoDI)

import rodi
from time import sleep

robot = rodi.RoDI()

while True:
    robot.move_forward()
    seek = int(robot.see())
    ui = robot.sense()
    if ui[1] > 200:
        robot.move_stop()
        robot.move_left()
        sleep(0.6)
        robot.move_stop()
    if seek > 20:
        robot.move(-20, 60)
        sleep(1)
    else:
        robot.move_forward()