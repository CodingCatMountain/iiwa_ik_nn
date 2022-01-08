#!/usr/bin/env python
#coding=utf-8
import kdl_parser_py.urdf as kdl_parser
import PyKDL as kdl
import os,sys
import rospy
import math
os.chdir(sys.path[0])

class ThreeLinksRobot():
    def __init__(self):
        flag,self.__robot = kdl_parser.treeFromFile("../urdf/threelinksrobot.urdf")
        self.__chain = self.__robot.getChain("link0","link3")
        self.__fk_solver = kdl.ChainFkSolverPos_recursive(self.__chain)
        self.__ik_v_solver = kdl.ChainIkSolverVel_pinv(self.__chain)
        self.__ik_solver = kdl.ChainIkSolverPos_NR(self.__chain,self.__fk_solver,self.__ik_v_solver,maxiter=100,eps=math.pow(10,-1))

    
    def fk(self,q,pos):
        fk_flag = self.__fk_solver.JntToCart(q,pos)
        return pos


    
    def ik(self,pose,q):
        q_init = kdl.JntArray(3) 
        if type(q) != kdl.JntArray:
            raise TypeError("the type of q isn't PyKDL.JntArray")
        self.__ik_solver.CartToJnt(q_init,pose,q)
        return q

if __name__=="__main__":
    robot = ThreeLinksRobot()
    pose = kdl.Frame()
    q = kdl.JntArray(3)
    for i in range(3):
        q[i] = 0
    q[1] = math.pi/2
    pos = robot.fk(q,pose)
    print(pos)
    q_out = kdl.JntArray(3)
    q = robot.ik(pos,q_out)
    print(q)

