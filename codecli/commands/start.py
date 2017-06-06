from codecli.utils import check_call, get_branches, ask
from codecli.commands.end import end_branch


def populate_argument_parser(parser):
    parser.add_argument('feature')
    parser.add_argument('-b', '--base', help="Branch to checkout")


def main(args):
    local_branch = args.feature
    checkout_branch = args.base or 'master'
    start(local_branch, checkout_branch=checkout_branch)


def start(branch, remote='upstream', checkout_branch='master',
          fetch_args=[]):
    existing_branches = get_branches()
    if branch in existing_branches:
        answer = ask("Branch %s exists, (s)witch to it or re(c)reate "
                     "it?  (S/c) " % branch, pattern=r'[sScC]',
                     default='s')
        answer = answer.lower()[0]

        if answer == 's':
            check_call(['git', 'checkout', branch])
            return

        elif answer == 'c':
            end_branch(branch, force=True)

    base_ref = '%s/%s' % (remote, checkout_branch)
    check_call(['git', 'fetch', remote] + fetch_args)
    check_call(['git', 'checkout', '-b', branch, '--no-track', base_ref])
