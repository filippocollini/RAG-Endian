from unstructured.partition.pdf import partition_pdf

def load_pdf(path):
    elements = partition_pdf(filename=path)
    return "\n".join([el.text for el in elements if el.text])
