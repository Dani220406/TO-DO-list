# 📋 TO-DO-list

## App for Easier Task Managment

## 🌐 Live Demo

Try the Live Demo at: **[To-Do-List](https://to-do-list-unict.streamlit.app/)**

## 🔍 How the app works

The app is divided into two "layers", an homepage and a list-page.

### Homepage

Opens after a welcome message. In the Homepage it's possible to do general actions onto the TO-DO Lists; more specifically:

- **Create New List**: Creates a new TO-DO List by adding its name.
- **Delete List**: Deletes the selected TO-DO List.
- **Create New Folder**: Creates a new folder by adding its name.
- **Manage Folders**: Moves a TO-DO List into the chosen folder.
- **Delete Folder**: Allows to delete the selected folder whilst preserving its contents.
- **My Folders**: Shows the created folders alongside its contents.

### List-Page

Opens when a TO-DO List is selected. In the List-Page it's possible to do specific actions onto the selected TO-DO List's elements; more specifically:

- **Back to Homepage**: Saves the updated contents of the TO-DO List and returns back to the Homepage.
- **Add Element**: Creates a new element in the TO-DO List by adding its name.
- **Edit Element**: Allows to edit the text of the selected element.
- **Delete Element**: Deletes the selected element.
- **Order Elements**: Allows to change the order of elements within the TO-DO List.
- **Complete Task**: Marks the selected task as completed.
- **Label**: Adds a label to the selected element to simbolize its priority compared to other elements.
- **Edit Style**: Allows to add Bold/Italics/Text-Color to the selected element.

## 🔗 How the Project is Structured

```
🌐TO-DO-LIST
    │
    ├── .devcontainer                        # Demo Cloud Streamlit
    │
    ├── .github/workflows/
    │       └── 👷 ci.yml                    # CI Pipeline
    │
    ├── 🖼️ project_showcase/
    │       ├── 📸 all_files_coverage.png     # Showcase Coverage Entire Project
    │       ├── 📸 code_coverage.png          # Showcase Coverage tests/
    │       ├── 📸 homepage_view.png          # Showcase Homepage View
    │       └── 📸 list_page_view.png         # Showcase List-Page View
    │
    ├── 🛠 todo_app/                          # App Folder
    │       ├── 💻 screens/                  # App Layers Folder
    │       │       ├── 🚧 __init__.py
    │       │       ├── 🏠 home.py           # Homepage Managment
    │       │       └── 👋 welcome.py        # Welcome Message
    │       │
    │       ├── ⛓️ sidebar/                   # Sidebar Methods Folder
    │       │       ├── 🚧 __init__.py
    │       │       ├── 🔘 elements.py       # List Elements Methods
    │       │       ├── 📁 folders.py        # Folder Methods
    │       │       ├── ℹ️ info.py           # Info on App Methods
    │       │       └── 📄 lists.py           # List Methods
    │       │
    │       ├── ⁉️ utils/                    # Utils Methods Folder
    │       │       ├── 🚧 __init__.py
    │       │       └── 🤲 helpers.py        # Subroutines of some Methods
    │       │
    │       ├── 🚧 __init__.py
    │       ├── ⚙️ config.py                 # App Configuration
    │       └── 📱 main.py                    # Main File
    │
    ├── 🖥️ app.py                            # App Deployment
    │
    ├── 🔬 tests/                            # Unit-Tests Folder
    │       ├── 🚧 __init__.py
    │       ├── 🏗️ test_config.py            # Unit-Tests *config.py* Methods
    │       ├── 🏗️ test_elements.py          # Unit-Tests *elements.py* Methods
    │       ├── 🏗️ test_folders.py           # Unit-Tests *folders.py* Methods
    │       ├── 🏗️ test_helpers.py           # Unit-Tests *helpers.py* Methods
    │       ├── 🏗️ test_home.py              # Unit-Tests *home.py* Methods
    │       ├── 🏗️ test_info.py              # Unit-Tests *info.py* Methods
    │       ├── 🏗️ test_lists.py             # Unit-Tests *lists.py* Methods
    │       ├── 🏗️ test_main.py              # Unit-Tests *main.py* Methods
    │       └── 🏗️ test_welcome.py           # Unit-Tests *welcome.py* Methods
    │
    ├── 🚫 .gitignore                       # Ignore Files on Git Push
    ├── 🔑 LICENSE                          # App License
    ├── ✏️ README.md                        # Project Description
    ├── 🔒 requirements_dev.txt             # Unit-Tests Requirements
    └── 🔒 requirements.txt                 # App Requirements
```

## ⬇️ Installing App Dependencies

### Pre-requirements

- Python 3.12.3+ (suggested)
- pip (package manager)
- venv (creating a virtual environment is suggested)

### Dependencies Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Dani220406/TO-DO-list.git
cd TO-DO-list
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

*otherwise manually:*

```bash
pip install streamlit
```

3. **Start the App:**

```bash
streamlit run app.py
```

## 📝 Unit-Tests
We've organized the Unit-Tests of all methods used in the app inside the **tests/** folder. To run the tests it's required: 

1. **Install dependencies:**

```bash
pip install -r requirements_dev.txt
```

*otherwise manually:*

```bash
pip install pytest pytest-mock pytest-cov pylint flake8 mypy black
```

2. **Run the Tests:**

The tests can be run all at the same time or each by themselves:

*All at the Same Time:*

```bash
cd TO-DO-list
pytest tests/
pytest --cov=tests/
```

*Each by Themselves:*

```bash
cd TO-DO-list
pytest tests/test_elements.py
pytest --cov=tests/test_elements.py
...
```

🏆 *The Project has a code coverage of: **~98%** !*

## 👨‍💻 Developers

- **[@Dani220406](https://github.com/Dani220406)**
- **[@MrMelus](https://github.com/MrMelus)**
- **[@BecherLiaoumi](https://github.com/BecherLiaoumi)**

---

🏅 *Project made for the Quality Development 2025/2026 course of the UNICT DMI*