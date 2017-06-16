import http.client


def test_intercepted_api_calls_in_session_log():
    conn = http.client.HTTPConnection("localhost", 8889)
    conn.request("GET", "http://www.httpbin.org/ip")
    response = conn.getresponse()
    content = response.read()
    print(content.decode("utf-8"))
