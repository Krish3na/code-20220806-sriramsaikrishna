import pandas as pd
import json
import traceback
import matplotlib.pyplot as plt
import numpy as np

class BMI_Calculator:
    """
    BMI_Calculator is used to calculate BMI of a person
    Body Mass Index (BMI) is a measure of body fat based on height and weight that applies to adult men and women
    It is calculated using formula BMI(kg/m^2) = mass(kg) / height(m)^2
    
    This class has two methods : calculate_bmi, count_category, read_data, save_result
    
    calculate_bmi - calculates 'BMI' values with given Height, Weight values and adds the 'BMI Category', status of 'Health risk'
    count_category - finds the count of people of specific category of the given input data
    read_data - reads the given json file converts it into DataFrame and assigns it to class variable
    save_result - saves the result and writes it to a json file   
    """
    def __init__(self) -> None:
        pass

    def calculate_bmi(self, weight: str, height: str, bmi_table: str = 'input/bmi_table.json') -> pd.DataFrame:
        """
        # INPUT
        weight -> str : WeightKg (column name)
        height -> str : HeightCm (column name)
        bmi_table -> str : BMI Reference Table file name

        # OUTPUT
        self.input_data -> pd.DataFrame : DataFrame with added columns - 'BMI', 'BMI Category', 'Health risk'
        """
        try:
            # calculates BMI values, saves in a new 'BMI' column
            self.input_data['BMI'] = round((self.input_data[weight] * 10000)/(self.input_data[height] ** 2), 1)
            # creating two empty columns 'BMI Category', 'Health risk'
            self.input_data.insert(4,'BMI Category',"-")
            self.input_data.insert(5,'Health risk',"-")         

            # reading a BMI Reference Table, converting it to a dictionary and assinging it to variable. Used to categorize people based on calculated BMI values
            with open(bmi_table,'r') as f:
                table_data = json.loads(f.read())
            table_data = pd.json_normalize(table_data)
            table_data = list(table_data.to_dict('index').values())
            
            # getting calcualted BMI values
            bmi_values = self.input_data['BMI'].values
            # based on calculated BMI values categorizing people to several categories and health risk comments in respective columns
            for bmi_index in range(len(bmi_values)):
                for row in table_data:
                    bmi_range = row['Range']
                    bmi_range = bmi_range.split('-')
                    lower_limit, upper_limit = float(bmi_range[0]), float(bmi_range[1])
                    
                    if lower_limit <= bmi_values[bmi_index] <= upper_limit:
                        bmi_category, health_risk = row['BMI Category'], row['Health risk']
                        break

                if bmi_category and health_risk :
                    self.input_data.loc[bmi_index, 'BMI Category'] = bmi_category           
                    self.input_data.loc[bmi_index, 'Health risk'] = health_risk

            return self.input_data           
                
        except Exception:
            print('Exception occured at : ', self.calculate_bmi.__name__)
            traceback.print_exc()

    def count_category(self, column: str, category: str) -> int:
        """
        # INPUT
        column -> str : column name
        category -> str : category name

        # OUTPUT
        count -> int : returns count of people with specific category of that specific column
        """
        try:
            count = 0
            # getting values of the column
            category_values = self.input_data[column].values
            # iterating over and adding up the count if given category and category of above list matches
            for c in category_values :
                if c == category:
                    count += 1
            return count

        except Exception:
            print('Exception occured at : ', self.count_category.__name__)
            traceback.print_exc()

    def read_data(self, input_file: str) -> pd.DataFrame:
        """
        # INPUT
        input_file -> str : input data file name

        # OUTPUT
        self.input_data -> pd.DataFrame : returns a DataFrame (file data converted to DataFrame)
        """
        try : 
            # reading json file and converting it to DataFrame
            with open(input_file,'r') as f:
                input_data = json.loads(f.read())
            self.input_data = pd.json_normalize(input_data)
            return self.input_data

        except Exception:
            print('Exception occured at : ', self.read_data.__name__)
            traceback.print_exc()

    def save_result(self, result_file: str) -> None:
        """
        # INPUT
        result_file -> str : output data file name to be named, to save data in it
        """
        try:
            # converting DataFrame to Dictinary and then to list
            self.result = list(self.input_data.to_dict('index').values())
            # converting the list to json_format dictionary
            result = json.dumps(self.result, indent=4)

            # writing it to a file
            with open(result_file, 'w') as outputfile:
                outputfile.write(result)
            
        except Exception:
            print('Exception occured at : ', self.save_result.__name__)
            traceback.print_exc()


def print_file_data(file: str) -> None:
    """
    # INPUT
    file -> str : file name to be read and print it
    """
    try:
        print()
        with open(file, 'r+') as rf:
            print(rf.read())

    except Exception:
        print('Exception occured at : ', print_file_data.__name__)
        traceback.print_exc()

def get_json_column(file: str, column: str) -> pd.Series:
    """
    # INPUT
    file -> str : file name to be read and print it
    column -> str : column name to be extracted

    # OUTPUT
    file_data[column] ->  pd.Series : Series with given column name of a DataFrame
    """
    try:
        file_data = pd.read_json(file)
        return file_data[column]

    except Exception:
        print('Exception occured at : ', get_json_column.__name__)
        traceback.print_exc()

def visualize_data(dictionary, file_name, xlabel, ylabel, title) :
    """
    # INPUT
    dictionary -> dict : dictionary with keys and values
    file_name -> str : file name of plot to be saved as
    xlabel -> str : x-axis title
    ylabel -> str : y-axis title
    title -> str : title of plot
    """
    try:
        values = list(dictionary.values())
        labels = list(dictionary.keys())
        colors = ['green','blue','purple','teal', 'brown', 'orange' ,'yellow', 'red', 'lime', 'orchid', 'grey', 'black', 'pink', 'gray', 'lightpink']

        # initializing the plot
        plt.figure(figsize=(15,8))
        
        if len(values) <= len(colors) :
            plt.barh(labels, values, color = colors[:len(values)])
        else:
            plt.barh(labels, values)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.savefig(file_name)

    except Exception:
        print('Exception occured at : ', visualize_data.__name__)
        traceback.print_exc()