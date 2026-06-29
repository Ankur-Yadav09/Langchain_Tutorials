from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:\\Users\\ankur.yadav\\Desktop\\Lessons\\Langchain_Tutorials\\7_langchain-document-loaders-main\\dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)