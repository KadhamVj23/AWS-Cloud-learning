# AWS Internet Gateway and Route Tables Explained for Beginners

After learning about **Public Subnets** and **Private Subnets**, the next question that comes across our mind is:

> How does traffic actually move inside AWS?

Creating a subnet alone doesn't make your application accessible.

AWS needs networking concepts to decide:

- Where the traffic comes from
- Where the traffic should go
- Whether internet access is allowed

This is where **Internet Gateways (IGW)** and **Route Tables** come into the picture.

Together, they act like roads and traffic signals for your AWS network.

---

## Imagine a Real City

Think of your AWS VPC as a city.

Inside the city, we have:

- **Buildings** = EC2 Instances
- **Neighborhoods** = Subnets
- **Roads** = Routes
- **City Gate** = Internet Gateway

Without roads and a city gate:

- Nobody can enter
- Nobody can leave

AWS networking works in a similar way.

### Real City

```text
City
 ├── Buildings
 ├── Roads
 └── Main Gate
```

### AWS Equivalent

```text
VPC
 ├── EC2 Instances
 ├── Route Tables
 └── Internet Gateway
```

---

# What is an Internet Gateway?

An Internet Gateway (IGW) is a VPC component that enables communication between:

- Your AWS VPC
- The Public Internet

It is the official entry and exit point for internet traffic.

---

## Real-World Example

Imagine a shopping mall.

It has:

- Shops inside
- Customers outside

Customers can only enter through the main entrance gate.

```text
Customers
     ↓
 Main Entrance
     ↓
 Shopping Mall
```

In AWS we can look the above situation as:

```text
Internet
     ↓
Internet Gateway
     ↓
VPC
```

The Internet Gateway acts as the main entrance gate.

---

## Without an Internet Gateway

Suppose you launch an EC2 instance. But there is no Internet Gateway attached.

```text
EC2 Instance
    ↓
Public Subnet
    ↓
VPC
```

### Result

- ❌ Users cannot access the application
- ❌ EC2 cannot browse the internet
- ❌ Software updates cannot be downloaded

Even though the EC2 instance exists, it is isolated from the internet.

---

# When an Internet Gateway is Attached

```text
Internet
     ↓
Internet Gateway
     ↓
VPC
     ↓
EC2
```

The VPC now has a connection to the outside world.

However, there is still one more requirement.

The traffic needs directions.

This is where Route Tables come in.

---

# What is a Route Table?

A Route Table is a set of rules that tells AWS:

> "Where should the traffic go?"

Think of it like Google Maps for network traffic.

When traffic arrives, AWS checks the Route Table and decides whether to:

- Send traffic to an Internet Gateway
- Send traffic to another subnet
- Send traffic to another network

---

## Real-World Example

Imagine you're driving a car.

When you reach an intersection, you see:

```text
Go Left  → Airport
Go Right → City Center
Go Straight → Highway
```

Road signs tell you where to go.

A Route Table does the same thing for network traffic.

---

## Understanding Routes

A route contains:

```text
Destination → Target
```

Example:

```text
0.0.0.0/0 → Internet Gateway
```

This means:

> Any traffic going anywhere on the internet should be sent to the Internet Gateway.

---

# What Does 0.0.0.0/0 Mean?

This confuses many beginners.

```text
0.0.0.0/0
```

means:

> Every possible IP address on the internet.

So this route means:

```text
All Internet Traffic
          ↓
Internet Gateway
```

---

# Complete Traffic Flow

Let's see what happens when a user opens a website.

## Step 1

User enters:

```text
www.example.com
```

## Step 2

The request reaches AWS.

```text
User
 ↓
Internet
```

## Step 3

Traffic enters through the Internet Gateway.

```text
User
 ↓
Internet
 ↓
Internet Gateway
```

## Step 4

AWS checks the Route Table.

```text
Internet Gateway
        ↓
    Route Table
```

## Step 5

The Route Table sends traffic to the correct subnet.

```text
Route Table
      ↓
Public Subnet
```

## Step 6

Traffic reaches the EC2 instance.

```text
Public Subnet
      ↓
EC2 Instance
```

### Complete Flow

```text
User
  ↓
Internet
  ↓
Internet Gateway
  ↓
Route Table
  ↓
Public Subnet
  ↓
EC2 Instance
```

---

# Public Route Table Example

A Public Subnet becomes public because its Route Table contains a route to the Internet Gateway.

| Destination | Target |
|------------|---------|
| VPC CIDR | Local |
| 0.0.0.0/0 | Internet Gateway |

Diagram:

```text
Public Subnet
       ↓
Route Table
       ↓
0.0.0.0/0
       ↓
Internet Gateway
       ↓
Internet
```

This allows:

- Incoming internet traffic
- Outgoing internet traffic

---

# Important Thing to Remember

Many beginners think:

> "If an EC2 is launched inside a public subnet, it automatically becomes public."

This is incorrect.

For an EC2 instance to be publicly accessible, it needs:

## Requirement 1

The subnet must have a route:

```text
0.0.0.0/0 → IGW
```

## Requirement 2

An Internet Gateway must be attached.

## Requirement 3

The EC2 instance must have a Public IP.

## Requirement 4

The Security Group must allow access.

Only then can internet users reach the EC2 instance.

---

## Private Subnet Route Table

A Private Subnet usually does not have a route to the Internet Gateway.

Example:

| Destination | Target |
|------------|---------|
| VPC CIDR | Local |

Notice:

```text
0.0.0.0/0 → IGW
```

does not exist.

Result:

- ❌ No direct internet access
- ❌ Internet users cannot reach resources
- ✅ Better security

---

# Real-World Architecture Example

Let's build a simple e-commerce website.

## Public Layer

- Load Balancer
- Web Server

## Private Layer

- Database

Architecture:

```text
Internet
    ↓
Internet Gateway
    ↓
Public Subnet
    ↓
Load Balancer
    ↓
Web Server
    ↓
Private Subnet
    ↓
Database
```

---

# Why Keep the Database in a Private Subnet?

Imagine if the database was directly accessible from the internet.

Anyone could attempt:

- Brute-force attacks
- Unauthorized access
- Data theft

Instead, we design the architecture like this:

```text
Internet
    ↓
Web Server
    ↓
Database
```

Only the Web Server can communicate with the Database.

Users cannot directly reach it.

This is a core AWS security principle.

---

# Public vs Private Subnet Visualization

```text
                    Internet
                        │
                Internet Gateway
                        │
                 Route Table
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼

    Public Subnet              Private Subnet

          │                           │
          ▼                           ▼

      Web Server                 Database
```

---

# Conclusion

Internet Gateway and Route Tables are the foundation of AWS networking.

In this article, we learned:

- What an Internet Gateway is
- Why it is required
- What Route Tables are
- How AWS routes traffic
- Difference between Public and Private Subnets
- Real-world examples of traffic flow
- How web applications securely communicate with databases

Once you understand Internet Gateway and Route Tables, AWS networking becomes much easier to visualize.

---

# Key Interview Question

### What makes an EC2 instance publicly accessible?

The following four conditions must be met:

```text
0.0.0.0/0 Route
        +
Internet Gateway
        +
Public IP
        +
Security Group Allow Rule
        =
Accessible from Internet
```

Remembering these four requirements helps answer many AWS networking interview questions.

---

# Next Article

In the next article, we'll explore:

- Security Groups
- Network ACLs (NACLs)
- How AWS protects resources at the network level