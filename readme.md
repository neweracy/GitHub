# Git

---

#### What is Git

Git is a version control system used for tracking changes in files.

#### Uses of Git

- Version control
- Backup
- Collaboration
- Branching and merging
- Continuous integration / deployment

### Main concepts and terminologies

- **Repository** :
A git **repository** is a collection of files and folders that are tracked and managed by Git.

- **Working directory** :
the **working directory** is a directory on your local machine where you are making changes to files in the git repository.

- **Staging area** :
the **staging area** is where you can prepare your changes to be committed to the Git repository. You can selectively commit changes stage changes that you want to include in the commit.

- **Commit** :
A **commit** is a snapshot of the changes you have made to the files in the Git repository.

- **Branch** :
A **branch** is a separate line of development that can be created in a git repository.

- **Merge** :
Merging is a process of combining changes from one branch into another.

- **Pull Request** :
A **pull request** is a request to merge changes from one branch into another.

---

``` mermaid
---
title: Working with GitHub in short
---


graph LR

A[Working Area]-->|git add| B[Staging Area]
B-->|git commit| c[Local Repo]
c-->|git push| d[Remote Repo]
d-->|git pull| A


```

---

#### Basic git commands

- git init &rarr; to initialize a local git repository
- git add <file_name> &rarr; to add files
- git status &rarr; to check status of working branch
- git log &rarr; to check the history
- git push &rarr; to push to remote repository
- git clone &rarr; to clone remote repository
- git help &rarr; to get assistance
