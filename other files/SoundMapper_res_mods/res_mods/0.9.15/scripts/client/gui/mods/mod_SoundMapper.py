# Embedded file name: mod_SoundMapper
import ResMgr
import WWISE
from debug_utils import *

def _OverrideMethod(handler, cls, method):
    orig = getattr(cls, method)
    newm = lambda *a, **k: handler(orig, *a, **k)
    if type(orig) is not property:
        setattr(cls, method, newm)
    else:
        setattr(cls, method, property(newm))


def _checkAndReplace(event):
    if event in myreplace:
        return myreplace[event]
    else:
        return event


def _WWISE_WW_eventGlobal(base, event):
    return base(_checkAndReplace(event))


def _WWISE_WW_eventGlobalPos(base, event, pos):
    return base(_checkAndReplace(event), pos)


def _WWISE_WW_getSoundObject(base, event, matrix, local):
    return base(_checkAndReplace(event), matrix, local)


def _WWISE_WW_getSound(base, eventName, objectName, matrix, local):
    return base(_checkAndReplace(eventName), _checkAndReplace(objectName), matrix, local)


def _WWISE_WW_getSoundCallback(base, eventName, objectName, matrix, callback):
    return base(_checkAndReplace(eventName), _checkAndReplace(objectName), matrix, callback)


def _WWISE_WW_getSoundPos(base, eventName, objectName, position):
    return base(_checkAndReplace(eventName), _checkAndReplace(objectName), position)


ms = ResMgr.openSection('../res_mods/configs/D2R52/mod_SoundMapper.xml')
if ms is not None:
    myreplace = {}
    for k, v in ms.items():
        myreplace[k] = v.asString

if len(myreplace) > 0:
    _OverrideMethod(_WWISE_WW_eventGlobal, WWISE, 'WW_eventGlobal')
    _OverrideMethod(_WWISE_WW_eventGlobalPos, WWISE, 'WW_eventGlobalPos')
    _OverrideMethod(_WWISE_WW_getSoundObject, WWISE, 'WW_getSoundObject')
    _OverrideMethod(_WWISE_WW_getSound, WWISE, 'WW_getSound')
    _OverrideMethod(_WWISE_WW_getSoundCallback, WWISE, 'WW_getSoundCallback')
    _OverrideMethod(_WWISE_WW_getSoundPos, WWISE, 'WW_getSoundPos')
    BigWorld.logInfo('LOAD', 'SoundMapper by D2R52', None)
else:
    BigWorld.logInfo('LOAD', 'SoundMapper by D2R52 is not loaded - missing configuration', None)
