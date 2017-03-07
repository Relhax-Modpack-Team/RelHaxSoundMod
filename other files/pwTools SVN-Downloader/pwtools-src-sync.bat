@ECHO OFF

SET DIRECTORY=pwtools-svn-src
SET REPOSITORY=http://pw-tools.googlecode.com/svn/trunk

IF EXIST %DIRECTORY%\.svn GOTO UPDATE

IF NOT EXIST %DIRECTORY% GOTO CHECKOUT

@rmdir /s /q %DIRECTORY%

:CHECKOUT
ECHO Checking out '%REPOSITORY%':
svn\svn.exe checkout %REPOSITORY% %DIRECTORY%

:UPDATE
ECHO.
svn\svn.exe update %DIRECTORY%