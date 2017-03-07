@ECHO OFF

SET DIRECTORY=pwtools-src
SET REPOSITORY=http://pw-tools.googlecode.com/svn/trunk

IF NOT EXIST %DIRECTORY% GOTO EXPORT

rmdir /s /q %DIRECTORY%

:EXPORT
ECHO Exporting '%REPOSITORY%':
svn\svn.exe export %REPOSITORY% %DIRECTORY%