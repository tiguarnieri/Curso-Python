@echo off
REM ===========================================
REM Script de sincronização automática com GitHub
REM Autor: Tiago Guarnieri
REM ===========================================

echo ==========================
echo  SINCRONIZANDO PROJETO...
echo ==========================

REM Entra na pasta do projeto (ajusta o caminho abaixo)
cd /d "C:\temp\Projeto"

REM Captura data e hora atuais (para nomear o commit)
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do (
    set DATA=%%a-%%b-%%c
)
for /f "tokens=1-2 delims=:." %%a in ("%time%") do (
    set HORA=%%a%%b
)

REM Passo 1: Atualiza o repositório local com as mudanças do GitHub
echo.
echo 🔄 Atualizando repositório local (git pull)...
git pull origin main --rebase

REM Passo 2: Adiciona todas as alterações locais
echo.
echo ➕ Adicionando arquivos alterados...
git add .

REM Passo 3: Cria um commit com data e hora
echo.
echo 🗒️ Criando commit...
git commit -m "Atualização automática em %DATA% às %HORA%"

REM Passo 4: Envia tudo para o GitHub
echo.
echo 🚀 Enviando para o GitHub...
git push origin main

echo.
echo =======================================
echo   ✅ Projeto sincronizado com sucesso!
echo =======================================
pause
