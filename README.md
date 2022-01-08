### README

--------------

_language: 中文_



#### 简介

1. 本功能包目标是借助**kdl**库完成iiwa机器人在已知各个连杆坐标系原点的xyz后求解出机器人关节角度的任务

2. 求解思路是: 借助KDL库中的逆解方法根据机器人末端的位置进行求解，求解完成后采取Damped-least-squared的方法进行最优逼近

3. 需要学习的内容有:

   KDL库的使用、Damped-least-squared的原理与python使用、机器人学导论中关于Jacobian矩阵作用、矩阵分析中的伪逆解的作用、Hessian矩阵的解释