from gendiff import cli
from gendiff.main import generate_diff


def main():
    args = cli.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
