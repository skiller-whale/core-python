# pylint: disable=pointless-string-statement
"""
EXERCISE 4: HTTP Response With Types
------------------------

The class `Response` mocks an HTTP Response, which contains a
    `status_code` and a `content`, which is a dict or a string.

`process_response` converts `Response` objects to user-friendly message.

* Start by copying your solution to the previous exercise.
* In addition now there are new rules for `status_code` 200:
    * If `response.content` is of type `str` you should return it.
    * If `response.content` is of type `list` you should return
        a string that concatenates the contents of `response.content`
        separated by a space.

HINT: There are hints at the bottom of this file.
"""

class Response:
    """An HTTP Response mock class."""
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    def __str__(self) -> str:
        return f'{self.status_code}, {self.content}'


def process_response(response):
    """Processes a Response object and returns a user-friendly message."""
    # TODO: Implement `process_response`


if __name__ == '__main__':
    bad_user = Response(401, {'error': 'bad_user'})
    bad_pass = Response(403, {'error': 'bad_password'})
    other_err = Response(401, {'error': 'unauthorized'})
    success = Response(200, 'Login successful.')
    success_2 = Response(200, ['Login', 'successful.'])
    success_3 = Response(200, {'text': 'Login successful.'})
    timeout = Response(504, 'gateway timeout')

    assert (resp :=process_response(bad_user)) == 'Bad username/password combination.', (
        f'wrong output for {bad_user} - {resp}'
    )
    assert (resp :=process_response(bad_pass)) == 'Bad username/password combination.', (
        f'wrong output for {bad_pass} - {resp}'
    )
    assert (resp :=process_response(other_err)) == 'Unknown error - unauthorized.', (
        f'wrong output for {other_err} - {resp}'
    )
    assert (resp :=process_response(success)) == success.content, (
        f'wrong output for {success} - {resp}'
    )
    assert (resp :=process_response(success_2)) == ' '.join(success_2.content), (
        f'wrong output for {success_2} - {resp}'
    )
    assert (resp :=process_response(success_3)) == f'Can not process content {success_3.content}.', (
        f'wrong output for {success_3} - {resp}'
    )
    assert (resp :=process_response(timeout)) == f'Can not process content {timeout.content}.', (
        f'wrong output for {timeout} - {resp}'
    )

    print('process_response works as expected.')
