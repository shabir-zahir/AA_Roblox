import cv2
import numpy as np
#from WindowCapture import windowcapture

#robloxCapture = WindowCapture('Roblox')


def green_mask(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(45, 100, 20), (80, 255, 255) )
    #cv2.imshow("GREEN", mask);cv2.waitKey();cv2.destroyAllWindows()
    return mask

def get_hills(before, after):
    before_mask = green_mask(before)
    after_mask = green_mask(after)  
    cv2.imshow("Before", before_mask);cv2.waitKey();cv2.destroyAllWindows()
    cv2.imshow("After", after_mask);cv2.waitKey();cv2.destroyAllWindows()
    new_green_features = cv2.subtract(after_mask, before_mask)
    cv2.imshow('NEW', new_green_features);cv2.waitKey();cv2.destroyAllWindows()
    return new_green_features

def largest_hill(hills):
    # this function is basically largest island on leetcode
    # however I make it so I return all pixels in the largest Island so i can pick multiple pixels
    def isValidPixel(i,j):
        return 0<=i < len(hills) and 0<= j < len(hills[0]) and hills[i][j] == 255
    def find_hill_size(i,j,root_x,root_y):
        size = 0
        axis = [(1,0), (0,1), (-1,0), (0,-1)]
        root_vals[(i,j)] = (root_x,root_y)
        for x,y in axis:
            r,c = i+x, j+y
            if isValidPixel(r,c):
                size += find_hill_size(r,c, root_x, root_y) + 1
                seen.add((r,c))
        return size
    seen = set()
    root_val = {}
    island_size = {}
    #255 = valid pixel
    for i in range(len(hills)):
        for j in range(len(hills[0])):
            if hills[i][j] == 255 and (i,j) not in seen:
                island_size[(i,j)] = find_hill_size(i,j,i,j)
            else:
                island_size[(i,j)] = island_size[root_val[(i,j)]]
    return island_size

images_dir = 'snow_inf_test_img'
# Specific image paths
image1_path = "snow_inf_test_img\post_hill_test.PNG"
image2_path = "snow_inf_test_img\pre_hill_test_v2.PNG"
image3_path = "snow_inf_test_img\pre_hill_test.PNG"

img1,img2,img3 = cv2.imread(image1_path), cv2.imread(image2_path),  cv2.imread(image3_path)

get_hills(img3, img1)

    
def compare_images(img1,img2):
    pass
    """
    Image Comparison:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        #cv2.imshow("Computer Vision". pre_click)
        #cv.imshow("Computer Vision". post_click)
        h, w = img1.shape
        def mse(img1, img2):
            h, w = img1.shape
            diff = cv2.subtract(img1, img2)
            err = np.sum(diff**2)
            mse = err/(float(h*w))
            return mse, diff

        error, diff = mse(img1, img2)
        print("Image matching Error between the two images:",error)

        cv2.imshow("difference", diff)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    """