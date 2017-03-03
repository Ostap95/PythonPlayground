'''
    Operating Systems define their file systems in a recursive manner. File system consists of a top-level
    directory (root), and the contents of this directory consists of files and directories.
    The OS allows directories to be nested infinitely deep, the only limitation is memory space.

     Given the recursive nature of the file systems, many common behaviours such as copying, moving or deleting
     a directory, are implemented with recursive algorithms.

    The following algorithm computes the total disk usage for all files and directories nested within a specific
    directory.
'''

import os


def disk_usage(path):
    """ Return the number of bytes used by a file/folder and any descendents """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)
    return total




















