import verify

image_mimes = ['image/gif', 'image/jpeg', 'image/png']

# Now setup verifya
v = verify.CheckImage('./hashes.txt')

sicko = open('./res/sicko.jpg', 'rb').read()


def response(flow):
    if 'Content-Type' in flow.response.headers and flow.response.headers['Content-Type'] in image_mimes:
        result = v.check_stream(flow.response.get_content())
        if result:
            flow.response.content = sicko
