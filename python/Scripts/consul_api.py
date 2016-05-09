import yaml
import argparse
import os
import json
import consul


def __parse_args():

    _description = """Small file for consul maintenance."""

    parser = argparse.ArgumentParser(description=_description)
    _help = 'Directory of config files used to populate consul'
    parser.add_argument('config_dir', help=_help)

    return parser.parse_args()


def __prepare_config(files):

    yaml_configs = [yaml.load(open(file, 'r')) for file in files]
    return yaml_configs


def put(config):

    _consul = consul.Consul(host='192.168.1.223', port=8500)
    return _consul.kv.put(config['task'], json.dumps(config['args']))


def delete(key):

    _consul = consul.Consul(host='192.168.1.223', port=8500)
    return _consul.kv.delete(key)


def get(key):

    _consul = consul.Consul(host='192.168.1.223', port=8500)
    return _consul.kv.get(key)


def __main(config_dir):

    files = [config_dir + file for file in os.listdir(config_dir)]
    prepped_data = __prepare_config(files)
    [put(data) for data in prepped_data]


if __name__ == '__main__':

    args = __parse_args()
    __main(args.config_dir)
