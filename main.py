from pyquery import PyQuery as pq
import requests

def cnblogParse(shortName):
    srcCode = requests.get(f'https://cnblogs.com/{shortName}').text
    # JX #
    jx = pq(srcCode)
    content = jx('div #main #mainContent .forFlow .day').items()
    for i in content:
        print(f"""===================
{i.text()}

文章链接：{i('.dayTitle a').attr('href')}
===================

""")

print(cnblogParse('hblthink'))
