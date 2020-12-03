from tkinter import *
from PIL import Image
from sklearn.cluster import KMeans
from PIL import ImageTk
import utils
import matplotlib.pyplot as plt
import argparse
from tkinter import filedialog
import cv2
def select_image():
	# grab a reference to the image panels
	global panelA, panelB
	path = filedialog.askopenfilename()
	k=int(e.get())
	if len(path) > 0:
			# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path)
		image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		#dinh dang hinh anh thanh 1 danh sach pixel ma tran Mxn,voi 3 mau RGB
		image1 = image2.reshape((image2.shape[0] * image2.shape[1], 3))
		#chinh kich thuoc anh ve 640x380
		image=cv2.resize(image,(640,380))
		image3 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		# khoi tao so luong cum mong muon
		clt = KMeans(n_clusters =k)
		#sap xep danh sach cac pixel
		clt.fit(image1)
		hist = utils.centroid_histogram(clt)
		edged = utils.plot_colors(hist, clt.cluster_centers_)		
		#tao hinh anh dung de ve tren plt
		image = Image.fromarray(image3)
		edged = Image.fromarray(edged)
		
		image = ImageTk.PhotoImage(image)
		edged = ImageTk.PhotoImage(edged)
	if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
			
			panelB = Label(image=edged)
			panelB.image = edged
			panelB.pack(side="right", padx=10, pady=10)
			
	else:
			
			panelA.configure(image=image)
			panelB.configure(image=edged)
			panelA.image = image
			panelB.image = edged
root=Tk()
panelA = None
panelB = None
#tao giao dien 720x640
root.minsize(720,640)
a=Label(root,text="cluster_centers")
a.pack()
e=Entry(root,width=50)
e.pack()
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="top", fill="both", expand="no", padx="10", pady="10")
root.mainloop();