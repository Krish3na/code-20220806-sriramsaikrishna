import unittest
import pandas as pd
from bmi.bmi_calculator import BMI_Calculator, get_json_column
import traceback


class BMI_Calculator_Test(unittest.TestCase):
    """
    BMI_Calculator_Test is used to test whether BMI_Calculator class is working as expected or not
    Body Mass Index (BMI) is a measure of body fat based on height and weight that applies to adult men and women
    It is calculated using formula BMI(kg/m^2) = mass(kg) / height(m)^2
    
    This class has two methods : calculate_bmi_test, count_category_test
    
    calculate_bmi_test - this method is used to test calculate_bmi method using test data and expected data
    count_category_test - this method is used to test count_category_test method using test data and validation data
    """
    def __init__(self, test_data: str, expected_data: str, bmi_table: str) -> None:
        """
        # INPUT
        test_data -> str : file that contains test data used for validation
        expected_data -> str : file that contains expected output data
        bmi_table -> str : BMI Reference Table file name
        """
        self.test_data, self.expected_data, self.bmi_table = test_data, expected_data, bmi_table
        # initializing the BMI_Calculator object
        self.test_obj = BMI_Calculator()

    def calculate_bmi_test(self) -> None:
        try:
            # calculating 'BMI', 'BMI Category', 'Health risk' for given test data
            self.test_obj.read_data(self.test_data)
            self.tested_data  = self.test_obj.calculate_bmi('WeightKg', 'HeightCm', self.bmi_table)
            # reading the expected output data
            self.expected_data = pd.read_json(self.expected_data)      

            # comparing the resulted output of test data and expected output data
            pd.testing.assert_frame_equal(self.tested_data[['BMI', 'BMI Category', 'Health risk']], self.expected_data[['BMI', 'BMI Category', 'Health risk']])
            # below statement is printed if both actual output and expected output are same, else exception is raised
            print('calculate_bmi method - tested successfully !')

        except Exception:
            print('Exception occured at : ', self.calculate_bmi_test.__name__)
            traceback.print_exc()

    
    def count_category_test(self, column: str) -> None:
        try:
            # getting 'BMI Category' values from BMI Reference Table 
            categories_list = list(get_json_column(self.bmi_table, column))
            # expected count of categories of test data
            count_expected_dict = {'Underweight' : 3, 'Normal weight' : 1, 'Overweight' : 4, 'Moderately obese' : 1, 'Severely obese' : 1, 'Very severely obese' : 2}

            # comparing the resulted output of test data and expected output data
            for category in categories_list:
                assert self.test_obj.count_category(column, category) == count_expected_dict[category]
            # below statement is printed if both actual output and expected output are same, else exception is raised
            print('count_category method - tested successfully !')

        except Exception:
            print('Exception occured at : ', self.count_category_test.__name__)
            traceback.print_exc()

