# We will put it here.
import os, errno
import mutagen
from mutagen.wave import WAVE 
# requests

allBooks = {
    "OldTestament": {
        "Genesis":  50,
        "Exodus":  40,
        "Leviticus":  27,
        "Numbers":  36,
        "Deuteronomy":  34,
        "Joshua":  24,
        "Judges":  21,
        "Ruth":  4,
        "1 Samuel":  31,
        "2 Samuel":  24,
        "1 Kings":  22,
        "2 Kings":  25,
        "1 Chronicles":  29,
        "2 Chronicles":  36,
        "Ezra":  10,
        "Nehemiah":  13,
        "Esther":  10,
        "Job":  42,
        "Psalm":  151,
        "Proverbs":  31,
        "Ecclesiastes":  12,
        "Song of Songs":  8,
        "Isaiah":  66,
        "Jeremiaja":  52,
        "Lamentations":  5,
        "Ezekiel":  48,
        "Daniel":  12,
        "Hosea":  14,
        "Amos":  9,
        "Micah":  7,
        "Joel":  3,
        "Obadiah":  1,
        "Jonah":  4,
        "Nahum":  3,
        "Habakkuk":  3,
        "Zephaniah":  3,
        "Haggai":  2,
        "Zechariah":  14,
        "Malachi":  4,
    },
    "NewTestament": {
        "Matthew": 28,
        "Mark": 16,
        "Luke": 24,
        "John": 21,
        "Acts": 28,
        "Romans": 16,
        "1 Corinthians": 16,
        "2 Corinthians": 13,
        "Galatians": 6,
        "Ephesians": 6,
        "Philippians": 4,
        "Colossians": 4,
        "1 Thessalonians": 5,
        "2 Thessalonians": 3,
        "1 Timothy": 6,
        "2 Timothy": 4,
        "Titus": 3,
        "Philemon": 1,
        "Hebrews": 13,
        "James": 5,
        "1 Peter": 5,
        "2 Peter": 3,
        "1 John": 5,
        "2 John": 1,
        "3 John": 1,
        "Jude": 1,
        "Revelation": 22,
    }
}


def download_create_files(category: str):
    failureCount = 0
    successCount = 0
    bookChapters = allBooks[category]
    try:
        os.mkdir( f"{category}")
    except:
        pass
    for book in bookChapters.keys():
        chapters = bookChapters[book]
        bookQuery = book.replace(" ", "")
        bookSave = book.replace(" ", "_")
        try:
            os.mkdir( f"{category}/{bookSave}", )
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        for chapter in range(1, chapters+1):
            chapterString = ""
            if chapter <= 9:
                chapterString = f"0{chapter}"
            else:
                chapterString = f"{chapter}"
            if os.path.exists(f"{category}/{bookSave}/Ch_{chapterString}.mp3"):
                continue
            response = requests.get(f"https://j-e-c.org/site/templates/BibleReading/{category}/{bookQuery}/Ch_{chapterString}.mp3")
            if response.status_code == 200:
                with open(f"{category}/{bookSave}/Ch_{chapterString}.mp3", "wb") as file:
                    file.write(response.content)
                    successCount+=1
            else:
                failureCount += 1
    print(f"{failureCount} failed to download\n {successCount} succesfully downloaded")
    

if __name__ == "__main__":
    download_create_files("OldTestament")
    download_create_files("NewTestament")