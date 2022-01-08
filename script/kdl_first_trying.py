#!/usr/bin/env python
#coding=utf-8
import numpy ;import sys ;import os 
#os.chdir(sys.path[0])
from math import pi

from pykdl_utils.kdl_kinematics import KDLKinematics
from pykdl_utils.kdl_parser import kdl_tree_from_urdf_model
from rospy.client import init_node
from urdf_parser_py.urdf import URDF

class Robot():
    
    def __init__(self,filepath):
        self.__robot = URDF.from_xml_file(filepath)
        self.__tree = kdl_tree_from_urdf_model(self.__robot)
        self.__chain_1 = self.__tree.getChain("iiwa_link_0","iiwa_link_2")

    def fk(self,q):
        self.__kdl_kin = KDLKinematics(self.__robot,"iiwa_link_0","iiwa_link_3",self.__tree)
        pose = self.__kdl_kin.forward(q)
        return pose
    
    def ik(self,pose):
        for i in range(100):
            init_angle = numpy.random.rand(3)
            q_ik = self.__kdl_kin.inverse(pose,init_angle.tolist())
            if q_ik is not None:
                return q_ik
            else: 
                continue
        return None


if __name__=="__main__":
    filepath = "/home/wujiajun/catkin_ws/src/iiwa_stack/iiwa_description/urdf/iiwa7.urdf"
    iiwa = Robot(filepath)
    q = [0.,21*pi/180,0.]
    pose = iiwa.fk(q)
    print(pose)
    q_ik = iiwa.ik(pose)
    print(q_ik)