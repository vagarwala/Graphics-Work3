import math


def print_matrix( matrix ):
    mat = "\n"
    for r in matrix:
        mat += "| "
        for e in r:
            mat += str(e) + " | "
        mat += "\n"
    print mat

def ident( matrix ):
    mat = []
    for r in range(row):
        temprow = []
        for c in range(col):
            if (c == r):
                temprow.append(1)
            else:
                temprow.append(0)
        mat.append(temprow)
    return mat

def scalar_mult( matrix, s ):
    mat = []
    for r in matrix:
        temprow = []
        for e in r:
            temprow.append(s * e)
        mat.append(temprow)
    return mat

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    mat = []
    for r in m1:
        temprow = []
        for c in range(len(m2[0])):
            tempelem = 0
            for e in range(len(m1[0])):
                tempelem += r[e] * m2[e][c]
            temprow.append(int(tempelem))
        mat.append(temprow)
    return mat




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def create_id(row=4, col=4):
    newmat = []
    for r in range(row):
        temprow = []
        for c in range(col):
            if (c == r):
                temprow.append(1)
            else:
                temprow.append(0)
        newmat.append(temprow)
    return newmat

def scale(x, y, z):
    newmat = []
    for r in range(4):
        temprow = []
        for c in range(4):
            temprow.append(0)
        newmat.append(temprow)
    newmat[0][0] = x
    newmat[1][1] = y
    newmat[2][2] = z
    newmat[3][3] = 1
    return newmat
    
def translate(x, y, z):
    newmat = create_id(4, 4)
    newmat[3][0] = x
    newmat[3][1] = y
    newmat[3][2] = z
    return newmat

def rotate_x(theta):
    newmat = create_id(4, 4)
    newmat[2][2] = math.cos(math.radians(theta))
    newmat[1][1] = math.cos(math.radians(theta))
    newmat[2][1] = math.sin(math.radians(theta))
    newmat[1][2] = math.sin(math.radians(theta))*-1
    return newmat
    
def rotate_y(theta):
    newmat = create_id(4, 4)
    newmat[0][0] = math.cos(math.radians(theta))
    newmat[2][2] = math.cos(math.radians(theta))
    newmat[0][2] = math.sin(math.radians(theta))*-1
    newmat[2][0] = math.sin(math.radians(theta))
    return newmat
    
def rotate_z(theta):
    newmat = create_id(4, 4)
    newmat[0][0] = math.cos(math.radians(theta))
    newmat[1][1] = math.cos(math.radians(theta))
    newmat[1][0] = math.sin(math.radians(theta))
    newmat[0][1] = math.sin(math.radians(theta))*-1
    return newmat
