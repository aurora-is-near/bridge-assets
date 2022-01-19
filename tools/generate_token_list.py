#!/usr/bin/env python3

"""
Script to generate token list automatically from all token descriptions in the repository.
# authoring-token-lists
The json generated follows the format specified at: https://github.com/Uniswap/token-lists
"""

import argparse
import pathlib
import json
from os.path import join, isfile
import jsonschema
import datetime


class Tags:
    NATIVE_AURORA = 'aurora'
    NATIVE_NEAR = 'near'
    NATIVE_ETHEREUM = 'ethereum'
    NATIVE_BSC = 'bsc'
    NATIVE_TERRA = 'terra'
    BRIDGE_ALLBRIDGE = 'allbridge'


class Aurora:
    NAME = 'Aurora'
    LOGO_URI = 'https://raw.githubusercontent.com/aurora-is-near/aurora-press-kit/master/Logos/SVG/aurora-stack.svg'
    KEYWORDS = ['aurora', 'near', 'rainbow', 'bridge', 'audited', 'verified']
    VERSION = {'major': 1, 'minor': 0, 'patch': 0}
    CHAIN_ID = 1313161554
    TAGS = {
        Tags.NATIVE_AURORA: {
            'name': "Native Aurora",
            'description': 'Tokens that were deployed initially on Aurora.'
        },
        Tags.NATIVE_NEAR: {
            'name': 'Native NEAR',
            'description': 'Tokens that were deployed initially on NEAR. They have an equivalent token in Aurora.'
        },
        Tags.NATIVE_ETHEREUM: {
            'name': 'Native Ethereum',
            'description': 'Tokens that were deployed initially on Ethereum. They have an equivalent token in NEAR and Aurora.'
        },
        Tags.NATIVE_BSC: {
            'name': 'Native BSC',
            'description': 'Tokens that were deployed initially on BSC. They have an equivalent token in NEAR and Aurora.'
        },
        Tags.NATIVE_TERRA: {
            'name': 'Native Terra',
            'description': 'Tokens that were deployed initially on Terra. They have an equivalent token in Aurora.'
        }
    }

    def __init__(self, path: str):
        path = pathlib.Path(path)

        self.tokens = []

        # Load all tokens in alphabetical order and process only json files
        list_of_tokens = sorted(
            filter(
                isfile,
                path.glob('*.json')
            )
        )

        for token in list_of_tokens:
            token_file_name = token.name[:-len('.json')]
            # Ignore example and testnet tokens
            if token_file_name.startswith('EXAMPLE') or token_file_name.endswith('_testnet'):
                continue

            token_desc = self.load_token(token)

            if token_desc is not None:
                self.tokens.append(token_desc)

    def load_token(self, token_path):
        svg_file_name = token_path.name[:-len('.json')] + '.svg'
        svg = token_path.parent / svg_file_name

        with open(token_path) as f:
            token_desc = json.load(f)

        tags = []

        if 'ethereum_address' in token_desc and token_desc['ethereum_address'] != '':
            tags.append(Tags.NATIVE_ETHEREUM)

        if 'terra_address' in token_desc and token_desc['terra_address'] != '':
            tags.append(Tags.NATIVE_TERRA)

        if 'bridge' in token_desc and token_desc['bridge'].lower() == 'allbridge':
            tags.append(Tags.BRIDGE_ALLBRIDGE)

        if token_desc['aurora_address'] == '':
            return None

        return dict(
            chainId=Aurora.CHAIN_ID,
            address=token_desc['aurora_address'],
            symbol=token_desc['symbol'],
            name=token_desc['name'],
            decimals=token_desc['decimals'],
            logoURI=f'https://raw.githubusercontent.com/aurora-is-near/bridge-assets/master/tokens/{svg.name}',
            tags=tags
        )

    def generate(self):
        return dict(
            name=Aurora.NAME,
            logoURI=Aurora.LOGO_URI,
            keywords=Aurora.KEYWORDS,
            tags=Aurora.TAGS,
            timestamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            tokens=self.tokens,
            version=Aurora.VERSION
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Aurora Token List Generator')
    parser.add_argument('--tokens', default='tokens',
                        help='Path to folder with all tokens.')

    parser.add_argument('--schema', default=join('assets', 'tokenlist.schema.json'),
                        help='Path to tokenlist schema. Downloaded from: https://uniswap.org/tokenlist.schema.json')

    parser.add_argument('--output', default=join(
        'assets', 'aurora.tokenlist.json'), help='Output file path.')

    args = parser.parse_args()

    tokens = Aurora(args.tokens)

    tokenlist = tokens.generate()

    # Verify schema
    with open(args.schema) as f:
        schema = json.load(f)

    # This function fails if there is any problem
    jsonschema.validate(tokenlist, schema)

    tokenlist_str = json.dumps(tokenlist, indent=2)

    if args.output == 'stdout':
        print(tokenlist_str)
    else:
        with open(args.output, 'w') as f:
            print(tokenlist_str, file=f, end='')
