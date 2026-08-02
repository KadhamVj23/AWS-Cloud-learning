# Preparing for AWS CI/CD Hands-On Project - Prerequisites

## Introduction

In the previous article, we learned how AWS CodePipeline automates the software delivery process.

Before we start building our AWS CI/CD pipeline, we need one more important tool: **Docker**.

Modern applications are rarely deployed directly from the source code. Instead, they are packaged into Docker images, making them portable and consistent across different environments.

In this article, we will prepare everything required for our CI/CD project by creating a Docker account and understanding how Docker images work.

---

# Why Do We Need Docker?

Imagine you are developing an application on your laptop.

It works perfectly on your machine.

But when another developer runs the same application, it suddenly fails because:

- A different Python version is installed.
- Some libraries are missing.
- The operating system is different.

This is a very common problem.

Docker solves it by packaging everything the application needs into a single unit called a **Docker image**.

Instead of saying:

> It works on my machine.

You can simply share the Docker image, and it works the same everywhere.

---

# What is Docker Hub?

Docker Hub is similar to GitHub, but instead of storing source code, it stores Docker images.

You can:

- Upload Docker images.
- Download images.
- Share images.
- Use images in your CI/CD pipelines.

Think of it like this:

| GitHub | Docker Hub |
|---------|------------|
| Stores source code | Stores Docker images |
| Git repositories | Docker repositories |

---

# Create a Docker Hub Account

1. Open your browser.
2. Visit **https://hub.docker.com/**
3. Click **Sign Up**.
4. Create a free account.
5. Verify your email address.
6. Sign in to Docker Hub.

Congratulations! Your Docker Hub account is ready.

---

Till now we have learned that AWS CodePipeline automates the software delivery process and how Docker helps package applications into portable Docker images.

But one important question still remains.

When a developer pushes code to GitHub:

- Who actually builds the application?
- Who compiles the code?
- Who runs the tests?
- Who creates the Docker image?

The answer is **AWS CodeBuild**.

---

# What is AWS CodeBuild?

AWS CodeBuild is a fully managed build service that automatically builds and tests your application whenever new code is pushed.

Instead of manually running the build commands on your laptop, CodeBuild creates a temporary build environment in AWS and performs all required tasks.

Think of CodeBuild as a robot builder.

You simply tell it what to do, and it performs the work automatically.

---

# Where Does CodeBuild Fit?

Let's look at the complete flow.

```text
Developer
   ⬇️
Push Code
   ⬇️
GitHub
   ⬇️
AWS CodePipeline
   ⬇️
AWS CodeBuild
   ⬇️
Docker Hub / Amazon ECR
   ⬇️
AWS CodeDeploy
   ⬇️
EC2 / ECS / EKS
```

Notice something important.

CodePipeline doesn't build your application.

It simply coordinates the workflow.

The actual build work is done by CodeBuild.

---

# What Happens Inside CodeBuild?

Whenever CodeBuild starts, it performs a series of automated steps.

A typical workflow looks like this:

```text
Download Source Code
        ⬇️
Install Dependencies
        ⬇️
Compile / Build Application
        ⬇️
Run Unit Tests
        ⬇️
Run Code Quality Checks
        ⬇️
Build Docker Image
        ⬇️
Push Docker Image
```

Each project may have different steps depending on the application.

---

# What is a Build Environment?

CodeBuild doesn't use your local computer.

Instead, AWS creates a temporary build server whenever a build starts.

This temporary environment includes:

- Operating system
- CPU and memory
- Required programming language
- Build tools
- Runtime

Once the build completes, AWS automatically removes the environment.

This means you don't need to manage build servers yourself.

---

# What is a `buildspec.yml` File?

One of the most important parts of CodeBuild is the `buildspec.yml` file.

Think of it as an instruction manual for CodeBuild.

It tells AWS exactly what commands should be executed during the build.

For example, it may contain instructions such as:

- Install dependencies.
- Run tests.
- Build the application.
- Build the Docker image.
- Push the image to Docker Hub.

Without a `buildspec.yml` file, CodeBuild wouldn't know what to do.

We will create and understand this file in our upcoming hands-on article.

---

# Real-World Example

Imagine a company developing an online banking application.

A developer fixes a bug and pushes the code to GitHub.

Immediately:

- GitHub notifies AWS CodePipeline.
- CodePipeline starts the workflow.
- CodeBuild downloads the latest code.
- It builds the application.
- It runs automated tests.
- It creates a Docker image.
- The Docker image is uploaded to Docker Hub.
- CodeDeploy deploys the new version.

All of this happens automatically without manual intervention.

---

# Why Use AWS CodeBuild?

AWS CodeBuild offers several advantages.

## Fully Managed

AWS manages the build infrastructure for you.

## Automatic Scaling

Multiple builds can run simultaneously without requiring manual setup.

## Pay Only for What You Use

You are billed only for the build time used.

## Easy Integration

CodeBuild integrates seamlessly with:

- GitHub
- AWS CodePipeline
- Docker Hub
- Amazon ECR
- CodeDeploy
- Amazon S3

## No Build Server Maintenance

There is no need to install or update build servers.

AWS handles everything behind the scenes.

---

# What's Next?

In the next article, we will start our hands-on implementation of the entire CI/CD process.

We will divide it into **3 to 4 articles** to make it easier to understand and keep the content clean and well organized.