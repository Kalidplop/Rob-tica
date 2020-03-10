from controller import Robot

TIME_STEP = 1000
robot = Robot() #Creación del robot
ds = [] #Sensores de distancia
dsNames = ['ds_right', 'ds_left'] 
for i in range(2):#inicializar sensores
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
wheels = [] # inicializar llantas
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = 1.0  # [rad/s]
    rightSpeed = 1.0 # [rad/s]
    if avoidObstacleCounter > 0:#girar 
        avoidObstacleCounter -= 1
        leftSpeed = 1.0 # [rad/s]
        rightSpeed = -1.0 # [rad/s]
    else:  # Leer sensores
        for i in range(2):
            if ds[i].getValue() < 950.0:#Distancia max
                avoidObstacleCounter = 100
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)