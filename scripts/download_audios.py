import os, requests, errno, json
# import mutagen
# import logging
# from mutagen.wave import WAVE 
from  download_tigrinya import printProgressBar
import time
import threading

# bookNamesShort = ["gen","Exo","Lev","Num","Deu","Jos","Jdg","Rut","1Sa","2Sa","1Ki","2Ki"] #,"1Ch","2Ch","Ezr","Neh","Est","Job","Psa","Pro","Ecc","SoS","Isa","Jer","lem","eza","dan","hos","joe","amo","oba","jon","mic","nah","hab","zep","hag","zec","mal","mat","mar","luk","joh","act","rom","1co","2co","gal","eph","php","col","1th","2th","1ti","2ti","tit","phi","heb","jam","1pe","2pe","1jo","2jo","3jo","jud","rev"]
# bookNamesShort = ["1Ch","2Ch","Ezr","Neh","Est","Job","Psa"]#,"Pro","Ecc","SoS","Isa","Jer","lem","eza","dan","hos","joe","amo","oba","jon","mic","nah","hab","zep","hag","zec","mal","mat","mar","luk","joh","act","rom","1co","2co","gal","eph","php","col","1th","2th","1ti","2ti","tit","phi","heb","jam","1pe","2pe","1jo","2jo","3jo","jud","rev"]
# bookNamesShort = ["Pro","Ecc","SoS","Isa","Jer","lem","eza",]#"dan","hos","joe","amo","oba","jon","mic","nah","hab","zep","hag","zec","mal","mat","mar","luk","joh","act","rom","1co","2co","gal","eph","php","col","1th","2th","1ti","2ti","tit","phi","heb","jam","1pe","2pe","1jo","2jo","3jo","jud","rev"]
# bookNamesShort = ["dan","hos","joe","amo","oba","jon","mic","nah",]#"hab","zep","hag","zec","mal","mat","mar","luk","joh","act","rom","1co","2co","gal","eph","php","col","1th","2th","1ti","2ti","tit","phi","heb","jam","1pe","2pe","1jo","2jo","3jo","jud","rev"]
bookNamesShort = ["hab","zep","hag","zec","mal","mat","mar","luk","joh","act","rom","1co","2co","gal","eph","php","col","1th","2th","1ti","2ti","tit","phi","heb","jam","1pe","2pe","1jo","2jo","3jo","jud","rev"]

headers  = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
    'Accept-Language': 'en-US,en;q=0.5',
    'Range': 'bytes=0-',
    'Connection': 'keep-alive',
    'Referer': 'http://bible.geezexperience.com/',
    'Sec-Fetch-Dest': 'audio',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site'
}


def downloadWavFiles():
    verseTakeLock = threading.Lock()
    writeVerseLock = threading.Lock()
    updateCountValues = threading.Lock()
    
    with open(f"Tigrinya/tig_train_3.txt", "a") as trainFile:
        for bns in bookNamesShort:
            with open(f"Tigrinya/verses_json/tigrinya_verses_{bns}.json", "r") as file:
                verses = json.load(file)
                totalVersesLength = len(verses)
                count =0
                def takeAndProcess():
                    nonlocal count
                    while True:
                        v = {}
                        with verseTakeLock:
                            if len(verses)==0:
                                break
                            v = verses.pop(0)
                            
                        if os.path.exists(f"Tigrinya/wav/ti{v['audioId']}.wav"):
                            with updateCountValues:
                                count +=1
                                continue

                        for r in range(5):
                            response = requests.get(f"https://mariqosay.com/static/bible/{v['book']}/{v['chaper']}/ti{v['audioId']}.wav", headers= headers)
                            if response.status_code != 200 and response.status_code != 206:
                                if r <4:
                                    printProgressBar(count, total=totalVersesLength, prefix=f"Start {bns}",  suffix= f"{count/totalVersesLength}%", retrying=True)
                                    time.sleep(.4)
                                    continue
                                raise Exception(f"failed to download an audio ti{v['audioId']}.wav of book {v['book']} and chapter {v['chaper']}  with status code: {response.status_code}")
                            with open(f"Tigrinya/wav/ti{v['audioId']}.wav", "wb") as audio:
                                with writeVerseLock:
                                    trainFile.write(f"ti{v['audioId']}.wav\t\t{v['article'].strip()}\n")
                                    audio.write(response.content)
                                    with updateCountValues:
                                        # audiosCount +=1
                                        count +=1
                                printProgressBar(count, total=totalVersesLength, prefix=f"Start {bns}",  suffix= f"{count/totalVersesLength}%", retrying=False)
                            break
                
                threads = []
                for i in range(3):
                    x= threading.Thread(target=takeAndProcess)
                    threads.append(x)
                    x.start()
                
                for index, thread in enumerate(threads):
                    thread.join()
            print()
                
if __name__ == "__main__":
    # dDowbloader = Downloader()
    # dDowbloader.downloadWavFiles()
    downloadWavFiles()
    
    
# class Downloader:
#     def __init__(self):
#         self.count =0
#         self.verses = []
#         self.verseTakeLock = threading.Lock()
#         self.writeVerseLock = threading.Lock()
#         self.updateCountValuesLock = threading.Lock()
        
    
#     def downloadWavFiles(self):
        
#         with open(f"Tigrinya/tig_train_1.txt", "a") as trainFile:
#             for bns in bookNamesShort:
#                 with open(f"Tigrinya/verses_json/tigrinya_verses_{bns}.json", "r") as file:
#                     self.verses = json.load(file)
#                     # totalVersesLength = len(self.verses)
#                     self.count =0
#                     def takeAndProcess():
#                         while True:
#                             v = {}
#                             with self.verseTakeLock:
#                                 if len(self.verses)==0:
#                                     break
#                                 v = self.verses.pop(0)
                            
#                             if os.path.exists(f"Tigrinya/wav/ti{v['audioId']}.wav"):
#                                 with self.updateCountValues:
#                                     self.count +=1
#                                     continue

#                             for r in range(5):
#                                 response = requests.get(f"https://mariqosay.com/static/bible/{v['book']}/{v['chaper']}/ti{v['audioId']}.wav", headers= headers)
#                                 if response.status_code != 200 and response.status_code != 206:
#                                     if r <4:
#                                         # printProgressBar(self.count, total=totalVersesLength, prefix=f"Start {bns}",  suffix= f"{self.count/totalVersesLength}%", retrying=True)
#                                         time.sleep(.4)
#                                         continue
#                                     raise Exception(f"failed to download an audio ti{v['audioId']}.wav of book {v['book']} and chapter {v['chaper']}  with status code: {response.status_code}")
#                                 with open(f"Tigrinya/wav/ti{v['audioId']}.wav", "wb") as audio:
#                                     with self.writeVerseLock:
#                                         trainFile.write(f"ti{v['audioId']}.wav\t\t{v['article'].strip()}\n")
#                                         audio.write(response.content)
#                                         with self.updateCountValuesLock:
#                                             # audiosCount +=1
#                                             self.count +=1
#                                     # printProgressBar(self.count, total=totalVersesLength, prefix=f"Start {bns}",  suffix= f"{self.count/totalVersesLength}%", retrying=False)
                                #  break
                    
#                     threads = []
#                     for i in range(3):
#                         x= threading.Thread(target=takeAndProcess)
#                         threads.append(x)
#                         x.start()
                    
#                     for index, thread in enumerate(threads):
#                         thread.join()
#                 print()
        
    