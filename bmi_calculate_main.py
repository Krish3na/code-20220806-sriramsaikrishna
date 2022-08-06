from bmi.bmi_calculator import BMI_Calculator, print_file_data, get_json_column, visualize_data
import pandas as pd

input_data = 'input/input_data.json'
bmi_table = 'input/bmi_table.json'
output_data = 'output/result_data.json'
text_output_file = 'output/output_text.txt'

# initializing BMI_Calculator object
bmi_calculator = BMI_Calculator()
# reading input data
data = bmi_calculator.read_data(input_data)
print(data)
# calculating 'BMI', 'BMI Category', 'Health risk' of input data
calculated_bmi_data  = bmi_calculator.calculate_bmi('WeightKg', 'HeightCm', bmi_table)
print(calculated_bmi_data)

# saving the result output in a json file
bmi_calculator.save_result(output_data)
print_file_data('output/result_data.json')

# printing BMI_Reference_Table
print_file_data('input/bmi_table.json')
# printing 'BMI Category' values
print(get_json_column(bmi_table, 'BMI Category'))

# finding the count of 'Overweight' people
overweight_people = bmi_calculator.count_category('BMI Category', 'Overweight')
print('\nCount of total number of Overweight people is ', str(overweight_people))


# getting the list of categories
categories_list = list(get_json_column(bmi_table, 'BMI Category'))
# dictionary to store category and it's count
count_dict = {}

# finding the count of each category
for category in categories_list:
    count_dict[category] = int(bmi_calculator.count_category('BMI Category', category))

print(count_dict)

# visualizing the 'BMI Category' categories and the count of people falling under those categories
visualize_data(count_dict, 'output/actual_input_data_bar_chart.png', 'Count of People', 'BMI Categories', 'BMI Categories (vs) Count')


# saving the output to a text file
with open(text_output_file, "w") as f:
    # Writing data to a file
    f.write(str(pd.read_json(input_data)))
    f.write('\n\n' + str(calculated_bmi_data))
    f.write('\n\n' + str(count_dict))
    f.write('\n\nCount of total number of Overweight people is ' + str(overweight_people) )

    



