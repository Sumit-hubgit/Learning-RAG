from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader



doc = Document(
    page_content="This is the story of a boy who lived in bengaluru and explored as much as he can.",
    metadata = {
        "source":"life.txt",
        "author":"sumit",
        "pages":"1",
        "date_created":"2026"
    }
)
print(doc)

import os 
os.makedirs("..data/text_files",exist_ok=True)

sample_texts={
    "..data/text_files/python_intro":""" Python is a high-level, interpreted, and beginner-friendly programming language created by Guido van Rossum. It is widely used in backend development, artificial intelligence, automation, data science, web development, and scripting because of its simple syntax and readability. Python supports multiple programming styles including procedural, object-oriented, and functional programming. It provides built-in data types such as lists, dictionaries, tuples, and sets, along with powerful concepts like functions, classes, inheritance, exception handling, decorators, generators, multithreading, and asynchronous programming. Python uses indentation instead of braces, making code cleaner and easier to understand. It also has a massive ecosystem of libraries and frameworks such as NumPy, Pandas, Flask, Django, and FastAPI that simplify complex tasks. Developers use `pip` to install packages and virtual environments to manage dependencies separately for projects. Python is heavily used for building REST APIs, automating repetitive tasks, handling databases, machine learning, cloud automation, and data analytics. Popular IDEs for Python include VS Code and PyCharm. Although Python may be slower than languages like C++ or Java, it allows much faster development and easier maintenance. Because of its versatility, simplicity, and industry demand, Python is considered one of the best languages for beginners as well as professional software engineers.
 """
}

for filepath , content in sample_texts.items():
    with open(filepath,'w',encoding="utf-8") as f:
        f.write(content)
    print("samle text file created!")


loader = TextLoader("..data/text_files/python_intro",encoding = "utf-8")
document = loader.load()
print(document)