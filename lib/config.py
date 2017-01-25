live_domain = 'http://phpcast.local/api/'
development_domain = 'http://localhost/api/'
development = False


def get_domain():
    if development is True:
        return development_domain
    else:
        return live_domain
