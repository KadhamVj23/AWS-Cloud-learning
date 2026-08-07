# CI Part of the Project

## Step 1: Introduction to Continuous Integration

## CI using AWS CodeBuild

### Objective

In this part of the project, we will automate the process of building our application using AWS CodeBuild.

Instead of manually building the Docker Image every time the application changes, AWS CodeBuild will automatically build it for us in the cloud.

By the end of this section, every build will:

- Download the latest source code from Github
- Read the Dockerfile.
- Build the Docker image.
- Push the Docker image to Docker Hub.

This is known as **Continuous Integration**.

---

## What is Continuous Integration?

Continuous Integration (CI) is the practice of automatically building and validating an application whenever new code is pushed to the source repository.

Instead of developers manually building the application after every change, a CI service performs the build automatically.

This helps identify issues early and ensures the application can always be built successfully.

In our project, AWS CodeBuild is the service responsible for performing these automated builds.

---

## Why are we using AWS CodeBuild?

AWS CodeBuild is a fully managed build service.

It provides a temporary build environment where our application can be compiled, testes and packaged without requiring us to manage our build servers.

For this project, CodeBuild will:

- Download the application from GitHub
- Read the Dockerfile
- Build the Docker image.
- Push the image to Docker Hub.

EVerything happens automatically inside AWS.

---

## CI workflow

Developer
        │
        ▼
Push Code to GitHub
        │
        ▼
AWS CodeBuild
        │
        ▼
Build Docker Image
        │
        ▼
Push Image to Docker Hub

---

## Step 2: Create an AWS CodeBuild Project

### Objective

In this step, we will create our first AWS CodeBuild project.

A CodeBuild project contains all the information AWS needs to build our application. It tells CodeBuild:

- where the source code is stored.
- Which operating system and runtime to use.
- How to build the application
- Where to send the build logs.

At this stage, we only creating the project, We will configure the build process in the following steps.

---

### Open AWS CodeBuild

1. Sign in to AWS Console using your IAM user.
2. In the search bar, search for **CodeBuild**.
3. Open the **AWS CodeBuild** service.
4. Click **Create build project**.

This opens the project configuration page where will define all the settings required for our build.

---

## Project Configuration

### Project Name

Project Name:

```text
cloud-notes-build
```

> Note: Use consistent naming conventions throughout the project. This makes it easier to identify AWS resources as our project grows.

