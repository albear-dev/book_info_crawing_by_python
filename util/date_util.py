from datetime import date, datetime, timedelta


class DateUtil:

    @classmethod
    def get_prev_ym(cls):
        today = date.today()
        month_ago = today.replace(day=1) - timedelta(days=1)
        year = str(month_ago.year)
        month = str(month_ago.month)
        return month_ago.strftime('%Y%m')+"0"

    @classmethod
    def get_prev_ymd(cls):
        yesterday = date.today() - timedelta(1)
        return yesterday.strftime('%Y%m%d')