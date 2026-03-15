import os
import sys
import invoke


@invoke.task(aliases={"venv"})
def virtualenvironment(c, update=False):
    print(f"***\nCreating VirtualEnvironment\n***")
    c.run("python3.14 -m venv .venv --prompt=ywg-parcel")
    c.run("pip install --upgrade 'pip<26' pip-tools --no-cache-dir -v", pty=True)
    if update:
        c.run("pip-compile requirements.in -v", pty=True)
    print(f"***\nInstalling project requirements\n***")
    c.run("pip install -r requirements.txt --no-cache-dir -v", pty=True)



@invoke.task
def startapp(c):
    print(f"***\nStarting YWG-Parcel App\n***")
    c.run("docker compose build")
    c.run("docker compose up")


@invoke.task
def down(c):
    print(f"***\n***\n")
    c.run("docker compose down")
    c.run("docker system prune -a", pty=True)


# Still has issues after jumping into container...
# @invoke.task
# def exec(c):
#     print(f"jumping into app")
#     c.run("docker exec -it fastapi /bin/bash", pty=True)





