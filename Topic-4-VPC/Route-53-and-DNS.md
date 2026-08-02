# Understanding DNS and AWS Route 53 for Beginners

In the previous articles, we learned about:

- VPC
- Subnets
- Internet Gateway
- Route Tables
- Security Groups
- Network ACLs (NACLs)

These components help us build and secure our AWS infrastructure.

But there is still one question:

> How do users actually find our application?

For example, when users open:

```text
www.amazon.com
```

how does the browser know where the website is running?

This is where **DNS** and **AWS Route 53** come into the picture.

In this article, we will understand:

- What DNS is
- Why DNS is needed
- What AWS Route 53 is
- How Route 53 works
- Real-world examples
- AWS examples

Let's get started.

---

# Why Do We Need DNS?

Imagine you want to call your friend.

Would you remember:

```text
9876543210
```

for every person in your contacts?

Probably not.

Instead, you save names like:

- Mom
- Dad
- Friend
- Office

Your phone automatically maps the name to the phone number.

DNS works exactly the same way.

Instead of remembering IP addresses like:

```text
54.210.100.25
```

we simply remember:

```text
www.google.com
```

DNS converts:

```text
Domain Name → IP Address
```

This makes websites easier for humans to use.

---

# What is DNS?

DNS stands for:

> Domain Name System

DNS is like the phonebook of the internet.

Its job is to convert:

```text
www.amazon.com
```

into something computers understand:

```text
54.xx.xx.xx
```

Without DNS, we would have to remember IP addresses for every website.

---

# Real-Life Example

Think of a restaurant.

People usually say:

```text
McDonald's
```

instead of saying:

```text
Building Number 25
Street Number 10
City XYZ
```

The restaurant name is easier to remember.

Similarly:

```text
www.youtube.com
```

is easier to remember than:

```text
142.250.182.206
```

---

# How DNS Works

Suppose a user opens:

```text
www.shopworld.com
```

The process looks like this:

```text
User
   ↓
DNS Lookup
   ↓
IP Address Found
   ↓
Application Server
```

DNS finds the IP address associated with the domain name and sends the user to the correct server.

---

# What is AWS Route 53?

AWS Route 53 is Amazon's managed DNS service.

It helps:

- Convert domain names into IP addresses
- Route users to AWS resources
- Improve application availability
- Register domain names

Simply put:

> Route 53 is AWS's DNS service.

---

# Why is it Called Route 53?

DNS communication uses:

```text
Port 53
```

That is why AWS named the service:

> Route 53

---

# How Route 53 Works

Suppose you have a website:

```text
www.shopworld.com
```

Your application is running behind a Load Balancer.

When a user enters the domain name, Route 53 finds the correct destination.

Flow:

```text
User
   ↓
www.shopworld.com
   ↓
Route 53
   ↓
Load Balancer
   ↓
Application Server
```

Route 53 does not host your application.

Its job is only to direct users to the correct resource.

---

# AWS Example

Suppose your architecture looks like this.

## Public Subnet

- Load Balancer

## Private Subnet

- Application Server

Users do not know the IP address of your Load Balancer.

Instead, they simply visit:

```text
www.shopworld.com
```

Route 53 translates the domain name and forwards users to the Load Balancer.

The Load Balancer then sends requests to the application server.

---

# Real-World Example

Imagine an e-commerce company.

Without DNS:

```text
http://44.210.150.20
```

Customers would need to remember the IP address.

With DNS:

```text
www.shopworld.com
```

Customers can easily remember and access the website.

DNS makes the internet user-friendly.

![Route 53 Architecture](screenshots/Route-53.png)

---

# Benefits of Route 53

Route 53 provides:

- High Availability
- Scalability
- Managed DNS Service
- Domain Registration
- Health Checks
- Traffic Routing Capabilities

Because AWS manages Route 53, we do not need to maintain DNS servers ourselves.

---

# Summary

DNS converts:

```text
Domain Name → IP Address
```

AWS Route 53 is Amazon's managed DNS service that helps users access applications using easy-to-remember domain names.

---

# Conclusion

DNS is one of the fundamental building blocks of the internet.

Without DNS, users would have to remember IP addresses for every website.

AWS Route 53 simplifies this process by providing a highly available and scalable DNS service.

Understanding DNS and Route 53 is an important AWS networking concept and is commonly used in real-world cloud architectures.

---

# What's Next?

In the next article, we will build a complete AWS VPC Project that can be added to your resume.

We will create:

- Custom VPC
- Public and Private Subnets
- Internet Gateway
- Route Tables
- Security Groups
- EC2 Instances

and understand how these components work together in a real-world architecture.

🚀 See you in the next article.