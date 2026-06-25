# Playbook: FastAPI Microservice

## Objective
Design and validate a FastAPI microservice that adheres to RESTful best practices and OSEF microservice architectures.

## 1. Initialization
```bash
osef scaffold api --framework fastapi
```
*What happens:* OSEF scaffolds a standard router-controller-service pattern. It includes dependency injection templates and Pydantic schema validation.

## 2. API Contract Enforcement
FastAPI generates OpenAPI specs automatically, but OSEF ensures you use them correctly.
```bash
osef analyze --plugin osef-fastapi
```
The plugin checks:
- Are all endpoints typed?
- Do all responses return Pydantic models (not arbitrary dicts)?
- Are database calls abstracted behind a service layer rather than residing in the router?

## 3. Security Auditing
FastAPI APIs are often public. Ensure CORS and Auth are configured.
```bash
osef audit security
```
OSEF warns if `CORSMiddleware` allows `["*"]` in production contexts or if endpoints lack authentication dependencies.

## 4. Dockerization
Generate a production-ready `Dockerfile` optimized for Python 3.13 and `uv`.
```bash
osef repair --rule docker-001
```
OSEF generates a multi-stage Dockerfile that minimizes image size and runs the FastAPI app as a non-root user.
