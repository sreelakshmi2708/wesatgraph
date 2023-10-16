import pandas as pd
import matplotlib.pyplot as plt
import csv

input_file_path = 'C:/Users/sreel/OneDrive/Desktop/SREE/var2/dummy1.csv'
output_csv_file_path = 'C:/Users/sreel/OneDrive/Desktop/SREE/var2/Average.csv'
file1 = pd.read_csv(input_file_path)

average = []
for i in range(0, len(file1), 60):
    data_to_average = file1.iloc[i:i + 60, 2]
    avg = data_to_average.mean()
    average.append(avg)
    
data_dict_list = [{'average': avg} for avg in average]

with open(output_csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['average']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_dict_list)

file2 = pd.read_csv(output_csv_file_path)

x = []
for j in range(0, len(file1), 60):
    temp = file1.iloc[j, 1]
    x.append(temp)
    
plt.plot(x, file2['average'], label='Average Line', color='g')
plt.title('Average Data Plot')
plt.xlabel('Time')
plt.ylabel('Average')
plt.legend()
plt.show()
