# 🚀 Modern Data & AI Engineering Monorepo

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![RAG Architecture](https://img.shields.io/badge/RAG_Architecture-000000?style=for-the-badge&logo=quicklook&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

## 📌 Overview
Welcome to my Data & AI Engineering monorepo. This repository serves as a centralized hub for my system design blueprints, analytical data pipelines, real-time streaming architectures, and privacy-first Generative AI (RAG & Agents) implementations.

As a **Lead Data / AI Engineer**, my philosophy is rooted in building systems that are **Scalable, Reliable, and Maintainable** (inspired by *Designing Data-Intensive Applications*), while seamlessly integrating large language models into enterprise data workflows and deploying them robustly using container orchestration.

## 📂 Repository Structure

This monorepo is divided into three main components:

### 1. `📁 architecture-designs/` (System Design & ADRs)
High-level system design documents and Architecture Decision Records (ADRs). Here I explore trade-offs between streaming vs. batch paradigms, data modeling strategies, and AI agent architectures.
* *Coming soon: Real-time Event Streaming Architecture.*
* *Coming soon: Enterprise RAG System with Local LLMs deployed on Kubernetes.*

### 2. `📁 projects/` (End-to-End Implementations)
Production-grade implementations focusing on the intersection of Data, AI, and scalable deployment.
* **`01-analytics-engineering/`**: Advanced SQL, Kimball dimensional modeling, and data transformations using **dbt**.
* **`02-streaming-data/`**: Event-driven architectures utilizing **Apache Kafka** and Python for real-time processing.
* **`03-genai-rag-agents/`**: Building privacy-first **RAG (Retrieval-Augmented Generation) pipelines**, semantic search with Vector Databases, and autonomous **AI Agents** using Python and open-source LLMs.
* **`04-k8s-deployments/`**: Kubernetes manifests, Helm charts, and Dockerfiles demonstrating how to package, scale, and deploy the data/AI applications above.

### 3. `📁 daily-leetcode-sql-python/` (Algorithmic & SQL Optimization)
Daily solutions to advanced problems, focusing on Time/Space complexity in **Python** and advanced query optimization/window functions in **SQL**.

## 🛠️ Core Engineering Principles
1. **Separation of Compute and Storage:** Utilizing cloud-native data lakes to decouple compute costs from durable storage for analytical workloads.
2. **Event Sourcing & Immutability:** Treating data as an immutable log of events to allow for robust auditability, easy debugging, and real-time streaming.
3. **AI-Driven Data Engineering:** Bridging the gap between raw data and LLMs through high-quality feature engineering, vector embeddings, and modular **RAG architectures** without relying exclusively on walled-garden APIs.
4. **Scalable Orchestration:** Packaging applications as microservices and leveraging **Kubernetes** for fault tolerance, auto-scaling, and resource management (e.g., GPU allocation for ML workloads).
5. **Data Quality & Compliance:** Designing robust pipelines with automated testing (dbt) while adhering to GDPR data minimization and data sovereignty principles.

---
*Open to discussions on Data Architecture, AI Engineering, and Streaming. Feel free to explore the code or reach out!*
