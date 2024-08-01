import pandas as pd

# 엑셀 파일 경로를 지정합니다
file_path = r"C:\Users\choiy\Documents\카카오톡 받은 파일\감정단어_final_with_sentiment_and_color.xlsx"

# 엑셀 파일을 데이터프레임으로 읽어옵니다
df = pd.read_excel(file_path)
df.to_csv('data.csv', index=False)
