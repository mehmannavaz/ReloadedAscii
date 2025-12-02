# Simple test
```python
In [10]: counter = 0
    ...: for line in Example2.replace("|", "\\").split("\n"):
    ...:     print(" " * counter + line)
    ...:     counter += 1
    ...:

  __________
  \  __  __  \
   \ \  \\  \ \
    \ \__\\__\ \
     \          \
      \__________\
```

# Theory after just round the head
```
  __________  << Here the index 0
  \  __  __  \ << index 1
   \ \  \\  \ \  << index 2
    \ \__\\__\ \  ...
     \          \
      \__________\
```

after that we need a system for -1 to -x to looks like the [3d head](./01-SImpleHead.md)
