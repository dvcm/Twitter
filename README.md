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

Versão atualizada em 9-12-2023


Para acessar o projeto voce precisa baixar uma copia do meu projeto
neste link github >> [Projeto Final Github](https://github.com/dvcm/Twitter)  
realizar o download na sua maquina e configurar
para rodar em python na versão 3.10

Voce precisa rodar este comando
[~/PycharmProjects/Twitter/social]

Rodar os codigos abaixo no terminal
source env/bin/activate

python3 manage.py runserver


Caso apresente este tipo de erro
Traceback (most recent call last):
  File "/home/patrick/PycharmProjects/Twitter/social/manage.py", line 11, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/patrick/PycharmProjects/Twitter/social/manage.py", line 22, in <module>
    main()
  File "/home/patrick/PycharmProjects/Twitter/social/manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?

>> entao rode este codigo
>> pip install django

Collecting django
  Using cached Django-5.0-py3-none-any.whl.metadata (4.1 kB)
Collecting asgiref>=3.7.0 (from django)
  Using cached asgiref-3.7.2-py3-none-any.whl.metadata (9.2 kB)
Collecting sqlparse>=0.3.1 (from django)
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Using cached Django-5.0-py3-none-any.whl (8.1 MB)
Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-5.0 sqlparse-0.4.4

>> Error
>> $ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/usr/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/home/patrick/PycharmProjects/Twitter/social/env/lib/python3.11/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/home/patrick/PycharmProjects/Twitter/social/env/lib/python3.11/site-packages/django/core/management/commands/runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "/home/patrick/PycharmProjects/Twitter/social/env/lib/python3.11/site-packages/django/core/management/base.py", line 556, in check
    raise SystemCheckError(msg)
django.core.management.base.SystemCheckError: SystemCheckError: System check identified some issues:

ERRORS:
musker.Profile.profile_image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".

Algo deu errado ao tentar rodar o runserver!

voltei ao terminal e rodei

>>  python3 -m pip install Pillow
Collecting Pillow
  Using cached Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (9.5 kB)
Using cached Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl (3.6 MB)
Installing collected packages: Pillow
Successfully installed Pillow-10.1.0

>>$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 29, 2023 - 12:38:13
Django version 5.0, using settings 'social.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[29/Dec/2023 12:38:17] "GET / HTTP/1.1" 200 6573
[29/Dec/2023 12:38:18] "GET /media/images/default_1NXqUU3.jpg HTTP/1.1" 304 0
[29/Dec/2023 12:38:18] "GET /static/images/default_profile_pic.png HTTP/1.1" 304 0

Se vc chegou ate aqui e deu certo! o projeto esta funcionando!

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
</br>
Ebac2023

Caso queria visualizar os dados dentro do banco de dados.


![](/home/ebac/PycharmProjects/Twitter/social/images/dbrowser.jpg)
![](/home/ebac/PycharmProjects/Twitter/social/images/db.sql.png)
![](/home/ebac/PycharmProjects/Twitter/social/images/dbsqlite-user.png)
![](/home/ebac/PycharmProjects/Twitter/social/images/dbsqlite.png)
