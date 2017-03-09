import numpy
import sys
import os

#def num_illuminated(matrix_illmn,on_x,on_y):
#    print(matrix_illmn)
#    switch_off(matrix_illmn,on_x,on_y)
#    print(matrix_illmn.sum())

#def switch_off(matrix_ill,on_x,on_y):
#    if on_x>=0 and on_x<matrix_ill.shape[0] and on_y>=0 and on_y<=matrix_ill.shape[1]:
#        matrix_ill[on_x,on_y] = 0
#        switch_off(matrix_ill,on_x,on_y-1)
#        switch_off(matrix_ill,on_x-1,on_y-1)


#num_illuminated(numpy.ones((3,5)),4,0)

def  num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):
    distBwnLampX = conn_x2 - conn_x1
    totalNumX = int(grid_width/distBwnLampX) + 1

    distBwnLampY = conn_y2 - conn_y1
    totalNumY = int(grid_height/distBwnLampY) + 1

    LampsOnMatrix = [[1 for x in range(totalNumX)] for y in range(totalNumY)]
    print("distBwnLampX={0},distBwmLampY={1}".format(distBwnLampX,distBwnLampY))
    switch_off(LampsOnMatrix,grid_width,grid_height,conn_x1,conn_y1,distBwnLampX,distBwnLampY,start_x,start_y)
    return(sum(sum(LampsOnMatrix, [])))

def switch_off(LampsOnMatrix,grid_width,grid_height,conn_x1,conn_y1,distBwnLampX,distBwnLampY,x,y):
    if x>=conn_x1 and x<=(grid_width - conn_x1) and y>=conn_y1 and y<=(grid_height - conn_y1):
        xCoord = (x - conn_x1)/distBwnLampX
        yCoord = (y - conn_y1)/distBwnLampY
        print("XCor={0},YCor={0}".format(int(xCoord),int(yCoord)))
        LampsOnMatrix[int(xCoord)][int(yCoord)] = 0
        switch_off(LampsOnMatrix,grid_width,grid_height,conn_x1,conn_y1,distBwnLampX,distBwnLampY,x-distBwnLampX,y)
        switch_off(LampsOnMatrix,grid_width,grid_height,conn_x1,conn_y1,distBwnLampX,distBwnLampY,x-distBwnLampX,y-distBwnLampY)

_grid_width = int(input())
_grid_height = int(input())
_conn_x1 = int(input())
_conn_y1 = int(input())
_conn_x2 = int(input())
_conn_y2 = int(input())
_start_x = int(input())
_start_y = int(input())

res = num_illuminated(_grid_width, _grid_height, _conn_x1, _conn_y1, _conn_x2, _conn_y2, _start_x, _start_y)
print(res)
