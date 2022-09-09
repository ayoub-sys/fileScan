# Import necessary packages for pdf 
import pdfx

#import necessary package for docx and docm 
import docxpy 

# Open The File in the Command
file = open("/home/ayoub/devHacking/python/pdfAnalysis/output.pdf", 'rb')

############# finding url for docx and docm file #############
def docLinkExtraction(file):
   doc=docxpy.DOCReader(file)
   doc.process()
   hyperlinks=doc.data['links']
   for x in hyperlinks:
      print(x[0])

############# finding url for pdf file ###########
def pdfLinkExtraction(file):
   pdf=pdfx.PDFx(file)
   metadata=pdf.get_references_as_dict()
   #print(metadata['url'])
   print(metadata['url'])


pdfLinkExtraction("/home/ayoub/devHacking/python/pdfAnalysis/output.pdf")