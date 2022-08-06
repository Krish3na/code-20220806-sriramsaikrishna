from bmi.bmi_calculator_test import BMI_Calculator_Test
from bmi.bmi_calculator import BMI_Calculator, print_file_data, get_json_column, visualize_data

test_data = 'input/test_data.json'
bmi_table = 'input/bmi_table.json'
expected_data = 'output/expected_data.json'

# initializing BMI_Calculator_Test object
test_bmi_calculator = BMI_Calculator_Test(test_data, expected_data, bmi_table)

# testing calculate_bmi method of BMI_Calculator class
test_bmi_calculator.calculate_bmi_test()

# testing count_category method of BMI_Calculator class
test_bmi_calculator.count_category_test('BMI Category')


# visualizing the count of people falling under several categories using BMI Category and specific count of each category
bmi_calculator = BMI_Calculator()
# reading input data
data = bmi_calculator.read_data(test_data)
print(data)
# calculating 'BMI', 'BMI Category', 'Health risk' of input data
calculated_bmi_data  = bmi_calculator.calculate_bmi('WeightKg', 'HeightCm', bmi_table)

# getting the list of categories
categories_list = list(get_json_column(bmi_table, 'BMI Category'))
# dictionary to store category and it's count
count_dict = {}

# finding the count of each category
for category in categories_list:
    count_dict[category] = int(bmi_calculator.count_category('BMI Category', category))

print(count_dict)

# visualizing the 'BMI Category' categories and the count of people falling under those categories
visualize_data(count_dict, 'output/test_data_bar_chart.png', 'Count of People', 'BMI Categories', 'BMI Categories (vs) Count')

