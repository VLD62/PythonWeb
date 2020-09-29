from urllib import parse

SAMPLE_URLS = ['http://mysite.com:80/demo/index.aspx', 'https://my-site.bg',
               'https://mysite.bg/demo/search?id=22o#go', 'https://mysite:80/demo/index.aspx',
               'somesite.com:80/search?', 'https/mysite.bg?id=2', 'http://softuni.bg/',
               'https://softuni.bg:447/search?Query=pesho&Users=true#go', 'http://google:443/']


def get_host(netloc):
    if ':' in netloc:
        return netloc.split(':')[0]
    else:
        return netloc


def get_port(netloc, scheme):
    scheme_to_port_map = {
        'http': 80,
        'https': 443,
    }
    result = None
    if ':' in netloc:
        result = int(netloc.split(':')[1])
        if scheme == 'http' and result > 100:
            result = None
        elif scheme == 'https' and 440 > result < 450:
            result = None
    else:
        if scheme == 'http':
            result = 80
        elif scheme == 'https':
            result = 443
    return result


def validate_url(url):
    components = parse.urlparse(url)
    result = {
        'Protocol': components.scheme,
        'Host': get_host(components.netloc),
        'Port': get_port(components.netloc, components.scheme),
        'Path': components.path if components.path else '/',
        'Query': components.query,
        'Fragment': components.fragment,

    }
    if result['Protocol'] and result['Host'] and result['Port']:
        print(result)
    else:
        print('Invalid URL')


for url in SAMPLE_URLS:
    validate_url(url)
