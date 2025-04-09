# 实验报告 - Pandas 数据操作练习

## 一、实验目的
阐述本次实验的主要目的，可参考任务目的部分。

## 二、实验步骤
详细描述你完成每个任务的步骤和方法，可结合代码进行说明。

### 任务 1: 读取数据
说明你使用的读取数据的函数和过程。


def load_data():
    
    """任务1: 读取数据文件"""
    
    return pd.read_csv('/home/victor-shao/桌面/data/data.csv')


### 任务 2: 查看数据基本信息
描述如何查看数据的基本信息。

def show_basic_info(data):
    
    """任务2: 显示数据基本信息"""
    
    print("数据基本信息：")
    
    data.info()

### 任务 3: 处理缺失值
说明你找出缺失值列和填充缺失值的方法。

def handle_missing_values(data):
    
    """任务3: 处理缺失值"""
    
    missing_columns = data.columns[data.isnull().any()].tolist()
    
    for col in missing_columns:
    
        if pd.api.types.is_numeric_dtype(data[col]):
        
            data[col] = data[col].fillna(data[col].mean())
    
    return data

### 任务 4: 数据统计分析
说明你计算数值列均值、中位数和标准差的方法。

def analyze_statistics(data):

    """任务4: 统计分析数值列"""
    
    numeric_columns = data.select_dtypes(include=['number']).columns
    
    for col in numeric_columns:
    
        mean_value = data[col].mean()
        
        median_value = data[col].median()
        
        std_value = data[col].std()
        
        print(f"{col} 列的均值: {mean_value}, 中位数: {median_value}, 标准差: {std_value}")

### 任务 5: 数据可视化
描述你选择的数值列和绘制直方图的过程。

def visualize_data(data, column_name='成绩'):

    """任务5: 数据可视化"""
    
    data[column_name].plot.hist()
    
    plt.show()

### 任务 6: 数据保存
说明你保存处理后数据的方法。

def save_processed_data(data):

    """任务6: 保存处理后的数据"""
    
    data.to_csv('processed_data.csv', index=False)

## 三、实验结果
展示每个任务的结果，可使用表格或图表进行呈现。

### 任务 1: 读取数据
展示读取的数据的基本信息（如列名、行数等）。
4列4行

### 任务 2: 查看数据基本信息
粘贴数据的基本信息输出。
![截图 2025-04-09 20-51-49](https://github.com/user-attachments/assets/2b7425d6-f0ea-446a-80b0-2be487c9f987)



def load_data():
    """任务1: 读取数据文件"""
    return pd.read_csv('/home/victor-shao/桌面/data/data.csv')

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("数据基本信息：")
    data.info()

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    missing_columns = data.columns[data.isnull().any()].tolist()
    for col in missing_columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            data[col] = data[col].fillna(data[col].mean())
    return data

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    numeric_columns = data.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        mean_value = data[col].mean()
        median_value = data[col].median()
        std_value = data[col].std()
        print(f"{col} 列的均值: {mean_value}, 中位数: {median_value}, 标准差: {std_value}")

def visualize_data(data, column_name='成绩'):
    """任务5: 数据可视化"""
    data[column_name].plot.hist()
    plt.show()

def save_processed_data(data):
    """任务6: 保存处理后的数据"""
    data.to_csv('processed_data.csv', index=False)

def main():
    """主函数，执行所有数据处理流程"""
    # 1. 读取数据
    data = load_data()
    
    # 2. 显示基本信息
    show_basic_info(data)
    
    # 3. 处理缺失值
    processed_data = handle_missing_values(data.copy())
    
    # 4. 统计分析
    analyze_statistics(processed_data)
    
    # 6. 数据可视化
    visualize_data(processed_data)
    
    # 7. 保存处理后的数据
    save_processed_data(processed_data)

if __name__ == "__main__":
    main()
utational physics.py…]()


### 任务 3: 处理缺失值
以平均值代替缺失值

### 任务 4: 数据统计分析
列出数值列的均值、中位数和标准差。
年龄均值26.25 中位数26.25 标准差3.0310889
成绩均值86.8  中位数88    标准差5.2273320


### 任务 5: 数据可视化
![Figure_1](https://github.com/user-attachments/assets/2153ba5b-e191-4894-a06a-43d244613c11)

### 任务 6: 数据保存
说明保存的文件路径和文件名。
processed_data.csv
