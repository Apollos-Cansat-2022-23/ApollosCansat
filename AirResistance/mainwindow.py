# This Python file uses the following encoding: utf-8
import sys
#from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QHBoxLayout
from PyQt6 import uic
from PyQt6.QtCore import QTimer
from math import pi

def calculateData(window):
    mass = 0.325
    start = 0
    end = 30
    intervalFactor = 100
    interval = 1/intervalFactor

    distance = 0
    velocity = 0

    times = []
    accelerations = []
    velocities = []
    distances = []

    for t in range(start * intervalFactor, end * intervalFactor + 1):
        realT = t * interval
        dF = 0.5 * (window.CDSlider.value()/100) * (window.DSlider.value()/1000) * pi * (window.radiusSlider.value()/1000)**2 * (velocity**2)
        aF = mass * -9.81

        tF = dF + aF
        acceleration = tF / mass

        velocity += acceleration * interval
        distance += velocity * interval

        accelerations.append(acceleration)
        velocities.append(velocity)
        distances.append(distance)
        times.append(realT)

    return times, distances, velocities, accelerations

def plotData(window):
    times, distances, velocities, accelerations = calculateData(window)
    distanceData, velocityData, accelerationData = None, None, None

    window.graph.plotItem.vb.setLimits(xMin=0, xMax=max(times)+5, yMin=min(distances)*1.01, yMax=max(distances)*1.001)
    distanceData = window.graph.plot(times, distances)
    window.graph.setTitle("Distance vs Time")
    window.graph.setLabel('left', 'Distance (m)')
    window.graph.setLabel('bottom', 'Time (s)')

    window.graph_3.plotItem.vb.setLimits(xMin=0, xMax=max(times)+5, yMin=min(velocities)*1.01, yMax=max(velocities)*1.001)
    velocityData = window.graph_3.plot(times, velocities)
    window.graph_3.setTitle("Velocity vs Time")
    window.graph_3.setLabel('left', 'Velocity (ms⁻¹)')
    window.graph_3.setLabel('bottom', 'Time (s)')

    window.graph_2.plotItem.vb.setLimits(xMin=0, xMax=max(times)+5, yMin=min(accelerations)*1.01, yMax=max(accelerations)*1.001)
    accelerationData = window.graph_2.plot(times, accelerations)
    window.graph_2.setTitle("Acceleration vs Time")
    window.graph_2.setLabel('left', 'Acceleration (ms⁻²)')
    window.graph_2.setLabel('bottom', 'Time (s)')

    return distanceData, velocityData, accelerationData

def update():
    # Too Lazy to use OOP
    global window, distanceData, velocityData, accelerationData


    times, distances, velocities, accelerations = calculateData(window)

    distanceData.setData(times, distances)
    velocityData.setData(times, velocities)
    accelerationData.setData(times, accelerations)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = uic.loadUi("mainwindow.ui")
    distanceData, velocityData, accelerationData = plotData(window)

    window.timer = QTimer()
    window.timer.setInterval(50)
    window.timer.timeout.connect(update)
    window.timer.start()

    window.show()
    app.exec()
