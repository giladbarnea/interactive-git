#!/usr/bin/env python3.8
import os
import sys

import click

import prompt
from util import shell

from branch import BranchTree


@click.command()
@click.argument('name')
def main(name):
    btree = BranchTree()
    branches = btree.branchnames
    if name in branches:
        if not prompt.ask(f'"{name}" already exists, check it out?'):
            sys.exit()
        shell.tryrun(f'git checkout {name}')
        return os.system('git pull')
    
    status = git.status().status
    stash = False
    if status:
        os.system('git status')
        answer = prompt.action('Uncommitted changes', 'stash → apply', 'just checkout', 'reset --hard', special_opts=True)
        if answer == 's':
            stash = True
            shell.tryrun('git stash')
        elif answer == 'r':
            shell.tryrun('git reset --hard')
        else:
            stash = False
    shell.tryrun(f'git checkout -b {name}',
                 f'git push --set-upstream origin {name}')
    if stash:
        shell.tryrun('git stash apply')
        from .addcommitpush import main as addcommitpush
        addcommitpush(f'new branch: {name}')


if __name__ == '__main__':
    main()