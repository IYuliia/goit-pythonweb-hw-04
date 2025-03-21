### **Asynchronous File Sorting Script**  

This Python script scans all files in a user-specified **source folder** and organizes them into subfolders in the **output folder** based on file extensions. The sorting process is performed asynchronously to efficiently handle a large number of files.  

---

### **Technical Description**  

- Import the necessary asynchronous libraries.  
- Create an `ArgumentParser` object to handle command-line arguments.  
- Add required arguments for specifying the source and destination folders.  
- Initialize asynchronous paths for the source and destination folders.  
- Implement an asynchronous function `read_folder` to recursively scan all files in the source folder and its subfolders.  
- Implement an asynchronous function `copy_file` to copy each file into the appropriate subfolder in the output directory based on its extension.  
- Configure error logging for handling exceptions.  
