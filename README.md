# PyShiny Basic Dashboard (Penguins)

## Tools

- Python
- Shiny for Python
- VS Code + Python Extension
- Git
- GitHub

## Try in the Browser

Go to PyShiny Templates at <https://shiny.posit.co/py/templates/>.
Go to Dashboards / Basic Dashboard.

- <https://shiny.posit.co/py/templates/dashboard/>

## Get the Code

Fork this project into your own GitHub account.
Clone **your** GitHub repo down to your local machine.
IMPORTANT: Use your GitHub **username** in place of denisecase.
[GitHub CLI](https://cli.github.com/) may work better on some machines.

```shell
git clone https://github.com/denisecase/cintel-07-tdash
```

## Run Locally - Initial Start

After cloning your project down to your Documents folder, open the project folder for editing in VS Code.

Create a local project virtual environment named .venv, activate it, and install the requirements.

When VS Code asks to use it for the workspace, select Yes.
If you miss the window, after installing, select from the VS Code menu, View / Command Palette, and type "Python: Select Interpreter" and select the .venv folder.

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands (for Windows - the activate command is slightly different Linux/Mac).

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
shiny run --reload --launch-browser app/app.py
```

Open a browser to <http://127.0.0.1:8000/> and test the app.

## Run Locally - Subsequent Starts

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny run --reload --launch-browser app/app.py
```

## After Changes, Export to Docs Folder

Export to docs folder and test GitHub Pages locally.

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
shiny static-assets remove
shinylive export app docs
py -m http.server --directory docs --bind localhost 8008
```

Open a browser to <http://[::1]:8008/> and test the Pages app.

## Push Changes back to GitHub

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
git add .
git commit -m "Useful commit message"
git push -u origin main
```

## Enable GitHub Pages

Go to your GitHub repo settings and enable GitHub Pages for the docs folder.

