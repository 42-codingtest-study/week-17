#
# 6841
# I Speak TXTMSG
# https://www.acmicpc.net/problem/6841

def txtmsg(msg):
    msg_map = {
        "CU": "see you",
        ":-)": "I’m happy",
        ":-()": "I’m unhappy",
        ";-)": "wink",
        ":-P": "stick out my tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computing Competition",
        "CUZ": "because",
        "TY": "thank-you",
        "YW": "you’re welcome",
        "TTYL": "talk to you later"
    }

    if msg in msg_map:
        msg = msg_map[msg]

    return msg

while 1:
    try:
        text = input()

        print(txtmsg(text))

        if text == "TTYL":
            exit()
    except:
        break