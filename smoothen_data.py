## Version 1.0

import matplotlib.pyplot as plt ## This module is used for plotting as we can comprehend the results better if we visualise them.


## This function is to retrieve noisy data from a file. This function assumes that the data is written in columns. I initially configured it to recognize the first column as the time values and the second column as our variable.
def GetTheNoisyData(n):

	f = open("datafile.txt","r") ## Open the file that contains the noisy data and initiate reading mode.

	lines = f.readlines() ## Read the fileline by line.
	time_values = [] ## An empty list to hold the time values.
	the_variable = [] ## An empty list to hold our variable.
	for x in lines: ## Append the read data to our empty lists.
		time_values.append(x.split(' ')[0])
		the_variable.append(x.split(' ')[1])

		f.close() ## Close the file as we are done with it.

	ready_to_process_data = [i.replace('\n','') for i in the_variable] ## Remove the "\n" character from every data point.
	ready_to_process_time = [i.replace('\n','') for i in time_values] ## Remove the "\n" character from every data point.

	print(ready_to_process_time)
	print(ready_to_process_data)

	if (n == 1):
		return ready_to_process_time
	else:
		return ready_to_process_data



## This function is to apply the moving averages method.
def MovingAverages():
	ready_to_process_time = GetTheNoisyData(1)
	ready_to_process_data = GetTheNoisyData(2)

	i = 0 ## Probably not the best way to do this, but I nneded my loop to "count" in some way. I can achieve this using this dummy variable later on.
	averaged_data = [] ## An empty list to hold our averaged data.
	number_of_time_periods = int(input("Enter your desired number of time periods:  ")) ## Different data may need different time periods, so I decided to take an input from the user to make my code more versatile.
	number_data_points = len(ready_to_process_time)
	time_periods = number_data_points / number_of_time_periods

## I really wanted to use a fancy series summation here but I couldn't find a way to do it without using the modules pandas or numpy.
	while i < number_data_points - time_periods + 1:
		current_period = number_data_points[i : i + time_periods]
		period_average = sum(current_period) / time_periods
		averaged_data.append(period_average)
		i += 1 ##

	return averaged_data ## Return the output to optain our averaged data.


def TheoreticalExpectationCalculator():
		theoretical_value_list = []
		for a in range(0, t):
		 individual_theoretical_values = 998 * t + 1234 ## INSERT THE FORMULA HERE ## I have just inserted a dummt function here.

		theoretical_value_list.append(individual_theoretical_values)

		return theoretical_value_list


## Version 0.1 note here ## I am not sure about the usage of the chi square test. I defined this function to return the so called "goodness of fit" attribute for both "theoretical data vs experimental data" and "average data vs experimental data". Don't know if this means anything. I will plot graphs for this regardless.
def ChiSquaredTest():
	ready_to_process_time = GetTheNoisyData(1)
	ready_to_process_data = GetTheNoisyData(2)
	MovingAverages()
	TheoreticalExpectationCalculator()

	chi_squared_for_theovsexp = [] ## Empty list to hold the chi square test data for theoretcial data vs experimental data
	chi_squared_for_avgvsexp = [] ## Empty list to hold the chi square test data for averaged data vs experimental data

	n = len(the_variable) ## "n" is an integer used for the chi square test. It is basically the number of data points.

	## This loop is for theoretical data vs experimental data.
	for i in range(0, n):
		individual_chi_squared_for_theovsexp = (theoretical_value_list[i] - experimental_value[i]) * (theoretical_value_list[i] - experimental_value[i]) / theoretical_value_list[i] ## This is the application of the "goodness of fit" formula for theoretical data vs experimental data.

		chi_squared_for_theovsexp.append(individual_chi_squared_for_theovsexp) ## Add the calculated chi squared test values to the empty list we created above.

    ## This loop is for averaged data vs experimental data.
	for j in range(0, n):
		individual_chi_squared_for_avgvsexp = (averaged_data[j] - experimental_value[j]) * (averaged_data[j] - experimental_value[j]) / averaged_data[j] ## This is the application of the "goodness of fit" formula for averaged data vs experimental data.

		chi_squared_for_avgvsexp.append(individual_chi_squared_for_avgvsexp) ## Add the calculated chi squared test values to the empty list we created above.


	return chi_squared_for_theovsexp ## Return the test results.
	return chi_squared_for_avgvsexp ## Return the test results.

def SubPlots():
	plt.subplot(2,1,1)
	plt.plot(time_values, averaged_data) ## Plot the averaged data.

	plt.subplot(2,1,2)
	plt.plot(time_values, the_variable)

	plt.show() ## Show the plot.



def main():
	ChiSquaredTest()
	SubPlots()

main() ## Execute the whole code using the main() function.
