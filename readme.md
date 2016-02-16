# OPR


Simple command line utility to open a GitHub PR from the command line.

### Usage

```
opr <base_branch> -m "Optional Message"

```

So, if you are working on a branch named `736_FixScrolling`, and you want to open a PR against master, after you commit, all you have to type is:

```
opr master
```

If you want to add a message, you can use the `-m` option.

```
opr master -m "Sorry."
```

### Installation
1. Clone this repo.
2. Run `(sudo) pip install --editable .`

