import itchat
from tuling import getResponse

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)
    responseinfo = getResponse(msg["Text"])
    if "url" in responseinfo:
        return responseinfo["text"] + responseinfo["url"]
    else:
        return responseinfo["text"]    

itchat.auto_login(enableCmdQR=True)
itchat.run()