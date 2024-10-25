from docx import Document
import pandas as pd

# Definir el diccionario de traducción manualmente
translations = {
    "DESARROLLADOR FULL STACK": "FULL STACK DEVELOPER",
    "William David Gómez Carrillo": "William David Gómez Carrillo",
    "OBJETIVO PROFESIONAL": "PROFESSIONAL OBJECTIVE",
    # Agrega aquí todas las traducciones necesarias...
}

# Cargar el nuevo documento subido
new_doc_path = 'C:/Users/willd/OneDrive/Desktop/CV_WILLIAM_DAVID.docx'
new_doc = Document(new_doc_path)

# Traducir el contenido manteniendo la estructura y los elementos del documento
for para in new_doc.paragraphs:
    for es_text, en_text in translations.items():
        if es_text in para.text:
            para.text = para.text.replace(es_text, en_text)

# Guardar el documento traducido sin modificaciones estructurales ni estéticas
new_translated_doc_path = 'C:/Users/willd/OneDrive/Desktop/CV_WILLIAM_DAVID_Translated_Unmodified_2.docx'
new_doc.save(new_translated_doc_path)

print("Documento traducido guardado en:", new_translated_doc_path)
