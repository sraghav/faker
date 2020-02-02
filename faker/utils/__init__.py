# coding=utf-8
import datetime

debug = True


def is_string(var):
    try:
        return isinstance(var, basestring)
    except NameError:
        return isinstance(var, str)


def quote(var):
    return ('"{0}"' if '"' not in var else "'{0}'").format(var)


def log(msg='Test Log Message', debug=True):
    dt = datetime.datetime.now()

    dt1 = dt.strftime("%Y%m%d%H%M%S")

    if debug:
        print("[" + dt1 + "]:" + str(msg))


def getProperties(propertiesFile='', delim=' ', key='', debug=debug):
    """
    Reads a .properties file and returns the key value pairs as dictionary.
    if key value is specified, then it will return its value alone.
    """

    log("Schema File => " + propertiesFile, debug)
    map = {}
    if not len(propertiesFile) > 0:
        raise ValueError('`propertiesFile` needs to be provided.')
    try:
        with open(propertiesFile) as f:
            for line in f.readlines():
                if not line.startswith('#') and line.strip():
                    log("Line => " + line, debug)

                    l = line.strip().split(delim)
                    if len(l) != 2:
                        ErrMsg = f"Structure not valid for property {l}"
                        log(ErrMsg)
                        raise ValueError(ErrMsg)
                    log("parsed list =>" + str(l), debug)
                    key = l[0]
                    try:
                        value = l[1]
                    except:
                        value = ""
                    map[key] = value
                    log("key = " + key, debug)
                    log("value = " + map[key], debug)

        # if key:
        #     return d[key]
        # else:
        #     return d
        return map
    except FileNotFoundError:
        raise FileNotFoundError('`propertiesfile` not found')
    except Exception as e:
        raise Exception(f"Something went wrong :: {e}")
