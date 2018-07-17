import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):
    Group('student').add(message.reply_channel)
    Group('student').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True,
            'code': 'console.log("Hello, World!")'
        })
    })


@channel_session_user
def ws_message(message):  # TODO: Send-Data to Correct Group (Group by Room ID) & Check room belongs to him as well
    if message.user.is_authenticated:
        Group("student").send({
            "text": json.dumps({
                'code': message.content['text'].replace("<", "&lt;").replace(">", "&gt;")
            })
        })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('student').discard(message.reply_channel)