import sqlite3
from os.path import basename


def create_tables(cursor):
    cursor.execute('''CREATE TABLE languages
                 (id INTEGER PRIMARY KEY, language text, answer text, answered int, guide text)''')

    cursor.execute('''CREATE TABLE sources
                 (lang_id int, source text, file_name text)''')


def get_file_contents(path):
    f = open(path, "r")
    contents = f.read()
    f.close()

    return contents


def insert(item, cursor):
    lang_id = item["lang_id"]
    language = item["language"]
    answer = item["answer"]
    guide = item["guide"]

    query_lang = "INSERT INTO languages VALUES(?, ?, ?, ?, ?)"
    cursor.execute(query_lang, (lang_id, language, answer, 0, guide))

    # handle multipel sources
    sources = []
    if not isinstance(item["source"], list):
        sources = [item["source"]]
    else:
        sources = item["source"]

    for source_path in sources:
        source = get_file_contents(source_path)
        query_source = "INSERT INTO sources(lang_id, source, file_name) VALUES(?, ?, ?)"
        cursor.execute(query_source, (lang_id, source, basename(source_path)))


data = [{
    "lang_id": 1,
    "language": "Python",
    "answer": "google",
    "guide": "A folder named Python was created. Go there and fight with program.py!",
    "source": "Python/program.py"
}, {
    "lang_id": 2,
    "language": "Go",
    "answer": "200 OK",
    "guide": "A folder named Go was created. Go there and try to make Google Go run.",
    "source": "Go/program.go"
}, {
    "lang_id": 3,
    "language": "Java",
    "answer": "object oriented programming",
    "guide": "A folder named Java was created. Can you handle the class?",
    "source": "Java/Program.java"
}, {
    "lang_id": 4,
    "language": "Haskell",
    "answer": "Lambda",
    "guide": "Something pure has landed. Go to Haskell folder and see it!",
    "source": "Haskell/program.hs"
}, {
    "lang_id": 5,
    "language": "C#",
    "answer": "NDI=",
    "guide": "Do you see sharp? Go to the C# folder and check out.",
    "source": "CSHARP/program.cs"
}, {
    "lang_id": 6,
    "language": "Ruby",
    "answer": "https://www.ruby-lang.org/bg/",
    "guide": "Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!",
    "source": "Ruby/program.rb"
}, {
    "lang_id": 7,
    "language": "C++",
    "answer": "header files",
    "guide": "Here be dragons! It's C++ time. Go to the C++ folder.",
    "source": ["C++/base64.cpp", "C++/base64.h", "C++/program.cpp"]
}, {
    "lang_id": 8,
    "language": "JavaScript",
    "answer": "Douglas Crockford",
    "guide": "NodeJS time. Go to JavaScript folder and Node your way!",
    "source": ["JavaScript/package.json", "JavaScript/program.js"]
}]


conn = sqlite3.connect("polyglot.db")
c = conn.cursor()

create_tables(c)

for item in data:
    insert(item, c)

conn.commit()
conn.close()
