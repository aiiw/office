from imbox import Imbox
import keyring
pwd = keyring.get_password("163", "aliaiiw@163.com")
print(pwd)

with Imbox('imap.163.com', 'aliaiiw@163.com', pwd, ssl=True) as imbox:
    all_inbox_messages = imbox.messages(unread=True)
    # for uid,message in all_inbox_messages:
    #     print(message.subject)
    #     print(message.body["plain"])


##未成功,如上代码