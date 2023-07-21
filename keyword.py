##

import pandas as pd
import numpy as np

# 設定要搜尋的特定字詞
search_word = 'ABC'

# 讀取Excel檔案
df = pd.read_excel('/Users/mei/Desktop/record/truncated_ramRAs/keyword_filtered/L1007vsOURS.xlsx')

# 將含有缺失值的列刪除或填入特定值
df.dropna(subset=['Gene_Desc'], inplace=True)
# 或
# df.fillna(value='', inplace=True)

# 搜尋包含特定字詞的列
filtered_df = df[df['Gene_Desc'].str.contains(search_word, na=False)]

# 將符合條件的整列資料寫入新的Excel檔案中，檔案名稱為特定字詞
filtered_df.to_excel(f'/Users/mei/Desktop/record/truncated_ramRAs/keyword_filtered/{search_word}.xlsx', index=False)

