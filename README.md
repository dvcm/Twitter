# Projeto Final
Trabalho de Conclusão de Curso 26-4-2023

A partir daqui voce vera as telas do projeto proposto.

![](/home/ebac/PycharmProjects/Twitter/social/images/projeto.png)


Front end
Página de login
![](/home/ebac/PycharmProjects/Twitter/social/images/login.png)
Página de logado
![](/home/ebac/PycharmProjects/Twitter/social/images/logado.png)
Página dos meus posts
![](/home/ebac/PycharmProjects/Twitter/social/images/meus-posts.png)
Página para atualizar o seu perfil
![](/home/ebac/PycharmProjects/Twitter/social/images/perfil-atualizar.png)
Página da lista de perfils
![](/home/ebac/PycharmProjects/Twitter/social/images/profile.png)
Página de posts que realizamos
![](/home/ebac/PycharmProjects/Twitter/social/images/texto-postado.png)
Botão Seguir 
![](/home/ebac/PycharmProjects/Twitter/social/images/seguir.png)
Botão Deixar de Seguir
![](/home/ebac/PycharmProjects/Twitter/social/images/deixar-seguir.png)
Back end


A partir do menu do site podemos entrar neste link (ADMIN)
![](/home/ebac/PycharmProjects/Twitter/social/images/django-administrator.png)
Lista de usuários
![](/home/ebac/PycharmProjects/Twitter/social/images/django-user.png)

Para ver o projeto rodando voce deve rodar no terminal

![](/home/ebac/PycharmProjects/Twitter/social/images/terminal.png)

![](/home/ebac/PycharmProjects/Twitter/social/images/python2 managepy runserver.png)

Versão atualizada em 9-12-2023


Para acessar o projeto voce precisa baixar uma copia do meu projeto
neste link github >> [Projeto Final Github](https://github.com/dvcm/Twitter)  
realizar o download na sua maquina e configurar
para rodar em python na versão 3.10

Para rodar o projeto voce precisa estar na pasta social
11:28:48 ツ ebac:(main)~/PycharmProjects/Twitter/social >$  python3 manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 11, 2023 - 14:28:51
Django version 5.0, using settings 'social.settings'
Starting development server at http://127.0.0.1:8000/


Pacotes necessários


django 5.0


pillow 10.1.0
>pip install pillow


asgiref 3.7.2


pip 23.3.1


setuptools 68.2.2


sqlparse 0.4.4


typing_extensions 4.8.0


wheel 0.41.2




Depois de instalado na máquina e verificado as dependências
Vá ao terminal e rode as seguintes instruções.


Se voce conseguir que o servidor apresente o endereco http://127.0.0.1:8000/


Otimo a copia do seu projeto está pronto para rodar!


> python3 manage.py runserver


Watching for file changes with StatReloader
Performing system checks...


System check identified no issues (0 silenced).
December 08, 2023 - 21:14:06
Django version 5.0, using settings 'social.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


No caso de querer alterar a senha de um usuário rode este comando no terminal
>python3 manage.py changepassword patrick
>
Changing password for user 'patrick'
Password:
Password (again):
Password changed successfully for user 'patrick'


Caso queria criar um super usuário rode esta instrução


>python3 manage.py createsuperuser


Username (leave blank to use 'ebac'): ebac
Email address: ebac@ebac.com.br
Password:
Password (again):
This password is too short. It must contain at least 8 characters. (Criar uma senha forte)
This password is entirely numeric.

Para se logar no sistema voce pode usar o usuario e a senha
</br>
Adm
Ebac2023

Caso queria visualizar os dados dentro do banco de dados.


![](/home/ebac/PycharmProjects/Twitter/social/images/dbrowser.jpg)
![](/home/ebac/PycharmProjects/Twitter/social/images/db.sql.png)
![](/home/ebac/PycharmProjects/Twitter/social/images/dbsqlite-user.png)
![](/home/ebac/PycharmProjects/Twitter/social/images/dbsqlite.png)
