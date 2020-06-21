import os
#從每個檔案提取出地名（有了所有地名）#step2
def extract_place(filename):
    return filename.split("_")[1]


#為每個地名創建目錄
def make_place_directories(places):
    for place in places:
        os.mkdir(place)


def orgize_photos (directory):
    #首先，從照片檔名中取得地名
    os.chdir(directory)#更改當前目錄去到要組織整理的目錄中
    originals = os.listdir() #列出這個目錄中所有檔案，並分配給變數（有了所有檔案名）#step1
    places = [] #建立一個地名表單,之後創建地名目錄會用到
    for filename in originals:#遍歷所有檔案,把列表裡含有的地名加入名單中#step3
        place = extract_place(filename) #提取檔案名中的地名
        if place not in places: #確保不會重複把一樣的地名加進去
            places.append(place) #把地名加入到地名表單中
    #利用地名表單places,為每個地點創建子目錄
    make_place_directories(places)
    #把每份文件歸檔 #step4
    for filename in originals: #遍歷所有文檔
        place = extract_place(filename) #提取文檔中的地名
        os.rename(filename,#把照片歸檔到符合該地名的目錄中
                  os.path.join(place, filename))    


orgize_photos("Photos") #記得把實參改成你要整理的資料夾#記得加上""以免被當成變量,會導致NameError
