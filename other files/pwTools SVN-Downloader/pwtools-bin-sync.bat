@ECHO OFF

SET DIRECTORY=pwtools-svn-bin
SET REPOSITORY=http://pw-tools.googlecode.com/svn/trunk/bin

IF EXIST %DIRECTORY%\.svn GOTO UPDATE

IF NOT EXIST %DIRECTORY% GOTO CHECKOUT

@rmdir /s /q %DIRECTORY%

:CHECKOUT
ECHO Checking out '%REPOSITORY%':
svn\svn.exe checkout %REPOSITORY% %DIRECTORY%

:UPDATE
ECHO.
svn\svn.exe update %DIRECTORY%