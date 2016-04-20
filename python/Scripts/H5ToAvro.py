import argparse
import json
import os
import pandas as pd
import re

import avro.schema

from avro.datafile import DataFileWriter
from avro.io import DatumWriter


def __parse_args():

    _description = """Script to convert dir of .h5 files to .avro using
    specified schemas"""

    parser = argparse.ArgumentParser(description=_description)
    _help = 'specify input directory containing .h5 files'
    parser.add_argument('input_dir', help=_help)

    _help = 'specify output directory which will contain .avro files'
    parser.add_argument('output_dir', help=_help)

    _help = 'specify avro schema to use for conversion'
    parser.add_argument('schema_uri', help=_help)

    return parser.parse_args()


def __main(input_dir, output_dir, schema_uri):

    read_dir_h5_convert_to_avro(input_dir, output_dir, schema_uri)


def read_dir_h5_convert_to_avro(input_dir, output_dir, schema_uri):

    files = [input_dir + file for file in os.listdir(input_dir)]

    for file in files:

        h5_as_json = __read_h5_as_json_str(file)
        file_name = __extract_file_name_from_uri(file)
        output_file = __convert_h5_extension_to_avro(file_name)
        write_json_to_avro(schema_uri, output_dir + output_file, h5_as_json)


def __read_h5_as_json_str(uri):

    return pd.read_hdf(uri).to_json(orient='records')


def __extract_file_name_from_uri(uri):

    return re.search('\w+\.h5', uri).group(0)


def __convert_h5_extension_to_avro(file_name):

    return file_name.replace('.h5', '.avro')


def write_json_to_avro(schema_uri, output_uri, json_str):

    schema = avro.schema.parse(open(schema_uri).read())
    writer = DataFileWriter(open(output_uri, "w"), DatumWriter(), schema)
    json_list = json.loads(json_str)

    for row in json_list:
        writer.append(row)

    writer.close()


if __name__ == '__main__':

    args = __parse_args()
    __main(args.input_dir, args.output_dir, args.schema_uri)
