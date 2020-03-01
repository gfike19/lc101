import re

uname_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_uname(uname):
    return uname_re.match(uname)

pwd_re = re.compile(r"^.{3,20}$")
def valid_pwd(pwd):
    return pwd_re.match(pwd)