# Security Groups vs NACLs Explained for Beginners

In the previous articles, we learned about:

- VPC
- Subnets
- Internet Gateway
- Route Tables

These components help AWS resources communicate with each other and with the internet.

But there is still one important question:

> Even if a server is reachable, should everyone be allowed to access it?

The answer is **No**.

We need security controls that decide:

- Who can access our resources
- Which traffic is allowed
- Which traffic should be blocked

AWS provides two important security layers for this:

- Security Groups
- Network Access Control Lists (NACLs)

At first, they may seem similar, but they work at different levels and have different purposes.

In this article, we will understand them using simple real-world examples.

---

# Why Do We Need Security Layers?

Imagine you own a house.

Just because a road leads to your house does not mean everyone should be allowed inside.

You still need:

- A gate around the property
- A lock on the door

AWS networking works in a similar way.

Even if:

- A route exists
- The internet can reach your subnet

You still need security rules that decide whether traffic should be allowed or blocked.

This is where Security Groups and NACLs come in.

---

# What is a Security Group?

A Security Group is a virtual firewall attached directly to an EC2 instance.

Simply put, Security Groups are created at the **instance level**.

It controls:

- Incoming Traffic (Inbound Rules)
- Outgoing Traffic (Outbound Rules)

Think of a Security Group as the security guard standing at the door of your house.

Every request must pass through the guard before reaching the server.

---

# Example

Suppose you have a web server running on an EC2 instance.

The website uses:

```text
Port 80
```

for HTTP traffic.

You can configure the Security Group to allow traffic on Port 80.

- Requests coming on Port 80 are allowed.
- Requests coming from other ports are blocked.

---

# Security Group Flow

```text
Internet
   ↓
Security Group
   ↓
EC2 Instance
```

If traffic matches an allowed rule:

- The request reaches the EC2 instance.

Otherwise:

- AWS blocks the request.

---

# Security Groups are Stateful

This is one of the most important concepts.

Suppose a user visits your website.

## Step 1: User accesses the website

```text
User
  ↓
EC2 Web Server
```

## Step 2: EC2 sends the response back

```text
EC2 Web Server
  ↓
User
```

When inbound traffic is allowed, AWS automatically allows the response traffic.

You do not need to create separate rules for return traffic.

This behavior is called:

> Stateful

Think of it like a phone call.

If you answer a call, you can automatically talk back without opening another connection.

---

# What is a NACL?

NACL stands for:

> Network Access Control List

A NACL acts as a firewall at the subnet level.

Instead of protecting a single EC2 instance, it protects the entire subnet.

Think of a NACL as the security gate at the entrance of an apartment complex.

Anyone entering the apartment complex must pass through the gate first.

---

# NACL Flow

```text
Internet
   ↓
NACL
   ↓
Subnet
   ↓
Security Group
   ↓
EC2 Instance
```

Notice that the NACL checks traffic before it reaches the Security Group.

---

# Example

Suppose your subnet contains:

- Web Server
- Application Server
- Monitoring Server

Instead of configuring rules individually on each server, you can create subnet-level rules using a NACL.

### Allow:

- Port 80
- Port 443

### Deny:

- Port 22 from the Internet

These rules apply to the entire subnet.

---

# NACLs are Stateless

Unlike Security Groups, NACLs are stateless.

This means AWS does **not** automatically allow return traffic.

You must explicitly configure:

- Inbound Rules
- Outbound Rules

## Example

If inbound HTTP traffic is allowed:

```text
Internet
   ↓
Subnet
```

You must also create outbound rules so the response can return:

```text
Subnet
   ↓
Internet
```

Otherwise, communication fails.

This behavior is called:

> Stateless

---

# Security Group vs NACL

| Feature | Security Group | NACL |
|-----------|---------------|-------|
| Works At | EC2 Instance Level | Subnet Level |
| Stateful | Yes | No |
| Allows Traffic | Yes | Yes |
| Denies Traffic | No | Yes |
| Applied To | EC2 Instances | Subnets |
| Protection Scope | Individual Resource | Entire Subnet |

---

# Easy Way to Remember

Think about an apartment building.

```text
Apartment Complex
        ↓
       NACL
        ↓
     Apartment
        ↓
 Security Group
```

### NACL

Security at the apartment gate.

### Security Group

Security at the apartment door.

Both work together.

---

# Why Does AWS Use Both?

AWS follows a security principle called:

> Defense in Depth

Instead of relying on a single security layer, AWS uses multiple layers of protection.

### Layer 1

- NACL protects the subnet.

### Layer 2

- Security Group protects the EC2 instance.

Even if one layer is misconfigured, another layer can still provide protection.

---

# Real-World Example

Imagine an online shopping application.

## Public Subnet

Contains:

- Load Balancer

## Private Subnet

Contains:

- Application Server
- Database

### Security Group Rules

- Allow users to access the Load Balancer
- Allow the Load Balancer to access the Application Server
- Allow the Application Server to access the Database

### NACL Rules

- Block unwanted traffic at the subnet level
- Allow only required ports

This creates multiple layers of security.

---

# Conclusion

Security Groups and NACLs both play an important role in AWS security, but they work at different levels.

## Security Groups

- Protect individual EC2 instances
- Are stateful
- Allow traffic

## NACLs

- Protect entire subnets
- Are stateless
- Can allow or deny traffic

Understanding the difference between Security Groups and NACLs is an important AWS networking concept.

---

# What's Next?

In the next article, we will perform a hands-on lab where we will:

- Create a custom VPC
- Launch an EC2 instance
- Allow traffic using a Security Group
- Block traffic using a NACL
- Observe how both security layers work together

🚀 Stay tuned for the hands-on implementation.