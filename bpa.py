import open3d as o3d
import numpy as np

class BPA :
    def ball_pivot(self,x,y,z):
        return np.sqrt(x*x+y*y+z*z)