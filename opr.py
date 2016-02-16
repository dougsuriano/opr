# The MIT License (MIT)
# 
# Copyright (c) 2016 Doug Suriano
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import click
import os
import requests
import sys
import subprocess
import re


GITHUB_API_TOKEN = 'OPR_GITHUB_API_TOKEN'


@click.command()
@click.argument('base')
@click.option('-m', '--message', default="", help='Description of your pull request')
@click.option('-t', '--title', default="", help='The title of your pull request (default is your branch name).')
def opr(base, message, title):

    if GITHUB_API_TOKEN not in os.environ:
        click.secho(u'OPR_GITHUB_API_TOKEN must be an environment variable.', fg='red')
        sys.exit(2)
    
    github_token = os.environ[GITHUB_API_TOKEN]
    
    current_branch = os.popen("git rev-parse --abbrev-ref HEAD").read().rstrip()
    origin_address = os.popen("git config --get remote.origin.url").read().rstrip()
    
    if 'git@github.com:' in origin_address:
        regex = r'git@github.com:(?P<repo_owner>[\w\.@\:/\-~]+)/(?P<repo_name>[\w\.@\:/\-~]+).git$'
        matches = re.search(regex, origin_address)
        repo_owner = matches.group('repo_owner')
        repo_name = matches.group('repo_name')
    else:
        click.secho(u'Only ssh cloned repos are supported (for now.)', fg='red')
        sys.exit(2)
    
    if not title:
        # Adapted from Stack Overflow: http://stackoverflow.com/a/5020947
        title = re.sub(r'([a-z])([A-Z])', r'\g<1> \g<2>', current_branch)
        title = title.replace('_', ' ').replace('-', ' ')
        
    subprocess.call("git push origin " + current_branch, shell=True)  
    
    headers = {
        'Authorization' : 'token {}'.format(github_token)
    }
    
    url = 'https://api.github.com/repos/{}/{}/pulls'.format(repo_owner, repo_name)
    
    request_json = {
        'title' : title,
        'body' : message,
        'base' : base,
        'head' : current_branch
    }
    
    r = requests.post(url, headers=headers, json=request_json)
    
    if r.status_code == 201:
        pr_url = r.json()["html_url"]
        click.secho(u'Your PR has been opened! {}'.format(pr_url), fg='green')
    else:
        response = r
        click.secho(u'Ugh, something went wrong.', fg='red')
