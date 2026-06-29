from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='C:\\Users\\ankur.yadav\\Desktop\\Lessons\\Langchain_Tutorials\\7_langchain-document-loaders-main\\Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])