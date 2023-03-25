import csv
import matplotlib.pyplot as plt

def read_csv(file_name):
    file = open(file_name)
    file_data = csv.reader(file)
    return file_data

def get_time():
    file_data = read_csv('sensor_data_with_noize_6000_samples.csv')
    time_data = []
    for columns in file_data:
        time_data.append(columns[0])
    return time_data
    
def get_encoder_position():
    file_data = read_csv('sensor_data_with_noize_6000_samples.csv')
    encoder_position_data = []
    for columns in file_data:
        encoder_position_data.append(columns[1])
    return encoder_position_data

def convert_scientific_notation_to_float(list_of_data):
    list_of_float_data = []
    for data in list_of_data:
        list_of_float_data.append((float(data)))
    return list_of_float_data

def move_window_and_filter(window_size):
    time_data = get_time()
    encoder_data = get_encoder_position()
    average_filtered_data = []
    for i in range(len(time_data)-window_size):
        window_average=get_window_average(encoder_data,i,window_size)
        average_filtered_data.append(window_average)
    return average_filtered_data

def get_list_average(data):
    sum = 0
    for value in data:
        sum =+ float(value)
    return sum/len(data)

def get_window_average(data,starting_index,window_size):
    window_data = []
    for i in range(starting_index,starting_index+window_size+1):
        window_data.append(data[i])
    window_average=get_list_average(window_data)
    return window_average

def plot_data(time,filtered_y, original_y):   
    plt.subplot(211)
    plt.plot(time, original_y)
    plt.subplot(212)
    plt.plot(time, filtered_y)
    plt.show()
    
filtered_y = move_window_and_filter(1200)
time = convert_scientific_notation_to_float(get_time())[0:len(filtered_y)]
original_y = convert_scientific_notation_to_float(get_encoder_position())[0:len(filtered_y)]
plot_data(time,filtered_y, original_y)