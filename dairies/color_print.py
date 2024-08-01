import pandas as pd

# CSV 파일 경로를 지정합니다
csv_file_path = "data.csv"

# CSV 파일을 데이터프레임으로 읽어옵니다
df = pd.read_csv(csv_file_path)

# 감정분류에서 유일한 값들을 추출합니다
unique_emotion_categories = ['슬픔', '기쁨', '사랑', '분노', '감사', '공포']
#긍정 부정 dataframe 찢기
positive_words_df = df[df['긍정부정'] == '긍정']
negative_words_df = df[df['긍정부정'] == '부정']

#색 도출 logic
def emotion_category_to_color(category, brightness_percentage):
    """
    Maps an emotion category to a specific color and applies brightness percentage.
    """
    if category == '슬픔':
        base_color = (0, 0, 255)  # 파란색
    elif category == '사랑':
        base_color = (255, 0, 0)  # 빨간색
    elif category == '분노':
        base_color = (0, 0, 0)  # 검은색
    elif category == '기쁨':
        base_color = (255, 255, 0)  # 노란색
    elif category == '감사':
        base_color = (255, 165, 0)  # 오렌지색
    elif category == '공포':
        base_color = (128, 128, 128)  # 회색

    # 명도 비율 적용 (각 채널에 비율을 곱함)
    brightness_ratio = brightness_percentage / 100
    adjusted_color = tuple(int(channel * brightness_ratio) for channel in base_color)

    return adjusted_color

#감정분류 빈도{}, color 도출
def analyze_emotions_using_words_df1(user_input):
    # 사용자 입력을 리스트로 변환
    #selected_emotions = [emotion.strip() for emotion in user_input.split(',')]
    selected_emotions=user_input
    
    # 감정분류별로 키워드를 분류
    category_counts = {category: 0 for category in unique_emotion_categories}

    # 각 키워드의 감정분류 확인 및 개수 세기
    total_count = 0
    for emotion in selected_emotions:
        matches = df[df['단어'] == emotion]
        if not matches.empty:
            for category in matches['감정범주'].unique():
                category_counts[category] += 1
                total_count += 1
        else:
            pass
            #print(f"{emotion}: 해당하는 감정 키워드가 없습니다.")

    # 가장 많은 키워드가 속한 감정분류 찾기
    max_category = max(category_counts, key=category_counts.get) #가장 많이 선택된 감정분류
    max_count = category_counts[max_category] #그 개수
    max_ratio = (max_count / total_count) * 100 if total_count > 0 else 0 #그 색조의 명도 결정

    #print(f"\n가장 많은 키워드가 속한 감정분류: {max_category}")

    # 해당 감정분류의 색상
    color = emotion_category_to_color(max_category, max_ratio)
    #print(f"{max_category}의 색상 (명도 비율 적용): {color}")

    return category_counts, color #카테고리 빈도 집계{}, 색조+명도 도출



#긍정/부정 명도 회색 도출
def analyze_emotions_using_words_df2(user_input):
    # 사용자 입력을 리스트로 변환
    selected_emotions =user_input

    # 각 키워드의 긍정/부정 여부 확인 및 개수 세기
    negative_emotions = negative_words_df['단어'].tolist()
    positive_emotions = positive_words_df['단어'].tolist()

    num_negative_selected = sum(1 for emotion in selected_emotions if emotion in negative_emotions)
    num_positive_selected = sum(1 for emotion in selected_emotions if emotion in positive_emotions)

    
    # 각 키워드의 긍정/부정 여부 출력
    '''
    print("\n각 키워드의 긍정/부정 여부:")
    for emotion in selected_emotions:
        if emotion in negative_emotions:
            print(f"{emotion}: 부정")
        elif emotion in positive_emotions:
            print(f"{emotion}: 긍정")
        else:
            print(f"{emotion}: 해당하는 감정 키워드가 없습니다.")
    '''

    # 사용자가 고른 키워드 개수 출력
    total_selected = len(selected_emotions)
    total_negative_ratio = (num_negative_selected / total_selected) * 100 if total_selected > 0 else 0
    total_positive_ratio = (num_positive_selected / total_selected) * 100 if total_selected > 0 else 0

    # 최종 점수 계산
    overall_score = (total_positive_ratio - total_negative_ratio + 100) / 2

    #print(f"\n내가 입력한 키워드 개수: {total_selected}개")
    #print(f"사용자가 고른 긍정 감정 키워드 개수: {num_positive_selected}개")
    #print(f"사용자가 고른 부정 감정 키워드 개수: {num_negative_selected}개")
    #print(f"사용자가 고른 키워드 중 부정 비율: {total_negative_ratio:.2f} %")
    #print(f"사용자가 고른 키워드 중 긍정 비율: {total_positive_ratio:.2f} %")
    #print(f"전체 감정 점수: {overall_score:.2f} % (0%: 가장 부정적, 100%: 가장 긍정적)")

    gray_value = int((overall_score / 100) * 255)
    return (gray_value, gray_value, gray_value)  #긍정/부정 명도색

def rgb_to_hex(rgb):
    return '#{:02X}{:02X}{:02X}'.format(rgb[0], rgb[1], rgb[2])