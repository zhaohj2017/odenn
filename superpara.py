#working 
#super parameter for example: dy / dt = y
DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

#the learn parameter
EPOCHS = 1
BATCH_SIZE = 10
BATCH_NUM = 0
#initial learning rate, initial alpha
LEARN_RATE = 0.5
#for learning rate adjustment; # rate = alpha / (1 + beta * itr^gamma)
ALPHA = 0.5 #initial learning rate
BETA = 1e-3 #if beta equals 0 then constant rate = alpha
GAMMA = 1 #when beta is nonzero, larger gamma gives faster drop of rate

#momentum coefficient
MOMENTUM_MU = 0 #if set to 0 then equivalent to pure gradient without momentum

#for bfgs
#if this number equals 1 and batch size equals 1, then degenerates to online SGD
#if this number equals old EPOCH, current epoch = 1, and batch size equals dataset length, then degerates to standard full batch bfgs
BFGS_BATCH_ITR_NUM = 5
PRINT_MINI = 1 #print mini batch errors etc.

#regularization factor
REGU_FACTOR = 0 # == lambda / len(dataset)

#the network
NUM_HIDDEN = 30

#the range and sampling granularity
RANGE_Y = [0, 1]
LENGTH_T = 0.367
RANGE_T = [0, LENGTH_T]

MESH_SIZE_Y = 0.1
MESH_SIZE_T = 0.0367

TEST_FACTOR_T = 20 #sample ten points for every training points
TEST_FACTOR_Y = 20
PLOT_MESH_Y = MESH_SIZE_Y / TEST_FACTOR_Y
PLOT_MESH_T = MESH_SIZE_T / TEST_FACTOR_T

#the time step of flowpipe
T_STEP = 0.367
NUM_STEP = int(round(LENGTH_T / T_STEP)) # very important
if LENGTH_T - NUM_STEP * T_STEP > 1e-3 * T_STEP: #not a whole step
    NUM_STEP += 1

#the blowup factor of flowpipe
ENLARGE_Y = MESH_SIZE_Y * 0
ENLARGE_T = MESH_SIZE_T * 0

#is it helpful to sample more points???
EPS_Y = 0.0
EPS_T = 0.0 # EPS_T should be less than T_STEP

"""
#****************************the following are fixed!!!**********************************************
#date 2019-01-10
#super parameter for example: dy / dt = exp(y)
DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

#the learn parameter
EPOCHS = 1
BATCH_SIZE = 10
BATCH_NUM = 0
#initial learning rate, initial alpha
LEARN_RATE = 0.5
#for learning rate adjustment; # rate = alpha / (1 + beta * itr^gamma)
ALPHA = 0.5 #initial learning rate
BETA = 1e-3 #if beta equals 0 then constant rate = alpha
GAMMA = 1 #when beta is nonzero, larger gamma gives faster drop of rate

#momentum coefficient
MOMENTUM_MU = 0 #if set to 0 then equivalent to pure gradient without momentum

#for bfgs
#if this number equals 1 and batch size equals 1, then degenerates to online SGD
#if this number equals old EPOCH, current epoch = 1, and batch size equals dataset length, then degerates to standard full batch bfgs
BFGS_BATCH_ITR_NUM = 20
PRINT_MINI = 1 #print mini batch errors etc.

#regularization factor
REGU_FACTOR = 0 # == lambda / len(dataset)

#the network
NUM_HIDDEN = 20

#the range and sampling granularity
RANGE_Y = [0, 1]
LENGTH_T = 0.36
RANGE_T = [0, LENGTH_T]

MESH_SIZE_Y = 0.1
MESH_SIZE_T = 0.02

TEST_FACTOR = 20 #sample ten points for every training points
PLOT_MESH_Y = MESH_SIZE_Y / TEST_FACTOR
PLOT_MESH_T = MESH_SIZE_T / TEST_FACTOR

#the time step of flowpipe
T_STEP = 0.12
NUM_STEP = int(round(LENGTH_T / T_STEP)) # very important
if LENGTH_T - NUM_STEP * T_STEP > 1e-3 * T_STEP: #not a whole step
    NUM_STEP += 1

#the blowup factor of flowpipe
ENLARGE_Y = MESH_SIZE_Y * 0
ENLARGE_T = MESH_SIZE_T * 0

#is it helpful to sample more points???
EPS_Y = 0.0
EPS_T = 0.0 # EPS_T should be less than T_STEP
"""

