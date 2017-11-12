from .. import documents

def read_header_xml_element(
        element,
        body_reader,
        notes=None,
        comments=None):
    
    if notes is None:
        notes = []
    if comments is None:
        comments = []
    
    return body_reader.read_all(element.children) \
        .map(lambda children: documents.document(
            children,
            notes=documents.notes(notes),
            comments=comments
        ))