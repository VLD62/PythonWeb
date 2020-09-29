from urllib import parse

TEST_URLS = ['http://www.google.bg/search?q=C%23',
             'https://mysite.com/show?n%40m3= p3%24h0',
             'http://url-decoder.com/i%23de%25?id=23',
             ]


def decode(encoded_url):
    return parse.unquote(encoded_url)


def test(test_urls):
    return [decode(url) for url in test_urls]


test_result = test(TEST_URLS)
print(test_result)