#****************************the following are fixed!!!*****************************************************
"""FIXED for dy / dt = exp(y) date 2018-12-27
DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

#the learn parameter
EPOCHS = 500
LEARN_RATE = 0.1
BATCH_SIZE = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
BATCH_NUM = 0

#the network
NUM_HIDDEN = 5

#the range and sampling granularity
RANGE_Y = [0, 1]
LENGTH_T = 0.36
RANGE_T = [0, LENGTH_T]

MESH_SIZE_Y = 0.1
MESH_SIZE_T = 0.02

TEST_FACTOR = 20 #sample ten points for every training points
PLOT_MESH_Y = MESH_SIZE_Y / TEST_FACTOR
PLOT_MESH_T = MESH_SIZE_T / TEST_FACTOR

#the time step of flowpipe
T_STEP = 0.12
NUM_STEP = int(round(LENGTH_T / T_STEP)) # very important
if LENGTH_T - NUM_STEP * T_STEP > 1e-3 * T_STEP: #not a whole step
    NUM_STEP += 1

#the blowup factor of flowpipe
ENLARGE_Y = MESH_SIZE_Y * 0
ENLARGE_T = MESH_SIZE_T * 0

#is it helpful to sample more points???
EPS_Y = 0.0
EPS_T = 0.0 # EPS_T should be less than T_STEP

# odenn setting
# #stochastic gradient descent
# backward.itrdescent(dataset, step) #first sgd, and then bfgs

# #bfgs: only works in batch mode
# superpara.EPOCHS = 500
# superpara.BATCH_SIZE = len(dataset)
# superpara.LEARN_RATE = 0.05
# bfgs.itrdescent(dataset, step)
# superpara.LEARN_RATE = 0.1
# superpara.EPOCHS = 500
"""


"""
#FIXED for dy / dt = exp(y)!!! data 2018-12-05
DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

#the learn parameter
EPOCHS = 20
LEARN_RATE = 0.2
BATCH_SIZE = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
BATCH_NUM = 0

#the network
NUM_HIDDEN = 5

#the range and sampling granularity
RANGE_Y = [0, 1]
LENGTH_T = 0.3
RANGE_T = [0, LENGTH_T]

MESH_SIZE_Y = 0.01
MESH_SIZE_T = 0.005

TEST_FACTOR = 10 #sample ten points for every training points
PLOT_MESH_Y = MESH_SIZE_Y / TEST_FACTOR
PLOT_MESH_T = MESH_SIZE_T / TEST_FACTOR

#the time step of flowpipe
T_STEP = 0.1
NUM_STEP = int(round(LENGTH_T / T_STEP)) # very important

#the blowup factor of flowpipe
ENLARGE_Y = MESH_SIZE_Y
ENLARGE_T = MESH_SIZE_T

#is it helpful to sample more points???
EPS_Y = 0.0
EPS_T = 0.0 # EPS_T should be less than T_STEP
"""



"""
#FIXED: dy / dt = y; date 2018-12-05
#the system 
DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

#the learn parameter
EPOCHS = 100
LEARN_RATE = 0.1
BATCH_SIZE = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
BATCH_NUM = 0

#the network
NUM_HIDDEN = 5

#the range and sampling granularity
RANGE_Y = [0, 1]
LENGTH_T = 3
RANGE_T = [0, LENGTH_T]

MESH_SIZE_Y = 0.05
MESH_SIZE_T = 0.1

TEST_FACTOR = 10 #sample ten points for every training points
PLOT_MESH_Y = MESH_SIZE_Y / TEST_FACTOR
PLOT_MESH_T = MESH_SIZE_T / TEST_FACTOR

#the time step of flowpipe
T_STEP = 1
NUM_STEP = int(round(LENGTH_T / T_STEP)) # very important

#the blowup factor of flowpipe
ENLARGE_Y = MESH_SIZE_Y
ENLARGE_T = MESH_SIZE_T

#is it helpful to sample more points???
EPS_Y = 0.0
EPS_T = 0.0 # EPS_T should be less than T_STEP
"""



