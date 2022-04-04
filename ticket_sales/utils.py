from kavenegar import KavenegarAPI, APIException, HTTPException


def send_otp_code(phone, code):
    try:
        api = KavenegarAPI(
            '63692F4778315056363552346E79796C55624C765973447649314859516156705A706557763430634D48513D')
        params = {
            'sender': '10008663',
            'receptor': f'{phone}',
            'message': f'خوش آمدید!\n کد تایید شما: {code}',
        }
        print(code)
        # response = api.sms_send(params)
        # print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


