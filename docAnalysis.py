from oletools.olevba import VBA_Parser, TYPE_OLE, TYPE_OpenXML, TYPE_Word2003_XML, TYPE_MHTML

def docScan(myfile):
    #myfile = '/home/ayoub/Downloads/file1.docm'
    filedata = open(myfile, 'rb').read()
    vbaparser = VBA_Parser(myfile, data=filedata)
    if vbaparser.detect_vba_macros():
        return "malicious"
    else:
        return "clean"