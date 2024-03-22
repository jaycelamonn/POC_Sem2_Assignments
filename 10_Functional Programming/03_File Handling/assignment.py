file_path = "C:\\Users\\moorejay003\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\myFile.txt"

try:
    stream = open(file_path)
    print(stream.read())
    stream.close()
  
    
except Exception as e:
    print('An error occurred: ', e)