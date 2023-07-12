import os
import openai
import argparse
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv('OPENAI_API_KEY')

def call_openai_api(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 모델 선택
        messages=messages
    )
    return response.choices[0].message['content']

def main():
    # 명령행 인자 파싱
    parser = argparse.ArgumentParser(description='OpenAI API Chat CLI')
    parser.add_argument('message', help='Messages for the API request')
    parser.add_argument('-s', '--system', help='System "role" for the API request')
    
    args = parser.parse_args()
    messages = []

    if (args.system != None):
        messages.append({'role': 'system', 'content': args.system})

    # 사용자가 입력한 메시지를 추가
    messages.append({'role': 'user', 'content': args.message})
    # OpenAI API 호출
    response = call_openai_api(messages)

    print(response)

if __name__ == '__main__':
    main()