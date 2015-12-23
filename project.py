import sys
import os
import shutil


def gen(base=sys.argv[1], project=sys.argv[2]):
    """
    Create project template with various sub-folders and files.

    :param base: Folder where main project folder will be created.
    :type base: string (but do not need quotation makes on command line)
    :param project: Name of project; this will be used to generate the main folder
    :type project: string (but do not need quotation makes on command line)
    :return: None
    """
    folders = (os.path.join(base, project),
               os.path.join(base, project, 'src'),
               os.path.join(base, project, 'src', 'code'),
               os.path.join(base, project, 'src', 'code', 'data_proc'),
               os.path.join(base, project, 'src', 'code', 'fig_gen'),
               os.path.join(base, project, 'src', 'code', 'stats'),
               #os.path.join(base, project, 'src', 'notes'),
               os.path.join(base, project, 'src', 'ethics'),
               #os.path.join(base, project, 'src', 'ms'),
               os.path.join(base, project, 'src', 'slides'),
               os.path.join(base, project, 'src', 'protocol'),
               os.path.join(base, project, 'src', 'results'),
               os.path.join(base, project, 'data'),
               os.path.join(base, project, 'data', 'raw'),
               os.path.join(base, project, 'data', 'proc'),
               os.path.join(base, project, 'doc'),
               os.path.join(base, project, 'doc', 'notes'),
               os.path.join(base, project, 'doc', 'ethics'),
               os.path.join(base, project, 'doc', 'ethics', 'scans'),
               os.path.join(base, project, 'doc', 'ms'),
               os.path.join(base, project, 'doc', 'slides'),
               os.path.join(base, project, 'doc', 'protocol'),
               os.path.join(base, project, 'doc', 'results'))

    for path in folders:
        try:
            print(path)
            os.mkdir(path)
        except FileExistsError:
            print('\nThe folder {} already exists. Please delete the project folder '
                  'and re-run this function if you truly want to create a blank template '
                  'project folder named "{}".\n'.format(path, project))
            sys.exit(1)  # abort
    shutil.copytree('./ms', os.path.join(base, project, 'src', 'ms'))
    shutil.copytree('./notes', os.path.join(base, project, 'src', 'notes'))

if __name__ == '__main__':
    gen()