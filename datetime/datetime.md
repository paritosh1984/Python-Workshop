## datetime packge

pip install python-dateutil

>mtime= '2015-01-27T04:07:19Z'
>from dateutil import parser
>date = parser.parse(eventName)
>date
datetime.datetime(2015, 1, 27, 4, 7, 19, tzinfo=tzutc())
>date.month
1
>date.year
2015
