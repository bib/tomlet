# tomlet

Select value(s) for scripts from TOML configurations.

`tomlet -c tests/example.toml One`

> {'one': {'first': 'val-1'}}

`cat tests/example.toml | tomlet Two.two2`

> val-2-2
