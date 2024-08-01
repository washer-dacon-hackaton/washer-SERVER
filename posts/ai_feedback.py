#pip install openai==0.28

import openai

openai.api_key = 'sk-proj-6Oo49M8kYFYwXAW2NXr0T3BlbkFJbTs7i42hDcvOWVBAduqn'
def ai_feedback(text):

#text='title: 나 오늘 혼자 산책하다가\n content : 노래들으려고 보니까 에어팟 충전 만땅이어서 기분 좋음'
    # 초기 시스템 메시지: 상담사의 역할을 부여합니다
    system_message = {
        "role": "system",
        "content": "당신은 친절하고 공감하는 상담사입니다. 사용자에게 격려와 지지를 제공하고, 그들의 문제를 이해하며 적절한 조언을 주는 역할을 합니다. 사용자의 행복게시글의 제목, 내용을 보고 적절한 피드백을 합니다."
        }
    messages = [system_message]
    messages.append({"role": "user", "content": text })
    # Use openai.ChatCompletion.create() directly
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )

    chat_response = completion.choices[0].message.content
    print(f"ChatGPT: {chat_response}")
    return chat_response