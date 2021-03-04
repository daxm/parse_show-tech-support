"""Parse a `show tech-support` output from Cisco IOS into structured data categorized by command."""
from pprint import pprint

input_file = "show-tech-support.txt"


def main():
    with open(input_file, 'r') as f:
        output_dict = {}
        command = ""
        for line in f:
            if line.startswith('--') and 'show' in line:
                # This is a new command since all commands are "formatted" starting/ending with a bunch of dashes.
                new_command = True
                command = line.strip("-\n ")
                output_dict[command] = ""
            else:
                if command:
                    output_dict[command] = output_dict[command] + line.strip("\n")
                new_command = False
    # pprint(output_dict)  # Print a "structured" version of show tech-support.  Still a work in progress.
    for key in output_dict:
        print(key)


if __name__ == '__main__':
    main()
