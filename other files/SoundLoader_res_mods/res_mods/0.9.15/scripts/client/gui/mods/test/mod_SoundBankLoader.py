# Embedded file name: mod_SoundBankLoader
import WWISE
import ResMgr
from debug_utils import *

def _OverrideMethod(handler, cls, method):
    orig = getattr(cls, method)
    newm = lambda *a, **k: handler(orig, *a, **k)
    if type(orig) is not property:
        setattr(cls, method, newm)
    else:
        setattr(cls, method, property(newm))


def _WWISE_WG_loadBanks(base, xmlPath, banks, isHangar, *args, **kwargs):
    if extraBanks:
        banks_list = (banks + ';' + extraBanks).split(';')
        banks_list = set([ x.strip() for x in banks_list if x and x.strip() ])
        banks = '; '.join(banks_list)
    base(xmlPath, banks, isHangar, *args, **kwargs)


extraBanks = ''
mysettings = ResMgr.openSection('../res_mods/configs/D2R52/mod_SoundBankLoader.xml/preloadSoundBanks')
if mysettings is not None:
    extraBanks = mysettings.asString.strip()
if extraBanks:
    _OverrideMethod(_WWISE_WG_loadBanks, WWISE, 'WG_loadBanks')
    BigWorld.logInfo('LOAD', 'SoundBankLoader by D2R52', None)
else:
    BigWorld.logInfo('LOAD', 'SoundBankLoader by D2R52 is not loaded - missing configuration', None)
