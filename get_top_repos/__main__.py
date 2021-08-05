from github import Github
import argparse
import time


def main():
    ### Manage Command Line Interface (CLI) information display and arguments
    # Create the parser object
    parser = argparse.ArgumentParser(prog = '',
                                    usage='''
                                    Usage:
                                    Pass the name of a github username to get the names of the top 5 most starred
                                    github repositories belonging to a specified github user together with the
                                    number of stars.
                                    ''',
                                    description='''
                                    -----------------------------------------------
                                    Description:
                                    This tool will display the names of the top 5 most starred github repositories
                                    belonging to a specified github user together with the number of stars.
                                    -----------------------------------------------
                                    ''',
                                    epilog="Kouo coding task, Irene Garcia (github @ire8)",
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    add_help=True
                                    )
    # Add the argument username
    parser.add_argument("username", type=str, help="Enter github username, for example: ire8", metavar="GITHUB USERNAME")
    arg = parser.parse_args()

    ### Get the 5 highest starred repositories from the passed USERNAME

    g = Github() # Create github object
    user = g.get_user(arg.username) # Get user by username

    # Get repositories and star count lists from the user
    stars = []
    names = []
    for repo in user.get_repos():
        stars.append(repo.stargazers_count)
        names.append(repo.name)

    sorted_repos = [(y,x) for x,y in sorted(zip(stars,names), reverse=True)] # Sort in descending stars order

    # Print the 5 top repositories names with their corresponding stars
    n_repos = 5 # Number of repositories to select
    for x,y in sorted_repos[:n_repos]:
        print("{0:40}  {1}".format(x, y))



if __name__ == '__main__':
    main()
