import PyPDF2

# with open("python\\course\\9\\pypdf\\first.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("python\\course\\9\\pypdf\\rotated.pdf", "wb") as output:
#         writer.write(output)


merger = PyPDF2.PdfFileMerger()
file_names = ["python\\course\\9\\pypdf\\first.pdf",
              "python\\course\\9\\pypdf\\second.pdf"]
for file in file_names:
    merger.append(file)
merger.write("python\\course\\9\\pypdf\\combined.pdf")
