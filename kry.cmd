@echo off
cls

:line4

where python >nul 2>&1

if errorlevel 1 (
    echo Error: Python is not installed.
    echo "Would you like to install it? (y/n) "
    set /p choice=Select:
    if /I "%choice%"=="y" (
        winget install Python.Python3.13
        goto line4
    )
    else if /I "%choice%"=="n" (
        cls
        exit /b
    )
    else (
        echo Invalid Input
        pause
        exit /b
    )
) else (
    if exist ".\dos\shell.py" (
        for /f %%L in (.\dos\dep\pylib.txt) do (
            python -m pip show %%L >nul 2>&1

            if errorlevel 1 (
                echo Seems like %%L is missing.
                echo "Would you like to install it? (y/n)"
                set /p idep=Select:

                if /I "%idep%"=="y" (
                    echo installing %%L...
                    python -m pip install %%L
                ) else if /I "%idep%"=="n" (
                    cls
                    exit /b
                ) else (
                    echo Invalid Input
                    pause
                    exit /b
                )
            )
        )
        python .\dos\shell.py
    ) else (
        echo Error: shell.py not found
        pause
        exit /b
    )
)