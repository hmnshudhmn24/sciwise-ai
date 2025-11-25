from .text_preprocessing import chunk_text
def create_chunks(record, chunk_size=500, overlap=50):
    text = record.get('text') or record.get('abstract','')
    return chunk_text(text, chunk_size, overlap)
