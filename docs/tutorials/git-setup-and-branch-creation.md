# Tutorial 14: Git Setup & Creation of New Branch

This tutorial covers the following Learning Objectives:

- Understand how to set up Git version control for KAIZEN projects.
- Learn how to create and manage branches for collaborative development.
- Explore best practices for Git workflow in KAIZEN development teams.

In this tutorial, you will learn how to set up Git version control for your KAIZEN projects and implement effective branching strategies for collaborative development. Proper Git setup and branch management are essential for team collaboration and code quality.

## Overview

Git Setup and Branch Management ensures smooth collaboration by enabling version control, branching, and code integration. Developers can work on separate features without conflict, while maintaining a clear and organized codebase. This tool supports efficient team workflows and ensures up-to-date code management.

## Prerequisites

Before starting this tutorial, ensure you have:
- Git installed on your development machine
- Access to a Git repository (GitHub, GitLab, Bitbucket, etc.)
- Basic understanding of Git commands
- KAIZEN project ready for version control

## Git Setup Process

### 1. Initial Repository Setup

1. **Create Repository**
   - Create a new repository on your Git hosting platform
   - Choose appropriate repository settings (public/private, README, .gitignore)
   - Note the repository URL for cloning

2. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

3. **Initialize Git in KAIZEN Project**
   - Navigate to your KAIZEN project directory
   - Initialize Git if not already done:
   ```bash
   git init
   git remote add origin <repository-url>
   ```

### 2. Configure Git User Information

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Create .gitignore File

Create a `.gitignore` file to exclude unnecessary files:

```gitignore
# KAIZEN specific files
*.tmp
*.log
node_modules/
dist/
build/

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Environment files
.env
.env.local
.env.production
```

## Branch Management Strategy

### 1. Branch Naming Conventions

Establish consistent naming conventions for branches:

- **Feature branches**: `feature/feature-name`
- **Bug fix branches**: `bugfix/issue-description`
- **Hotfix branches**: `hotfix/critical-fix`
- **Release branches**: `release/version-number`

### 2. Main Branch Structure

```
main (or master)
├── develop
├── feature/user-authentication
├── feature/dashboard
├── bugfix/login-validation
└── hotfix/security-patch
```

## Creating and Managing Branches

### 1. Create New Feature Branch

```bash
# Ensure you're on the main branch
git checkout main

# Pull latest changes
git pull origin main

# Create and switch to new feature branch
git checkout -b feature/your-feature-name
```

### 2. Working on Your Branch

```bash
# Make your changes
# Add files to staging
git add .

# Commit changes with descriptive messages
git commit -m "feat: add user authentication functionality

- Implement login form
- Add password validation
- Create user session management"
```

### 3. Pushing Your Branch

```bash
# Push your branch to remote repository
git push origin feature/your-feature-name

# Set upstream for future pushes
git push --set-upstream origin feature/your-feature-name
```

## Collaborative Development Workflow

### 1. Pull Request Process

1. **Create Pull Request**
   - Push your feature branch to remote
   - Create a pull request on your Git platform
   - Add descriptive title and description
   - Assign reviewers if applicable

2. **Code Review**
   - Team members review your code
   - Address feedback and make necessary changes
   - Update the pull request with new commits

3. **Merge Process**
   - Once approved, merge to main branch
   - Delete the feature branch after successful merge
   - Update local repository

### 2. Handling Merge Conflicts

```bash
# Pull latest changes from main
git checkout main
git pull origin main

# Switch back to your feature branch
git checkout feature/your-feature-name

# Merge main into your branch to resolve conflicts
git merge main

# Resolve conflicts manually
# Add resolved files
git add .

# Complete the merge
git commit -m "merge: resolve conflicts with main branch"
```

## Best Practices for Git Workflow

### 1. Commit Guidelines

- **Conventional Commits**: Use standardized commit message format
- **Atomic Commits**: Make small, focused commits
- **Descriptive Messages**: Write clear, concise commit descriptions
- **Reference Issues**: Link commits to issue tracking systems

### 2. Branch Management

- **Keep Branches Short-lived**: Merge feature branches quickly
- **Regular Updates**: Pull latest changes from main regularly
- **Clean History**: Maintain clean, linear commit history
- **Branch Cleanup**: Delete merged branches promptly

### 3. Team Collaboration

- **Communication**: Communicate branch intentions with team
- **Code Reviews**: Participate actively in code review process
- **Documentation**: Document complex changes and decisions
- **Testing**: Ensure code works before pushing

## Advanced Git Features

### 1. Git Hooks

Implement Git hooks for automated processes:
- **Pre-commit**: Run tests and linting
- **Pre-push**: Validate code quality
- **Post-merge**: Update dependencies and documentation

### 2. Git Aliases

Create useful Git aliases for common operations:

```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

### 3. Git Submodules

Manage external dependencies:
- **Add Submodules**: Include external libraries
- **Update Submodules**: Keep dependencies current
- **Submodule Workflow**: Handle submodule changes

## Troubleshooting Common Issues

### 1. Undo Last Commit

```bash
# Undo last commit, keep changes
git reset --soft HEAD~1

# Undo last commit, discard changes
git reset --hard HEAD~1
```

### 2. Recover Deleted Branch

```bash
# Find deleted branch commit
git reflog

# Recreate branch from commit
git checkout -b feature/recovered-branch <commit-hash>
```

### 3. Clean Working Directory

```bash
# Remove untracked files
git clean -f

# Remove untracked directories
git clean -fd

# See what would be removed
git clean -n
```

## Key Learning Points

- **Git Setup**: Properly configuring Git for KAIZEN projects
- **Branch Strategy**: Implementing effective branching workflows
- **Collaboration**: Working effectively with team members
- **Conflict Resolution**: Handling merge conflicts professionally
- **Best Practices**: Following Git workflow best practices

## Expected Outcome

By the end of this tutorial, you will have mastered Git setup and branch management that demonstrates:
- Professional Git repository configuration
- Effective branching strategies for team development
- Smooth collaboration workflows
- Professional conflict resolution skills
- Best practices for version control

This foundation will prepare you for professional development environments with robust version control and collaborative development practices.
