#!/usr/bin/env python
# coding: utf-8

# In[8]:


###################################################################
# Do not include any additional import statements
import numpy as np
import time
import random
###################################################################
# - Fill in the code below the comment Python and NumPy same as in example.
# - Follow instructions in document.


def examples():
    ###################################################################
    # Example: Create a zeros vector of size 10 and store it in variable tmp.
    # Python
    pythonStartTime = time.time()
    tmp_1 = [0 for i in range(10)]
    pythonEndTime = time.time()

    # NumPy
    numPyStartTime = time.time()
    tmp_2 = np.zeros(10)
    numPyEndTime = time.time()
    print('Python time: {0} sec.'.format(pythonEndTime-pythonStartTime))
    print('NumPy time: {0} sec.'.format(numPyEndTime-numPyStartTime))


def question_set_1(): 
    ################################################################
    # This set of tasks is designed to build familiarity with manipulating
    # the elements of arrays.
    ################################################################
    z_1 = None
    z_2 = None
    ################################################################
    # 1. Create a zeros array of size (3,5) and store in variable z.
    # Python
    pythonStartTime = time.time()
    z_1 = [[0 for i in range(5)] for j in range(3)]
    pythonEndTime = time.time()
    # TODO 1a
    # NumPy
    numPyStartTime = time.time()
    z_2 = np.zeros((3,5),dtype='int')
    numPyEndTime = time.time()
    # TODO 1b
    print('Python time: {0} sec.'.format(pythonEndTime-pythonStartTime))
    print('NumPy time: {0} sec.'.format(numPyEndTime-numPyStartTime))
    #################################################
    # 2. Set all the elements in first row of z to 7.
    # Python
    pythonStartTime = time.time()
    for i in range(5):
        z_1[0][i] = 7
    pythonEndTime = time.time()
    # TODO 2a
    # NumPy
    numPyStartTime = time.time()
    z_2[0] = 7
    numPyEndTime = time.time()
    # TODO 2b

    #####################################################
    # 3. Set all the elements in second column of z to 9.
    # Python
    pythonStartTime = time.time()
    for i in range(3):
        z_1[i][1] = 9
    pythonEndTime = time.time()    
    # TODO 3a
    # NumPy
    numPyStartTime = time.time()
    z_2[:,1] = 9
    numPyEndTime = time.time()
    # TODO 3b

    #############################################################
    # 4. Set the element at (second row, third column) of z to 5.
    # Python
    pythonStartTime = time.time()
    z_1[2][3] = 5
    pythonEndTime = time.time()   
    # TODO 4a
    # NumPy
    numPyStartTime = time.time()
    z_2[2,3] = 5
    numPyEndTime = time.time()
    # TODO 4b

    ##############
    print(z_1)
    print(z_2)
    ##############
    # Do not modify the return statement.
    return z_1, z_2
    ##############


def question_set_2():
    ################################################################
    # This set of tasks is designed to build familiarity with creating
    # arrays with various entries.
    ################################################################
    x_1 = None
    x_2 = None
    ##########################################################################################
    # 5. Create a vector of size 50 with values ranging from 50 to 99 and store in variable x.
    # Python
    pythonStartTime = time.time()
    x_1=[i for i in range(50,100)]
    pythonEndTime = time.time()   
    # TODO 5a
    # NumPy
    numPyStartTime = time.time()
    x_2 = np.arange(50,100)
    numPyEndTime = time.time()
    # TODO 5b
    ##############
    print(x_1)
    print(x_2)
    ##############

    y_1 = None
    y_2 = None
    ##################################################################################
    # 6. Create a 4x4 matrix with values ranging from 0 to 15 and store in variable y.
    # Python
    pythonStartTime = time.time()
    y_1 = [[0 for i in range(4)] for j in range(4)]
    a=0
    for i in range(0,4):
        for j in range (0,4):
            a+=1
            y_1[i][j] = a
    pythonEndTime = time.time()  
    # TODO 6a
    numPyStartTime = time.time()
    y_2 = np.arange(0,16).reshape(4,4)
    numPyEndTime = time.time()
    # TODO 6b

    ##############
    print(y_1)
    print(y_2)
    ##############

    tmp_1 = None
    tmp_2 = None
    ####################################################################################
    # 7. Create a 5x5 array with 1 on the border and 0 inside amd store in variable tmp.
    # Python
    pythonStartTime = time.time()
    tmp_1 = [[1 for j in range(5)]for i in range(5)]
    for i in range(1,4):
        for j in range(1,4):
            tmp_1[i][j]=0
    pythonEndTime = time.time()  
    # TODO 7a
    # NumPy
    numPyStartTime = time.time()  
    tmp_2 = np.ones((5,5))
    tmp_2[1:-1,1:-1]=0
    numPyEndTime = time.time()
    # TODO 7b

    ##############
    print(tmp_1)
    print(tmp_2)
    ##############
    return x_1, x_2, y_1, y_2, tmp_1, tmp_2


