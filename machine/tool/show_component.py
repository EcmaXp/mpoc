#!/usr/bin/env python3

path = "../../OpenComputers/src/main/scala/li/cil/oc/server/component"

import os

typedef = (
    ("string", "str"),   
    ("number", "int"),
    ("boolean", "bool"),
    ("nil", "None"),
)

emptydef = dict((
    ("str", repr("")),
    ("int", repr(0)),
    ("bool", repr(None)),
))

argdef = tuple((":" + x, ":" + y) for x, y in typedef)

def write(level, *args, **kwargs):
    print(" " * (4 * level), end="")
    print(*args, **kwargs)

for path, folders, files in os.walk(path):
    for filename in files:
        if not filename.endswith(".scala"):
            continue
        
        filepath = os.path.join(path, filename)
        with open(filepath) as fp:
            hasfunc = False
            f = iter(fp)
            for line in f:
                line = line.strip()
                if not line.startswith("@Callback"):
                    continue
                
                info = line
                
                if not hasfunc:
                    write(0)
                    write(0, "#", filename)
                    write(0, "class", filename.replace(".scala", ""), end=":\n")
                    hasfunc = True
                
                doc = ""
                if 'doc = """' in info:
                    doc = info.partition('doc = """')[2].partition('"""')[0]
                    info = info.replace('doc = """' + doc + '"""', '')
                elif 'doc = "' in info:
                    doc = info.partition('doc = "')[2].partition('"')[0]
                    info = info.replace('doc = "' + doc + '"', '')
                
                info = info.replace(", )", ")")
                func = next(f).strip().partition("):")[0] + ")"
                
                args = ""
                ret = ""
                
                predoc, _, doc = doc.partition("--")
                predoc = predoc.strip()
                doc = doc.strip()
                _predoc = predoc
                
                if predoc.startswith("function(") and "context: Context, args: Arguments" in func:
                    args = predoc[len("function("):]
                    args = args.partition(")")[0]
                    if "):" in predoc:
                        ret = predoc.partition("):")[2]
                    predoc = ""

                if ", " in ret:
                    ret = "({})".format(ret)
                    
                if args:
                    for luatype, pytype in argdef:
                        args = args.replace(luatype, pytype)

                if ret:   
                    for luatype, pytype in typedef:
                        ret = ret.replace(luatype, pytype)
                
                while "[" in args:
                    assert "]" in args
                    args, _, arg = args.partition("[")
                    arg, _, left_args = arg.partition("]")
                    sep = ""
                    if arg.startswith(","):
                        sep = ","
                        arg = arg[len(','):]
                    argtype = arg.partition(":")[2]
                    if "or" in argtype:
                        argtype = "OR({})".format("<OR> ".join(map(str.strip, argtype.split("or"))))
                    arg = arg.replace(":", "="+emptydef.get(argtype, argtype + "()")+":")
                    args += sep + arg + left_args
                
                if args:
                    args = "self, context:Context, " + args
                else:
                    args = "self, context:Context"
                
                func = func.replace("context: Context, args: Arguments", args)
                
                if ret:
                    func += " -> " + ret
                
                write(1, info)
                if func.startswith("override "):
                    func = func[len("override "):]
                    write(1, "@Override")
                write(1, func + ":")
                
                def writedoc(doc):
                    if '"' in doc or "'" in doc:
                        write(2, '"""' + doc + '"""')
                    else:
                        write(2, '"' + doc + '"')
                
                if predoc:
                    writedoc(predoc)
                if doc:
                    writedoc(doc)
                
                write(2, "pass")
                write(0)
