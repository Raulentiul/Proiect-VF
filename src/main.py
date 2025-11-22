import argparse
from src.writer.yaml_generator import get_yaml
from src.writer.yaml_to_markdown_tools import write_markdown_file
from src.writer.yaml_writer import save_yaml

DEFAULT_QUERY = 'verification OR "neural network verification" OR termination OR QBF'

def main():
    parser = argparse.ArgumentParser(description="Generate tools MD file from a zenodo search query")
    parser.add_argument('query', nargs='*',
                        help='Search query string (wrap in double quotes on Windows if needed)')
    parser.add_argument('-p', '--pages', type=int, default=5,
                        help='Number of pages to process (default: 5)')

    args = parser.parse_args()

    if args.query:
        query = ' '.join(args.query)
    else:
        query = DEFAULT_QUERY

    yaml = get_yaml(query, pages=args.pages)
    save_yaml(yaml)
    write_markdown_file()

if __name__ == "__main__":
    main()
