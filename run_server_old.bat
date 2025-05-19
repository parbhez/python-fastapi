#https://www.youtube.com/watch?v=oKciAtJTuSw&list=LL&index=1&t=600s

call nssm.exe install my_fastapi_app "%cd%\run_server.bat"
call nssm.exe set my_fastapi_app AppStdout "%cd%\logs\my_fastapi_app_logs.log"
call nssm.exe set my_fastapi_app AppStderr "%cd%\logs\my_fastapi_app_logs.log"
call nssm set my_fastapi_app AppRotateFiles 1
call nssm set my_fastapi_app AppRotateOnline 1
call nssm set my_fastapi_app AppRotateSeconds 86400
call nssm set my_fastapi_app AppRotateBytes 1048576
call sc start my_fastapi_app