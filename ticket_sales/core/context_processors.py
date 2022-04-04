from site_settings.models import SiteSetting


def site_settings(request):
    site_setting = SiteSetting.load()
    return {
        'site_settings': site_setting,
    }
