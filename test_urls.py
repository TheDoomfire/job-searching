from requests_html import HTMLSession

urls = ['https://oak.varbi.com/se/apply/positionquick/640016/?where=1', 
'https://jobs.newyorker.de/se/jobs/sweden?rmpage=apply&rmjob=2965&ref=https%3A%2F%2Farbetsformedlingen.se%2Fplatsbanken%2F&utm_medium=talentech_publishing&utm_source=platsbanken'
]

s = HTMLSession()
for url in urls:
    r = s.get(url)
    print(r.html.find('title', first=True).text)