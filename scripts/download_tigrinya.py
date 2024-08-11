import requests
import json
import time
import errno
import os


books = [
    {
    "bookNumber": 1,
    "englishShortName": 'gen',
    "englishName": 'Genesis',
    "shortName": 'ዘፍ',
    "middleName": 'ዘፍጥረት',
    "longName": 'ኦሪት ዘፍጥረት',
    "chapterSize": 50
    },
    {
    "bookNumber": 2,
    "englishShortName": 'Exo',
    "englishName": 'Exodus',
    "shortName": 'ዘጸ',
    "middleName": 'ዘጸአት',
    "longName": 'ኦሪት ዘጸአት',
    "chapterSize": 40
    },
    {
    "bookNumber": 3,
    "englishShortName": 'Lev',
    "englishName": 'Leviticus',
    "shortName": 'ዘሌ',
    "middleName": 'ዘሌዋውያን',
    "longName": 'ኦሪት ዘሌዋውያን ',
    "chapterSize": 27
    },
    {
    "bookNumber": 4,
    "englishShortName": 'Num',
    "englishName": 'Numbers',
    "shortName": 'ዘህ',
    "middleName": 'ዘህልቍ',
    "longName": 'ኦሪት ዘህልቍ',
    "chapterSize": 36
    },
    {
    "bookNumber": 5,
    "englishShortName": 'Deu',
    "englishName": 'Deuteronomy',
    "shortName": 'ዘዳ',
    "middleName": 'ዘዳግም',
    "longName": 'ኦሪት ዘዳግም',
    "chapterSize": 34
    },
    {
        "bookNumber": 6,
        "englishShortName": 'Jos',
        "englishName": 'Joshua',
        "shortName": 'ኢያ',
        "middleName": 'ኢያሱ',
        "longName": 'መጽሓፍ ኢያሱ ወልደ ነዌ',
        "chapterSize": 24
    },
    {
        "bookNumber": 7,
        "englishShortName": 'Jdg',
        "englishName": 'Judges',
        "shortName": 'መሳ',
        "middleName": 'መሳፍንቲ',
        "longName": 'መጽሓፍ መሳፍንቲ',
        "chapterSize": 21
    },
    {
        "bookNumber": 8,
        "englishShortName": 'Rut',
        "englishName": 'Ruth',
        "shortName": 'ሩት',
        "middleName": 'ሩት',
        "longName": 'መጽሓፍ ሩት',
        "chapterSize": 4
    },
    {
        "bookNumber": 9,
        "englishShortName": '1Sa',
        "englishName": '1 Samuel',
        "shortName": '1ሳሙ',
        "middleName": '1ይ ሳሙኤል',
        "longName": '1ይ መጽሓፍ ሳሙኤል',
        "chapterSize": 31
    },
    {
        "bookNumber": 10,
        "englishShortName": '2Sa',
        "englishName": '2 Samuel',
        "shortName": '2ሳሙ',
        "middleName": '2ይ ሳሙኤል',
        "longName": '2ይ መጽሓፍ ሳሙኤል',
        "chapterSize": 24
    },
    {
        "bookNumber": 11,
        "englishShortName": '1Ki',
        "englishName": '1 Kings',
        "shortName": '1ነገ',
        "middleName": '1ይ ነገስት',
        "longName": '1ይ መጽሓፍ ነገስት',
        "chapterSize": 22
    },
    {
        "bookNumber": 12,
        "englishShortName": '2Ki',
        "englishName": '2 Kings',
        "shortName": '2ነገ',
        "middleName": '2ይ ነገስት',
        "longName": '2ይ መጽሓፍ ነገስት',
        "chapterSize": 25
    },
    {
        "bookNumber": 13,
        "englishShortName": '1Ch',
        "englishName": '1 Chronicles',
        "shortName": '1ዜና',
        "middleName": '1ይ ዜና መዋዕል',
        "longName": '1ይ መጽሓፍ ዜና መዋዕል ',
        "chapterSize": 29
    },
    {
        "bookNumber": 14,
        "englishShortName": '2Ch',
        "englishName": '2 Chronicles',
        "shortName": '2ዜና',
        "middleName": '2ይ ዜና መዋዕል',
        "longName": '2ይ መጽሓፍ ዜና መዋዕል',
        "chapterSize": 36
    },
    {
        "bookNumber": 15,
        "englishShortName": 'Ezr',
        "englishName": 'Ezra',
        "shortName": 'እዝ',
        "middleName": 'እዝራ',
        "longName": 'መጽሓፍ እዝራ',
        "chapterSize": 10
    },
    {
        "bookNumber": 16,
        "englishShortName": 'Neh',
        "englishName": 'Nehemiah',
        "shortName": 'ነህ',
        "middleName": 'ነህምያ',
        "longName": 'መጽሓፍ ነህምያ',
        "chapterSize": 13
    },
    {
        "bookNumber": 17,
        "englishShortName": 'Est',
        "englishName": 'Esther',
        "shortName": 'አስ',
        "middleName": 'ኣስቴር',
        "longName": 'መጽሓፍ ኣስቴር',
        "chapterSize": 10
    },
    {
    "bookNumber": 18,
    "englishShortName": 'Job',
    "englishName": 'Job',
    "shortName": 'ኢዮ',
    "middleName": 'ኢዮብ',
    "longName": 'መጽሓፍ ኢዮብ',
    "chapterSize": 42
    },
    {
    "bookNumber": 19,
    "englishShortName": 'Psa',
    "englishName": 'Psalms',
    "shortName": 'መዝ',
    "middleName": 'ዳዊት',
    "longName": 'መዝሙር ዳዊት',
    "chapterSize": 150
    },
    {
    "bookNumber": 20,
    "englishShortName": 'Pro',
    "englishName": 'Proverbs',
    "shortName": 'ምሳ',
    "middleName": 'ምሳሌ',
    "longName": 'መጽሓፍ ምሳሌ',
    "chapterSize": 31
    },
    {
    "bookNumber": 21,
    "englishShortName": 'Ecc',
    "englishName": 'Ecclesiastes',
    "shortName": 'መክ',
    "middleName": 'መክብብ',
    "longName": 'መጽሓፍ መክብብ',
    "chapterSize": 12
    },
    {
    "bookNumber": 22,
    "englishShortName": 'SoS',
    "englishName": 'Song of Solomon',
    "shortName": 'መሃ',
    "middleName": 'መኃልየ መኃልየ',
    "longName": 'መኃልየ መኃልየ ዘሰሎሞን',
    "chapterSize": 8
    },
    {
    "bookNumber": 23,
    "englishShortName": 'Isa',
    "englishName": 'Isaiah',
    "shortName": 'ኢሳ',
    "middleName": 'ኢሳይያስ',
    "longName": 'ትንቢት ኢሳይያስ',
    "chapterSize": 66
    },
    {
    "bookNumber": 24,
    "englishShortName": 'Jer',
    "englishName": 'Jeremiah',
    "shortName": 'ኤር',
    "middleName": 'ኤርምያስ',
    "longName": 'ትንቢት ኤርምያስ',
    "chapterSize": 52
    },
    {
    "bookNumber": 25,
    "englishShortName": 'lem',
    "englishName": 'Lamentations',
    "shortName": 'ድጒ',
    "middleName": 'ድጒዓ ኤርምያስ',
    "longName": 'ድጒዓ ኤርምያስ',
    "chapterSize": 5
    },
    {
    "bookNumber": 26,
    "englishShortName": 'eza',
    "englishName": 'Ezekiel',
    "shortName": 'ህዝ',
    "middleName": 'ህዝቅኤል',
    "longName": 'ትንቢት ህዝቅኤል',
    "chapterSize": 48
    },
    {
    "bookNumber": 27,
    "englishShortName": 'dan',
    "englishName": 'Daniel',
    "shortName": 'ዳን',
    "middleName": 'ዳንኤል',
    "longName": 'ትንቢት ዳንኤል',
    "chapterSize": 12
    },
    {
    "bookNumber": 28,
    "englishShortName": 'hos',
    "englishName": 'Hosea',
    "shortName": 'ሆሴ',
    "middleName": 'ሆሴእ',
    "longName": 'ትንቢት ሆሴእ',
    "chapterSize": 14
    },
    {
    "bookNumber": 29,
    "englishShortName": 'joe',
    "englishName": 'Joel',
    "shortName": 'ዮኤል',
    "middleName": 'ዮኤል',
    "longName": 'ትንቢት ዮኤል',
    "chapterSize": 3
    },
    {
    "bookNumber": 30,
    "englishShortName": 'amo',
    "englishName": 'Amos',
    "shortName": 'አሞ',
    "middleName": 'አሞጽ',
    "longName": 'ትንቢት አሞጽ',
    "chapterSize": 9
    },
    {
    "bookNumber": 31,
    "englishShortName": 'oba',
    "englishName": 'Obadiah',
    "shortName": 'አብ',
    "middleName": 'አብድያ',
    "longName": 'ትንቢት አብድያ',
    "chapterSize": 1
    },
    {
    "bookNumber": 32,
    "englishShortName": 'jon',
    "englishName": 'Jonah',
    "shortName": 'ዮና',
    "middleName": 'ዮናስ',
    "longName": 'ትንቢት ዮናስ',
    "chapterSize": 4
    },
    {
    "bookNumber": 33,
    "englishShortName": 'mic',
    "englishName": 'Micah',
    "shortName": 'ሚክ',
    "middleName": 'ሚክያስ',
    "longName": 'ትንቢት ሚክያስ',
    "chapterSize": 7
    },
    {
    "bookNumber": 34,
    "englishShortName": 'nah',
    "englishName": 'Nahum',
    "shortName": 'ናሆ',
    "middleName": 'ናሆም',
    "longName": 'ትንቢት ናሆም',
    "chapterSize": 3
    },
    {
    "bookNumber": 35,
    "englishShortName": 'hab',
    "englishName": 'Habakkuk',
    "shortName": 'ዕን',
    "middleName": 'ዕንባቆም',
    "longName": 'ትንቢት ዕንባቆም',
    "chapterSize": 3
    },
    {
    "bookNumber": 36,
    "englishShortName": 'zep',
    "englishName": 'Zephaniah',
    "shortName": 'ሶፎ',
    "middleName": 'ሶፎንያስ',
    "longName": 'ትንቢት ሶፎንያስ',
    "chapterSize": 3
    },
    {
    "bookNumber": 37,
    "englishShortName": 'hag',
    "englishName": 'Haggai',
    "shortName": 'ሐጌ',
    "middleName": 'ሐጌ',
    "longName": 'ትንቢት ሐጌ',
    "chapterSize": 2
    },
    {
    "bookNumber": 38,
    "englishShortName": 'zec',
    "englishName": 'Zechariah',
    "shortName": 'ዘካ',
    "middleName": 'ዘካርያስ',
    "longName": 'ትንቢት ዘካርያስ',
    "chapterSize": 14
    },
    {
    "bookNumber": 39,
    "englishShortName": 'mal',
    "englishName": 'Malachi',
    "shortName": 'ሚል',
    "middleName": 'ሚልክያስ',
    "longName": 'ትንቢተ ሚልክያስ',
    "chapterSize": 4
    },
    {
    "bookNumber": 40,
    "englishShortName": 'mat',
    "englishName": 'Matthew',
    "shortName": 'ማቴ',
    "middleName": 'ማቴዎስ',
    "longName": 'ወንጌል ማቴዎስ',
    "chapterSize": 28
    },
    {
    "bookNumber": 41,
    "englishShortName": 'mar',
    "englishName": 'Mark',
    "shortName": 'ማር',
    "middleName": 'ማርቆስ',
    "longName": 'ወንጌል ማርቆስ',
    "chapterSize": 16
    },
    {
    "bookNumber": 42,
    "englishShortName": 'luk',
    "englishName": 'Luke',
    "shortName": 'ሉቃ',
    "middleName": 'ሉቃስ',
    "longName": 'ወንጌል ሉቃስ',
    "chapterSize": 24
    },
    {
    "bookNumber": 43,
    "englishShortName": 'joh',
    "englishName": 'John',
    "shortName": 'ዮሃ',
    "middleName": 'ወ. ዮሐንስ',
    "longName": 'ወንጌል ዮሐንስ',
    "chapterSize": 21
    },
    {
    "bookNumber": 44,
    "englishShortName": 'act',
    "englishName": 'Acts',
    "shortName": 'ግብ',
    "middleName": 'ግብሪ ሃዋርያት',
    "longName": 'ግብሪ ሃዋርያት',
    "chapterSize": 28
    },
    {
    "bookNumber": 45,
    "englishShortName": 'rom',
    "englishName": 'Romans',
    "shortName": 'ሮሜ',
    "middleName": 'ሮሜ',
    "longName": 'መልእኽቲ ጳውሎስ ናብ ሰብ ሮሜ',
    "chapterSize": 16
    },
    {
    "bookNumber": 46,
    "englishShortName": '1co',
    "englishName": '1 Corinthians',
    "shortName": '1ቆሮ',
    "middleName": '1ይ ቆሮንቶስ',
    "longName": '1ይ መልእኽቲ ጳውሎስ ናብ ሰብ ቆሮንቶስ',
    "chapterSize": 16
    },
    {
    "bookNumber": 47,
    "englishShortName": '2co',
    "englishName": '2 Corinthians',
    "shortName": '2ቆሮ',
    "middleName": '2ይ ቆሮንቶስ',
    "longName": '2ይ መልእኽቲ ጳውሎስ ናብ ሰብ ቆሮንቶስ',
    "chapterSize": 13
    },
    {
    "bookNumber": 48,
    "englishShortName": 'gal',
    "englishName": 'Galatians',
    "shortName": 'ገላ',
    "middleName": 'ገላትያ',
    "longName": 'መልእኽቲ ጳውሎስ ናብ ሰብ ገላትያ',
    "chapterSize": 6
    },
    {
    "bookNumber": 49,
    "englishShortName": 'eph',
    "englishName": 'Ephesians',
    "shortName": 'ኤፌ',
    "middleName": 'ኤፌሶን',
    "longName": 'መልእኽቲ ጳውሎስ ናብ ሰብ ኤፌሶን',
    "chapterSize": 6
    },
    {
    "bookNumber": 50,
    "englishShortName": 'php',
    "englishName": 'Philippians',
    "shortName": 'ፊል',
    "middleName": 'ፊሊጲ',
    "longName": 'መልእኽቲ ጳውሎስ ናብ ሰብ ፊሊጲ',
    "chapterSize": 4
    },
    {
    "bookNumber": 51,
    "englishShortName": 'col',
    "englishName": 'Colossians',
    "shortName": 'ቆሎ',
    "middleName": 'ቆሎሴ',
    "longName": 'መልእኽቲ ጳውሎስ ናብ ሰብ ቆሎሴ',
    "chapterSize": 4
    },
    {
    "bookNumber": 52,
    "englishShortName": '1th',
    "englishName": '1 Thessalonians',
    "shortName": '1ተሰ',
    "middleName": '1ይ ተሰሎንቄ',
    "longName": '1ይ መልእኽቲ ጳውሎስ ናብ ሰብ ተሰሎንቄ',
    "chapterSize": 5
    },
    {
    "bookNumber": 53,
    "englishShortName": '2th',
    "englishName": '2 Thessalonians',
    "shortName": '2ተሰ',
    "middleName": '2ይ ተሰሎንቄ',
    "longName": '2ይ መልእኽቲ ጳውሎስ ናብ ሰብ ተሰሎንቄ',
    "chapterSize": 3
    },
    {
    "bookNumber": 54,
    "englishShortName": '1ti',
    "englishName": '1 Timothy',
    "shortName": '1ጢሞ',
    "middleName": '1ይ ጢሞቴዎስ',
    "longName": '1ይ መልእኽቲ ጳውሎስ ናብ ጢሞቴዎስ',
    "chapterSize": 6
    },
    {
    "bookNumber": 55,
    "englishShortName": '2ti',
    "englishName": '2 Timothy',
    "shortName": '2ጢሞ',
    "middleName": '2ይ ጢሞቴዎስ',
    "longName": '2ይ መልእኽቲ ጳውሎስ ናብ ጢሞቴዎስ',
    "chapterSize": 4
    },
    {
    "bookNumber": 56,
    "englishShortName": 'tit',
    "englishName": 'Titus',
    "shortName": 'ቲቶ',
    "middleName": 'ቲቶ',
    "longName": 'መልእኽቲ ጳውሎስ ናብ ቲቶሰ',
    "chapterSize": 3
    },
    {
    "bookNumber": 57,
    "englishShortName": 'phi',
    "englishName": 'Philemon',
    "shortName": 'ፊል',
    "middleName": 'ፊልሞን',
    "longName": 'መልእኽቲ ጳውሎስ ናብ ፊልሞን',
    "chapterSize": 1
    },
    {
    "bookNumber": 58,
    "englishShortName": 'heb',
    "englishName": 'Hebrews',
    "shortName": 'ዕብ',
    "middleName": 'ዕብራውያን',
    "longName": 'መልእኽቲ ናብ እብራውያን',
    "chapterSize": 13
    },
    {
    "bookNumber": 59,
    "englishShortName": 'jam',
    "englishName": 'James',
    "shortName": 'ያዕ',
    "middleName": 'ያዕቆብ',
    "longName": 'መልእኽቲ ያዕቆብ',
    "chapterSize": 5
    },
    {
    "bookNumber": 60,
    "englishShortName": '1pe',
    "englishName": '1 Peter',
    "shortName": '1ጴጥ',
    "middleName": '1ይ ጴጥሮስ',
    "longName": '1ይ መልእኽቲ ጴጥሮስ',
    "chapterSize": 5
    },
    {
    "bookNumber": 61,
    "englishShortName": '2pe',
    "englishName": '2 Peter',
    "shortName": '2ጴጥ',
    "middleName": '2ይ ጴጥሮስ',
    "longName": '2ይ መልእኽቲ ጴጥሮስ',
    "chapterSize": 3
    },
    {
    "bookNumber": 62,
    "englishShortName": '1jo',
    "englishName": '1 John',
    "shortName": '1ዮሃ',
    "middleName": '1ይ ዮሐንስ',
    "longName": '1ይ መልእኽቲ ዮሐንስ',
    "chapterSize": 5
    },
    {
    "bookNumber": 63,
    "englishShortName": '2jo',
    "englishName": '2 John',
    "shortName": '2ዮሃ',
    "middleName": '2ይ ዮሐንስ',
    "longName": '2ይ መልእኽቲ ዮሐንስ',
    "chapterSize": 1
    },
    {
    "bookNumber": 64,
    "englishShortName": '3jo',
    "englishName": '3 John',
    "shortName": '3ዮሃ',
    "middleName": '3ይ ዮሐንስ',
    "longName": '3ይ መልእኽቲ ዮሐንስ',
    "chapterSize": 1
    },
    {
    "bookNumber": 65,
    "englishShortName": 'jud',
    "englishName": 'Jude',
    "shortName": 'ይሁ',
    "middleName": 'ይሁዳ',
    "longName": 'መልእኽቲ ይሁዳ',
    "chapterSize": 1
    },
    {
    "bookNumber": 66,
    "englishShortName": 'rev',
    "englishName": 'Revelation',
    "shortName": 'ራእ',
    "middleName": 'ራእይ ዮሐንስ',
    "longName": 'ራእይ ዮሐንስ',
    "chapterSize": 22
    }
]

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r", retrying=False):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    deduction =0
    if retrying:
        deduction= 1
    bar = fill * (filledLength- deduction) + ("x"* deduction) + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def downloadVerses():
    for i in books:
        if os.path.exists(f"tigrinya_verses_{i['englishShortName']}.json"):
            continue
        versesList = []
        for c in range(1, i["chapterSize"]+1):
            for r in range(5):
                try:
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0",
                        "Accept": "application/json, text/plain, */*",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "keep-alive",
                        "Referer": f"http://bible.geezexperience.com/tigrinya/chapter/{i['bookNumber']}/{c}",
                    }
                    response = requests.get(f"http://bible.geezexperience.com/server/list_api.php?language=tigrinya&book={i['bookNumber']}&chapter={c}", headers=headers)
                    if response.status_code == 200:
                        # response.content)
                        incoming = json.loads(response.content)
                        if len(incoming)==0:
                            raise Exception(f"Exception loading {i['shortName']} chapter {c}")
                        else:
                            for v in incoming:
                                article = v['article'].strip()
                                versesList.append(
                                    {
                                        "book": v["book"],
                                        "chaper": v["chapter"],
                                        "audioId": str(17 * int(v['noStart'])) +''+str(13*i['bookNumber']) + str(81*c),
                                        "article": article,
                                    }
                                )
                except requests.ConnectionError as e:
                    if r <4:
                        # Sleep for 1 second and retry
                        time.sleep(2)
                        printProgressBar(c-1, total=i["chapterSize"], prefix=f"Start {i['middleName']}", suffix=f"Complete {i['middleName']}", retrying=True)
                        continue
                    print(f"http://bible.geezexperience.com/server/list_api.php?language=tigrinya&book={i['bookNumber']}&chapter={c}")
                    raise e
                printProgressBar(c-1, total=i["chapterSize"], prefix=f"Start {i['middleName']}", suffix=f"Complete {i['middleName']}", retrying=False)
                break
            time.sleep(2)
        print()
        with open(f"tigrinya_verses_{i['englishShortName']}.json", "w") as file:
            json.dump(versesList, file)
    
    print("Loading Completed!")

if __name__ == '__main__':
    downloadVerses()