def question_set_3():
    #############################################################################################
    # This final set focuses on actions on matrices.
    a_1 = None; a_2 = None
    b_1 = None; b_2 = None
    c_1 = None; c_2 = None
    #############################################################################################
    # 8. Generate a 50x100 array of integer between 0 and 5,000 and store in variable a.
    # Python
    pythonStartTime = time.time()
    a=0
    a_1=[[0 for i in range(100)]for j in range(50)]
    for i in range(50):
        for j in range(100):
            a+=1
            a_1[i][j]=a
    pythonEndTime = time.time()    
    # TODO 8a
    # NumPy
    numPyStartTime = time.time()  
    a_2=np.arange(5000).reshape(50,100)
    numPyEndTime = time.time()
    # TODO 8b

    ###############################################################################################
    # 9. Generate a 100x200 array of integer between 0 and 20,000 and store in variable b.
    # Python
    pythonStartTime = time.time()
    b=0
    b_1=[[0 for i in range(200)]for j in range(100)]
    for i in range(100):
        for j in range(200):
            b+=1
            b_1[i][j]=b
    pythonEndTime = time.time()    
    # TODO 9a
    # NumPy
    numPyStartTime = time.time() 
    b_2=np.arange(20000).reshape(100,200)
    numPyEndTime = time.time()    
    # TODO 9b

    #####################################################################################
    # 10. Multiply matrix a and b together (real matrix product) and store to variable c.
    # Python
    pythonStartTime = time.time()
    c_1 = [[0 for j in range(200)] for i in range(50)]
    for i in range(50):
        for k in range(100):
            for j in range(200):
                c_1[i][j]=c_1[i][j]+ a_1[i][k]*b_1[k][j]
    pythonEndTime = time.time()
    # TODO 10a
    # NumPy
    numPyStartTime = time.time()
    c_2 = np.matmul(a_2,b_2)
    numPyEndTime = time.time()
    # TODO 10b

    d_1 = None; d_2 = None
    ################################################################################
    # 11. Normalize a 3x3 random matrix ((x-min)/(max-min)) and store to variable d.
    # Python
    pythonStartTime = time.time()
    d_1 = [[0 for i in range(3)]for j in range(3)]
    for i in range(3):
        for j in range(3):
            d_1[i][j]=random.randint(1,100)
    Min=min(min(d_1))
    Max=max(max(d_1))
    for i in range(3):
        for j in range(3):
            d_1[i][j]=(d_1[i][j]-Min)/(Max-Min)
    pythonEndTime = time.time()
    # TODO 11a
    # NumPy
    numPyStartTime = time.time()
    d_2=np.random.randint(100,size=(3,3))
    Min,Max=d_2.min(),d_2.max()
    d_2=(d_2-Min)/(Max-Min)
    numPyEndTime = time.time()    
    # TODO 11b

    ##########
    print(d_1)
    print(d_2)
    #########

    ################################################
    # 12. Subtract the mean of each row of matrix a.
    # Python
    pythonStartTime = time.time()
    for i in range(len(a_1)):
        m_1 =sum(a_1[i])/len(a_1[0])
        for j in range(len(a_1[i])):
            a_1[i][j]= a_1[i][j]-m_1
    pythonEndTime = time.time()
    # TODO 12a
    # NumPy
    numPyStartTime = time.time()
    a_2=a_2-np.mean(a_2,axis=1,keepdims=True)
    numPyEndTime = time.time()  
    # TODO 12b

    ###################################################
    # 13. Subtract the mean of each column of matrix b.
    # Python
    pythonStartTime = time.time()
    B_1=[[0 for i in range(len(b_1))]for j in range(len(b_1[0]))]

    for i in range(len(B_1)):
        for j in range(len(B_1[i])):
            B_1[i][j] = b_1[j][i]
    
    for i in range(len(B_1)):
        m_1 =sum(B_1[i])/len(B_1[0])
        for j in range(len(B_1[i])):
            B_1[i][j]= B_1[i][j]-m_1
    
    for i in range(len(b_1)):
        for j in range(len(b_1[i])):
            b_1[i][j] = B_1[j][i]
    # TODO 13a
    # NumPy
    numPyStartTime = time.time()
    b_2=b_2-np.mean(b_2,axis=0,keepdims=True)
    numPyEndTime = time.time()  
    # TODO 13b

    ################
    print(np.sum(a_1 == a_2))
    print(np.sum(b_1 == b_2))
    ################
    
    e_1 = None; e_2 = None
    ###################################################################################
    # 14. Transpose matrix c, add 5 to all elements in matrix, and store to variable e.
    # Python
    pythonStartTime = time.time()
    e_1=[[0 for i in range(len(c_1))]for j in range(len(c_1[0]))]

    for i in range(len(e_1)):
        for j in range(len(e_1[i])):
            e_1[i][j] = c_1[j][i] + 5
    pythonEndTime = time.time()
    # TODO 14a
    # NumPy
    numPyStartTime = time.time()
    e_2 = np.transpose(c_2)
    e_2 = e_2 + 5
    numPyEndTime = time.time()  
    # TODO 14b

    ##################
    print(np.sum(e_1 == e_2))
    ##################

    f_1 = None; f_2 = None
    g_1 = None; g_2 = None
    #####################################################################################
    # 15. Reshape matrix e to 1d array, store to variable f, and store the shape of f in
    # variable g. Finally, print g (the shape of f matrix).

    # Python
    pythonStartTime = time.time()
    f_1=[0 for i in range(len(e_1)*len(e_1[0]))]
    k=0
    for i in range(len(e_1)):
        for j in range(len(e_1[0])):
            f_1[k]=e_1[i][j]
            k+=1
    pythonEndTime = time.time()
    # TODO 15a
    # NumPy
    numPyStartTime = time.time()
    f_2=e_2.reshape(-1)
    g_2=f_2.shape
    print(g_2)
    numPyEndTime = time.time() 
    # TODO 15b

    ################
    return a_1, a_2, b_1, b_2, c_1, c_2, d_1, d_2, e_1, e_2, f_1, f_2, g_1, g_2
    ################


#####################################################################################
# For your benefit, this section will help you check your answers. Feel free to comment out
# sections as you move through the problems.
if __name__ == "__main__":
    print("CSE 691 - Assignment #1 - Timing differences between Vanilla Python and Numpy")
    print("Set #1")
    question_set_1()
    print("Set #2")
    question_set_2()
    print("Set #3")
    question_set_3()

