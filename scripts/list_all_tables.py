import os
import re
import sys


def extract_created_tables_from_sql(sql):
    pattern = re.compile(
        r"CREATE\s+TABLE\s+(IF\s+NOT\s+EXISTS\s+)?[`'\"]?([a-zA-Z0-9_.]+)[`'\"]?",
        re.IGNORECASE,
    )
    matches = pattern.findall(sql)
    for match in matches:
        print(match[1])
    return [match[1] for match in matches]


def find_sql_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".sql"):
                yield os.path.join(root, file)


def main(directory):
    created_tables = set()

    for sql_file in find_sql_files(directory):
        try:
            print("\nFILE:", os.path.basename(sql_file))
            with open(sql_file, "r", encoding="utf-8") as f:
                content = f.read()
                tables = extract_created_tables_from_sql(content)
                created_tables.update(tables)
        except Exception as e:
            print(f"Error reading {sql_file}: {e}", file=sys.stderr)

    output_file = f"{os.path.basename(os.path.abspath(directory))}_tables.sql"
    with open(output_file, "w", encoding="utf-8") as f:
        for table in sorted(created_tables):
            f.write(f"{table}\n")

    print(f"Wrote {len(created_tables)} unique table(s) to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_created_tables.py <path_to_sql_directory>")
        sys.exit(1)
    main(sys.argv[1])
