import os

if __name__ =="__main__":

    path = ".\image0"
    file = open('source_data0.txt','wb+')

    for i in os.listdir(path):

        img_path = os.path.join(os.getcwd(), 'image0', i)
        file.write(img_path+'\r\n')
        num = int(i.split('.')[0])
        file.write(str(num//30)+ '\r\n')
        print img_path
