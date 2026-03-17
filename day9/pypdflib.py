from PyPDF2 import PdfReader
import os
reader= PdfReader(r"C:\Users\Gautam G\OneDrive\Desktop\_Java_Module 5.pdf")        
print(len (reader.pages))
print(os.getcwd())