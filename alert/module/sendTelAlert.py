from qcloudsms_py import TtsVoiceSender
from qcloudsms_py.httpclient import HTTPError
import config


def callPhone(params, phoneList):
    global result
    tvsender = TtsVoiceSender(config.appid, config.appkey)
    try:
        for phone in phoneList:
            print(phone)
            print(params)
            result = tvsender.send(config.template_id, [params], phone,
                                   nationcode="86", playtimes=2, ext="")
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
    return result
