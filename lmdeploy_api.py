from lmdeploy.serve.openai.api_client import APIClient
server_ip = '127.0.0.1'
server_port = 23333
api_client = APIClient(f'http://{server_ip}:{server_port}')
def chat():
    model_name = api_client.available_models[0]
    messages = [{"role": "user", "content": "你是谁"}]
    for item in api_client.chat_completions_v1(model=model_name, messages=messages):
        print(item)


def interactive():
    messages = [
        "你是谁",
        "北京奥运会哪一年举办的",
        "我今年30岁，有点胖，有什么建议",
        "我多少岁了"
    ]
    for message in messages:
        for item in api_client.chat_interactive_v1(prompt=message,
                                                session_id=1,
                                                interactive_mode=True,
                                                stream=False):
            print(item)

if __name__ == "__main__":
    interactive()