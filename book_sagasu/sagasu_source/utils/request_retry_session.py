import requests
import functools
from requests.adapters import HTTPAdapter,Retry


def requests_retry_session(
        retries=1,
        backoff_factor=2,
        status_forcelist=(500, 502, 503, 504),
        session=None,
        ) -> requests.Session:
    session = session or requests.Session()
    retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    # set default timeout
    for method in ('get', 'options', 'head', 'post', 'put', 'patch', 'delete'):
        setattr(session, method, functools.partial(getattr(session, method), timeout=30))
    return session