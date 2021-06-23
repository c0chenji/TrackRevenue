# jsonToCsv
A table generator based on the data of provided json file 

---
## Table of contents
* [General Info](#general-info)
* [Project Structure](#project-structure)
* [Technologies](#technologies)
* [Installation](#installation)
* [Usage](#usage)
* [Test](#test)

--- 
## General Info
A simple program that converts json file to csv file in specific format

---
## Technologies
Project is created with:
* python 3.9.1

---
## Project Structure
    .
    ├── helper_functions                       # Helper function folder
    │   ├── helpers.py  
    ├── test_sample                # Folder of json files for testing
    ├── test.py                      # Unittest  
    ├── jsonToCsv.py
    ├── input.json                    # Should be created before running the 
    ├── output.csv                    #result
    ├── requirements.txt
    └── README.md

---
## Installation

Follow the [instruction](https://wiki.python.org/moin/BeginnersGuide/Download) to install python3.  

Install required packages in requirements.txt(Creating an virtual environment would be recommand)

```python
pip3 install -r requirements.txt
```  

---
## Usage
Under the main block of jsonToCsv.py, modify the direcotries of input file or output file if you want to.

```python
if __name__ == "__main__": 
    # The directories of input and output could be changed based on requirements
    result = InputFile(r"input.json",r"output.csv")
    result.export_to_csv()
```  
To test the application, change current directory to TrackRevenue folder and run: 

```python
python jsonToCsv.py
```  
Then a file named output.csv would be generated.(change the second class input to modify the name of output file)

---
## Test
Test cases are forcusing on the helper functions and the generated results.
To check tests, change current directory to TrackRevenue folder and run:    

```python
python -m unittest test
``` 
---

##  Contributors
- Jarick Chen <jarick@live.ca>
---
## License & Copyright
&copy; Jarick Chen