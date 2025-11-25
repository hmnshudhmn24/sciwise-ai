import re
def extract_citations(text):
    return re.findall(r"\[\d+\]", text)
