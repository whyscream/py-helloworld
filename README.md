# Hello world

Hello world is a minimal example project to document how to add various parts to a basic Python project.

## The `helloworld` program

The `helloworld` program implements a few very simple functionalities.

1. A package with an importable method that you can use from other Python code:

```Python
>>> from helloworld import hello
>>> hello()
'Hello world!'
>>> hello("John")
'Hello John!'
>>>
```

2. A commandline script that executes the hello function:

```shell
$ pip install .
[...]
Successfully installed helloworld-0.0.0
$ hello
Hello world!
$ hello John
Hello John!
```

3. A python module that can be executed using Python from the commandline:

```shell
$ pip install .
[...]
Successfully installed helloworld-0.0.0
$ python -m helloworld
Hello world!
$ python -m helloworld John
Hello John!
```

## Building a pip package

The `pyproject.toml` defines a build system, so you can actually build this into an installable pip package.

```shell
$ pip install build
[...]
Successfully installed build-1.1.1 pyproject_hooks-1.0.0
$ python -m build
[...]
Successfully built helloworld-0.0.0.tar.gz and helloworld-0.0.0-py3-none-any.whl
$ ls dist/
helloworld-0.0.0-py3-none-any.whl  helloworld-0.0.0.tar.gz
$ pip install ./dist/helloworld-0.0.0-py3-none-any.whl
[...]
Successfully installed helloworld-0.0.0
```
