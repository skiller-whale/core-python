# pylint: disable=pointless-string-statement
"""
EXERCISE 1: MAZE GAME
------------------------

The code below implements a simple game, where the player needs to escape
    from a maze by using their ability called teleport ('use teleport').

The game accepts the following inputs:
    'help' -- prints a help message
    'go <direction>' -- prints a message that the player is still lost
    'ask what is my ability called' -- displays the ability name
    'ask how do i use teleport' -- should print 'Just type 'use teleport''
    'use teleport' -- breaks out of the loop (win condition)

However, there's currently a bug. If you type in this series of commands,
    you can escape the maze (and shouldn't be able to):

```
>>> ask how do i use escape
Just type 'use escape'

>>> use escape
Success! You have escaped.
```

    * Fix the bug so that the player can only escape when typing 'use teleport'.
        Hints are at the bottom of the file.
"""


if __name__ == '__main__':
    print('You are lost in a maze. You must escape!')
    ability_name = 'teleport'

    while user_input := input('>>> '):
        match user_input.lower().split():
            case ['help']:
                # print help message, except how to use ability
                print('Available commands:')
                print('\t go <direction>')
                print('\t ask <question>')
            case ['go', direction]:
                # go doesn't do anything -- still lost in the maze!
                print(f'You went {direction}.')
                print('\t Unfortunately, you are still lost.')
            case ['ask', 'what', 'is', 'my', 'ability', 'called']:
                # print name of ability without how to use it
                print(f'Your ability is called {ability_name}')
            case ['ask', 'how', 'do', 'i', 'use', ability_name]:
                # print how to use ability
                print(f'Just type \'use {ability_name}\'')
            case ['use', ability_name]:
                # win condition
                print('Success! You have escaped.')
                break
            case command:
                # other commands are ignored
                print('I do not understand your command.')


# There are multiple ways you can solve this:
# 1: You can use a string literal (constant) instead of `ability_name`. 
# 2: Instead of a variable, use a custom class `Ability` that has a single attribute called `name`.
