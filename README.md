# Academic-Automation

This project contains the automation scripts required to perform frequently academic related work.
## 1. Student Performance Categorization Based on Marks
- The first automation task taken into account is automation for the categorizing students list based on Marks obtained in examination.
- This categorization is into three differnt classes as Outstanding, Good and Poor.
- Automation script (performancecategory.py) is prepapred in the python language.
- As numerical processing is required, pandas python library is used.
- Also the file format is .xls sheet, so used openpyxl python library.
- This project is developed with the following:
  - Operating System: Ubuntu 22.0
  - Language: Python-3
  - 
### 1.1. Following are the pre-requisite
1. Install the pip
   - **sudo apt install python3-pip**
     ![Pip Installation](pipinstallation.png)
3. Install pandas python library
   - **pip install pandas -y**
     ![pandas installation](pandasinstallation.png)
4. Install openpyxl python library
   - **pip install openpyxl -y**
     ![openpyxl installation](openxls_installation.jpeg)
5. xlsx file with the data of students (Name and Marks)


### 1.2 Output
- Execute the command on Ubuntu Terminal : **python3 performancecategory.py**
- This execution generates the output file in xlsx, with the classification categories as Outstanding, Good and Poor.
  
### 1.3 Achievement
- Before this automation, time required to generate the xls sheet with the claissifcation Outstanding, Good and Poor was 20-30 mintues, but with this automation time required to geenrate classified xls sheet is ~ 5-7 Seconds.

      
 
