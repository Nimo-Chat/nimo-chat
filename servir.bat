@echo off
REM ---------------------------------------------------------------------
REM  Sobe o site numa janela local, em http://localhost:8080
REM  Fecha com Ctrl+C. Nada sai da sua maquina.
REM ---------------------------------------------------------------------
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo.
  echo   Python nao encontrado no PATH.
  echo   Voce ainda pode testar dando dois cliques em index.html.
  echo.
  pause
  exit /b 1
)

echo.
echo   Nimo Chat - servidor local
echo   --------------------------
echo   Abra:  http://localhost:8080
echo   Parar: Ctrl+C
echo.

start "" http://localhost:8080
python -m http.server 8080
