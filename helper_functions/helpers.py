import json
import pandas as pd
def json_data(file_loc):
    # input should be directory of the targeted json file
    # return data of json file
    try:
        with open(file_loc) as f:
            data = json.load(f)
        return data
    except:
        print("invalid file or directory!")

def get_header_set(input):
    """Return the set of header labels """
    # use set to avoid duplicate items.
    temp_set = set()
    if len(input) == 0:
        return {}
    else:
    # add list to temp_set to create non-duplicate header label set
        for i in input.values():
            temp_set.update(i)
    return temp_set


def get_data_dict(filename):
    """The functionality is similar to the on in JsonToCsv, only for test purpose"""
    result=[]
    input_data = json_data(filename)
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
    return result