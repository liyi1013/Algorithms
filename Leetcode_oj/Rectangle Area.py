class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1=(C-A)*(D-B)
        area2=(G-E)*(H-F)
        area_overlapped=0
        print 'area1:',area1
        print 'area2:',area2
        x_overlapped=(A-G)*(C-E)
        y_overlapped=(B-H)*(D-F)
        if x_overlapped>=0 or y_overlapped>=0: #x and y not overlap
            return area1+area2
        else :
            x1=max(A,E)
            y1=max(B,F)
            x2=min(C,G)
            y2=min(D,H)
            area_overlapped=(x2-x1)*(y2-y1)
            print 'overlap:',area_overlapped
            return area1+area2-area_overlapped

if __name__ == '__main__':
    s=Solution()
    print (s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4))