import os

def check_exist_dir(dir_name = None):
    return os.path.exists(dir_name)

def path_join(dir_name = None,file_name = None):
    assert (dir_name is not None) & (file_name is not None), "Please check file path"
    return os.path.join(dir_name,file_name)

def make_dir(file_name = None, path_name = None, parant_dir = None, df=None):
    new_path = os.path.join(parant_dir,path_name)
    make_dir(new_path)
    file_dir = os.path.join(new_path,file_name)
    df.to_csv("{}".format(file_dir))

def to_csv(dir_path = None, file_name = None, df = None):
    if not check_exist_dir(dir_path):
        make_dir(dir_path)
    path_dir = path_join(dir_path,file_name)
    df.to_csv(path_dir)

def make_dir(path_name = None):
    assert (path_name is not None),"Please choose correct directory"
    if not check_exist_dir(path_name):
        os.makedirs(path_name)

def isfile_exists(file_name = None):
    """
    check the given file exists in given directory
    PLease check directory or set correct directory for given file
    """
    os.path.isfile(file_name)

def isdir_exists(path_name = None):
    return os.path.isdir(path_name)

def make_cwd(path_name = None):
    assert path_name is not None, "Please check file path"
    cwd  = os.getcwd()
    cwd_dir = cwd.split("\\")[-1]
    print(cwd_dir)
    if cwd_dir == path_name:
        return "Working directory already set :{}".format(os.getcwd())
    if isdir_exists(path_name = path_name):
        os.chdir(path_name)
        return "Current working directory:{}".format(os.getcwd())

def back_from_directory():
    os.chdir("..")
    return "Current working directory:{}".format(os.getcwd())


if "__main__" == __name__:
    print(make_cwd("New Data"))


