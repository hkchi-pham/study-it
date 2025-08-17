# Docker & Docker compose

## 1. What is Docker?
- Docker = platform to develop, ship, and run applications in containers.
- Container = lightweight, isolated environment that packages app + dependencies (libraries, runtime, configs).
- Runs on top of OS kernel, shares system resources → faster and smaller than VMs.

## 2. Why use Docker?
- Consistency: Same environment everywhere (dev, test, prod).
- Lightweight: Containers share the host OS → smaller, faster than VMs.
- Portability: Run anywhere (Windows, Linux, Mac, cloud).
- Scalability: Spin up multiple containers easily.
- DevOps: Easy CI/CD integration.

## 3. What is Docker Compose?
- A tool to define & run multi-container apps (e.g., web + DB + cache).
- Uses docker-compose.yml file:
  - Define services (containers)
  - Define networks
  - Define volumes (persistent data)
 
## 4. Docker vs Virtual Machine(VMs)
  
  | Feature         | Docker (Containers)                             | Virtual Machine (VM)                             |
| --------------- | ----------------------------------------------- | ------------------------------------------------ |
| **Isolation**   | Process-level isolation (shares host OS kernel) | Full OS isolation (each VM has its own kernel)   |
| **Size**        | Lightweight (MBs)                               | Heavy (GBs)                                      |
| **Startup**     | Seconds                                         | Minutes                                          |
| **Performance** | Near-native (less overhead)                     | Slower (more overhead due to hypervisor)         |
| **Portability** | Very portable                                   | Less portable                                    |
| **Use cases**   | Microservices, DevOps, CI/CD, scalable apps     | Full OS emulation, legacy apps, strong isolation |

## 5. Basic Commands
```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
docker ps
docker stop <container_id>
docker-compose up
docker-compose down
```
