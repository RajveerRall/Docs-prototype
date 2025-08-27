from pdf2docx import Converter

# Define the paths for your PDF and the desired DOCX file
pdf_file = 'KAIZEN-Training-Material.pdf'
docx_file = 'converted_document.docx'

# Create a Converter object
cv = Converter(pdf_file)

# Perform the conversion
cv.convert(docx_file, start=0, end=None)

# Close the converter object
cv.close()

print(f"Successfully converted '{pdf_file}' to '{docx_file}'")