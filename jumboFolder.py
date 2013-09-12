#!/usr/bin/env python
#
# This python script is a command line utility for Windows systems to find 
# large folders in a given directory

 
import os


def get_size(_dir):
    """ 
    Recursive traverse through the dir
    and return the total sizes files found in MB

    """
    total_size = 0
    _kb = 0.0009765625
    _mb = _kb * 0.0009765625
    size = {}
    if os.path.isdir(_dir):
        for root, dirnames, filenames in os.walk(_dir):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                if os.path.exists(file_path):
                    _size = os.path.getsize(file_path)
                    total_size += _size
        tSize_mb = (total_size * _mb)
        size[_dir] = tSize_mb
    else:
        size[_dir] = (os.path.getsize(_dir) * _mb)
    return size


#Walk through the root directory
def walk_through(root_dir):
    h = {}                  # dictionary for the folders
    if os.path.isdir(root_dir):
        dirnames = os.listdir(root_dir)
        for dir in dirnames:
            h.update(get_size(os.path.join(root_dir, dir)))
        for key, value in sorted(h.iteritems(),
                                 key=lambda (k, v): (v, k), reverse=True):  # descending order
                print "%s ==> %s MB" % (key, h[key])
    else:
        print "No such file/Dir found !!"


path = raw_input('Enter the root path :')
walk_through(path)