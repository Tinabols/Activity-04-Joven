import cv2
path = r'C:\Users\christina mae joven\Desktop\michaeng.jpg'
image = cv2.imread(path)
window_name = 'MiChaeng work in progress'
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
