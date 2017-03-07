@ECHO OFF

SET FILE=changelog.txt
SET REPOSITORY=http://pw-tools.googlecode.com/svn/trunk

ECHO Downloading log '%REPOSITORY%':
svn\svn.exe log %REPOSITORY% -r HEAD:1 > %FILE%

START notepad.exe %FILE%