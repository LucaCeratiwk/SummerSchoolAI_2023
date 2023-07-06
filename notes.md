# Notes for project tutorial and kick-off

## Installations
`pip install python-telegram-bot` not, repeat *not*, ~~`pip install telegram`~~

## Issues and the importance of thinking 
There are some issues at runtime.
We check the documentation [https://docs.python-telegram-bot.org/en/stable/index.html](https://docs.python-telegram-bot.org/en/stable/index.html) and we notice 
> PTB has undergone significant changes in v20. Please read the documentation carefully and also check out the transition guide in the [wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Transition-guide-to-Version-20.0).

This sounds like a :warning: !

The developer knows this is a major break and has provided a "Transition Script"!

Will it work?
Backup the code before any experiment:
```shell
cp test_TFfront_end_bot.py backup_test_TFfront_end_bot.py
```
**Note:** If you have a repo this is not needed. You can always rollback (if you have committed regularly!).

Download the transition script and run it.

It works - sort of.

We need to add `ContextTypes, Application` to the import directive.

## Modifications
`Filters` class does not exist anymore, the import should refer to `filters`.