"""
# FIXED!!! for dy / dt = exp(y)
EPOCHS = 20
LEARN_RATE = 0.2

DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

NUM_HIDDEN = 5

BATCH_SIZE = 1
BATCH_NUM = 0

MESH_SIZE_Y = 0.01
MESH_SIZE_T = 0.005

EPS_Y = 0.0
EPS_T = 0.0 # EPS_T should be less than T_STEP

RANGE_Y = [0, 1]

LENGTH_T = 0.3
RANGE_T = [0, LENGTH_T]

T_STEP = 0.3
NUM_STEP = int(round((RANGE_T[1] - RANGE_T[0]) / T_STEP)) #very important

TEST_FACTOR = 10

PLOT_MESH_Y = MESH_SIZE_Y / TEST_FACTOR
PLOT_MESH_T = MESH_SIZE_T / TEST_FACTOR

RAND_SIZE_Y = 100
RAND_SIZE_T = 30
"""




"""
very strange: when enlarging the initial set the algorithm even performs better?
RANGE_Y = [0, 1] vs RANGE_Y = [1, 1]
why!!!!

found the reason: learning rate too small is not good!!! \\eita = 0.01; y = 1 (restart) vs \\eita = 0.05; y = 1
but with \\eita = 0.01; y \\in [0, 1] (no problem) 

summary: enlarging range_y is good? enlarging learning rate sometimes is also good?

how about enlarging T???
"""




""" **********  NOT RESOLVED!!!  **********************
#**************    dy / dt = exp(y)  *********************************

#super parameter for example: dy / dt = exp(y)
#comparison with Flow*

EPOCHS = 10
LEARN_RATE = 1

DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

MESH_SIZE_Y = 0.01
MESH_SIZE_T = 0.01

EPS_Y = 0.05
EPS_T = 0.05 # EPS_T should be less than T_STEP

RANGE_Y = [0, 1]

LENGTH_T = 1
RANGE_T = [0, LENGTH_T]

NUM_HIDDEN = 10

BATCH_SIZE = 20
BATCH_NUM = 0

T_STEP = 1
NUM_STEP = int((RANGE_T[1] - RANGE_T[0]) / T_STEP)
"""


""" ********************* FIXED !!! DO NOT CHANGE !!! ************************
#**************  dy  /dt = y (using sigmoid) *************************

#super parameter for example: dy / dt = y
EPOCHS = 10
LEARN_RATE = 1

DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

MESH_SIZE_Y = 0.01
MESH_SIZE_T = 0.01

EPS_Y = 0.05
EPS_T = 0.05 # EPS_T should be less than T_STEP

RANGE_Y = [0, 1]

LENGTH_T = 1
RANGE_T = [0, LENGTH_T]

NUM_HIDDEN = 5

BATCH_SIZE = 1
BATCH_NUM = 0

T_STEP = 1
NUM_STEP = int((RANGE_T[1] - RANGE_T[0]) / T_STEP)
"""



"""******* FIXED for fast sigmoid with dy / dt = y **************
EPOCHS = 3

LEARN_RATE = 0.18

DIMENSON = 1
INPUT_SIZE = DIMENSON + 2

MESH_SIZE_Y = 0.01
MESH_SIZE_T = 0.01

EPS_Y = 0.05
EPS_T = 0.05 # EPS_T should be less than T_STEP

RANGE_Y = [0, 1]

LENGTH_T = 1
RANGE_T = [0, LENGTH_T]

NUM_HIDDEN = 130

BATCH_SIZE = 1
BATCH_NUM = 0

T_STEP = 1
NUM_STEP = int((RANGE_T[1] - RANGE_T[0]) / T_STEP)
"""




"""
#for uniform random data generation
#used in trainset.py
#obsolete!!!
RAND_SIZE_Y = 100
RAND_SIZE_T = 30
"""