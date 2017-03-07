@ECHO OFF

SET DIRECTORY=pwtools-bin
SET REPOSITORY=http://pw-tools.googlecode.com/svn/trunk/bin

IF NOT EXIST %DIRECTORY% GOTO EXPORT

rmdir /s /q %DIRECTORY%

:EXPORT
ECHO Exporting '%REPOSITORY%':
svn\svn.exe export %REPOSITORY% %DIRECTORY%