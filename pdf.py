import PyPDF2

with open('PDF/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    writer = PyPDF2.PdfWriter()
    writer.add_page(page.rotate(90))
    with open('./PDF/upsidedown.pdf', 'wb') as new_file:
        writer.write(new_file)
