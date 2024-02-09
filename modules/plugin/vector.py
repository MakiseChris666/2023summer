from langchain.embeddings import HuggingFaceEmbeddings, OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
import os

os.environ['OPENAI_API_KEY'] = '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'
splitter = CharacterTextSplitter(separator = '\n', chunk_size = 1000, chunk_overlap = 200, length_function = len)
# emb = OpenAIEmbeddings()
emb = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2')
_db: FAISS

def loadDB(file):
    global _db
    with open(file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    splitted = splitter.split_text(text)
    print(len(splitted))
    _db = FAISS.from_texts(splitted, emb)

def search(query, k = 1):
    res = _db.similarity_search(query, k = k)
    return res

def query(msg, history = None):
    vdata = search(msg)
    res = ''
    for d in vdata:
        res = res + d.page_content + '\n'
    res += '请根据上文回答以下问题：\n'
    return res + msg

# loadDB('./external/bjtu.txt')
if __name__ == '__main__':
    res = search('北京交通大学的网址')
    for d in res:
        print(d.page_content)