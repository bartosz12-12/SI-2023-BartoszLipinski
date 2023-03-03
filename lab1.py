import numpy as np
import pandas as pd
# 3)
diabetes = np.loadtxt("australian.txt")
diabetes_type = np.loadtxt("australian-type.txt", dtype=str)


# a)
# print(np.unique(diabetes[:, -1]))

# # b)
# print(len(diabetes))
# #
# # # c)
# for i in range(len(diabetes[0,:])):
#     print(i, "min = ", np.min(diabetes[:, i]))
#     print(i, "max = ", np.max(diabetes[:, i]))
#
# # d)
# for i in range(len(diabetes[0,:])):
#     print(i,len(np.unique(diabetes[:, i])))
#
# e)
# for i in range(len(diabetes[0,:])-1):
#     print(i, np.unique(diabetes[:, i]))
#
# # f)
# for i in range(len(diabetes[0,:])):
#     print(i, np.std(diabetes[:, i]))

# zad 4
# a
# file_data1 = np.loadtxt("australian.txt", dtype=str)
# file_data = file_data1.copy()
#
# attribute_2 = np.loadtxt("australian.txt", dtype=float, usecols=1)
# average_val = np.mean(attribute_2)
#
# ten_percent = int(0.1*len(file_data))
# r = np.random.choice(range(len(attribute_2)), ten_percent, replace=False)
#
# attribute_2 = np.asarray(attribute_2, dtype=str)
# for r in r:
#     attribute_2[r] = "?"
#
# # print("\n", attribute_2)  # attribute 2 with 10% unknown values
#
# for x in range(len(attribute_2)):
#     if attribute_2[x] == "?":
#         attribute_2[x] = average_val
#
# attribute_2 = np.asarray(attribute_2, dtype=float)
# print("\n", attribute_2)  # attribute 2 with unknown values changed to average value



# b
# file = "australian.txt"
# file_data1 = np.loadtxt(file, dtype=str)
# file_data = file_data1.copy()
#
# x=len(file_data1[0,:])-1
#
# numeric_attributes2 = np.loadtxt(file, dtype=float, usecols=1)
# numeric_attributes9 = np.loadtxt(file, dtype=float, usecols=x)
#
# min_a2 = min(numeric_attributes2)
# max_a2 = max(numeric_attributes2)
# min_a9 = min(numeric_attributes9)
# max_a9 = max(numeric_attributes9)
#
# norm1_att_2 = np.empty(shape=numeric_attributes2.shape)
# norm2_att_2 = np.empty(shape=numeric_attributes2.shape)
# norm3_att_2 = np.empty(shape=numeric_attributes2.shape)
#
# norm1_att_9 = np.empty(shape=numeric_attributes2.shape)
# norm2_att_9 = np.empty(shape=numeric_attributes2.shape)
# norm3_att_9 = np.empty(shape=numeric_attributes2.shape)
#
# for i in range(len(numeric_attributes2)):
#     norm1_att_2[i] = ((numeric_attributes2[i]-min_a2)*(1+1) / (max_a2 - min_a2)) - 1
#     norm2_att_2[i] = ((numeric_attributes2[i]-min_a2) * 1 / (max_a2 - min_a2))
#     norm3_att_2[i] = ((numeric_attributes2[i]-min_a2)*(10+10) / (max_a2 - min_a2)) - 10
#
#     norm1_att_9[i] = ((numeric_attributes9[i]-min_a9)*(1+1) / (max_a9 - min_a9)) - 1
#     norm2_att_9[i] = ((numeric_attributes9[i]-min_a9) * 1 / (max_a9 - min_a9))
#     norm3_att_9[i] = ((numeric_attributes9[i]-min_a9)*(10+10) / (max_a9 - min_a9)) - 10
#
#
# print("\nattribute 2 normalized into intervals <-1,1> : \n")
# print(norm1_att_2)
# print("\n\nattribute 2 normalized into intervals <0,1> : \n")
# print(norm2_att_2)
# print("\n\nattribute 2 normalized into intervals <-10,10> : \n")
# print(norm3_att_2)
#
# print("\nattribute 9 normalized into intervals <-1,1> : \n")
# print(norm1_att_9)
# print("\n\nattribute 9 normalized into intervals <0,1> : \n")
# print(norm2_att_9)
# print("\n\nattribute 9 normalized into intervals <-10,10> : \n")
# print(norm3_att_9)



# c
# file_data1 = np.loadtxt("australian.txt", dtype=str)
# file_data = file_data1.copy()
# x=len(file_data1[0,:])-1
#
# numeric_attributes2 = np.loadtxt("australian.txt", dtype=float, usecols=1)
# numeric_attributes9 = np.loadtxt("australian.txt", dtype=float, usecols=x)
# standarized2 = np.empty(shape=numeric_attributes2.shape)
# standarized9 = np.empty(shape=numeric_attributes9.shape)
# variance2 = np.empty(shape=numeric_attributes2.shape)
# variance9 = np.empty(shape=numeric_attributes9.shape)
#
# mean2 = round(sum(numeric_attributes2) / len(numeric_attributes2), 2)
# mean9 = round(sum(numeric_attributes9) / len(numeric_attributes9), 2)
#
# for i in range(len(numeric_attributes2)):
#     variance2[i] = pow(numeric_attributes2[i] - mean2, 2)
#     variance9[i] = pow(numeric_attributes9[i] - mean9, 2)
#
# #sum of variance values
# var2 = round(sum(variance2), 2)
# var9 = round(sum(variance9), 2)
#
# for i in range(len(numeric_attributes2)):
#     standarized2[i] = round((numeric_attributes2[i] - mean2) / var2, 2)
#     standarized9[i] = round((numeric_attributes9[i] - mean9) / var9, 2)
#
#
# print("\n\nStandarized values of attribute 2: ")
# print("\n", standarized2)
#
# print("\n\nStandarized values of attribute 9: ")
# print("\n", standarized9)
#


# d
file = "Churn_Modelling.csv"
df = pd.read_csv(file, index_col=0)
print(df.head().to_string())

df_dummied = pd.get_dummies(df, columns=['Geography'])
df_dummied.drop('Geography_Germany', inplace=True, axis=1)
print("\n\n")
print(df_dummied.head().to_string())  # displays 5 first rows, with dummy variables, without the 'Germany' variable
