# Git

## 1. What is Git?
It is a version control system, used to track changes of code files overtime so user can recall specific version later, documenting the progress of a codebase.

It allows web designer, software developer that want to keep every version of a code layout, including tasks like reverting selected file back to a previous state, reverting the entire project back to a previous stage,
comparing changes overtime...

If you screw up things or lose a file, using a VCS will be very helpful for an easy recover.

Now, Git thinks of data more like a series of snapshot. Everytime you commit, or save a certain stage of a project, Git basically takes a snapshot of what all your files look like at that moment and stie a reference to that snapshot.

## 2. What is it used for?
- Version control
- Collaboration between developer
- Branching & merging
- Code history & rollback

## 3. Basic Git Commands
```git config --global user.name "[name]"``` : Set an indentifiable name 

```git config --global user.email [email]``` : set an email address that will be associated with each history marker
  
```git init``` : initialise an existing directory as a list repository
  
```git clone [URL]``` : retrieve an entire repository from a host location via URL

```git status``` : show modified files in working directory, staged for your next commit

```git add [file]``` : add a file as it looks now to the next commit

```git reset [file]``` : unstage a file while retaining the changes in working directory

```git commit -m "[descriptive message]"``` : commit your staged content as a new commit snapshot

```git branch``` : list your branches. a * will appear next to the currently working branch

```git branch [branch name]``` : create a new branch at the current commit

```git push``` : transmit local branch commits to the current commit

```git pull``` : fetch and merge any commit from the tracking remote branch

```git stash``` :save modified or staged changes that aren't ready to be commit yet

```git checkout``` : switch to another branch ans check it out onto your working directory

## 4. Git message convention via Convention Commit
- a set of agreed-upon guidelines for structuring and writing commit messages in a Git repository.

- Structure:
```<type> [optional scope]: <description>```

- Structural elements to communicate intent of the commit:
  1. ```fix``` : a commit of type fix patches of bug in the codebase
  2. ```feat``` : a commit of type feat introduces a new feature to the codebase
  3. ```BREAKING CHANGE``` : a commit that have a footer BREAKING CHANGE; or append a "!" after the type/scope, introduces a breaking API change
  4. ```docs```: Documentation changes only (README, inline docs, API docs, etc.).
  5. ```style``` : Code style changes (formatting, whitespace, semicolons) — no logic changes.
  6. ```refactor``` : Changes code structure without altering its external behavior.
  7. ```perf``` : Improves performance without changing features.
  8. ```test``` : Adds or updates tests without changing production code.
  9. ```build``` : Changes to build system, package manager, or external dependencies.
  10. ```ci``` : Continuous integration / deployment configuration changes.
  11. ```chore``` : Routine tasks or maintenance that don’t affect production code.
  12. ```revert``` : Reverts a previous commit.

- Examples:
  
```feat: add dark mode display```

```fix: prevetn crash out on null user profile```

```feat!: send a message to mentor when finish researching```

  


