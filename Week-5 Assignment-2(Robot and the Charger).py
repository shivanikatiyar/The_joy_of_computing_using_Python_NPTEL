#Programming Assignment 2: Robot and the Charger
#There is a robot which wants to go the charging point to charge itself. The robot moves in a 2-D plane from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2 The numbers after the direction are steps. Write a program to compute the distance between the current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer (use round() function for that and then convert it into an integer). Input Format: The first line of the input contains a number n which implies the number of directions to be given. The next n lines contain the direction and the step separated by a space. Output Format: Print the distance from the original position to the current position. Example: Input: 4 UP 5 DOWN 3 LEFT 3 RIGHT 2 Output: 2 Explanation: After the movements, the robot is at the position (-1, 2). Distance from the (0, 0) to the point (-1, 2) is calculated using Euclidean distance. The round value of which is 2.0, and int value is 2. NOTE: Import math library and use the sqrt() function of the math library to compute the Euclidean distance
import math
(n,robot_move,x,y)=(int(input()),[],0,0)

for robot in range(n):
  direction,magnitude=input().split()
  if direction=='UP':
    y=y+int(magnitude)
  if direction=='DOWN':
    y=y-int(magnitude)
  if direction=='RIGHT':
    x=x+int(magnitude)
  if direction=='LEFT':
    x=x-int(magnitude)
    
print(round(math.sqrt(x*x+y*y)),end="")