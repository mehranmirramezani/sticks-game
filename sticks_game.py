import numpy as np
# This class and the following functions are used to check if two segments intersect!
# These are from https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
def onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False
  
def orientation(p, q, r):
      
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
        return 1
    elif (val < 0):
        return 2
    else:
        return 0
        
def doIntersect(p1,q1,p2,q2):
      
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
  
    if ((o1 != o2) and (o3 != o4)):
        return True
  
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
  
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
  
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
  
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True

    return False


# This function determines the number of groups of sticks!
# The "Sweep Line Algorithm" can potentially reduce the complexity and computational cost; however, I did not implement this here.
#The "Sweep Line Algorithm" is described here: https://www.geeksforgeeks.org/given-a-set-of-line-segments-find-if-any-two-segments-intersect/
def number_of_groups(input_data):

    segs = np.loadtxt(input_data, dtype='f', delimiter=' ')
    n = np.shape(segs)[0]

    visit = [1] * n
    No_of_Groups = 0

    while len(np.nonzero(visit)[0]) != 0:
            
            i = np.nonzero(visit)[0][0]
            visit[i] = 0
            queue = []
            for j in np.nonzero(visit)[0]:
                if doIntersect(Point(segs[i,0],segs[i,1]),Point(segs[i,2],segs[i,3]),Point(segs[j,0],segs[j,1]),Point(segs[j,2],segs[j,3])):
                   queue.append(j)
                   visit[j] = 0
            
            while len(queue) != 0:

                j_aux = queue.pop()

                for k in np.nonzero(visit)[0]:
                    if doIntersect(Point(segs[j_aux,0],segs[j_aux,1]),Point(segs[j_aux,2],segs[j_aux,3]),Point(segs[k,0],segs[k,1]),Point(segs[k,2],segs[k,3])):
                       queue.append(k)
                       visit[k] = 0
                    
            No_of_Groups += 1

    return No_of_Groups
  
if __name__ == '__main__':

    No_of_Groups = number_of_groups("lines_286.txt")
    print ("Number of Groups =",No_of_Groups)
    