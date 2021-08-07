import os
class sort_files:

    """
    Dosya ismine ek olan sayılara göre sıralama yapar (küçükten büyüğe doğru)
    Sadece belirtilen isimdeki(argüman olarak verilen, file_name parametresi) dosyaları sıralı olarak listeler

    output0.mp3,output1.mp3,output2.mp3,output3.mp3,output4.mp3 için;
    output kelimesinin sonundaki sayılara göre, verilen dizindeki dosyaları sıralar

    """

    def __init__(self,directory,file_name,extension):
        self.extension=extension
        self.files= [file for file in os.listdir(directory) if file.endswith(self.extension)]
        self.file_name=file_name

        self.number_of_files = len(self.files)

    def __sort_number(self):
        numbers=[]
        start=len(self.file_name)
        for i in range(self.number_of_files):
            numbers.append(int(self.files[i][start:-1*len(self.extension)]))
        return sorted(numbers)

    def sorted_files(self):
        sorted_files=[]
        sorted_nums=self.__sort_number()
        for i in range(self.number_of_files):
            sorted_files.append(self.file_name+str(sorted_nums[i])+self.extension)
        return sorted_files

if __name__=="__main__":
    sort_files=sort_files(directory="/home/veysel/deneme/mp3/",file_name="output",extension=".mp3")
    sorted_files=sort_files.sorted_files()
    for i in sorted_files:
        print(i)
