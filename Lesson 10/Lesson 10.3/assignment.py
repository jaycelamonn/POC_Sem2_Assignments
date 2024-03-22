file_path = "C:\\Users\\moorejay003\\POC_Sem2_Assignments\\Lesson 10\\Lesson 10.3\\newfile.txt"

try:
    stream = open(file_path)
     print(stream.read())
     stream.close()
  
    
except Exception as e:
     print('An error occurred: ', e)
    

