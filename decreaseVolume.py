import requests
from lib.config import get_domain, api_issues


def get_volume(session):
    try:
        return session.get(get_domain() + 'getVolume').text
    except:
        api_issues()


def decrease_volume(session, volume):
    try:
        volume = (int(volume) - 10)
        return session.post(get_domain() + 'setVolume', data={'volume': volume})
    except:
        api_issues()


def main():
    session = requests.session()

    volume = get_volume(session)
    decrease_volume(session, volume)

    session.close()


main()
