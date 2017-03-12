#!/usr/bin/env python -tt
'''
This is keypair parser, will read the keypair value text file
fill the values in Python Dictionary

Author: Bipin Bachhao (bipinbachhao@gmail.com)

Copyright 2017 Bipin Bachhao (bipinbachhao@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
s

'''
import os
import sys
import argparse

keypair_dir = os.getcwd()
keypair_file_name = 'key_pairs.txt'
# file_path = os.path.join(keypair_dir, keypair_file_name)


def main():
    print "File Name: %s" %(args.f)
    print "Directory Path: %s" %(args.d)
    print "Will read the keypair value text file from below path"
    print "Full file path: %s" %file_path

def keypair_convert(file_loc):
    myvars = {}
    with open(file_loc) as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            myvars[name.strip()] = var
    return myvars


if __name__ == "__main__":
# Will call function only if run as a script
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '-file', default='key_pairs.txt', help="File name, Default: key_pairs.txt")
    parser.add_argument('-d', '-dir', default=os.getcwd(), help="Directory, Default:current working dir")
    args = parser.parse_args()

    file_path = os.path.join(args.d, args.f)

    main()

    keypair_dict = keypair_convert(file_path)
    print keypair_dict
    print keypair_dict['Test1']
