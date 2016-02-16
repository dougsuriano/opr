import click


import getopt
import os
import requests
import sys
import subprocess

GITHUB_API_TOKEN = "OPR_GITHUB_API_TOKEN"

@click.command()
@click.argument('head')
@click.option('-m', '--message', default="", help='Description of your pull request')
def opr(head, message):
    click.echo("Hey There")
    click.echo("head " + head)
    click.echo("message: " + message)
    
    if GITHUB_API_TOKEN not in os.environ:
        click.echo('OPR_GITHUB_API_TOKEN must be an environment variable', error=True)
        sys.exit(2)
    
    
    proc = subprocess.Popen('git rev-parse --abbrev-ref HEAD', stdout=subprocess.PIPE)
    #proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    current_branch = proc.stdout.read()
    
    click.echo(current_branch)
    

# 
#
# def main(argv):
#
#     if GITHUB_API_TOKEN not in os.environ:
#         print 'OPR_GITHUB_API_TOKEN must be an environment variable'
#         sys.exit(2)
#
#     open_pr_against = argv[0]
#
#     try:
#         opts, args = getopt.getopt(argv[1:], "hm:")
#     except:
#         print 'ocr <branch_to_compare_against> -m <message>'
#         sys.exit(2)
#
#     proc = subprocess.Popen('git rev-parse --abbrev-ref HEAD', stdout=subprocess.PIPE)
#     current_branch = proc.stdout.read()
#
# if __name__ == "__main__":
#     main(sys.argv[1:])