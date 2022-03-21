from datetime import datetime

input_format = '%Y-%m-%d %H:%M:%S'
output_format = '%A %d %b %Y, %I:%M:%S %p'
class DateFormat:
    def __call__(self, form_in='%Y-%m-%d %H:%M:%S', form_out='%A %d %b %Y, %I:%M:%S %p'):
        input_format = form_in
        output_format = form_out

    @classmethod
    def format_date(cls, strdate):
        dt = datetime.strptime(str(strdate), input_format)
        return dt.strftime(output_format)
