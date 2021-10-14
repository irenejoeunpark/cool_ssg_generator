import argparse
import utils.config_util as config_util

def parseArguments():
    parser = argparse.ArgumentParser(
        description="Generate HTML website from raw data")
    
    parser.add_argument('-v', '--version', action='version',
                        version='cool_ssg_generator release 0.1', help='display the current version')
    parser.add_argument('-i', '--input', nargs='+',
                        help='path to input file or directory')
    parser.add_argument('-o', '--output',
                        help='path to output directory')
    parser.add_argument('-s', '--stylesheets', nargs='+',
                        help='attach stylesheet URLs')
    parser.add_argument('-l', '--lang',
                        help='language of the generated documents, default is en-CA')
    parser.add_argument('-c', '--config',
                        help='path to the config file')

    args = parser.parse_args()

    options = vars(args)

    if args.config:
        config_util.get_config(args.config, options)

    # Assign default value for unspecified required options
    options["lang"] = "en-CA" if options["lang"] is None else options["lang"]

    return options