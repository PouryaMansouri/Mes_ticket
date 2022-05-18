from kavenegar import KavenegarAPI, APIException, HTTPException

from site_settings.models import SiteSetting


# todo: in function age taske celery bashe performancesh behtare
def send_successful_ticket_sms(phone, national_code):
    site_setting = SiteSetting.load()
    print(national_code)
    if site_setting and site_setting.kavenegar_sender and site_setting.kavenegar_api_key:
        try:
            api = KavenegarAPI(site_setting.kavenegar_api_key)
            params = {
                'sender': site_setting.kavenegar_sender,
                'receptor': f'{phone}',
                'message': f'سلام هوادار گرامی\nبلیط شما برای بازی مس-ملوان با کدملی {national_code} در تاریخ ۵ اردیبهشت رزرو گردید.\nلطفا در هنگام ورود کارت ملی و کارت واکسن همراه داشته باشید.\nاز ورود شما بدون کارت واکسن جلوگیری میشود.',
            }
            response = api.sms_send(params)
            # todo: uncomment upper line
            # print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)


def change_jajali_time_to_string(time):
    res = time.strftime("%Y %m %d")
    res = res.split()
    year = res[0]
    month = res[1]
    day = res[2]
    month_dict = {
        '01': "فروردین", '02': "اردیبهشت", '03': "خرداد", '04': "تیر", '05': "مرداد", '06': "شهریور",
        '07': "مهر", '08': "آبان", '09': "آذر", '10': "دی", '11': "بهمن", '12': "اسفند",
    }
    day_dict = {
        '01': 'یکم', '02': 'دوم', '03': 'سوم', '04': 'چهارم', '05': 'پنجم', '06': 'ششم', '07': 'هفتم', '08': 'هشتم',
        '09': 'نهم', '10': 'دهم', '11': 'یازدهم', '12': 'دوازدهم', '13': 'سیزدهم', '14': 'چهاردهم', '15': 'پانزدهم',
        '16': 'شانزدهم', '17': 'هفدهم', '18': 'هجدهم', '19': 'نوزدهم', '20': 'بیستم', '21': 'بیست و یکم',
        '22': 'بیست و دوم', '23': 'بیست و سوم','24': 'بیست و چهارم', '25': 'بیست و پنجم', '26': 'بیست و ششم',
        '27': 'بیست و هفتم', '28': 'بیست و هشتم', '29': 'بیست و نهم', '30': 'سی ام','31': 'سی و یکم'
    }
    day = day_dict[day]
    month = month_dict[month]
    return f" {day} {month} {year}"
