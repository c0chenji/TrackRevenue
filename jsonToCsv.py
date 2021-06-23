from helper_functions.helpers import *
import pandas as pd

class InputFile:
    def __init__(self,filename,output_file):
        self.filename = filename
        self.output_file = output_file
    
    def export_to_csv(self):
        result=[]
        input_data = json_data(self.filename)
        header_labels= get_header_set(input_data)
        for i,v in input_data.items():
            temp_dict={}
            # classify labels with zero value and one values
            # store selected items in dictionary
            ones_set= set(v)
            zeros_set = header_labels- set(v)
            ones_dict= { i:1 for i in ones_set}
            zeros_dict={ i:0 for i in zeros_set} 
            #combine role, 0s and 1s into one dictionary
            temp_dict = {"":i,**ones_dict,**zeros_dict}
            # construct list of dictionarys to support dataframe
            result.append(temp_dict)
        output_data = pd.DataFrame.from_records(result)
        output_data.to_csv(self.output_file,index=False)


if __name__ == "__main__": 
    # The directories of input and output could be changed based on requirements
    result = InputFile(r"input.json",r"output.csv")
    result.export_to_csv()

    
