# pylint: disable=pointless-string-statement
"""
EXERCISE 3: HTTP Response
------------------------

The class `Response` mocks an HTTP Response, which contains a
    `status_code` and a `content`, which is a dict or a string.

`process_response` converts `Response` objects to user-friendly message.

* Implement `process_response` so that it returns:
    For `status_code` 401 or 403:
        - 'Bad username/password combination.' for `bad_user` or `bad_password` errors.
        - f'Unknown error - {err}.', where `err` is the error code.
        - f'Can not process content {response.content}.' if none of the above.
    For `status_code` 200:
        - `response.content`
    Otherwise:
        - f'Can not process content {response.content}.' if none of the above.

HINT: The `assert` statements at the bottom of this file will contain the expected
    output as well.
"""

class Response:
    """An HTTP Response mock class."""
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    def __str__(self) -> str:
        return f'{self.status_code}, {self.content}'


def process_response(response: Response):
    """Processes a Response object and returns a user-friendly message."""
    # TODO: Implement `process_response`


if __name__ == '__main__':
    bad_user = Response(401, {'error': 'bad_user'})
    bad_pass = Response(403, {'error': 'bad_password'})
    other_err = Response(401, {'error': 'unauthorized'})
    success = Response(200, 'Login successful.')
    timeout = Response(504, 'gateway timeout')
    unknown_content = Response(
        401, '<Error><Message>Unknown error, please retry.</Message></Error>'
    )

    assert (resp := process_response(bad_user)) == 'Bad username/password combination.', (
        f'wrong output for {bad_user} - {resp}'
    )
    assert (resp := process_response(bad_pass)) == 'Bad username/password combination.', (
        f'wrong output for {bad_pass} - {resp}'
    )
    assert (resp := process_response(other_err)) == 'Unknown error - unauthorized.', (
        f'wrong output for {other_err} - {resp}'
    )
    assert (resp := process_response(success)) == success.content, (
        f'wrong output for {success} - {resp}'
    )
    assert (resp := process_response(timeout)) == f'Can not process content {timeout.content}.', (
        f'wrong output for {timeout} - {resp}'
    )
    assert (resp := process_response(unknown_content)) == \
          f'Can not process content {unknown_content.content}.', (
        f"wrong output for {unknown_content} - {resp}"
    )

    print('process_response works as expected.')
