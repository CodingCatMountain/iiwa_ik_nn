#!/usr/bin/env python
#coding=utf-8

import numpy
import sys
from urdf_parser_py.urdf import URDF
from pykdl_utils.kdl_kinematics import KDLKinematics
from pykdl_utils.kdl_parser import kdl_tree_from_urdf_model
import os
os.chdir(sys.path[0])
robot = URDF.from_xml_file("/home/wujiajun/catkin_ws/src/iiwa_stack/iiwa_description/urdf/iiwa7.urdf")
tree = kdl_tree_from_urdf_model(robot)
print(tree.getNrOfSegments())
chain = tree.getChain("iiwa_link_0","iiwa_link_6")
print(chain.getNrOfJoints())
kdl_kin = KDLKinematics(robot,"iiwa_link_0","iiwa_link_6",tree)
q = [0,0,0,0,0,0]
pose = kdl_kin.forward(q)   # forward kinematics(returns homogeneous 4x4 numpy.mat)
print(pose)
q_ik = kdl_kin.inverse(pose,[0.1,0,-0.1,0.1,0.1,0.1])
if q_ik is not None:
    pose_sol = kdl_kin.forward(q_ik)
# J = kdl_kin.jacobian(q)
print("q:",q)
print("q_ik:",q_ik)
print("pose:",pose)
if q_ik is not None:
    print("pose_sol:",pose_sol)