import urlparse
#import urllib.parse as urlparse

def app(environ, start_response):

        data = dict(urlparse.parse_qsl(environ["QUERY_STRING"]))

        result = [bytes("%s=%s\n" % (x, y), "utf-8") for x, y in data.items()]

        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(sum([len(x) for x in result])))
        ])

        return result
