import cv2, os
base_path = "VeriFinger_Sample_DB/"
new_path = "dataFinal2/"
for path, subdirs, files in os.walk(base_path):
    for name in files:
        #print()
        if name.endswith(".tif"):
          #print ("file : " ,path,name)
          read = cv2.imread(os.path.join(path, name),cv2.IMREAD_GRAYSCALE)
          outfile = name.split('.')[0] + '.jpg'
          #print(new_path+path+outfile)
          #print(read.shape)
          
          p_to_creat=""
          #print(path+"#############")
          for p in path.split("/"):
                p_to_creat=p_to_creat+p+"/"
                if  not os.path.exists(new_path+p_to_creat):
                  
                  os.makedirs(new_path+p_to_creat)
          
          #print(new_path+p_to_creat,os.path.exists(new_path+p_to_creat))
          out=cv2.imwrite(new_path+path+outfile,read,[int(cv2.IMWRITE_JPEG_QUALITY), 200])
          print(out,new_path+path+outfile)
          #print(os.path.exists(new_path+p_to_creat+outfile))

    
