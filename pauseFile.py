import requests
from lib.config import get_domain, api_issues


def get_file_name(session):
    try:
        return session.get(get_domain() + 'getPlaying').text
    except:
        api_issues()


def set_paused(session, fileName, string):
    try:
        print(string + ' ' + fileName)
        return session.post(get_domain() + 'setPaused', data={'fileName': fileName})
    except:
        api_issues()


def is_paused(session):
    try:
        return session.get(get_domain() + 'isPaused').text
    except:
        api_issues()


def main():
    session = requests.session()
    fileName = get_file_name(session)
    paused = is_paused(session)

    if paused == 'true':
        set_paused(session, fileName, 'Unpaused')
    else:
        set_paused(session, fileName, 'Paused')

    session.close()


main()
