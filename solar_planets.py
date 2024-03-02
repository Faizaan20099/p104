import cv2
img = cv2.imread("solar-system.jpg")
text_to_show = "sun"
text_to_show1 = "mercury"
text_to_show2 = "venus"
text_to_show3 = "earth"
text_to_show4 = "mars"
text_to_show5 = "jupiter"
text_to_show6 = "saturn"
text_to_show7 = "uranus"
text_to_show8 = "neptune"
cv2.putText(img,text_to_show,(100,380),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show1,(100,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show2,(180,150),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show3,(280,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show4,(380,240),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show5,(560,420),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show6,(750,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show7,(960,290),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,text_to_show8,(1100,310),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
print(img)
cv2.imshow("display image", img)
cv2.waitKey(0)