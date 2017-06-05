import argparse


class StringArgumentParser:
    def __init__(self):
        self.users_input = ""
        self.parse_arguments()

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Find if your input text is fake!!",
                                       formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument("news",
                            help="Url in a string format",  nargs='+')

        args = parser.parse_args()
        self.users_input = ' '.join(args.news)

    def get_users_input(self):
        return self.users_input
