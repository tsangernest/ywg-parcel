import invoke


@invoke.task
def down(c):
    print(f"***\n***\n")
    c.run("docker compose down", pty=True)
    c.run("docker system prune -af", disown=True, pty=True)


@invoke.task
def startapp(c):
    print(f"***\nStarting YWG-Parcel App\n***")
    c.run("docker compose build")
    c.run("docker compose up", pty=True)


@invoke.task(aliases=["up"])
def update_requirements(c):
    print(f"\n***[ === Compiling requirements === ]***\n")
    c.run("pip-compile -v  requirements.in", pty=True)


@invoke.task(aliases={"venv"})
def virtualenvironment(c, update=False):
    print(f"***\nCreating VirtualEnvironment\n***")
    c.run("python3.14 -m venv .venv --prompt=ywg-parcel")
    c.run("pip install --upgrade pip pip-tools --no-cache-dir -v", pty=True)
    if update:
        c.run("pip-compile requirements.in -v", pty=True)
    print(f"***\nInstalling project requirements\n***")
    c.run("pip install -r requirements.txt --no-cache-dir -v", pty=True)


# Still has issues after jumping into container even with python 3.12...
# @invoke.task
# def exec(c, container_name: str = "fastapi"):
#     print(f"jumping into app")
#     c.run(f"docker exec -it {container_name} /bin/bash", pty=True)





