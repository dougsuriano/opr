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

You can specify a title of your PR with the `-t` option. If you don't specify a title, `opr` will just use your current branch name as the title.

```
opr master -t "REVIEW THIS NOW SO I CAN GO TO THE BAR"
```

If you want to add a message, you can use the `-m` option.

```
opr master -m "Sorry."
```

### Installation
1. Clone this repo.
2. Run `(sudo) pip install --editable .`
3. [Create a GitHub personal access token](https://github.com/settings/tokens) for `opr` and set it as a shell environment variable `OPR_GITHUB_API_TOKEN`.

