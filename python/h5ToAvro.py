import pandas as pd
import os
import json
import re
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


def read_h5_as_json_str(uri):
    return pd.read_hdf(uri).to_json(orient='records')


def write_json_to_avro(schema_uri, output_uri, json_str):

    schema = avro.schema.parse(open(schema_uri).read())
    writer = DataFileWriter(open(output_uri, "w"), DatumWriter(), schema)
    json_list = json.loads(json_str)

    for row in json_list:
        writer.append(row)

    writer.close()


def read_avro_as_df(input_uri):

    reader = DataFileReader(open(input_uri, "r"), DatumReader())
    output = []

    for row in reader:
        output.append(row)

    reader.close()

    return pd.DataFrame(output)


def read_dir_h5_convert_to_avro(input_dir, output_dir, schema_uri):
    files = [input_dir + file for file in os.listdir(input_dir)]

    for file in files:
        h5_as_json = read_h5_as_json_str(file)
        file_name = extract_file_name_from_uri(file)
        output_file = convert_h5_extension_to_avro(file_name)
        write_json_to_avro(schema_uri, output_dir + output_file, h5_as_json)


def extract_file_name_from_uri(uri):
    return re.search('\w+\.h5', uri).group(0)


def convert_h5_extension_to_avro(file_name):
    return file_name.replace('.h5', '.avro')


def main(input_dir, output_dir, schema_uri):
    read_dir_h5_convert_to_avro(input_dir, output_dir, schema_uri)


if __name__ == '__main__':
    input_dir = '/nfs/profiler_data/dec/fan_star/gb/'
    output_dir = '/home/shaun/Desktop/Scripts/avro/data/fan_star/'
    schema_uri = '/home/shaun/Desktop/Scripts/avro/schema/fan_star.avsc'
    main(input_dir, output_dir, schema_uri)
