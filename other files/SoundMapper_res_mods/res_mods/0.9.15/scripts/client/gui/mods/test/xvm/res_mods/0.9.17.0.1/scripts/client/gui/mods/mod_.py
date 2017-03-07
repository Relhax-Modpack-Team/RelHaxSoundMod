# Embedded file name: scripts/client/gui/mods/mod_.py
""" XFW Entry point file (c) www.modxvm.com 2013-2016 """
import imp
import os
import platform
import sys
import ResMgr

def find_wd_dir():
    try:
        path = './res_mods/mods/'
        if os.path.isdir(path) and (os.path.isfile(path + 'xfw/python/xfw_loader.pyc') or os.path.isfile(path + 'xfw/python/xfw_loader.py')):
            return path
        sec = ResMgr.openSection('../paths.xml')
        subsec = sec['Paths']
        vals = subsec.values()
        for val in vals:
            path = val.asString + '/mods/'
            if os.path.isdir(path) and (os.path.isfile(path + 'xfw/python/xfw_loader.pyc') or os.path.isfile(path + 'xfw/python/xfw_loader.py')):
                return path

        raise Exception('[XFW][Entrypoint] xfw_loader.py[c] is not found in the paths')
    except Exception as err:
        print ('[XFW][Entrypoint] Error locating working directory: ', err)
        wd = 'res_mods/mods/'
        print '[XFW][Entrypoint]  fallback to the default path: %s' % wd
        return wd


try:
    wd = find_wd_dir()
    python27 = imp.load_dynamic('python27', '%s/xfw/native/python27.dll' % wd)
    if platform.version().startswith('5.'):
        print '[XFW][Entrypoint] Applying fix for Windows XP/2003. Please update your OS as soon as possible! http://windows.com/'
        XVMNativeXPFix = imp.load_dynamic('XVMNativeXPFix', '%s/xfw/native/XVMNativeXPFix.pyd' % wd)
    sys.path.insert(0, '%s/xfw/python' % wd)
    sys.path.insert(0, '%s/xfw/native/lib' % wd)
    import xfw_loader
except:
    print '============================='
    import traceback
    traceback.print_exc()
    print '============================='
