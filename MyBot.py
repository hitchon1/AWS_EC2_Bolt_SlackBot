from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from openai import OpenAI

client2 = OpenAI()



app = App(token="xoxb-FIND YOUR BOT CODE")

@app.event("app_mention")
def hello_command(ack, body, say, client):
    message = str(body['event']['blocks'][0]['elements'][0]['elements'][1]['text'])
    completion = client2.chat.completions.create(
        model="gpt-3.5-turbo",
            messages=[
        {"role": "system", "content": "You are SuperBot you are like the superman of AI and love to help people your favorite color is blue"},
        {"role": "user", "content": message}
            ]
    
    )

    say(str(completion.choices[0].message.content))


if __name__ == "__main__":
    SocketModeHandler(app, "xapp-FIND YOUR SOCKET MODE CODE").start()
