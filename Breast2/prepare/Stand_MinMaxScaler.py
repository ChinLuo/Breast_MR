import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def Stand_MinMaxScaler(input_path, output_path):

    # 读取CSV文件
    data = pd.read_csv(input_path)

    # 提取特征列
    features = data.drop('Name', axis=1)

    # 初始化标准化器
    scaler_standard = StandardScaler()

    # 对特征进行标准化
    scaled_features = scaler_standard.fit_transform(features)

    # 将标准化后的特征重新添加到原始DataFrame中
    scaled_data = pd.DataFrame(scaled_features, columns=features.columns)
    scaled_data.insert(0, 'Name', data['Name'])

    # 初始化归一化器
    scaler_minmax = MinMaxScaler()

    # 对标准化后的特征进行归一化
    normalized_features = scaler_minmax.fit_transform(scaled_data.drop('Name', axis=1))

    # 将归一化后的特征重新添加到DataFrame中
    normalized_data = pd.DataFrame(normalized_features, columns=features.columns)
    normalized_data.insert(0, 'Name', data['Name'])

    # 定义处理后的文件路径
    output_file = output_path

    # 将处理后的数据保存到CSV文件中
    normalized_data.to_csv(output_file, index=False)

    # 打印成功信息
    print("数据已经成功标准化和归一化，并保存到文件:", output_file)

input_path = r"C:\Users\Administrator\Desktop\Breast\benignDCE_T2.csv"
output_path = r'C:\Users\Administrator\Desktop\Breast\benignDCET2_Stand_MinMaxScaler.csv'
Stand_MinMaxScaler(input_path, output_path)
print('良性数据已完成标准化和归一化。')
input_path = r"C:\Users\Administrator\Desktop\Breast\malignantDCE_T2.csv"
output_path = r'C:\Users\Administrator\Desktop\Breast\malignantDCET2_Stand_MinMaxScaler.csv'
Stand_MinMaxScaler(input_path, output_path)
print('恶性数据已完成标准化和归一化。')