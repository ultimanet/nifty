# -*- coding: utf-8 -*-

import numpy as np

def MIN():
    return np.min
    
def MAX():
    return np.max
    
def SUM():
    return np.sum    



class _COMM_WORLD():
    def __init__(self):
        self.rank = 0
        self.size = 1
    
    def Get_rank(self):
        return self.rank
    
    def Get_size(self):
        return self.size
    
    def _scattergather_helper(self, sendbuf, recvbuf=None):
        if recvbuf != None:        
            recvbuf[:] = sendbuf
            return recvbuf
        else:
            recvbuf = np.copy(sendbuf)
            return recvbuf
    
    def bcast(self, sendbuf, *args, **kwargs):
        return sendbuf
    
    def Bcast(self, sendbuf, *args, **kwargs):
        return sendbuf
    
    def scatter(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)
    
    def Scatter(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)
    
    def Scatterv(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)

    def gather(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)
    
    def Gather(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)

    def Gatherv(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)

    def allgather(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)       
    
    def Allgather(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)
    
    def Allgatherv(self, *args, **kwargs):
        return self._scattergather_helper(*args, **kwargs)
    
    def Allreduce(self, sendbuf, recvbuf, op, **kwargs):
        recvbuf[None] = op(sendbuf)
        return recvbuf
        
    def allreduce(self, sendbuf, recvbuf, op, **kwargs):
        recvbuf[None] = op(sendbuf)
        return recvbuf
    
    def _unwrapper(self, x):
        if isinstance(x, list):
            return x[0]
        else:
            return x
        

class _datatype():
    def __init__(self, name):
        self.name = str(name)
        
SHORT = _datatype('MPI_SHORT')


UNSIGNED_SHORT = _datatype("MPI_UNSIGNED_SHORT")
UNSIGNED_INT = _datatype("MPI_UNSIGNED_INT")
INT = _datatype("MPI_INT")
LONG = _datatype("MPI_LONG")
UNSIGNED_LONG = _datatype("MPI_UNSIGNED_LONG")
LONG_LONG = _datatype("MPI_LONG_LONG")
UNSIGNED_LONG_LONG = _datatype("MPI_UNSIGNED_LONG_LONG")
FLOAT = _datatype("MPI_FLOAT")
DOUBLE = _datatype("MPI_DOUBLE")
LONG_DOUBLE = _datatype("MPI_LONG_DOUBLE")
COMPLEX = _datatype("MPI_COMPLEX")
DOUBLE_COMPLEX = _datatype("MPI_DOUBLE_COMPLEX")

        
COMM_WORLD = _COMM_WORLD()
        
        
        
        
        
        
        
        
        
        
        
        