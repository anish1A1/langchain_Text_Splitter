from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
text = """
Space exploration has led to incredible scientific discoveries.
From landing on the Moon to exploring Mars, humanity
continues to push the boundaries of what’s possible beyond our
planet.
These missions have not only expanded our knowledge of the
universe but have also contributed to advancements in
technology here on Earth. Satellite communications, GPS, and
even certain medical imaging techniques trace their roots back
to innovations driven by space programs.
"""

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()
splitter = CharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=10,
    separator=' '
)

result = splitter.split_documents(docs)
print(result)
print('\n\n',result[0].page_content)


# for texts
result2 = splitter.split_text(text)
print('\n',result2)