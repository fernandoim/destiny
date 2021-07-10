import glob
import os
from pathlib import Path
import sys

def mkdirs(directory):
    """ It recursively creates directories from a Path object.

    Which cannot be done directly with os.mkdirs.

    Attributes:
        directory: Full path to create.
    """
    not_dirs = ('.', '..', '~')
    if directory.startswith('~/'):
        directory = Path(directory).expanduser()
    path_src = Path(directory)
    if not os.path.isdir(directory):
        os.mkdir(directory)
        for i in range(len(path_src.parents) -1):
            if not os.path.isdir(path_src.parents[i]) and \
                path_src.parents[i] not in not_dirs:
                os.mkdir(path_src.parents[i])

def destiny(src, dst='', ext='', mkdir=True, forced=False,
            pattern='', underline=True, digits=4):

    """ Generate filenames when many files are automatically generated.

    Generate filenames when many files are automatically generated, for example,
    the frames of a scene or a series of text files that you want to order
    successively but without using the creation date, instead, they want to be
    saved as file_0.png, file_1.png...

    Attributes:
        src: The source file from which it will be extracted,
            in case the destination is a directory, the name of the file and
            the extension to generate the new names. If a file name is not
            specified for the destination, it will be generated from this.
        dst: The destination file or directory.
        ext: The extension for the destination files,
            in case you want to change the extension. For example,
            if a video is generated from an image, the extension of the source
            file can be .png and the extension of the destination file
            can be .mp4.
            mkdir: If True, if the destination directory does not exist,
                it generates it. By default, its value is True.
            forced: If the destination file exists, it deletes it and returns
                its name. It's forced to overwrite that file. By default,
                its value is False.
            pattern: Pattern to append to the name of the file that is
                indicated as destination. For example, to generate
                town_photography_0001.png, it will be indicated as destination
                'town' and as pattern, 'photograph'. By default
                it does not generate patterned file names.
            underline: If its value is True, between the filename and the
                pattern and the pattern and the numeral (in case the pattern
                exists) or between the filename and the numbering, it will add
                a '_'. By default, its value is True.
            digits: The number of digits the numbering will contain. By default,
                its value is 4. If 0 or '' is indicated, it will number
                consecutively with the corresponding number:
                file_0.png, file_1.png, [...],
                file_8.png, file_9.png, file_10 .png, file_11.png, [...],
                file_98.png, file_99.png, file_100.png, file_101.png ...
    """
    if src.startswith('~/'):
        src = Path(src).expanduser()
        src = str(src)
    path_src = Path(src)
    if dst and dst.startswith('~/'):
        dst = Path(dst).expanduser()
        dst = str(dst)

    if not os.path.isfile(src) and not dst:
        return src
    elif os.path.isfile(src) and dst and not os.path.isfile(dst):
        # Complete route with slash (directory) and dot (file)
        if (dst.rfind('.') > dst.rfind('/') and dst.find('/') >= 0) or \
           (dst.rfind('.') > dst.rfind('\\') and dst.find('\\') >= 0):
            path_dst = Path(dst)
            directory = str(path_dst.parent)
            if not Path(directory).exists():
                if mkdir:
                    mkdirs(directory)
                else:
                    raise Exception(f'{directory} is not a valid file '
                                     'and mkdir is False')
            return dst


        elif not os.path.isdir(dst) and mkdir:
            mkdirs(dst)
            dst = Path(dst, path_src.name)
            return dst
        elif os.path.isdir(dst):
            dst_ = Path(dst, path_src.name)
            if os.path.isfile(dst_):
                if forced:
                    os.remove(dst_)
                    return dst
                else:
                    raise Exception(f'{dst_} exists and forced is False')
            else:
                name = path_src.stem
                if not ext:
                    ext = path_src.suffix
                if not ext.startswith('.'):
                    ext = '.' + ext
                if pattern and underline:
                    name = name + '_' + pattern + '_'
                elif pattern and not underline:
                    name = name + pattern
                elif not pattern and underline:
                    name = name + '_'
                route = str(Path(dst, name)) + '*'
                numeral = len(glob.glob(route))
                if digits:
                    numeral = str(numeral).zfill(digits)
                dst = str(Path(dst, name)) + numeral + ext

                return dst

if __name__ == '__main__':
    try:
        filename = destiny(sys.argv[1], sys.argv[2])
        print(filename)
    except Exception as e:
        print(e)
