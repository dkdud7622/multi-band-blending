import cv2
import numpy as np

def getMask(img) :
    # Output is 2-dim
    _,Mask = cv2.threshold(cv2.cvtColor((255 - img),cv2.COLOR_BGR2GRAY),1,255,cv2.THRESH_BINARY)
    Mask = 255-Mask
    # Make 3-Channel 
    Mask = cv2.merge((Mask,Mask,Mask))
    return Mask

def makeGaussianPyr(img,deep,shapes = None) :
    G = img.copy()
    gpList = [G]

    if(shapes is not None) : shapes.append(G.shape)
    for i in range(deep) :
        G = cv2.pyrDown(G)
        gpList.append(G)
        if (shapes is not None) :
            shapes.append(G.shape)

    if (shapes is not None) :
        return gpList, shapes
    return gpList

def makeLaplacianPyr(gpList, shapes, deep) :
    lpList = [gpList[deep-1]]
    for i in range(deep-1,0,-1) :
        GE = cv2.pyrUp(gpList[i])
        GE = cv2.resize(GE, dsize = (shapes[i-1][1],shapes[i-1][0]),interpolation = cv2.INTER_CUBIC)
        L = cv2.subtract(gpList[i-1],GE)
        lpList.append(L)
    return lpList

def multiBlending(img1,img2,Mask,deep) :
    gpMask=[]
    shapes=[]
    gpImg1=[]
    gpImg2=[]
    lpImg1=[]
    lpImg2=[]

    # normalize
    img1 = img1/255
    img2 = img2/255
    Mask = Mask/255

    gpMask,shapes = makeGaussianPyr(Mask,deep,shapes)
    gpImg1 = makeGaussianPyr(img1,deep)
    gpImg2 = makeGaussianPyr(img2,deep)

    lpImg1 = makeLaplacianPyr(gpImg1,shapes,deep)
    lpImg2 = makeLaplacianPyr(gpImg2,shapes,deep)

    blending = []
    shapes = []
    for i in range(deep) : 
        ls = ((1-gpMask[-i-2])*lpImg2[i]+(gpMask[-i-2])*lpImg1[i])
        shapes.append(ls.shape)
        blending.append(ls)

    ls_ = blending[0]
    for i in range(1,deep) :
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.resize(ls_, dsize=(shapes[i][1], shapes[i][0]), interpolation=cv2.INTER_CUBIC)
        ls_ = cv2.add(ls_,blending[i])
    

    
    return ls_*255

def main() :
    img1 = cv2.imread("./data/apple.png")
    img2 = cv2.imread("./data/orange.png")
    mask = cv2.imread("./data/mask.png")
    result = multiBlending(img1,img2,mask,deep=10)
    cv2.imwrite("data/result.png",result)
    

    testMask = cv2.imread("./data/testMask.png")
    binaryMask = getMask(testMask)
    cv2.imwrite("data/binaryMask.png",binaryMask)

if __name__ == "__main__":
    main()

