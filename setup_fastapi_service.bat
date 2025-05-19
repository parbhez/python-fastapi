
@echo off
setlocal

:: Set project and venv paths
set PROJECT_DIR=C:\Users\DELL\Desktop\fastapi
set PYTHON_PATH=C:\Users\DELL\Desktop\fastapi\venv\Scripts\python.exe
set NSSM_PATH=C:\nssm-2.24\win64\nssm.exe

:: Install service
%NSSM_PATH% install FastAPIService %PYTHON_PATH% -m uvicorn main:app --host 0.0.0.0 --port 8000

:: Set working directory
%NSSM_PATH% set FastAPIService AppDirectory %PROJECT_DIR%

:: Optional: Set display name and description
%NSSM_PATH% set FastAPIService DisplayName "FastAPI Herd Service"
%NSSM_PATH% set FastAPIService Description "FastAPI running as Windows Service using NSSM"

:: Optional: Set service to auto-start with Windows
%NSSM_PATH% set FastAPIService Start SERVICE_AUTO_START

:: Optional: Setup log files (create logs folder manually beforehand)
%NSSM_PATH% set FastAPIService AppStdout %PROJECT_DIR%\logs\out.log
%NSSM_PATH% set FastAPIService AppStderr %PROJECT_DIR%\logs\err.log

:: Start the service
%NSSM_PATH% start FastAPIService

echo.
echo FastAPIService has been installed and started successfully!
pause
endlocal
