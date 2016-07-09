from codecli.utils import (
    get_current_branch_name,
    merge_with_base,
    sync_to_remote,
)


def populate_argument_parser(parser):
    parser.add_argument('-r', '--rebase', action='store_true',
                        help="rebase with upstream")
    parser.add_argument('-b', '--base', help="Branch to rebase on")
    parser.add_argument('-R', '--remote', default="upstream",
                        help="Remote to fetch")
    parser.add_argument('-a', '--action', default="pull",
                        choices=('pull', 'push'), help="pull/push")


def main(args):
    branch = get_current_branch_name()
    if args.action == 'pull':
        merge_with_base(branch, rebase=args.rebase,
                        remote_branch=args.base, remote=args.remote)
    else:
        sync_to_remote(branch, remote=args.remote, remote_branch=args.base)
