from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end,file):
    inputPdf = PdfFileReader(open(file,"rb"))
    outPdf = PdfFileWriter()
    with open(file.split(".")[0]+"cropped"+".pdf","wb") as ostream:
        while start <= end:
          outPdf.addPage(inputPdf.getPage(start))
          outPdf.write(ostream)
          start+=1

# cropper(1,3,"sample.pdf")