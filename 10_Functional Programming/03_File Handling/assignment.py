file_path = "C:\\Users\\moorejay003\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\myFile.txt"

try:
    stream = open(
        "C:\\Users\\moorejay003\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\myFile.txt")

    
    print(stream.read())
    stream.write('This is your file')
    stream.write('Run this to see if its your file!')
    stream.write('This is still your file')
    stream.close()
  
    
except Exception as e:
    print('An error occurred: ', e)