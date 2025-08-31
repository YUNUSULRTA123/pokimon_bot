# Security Policy

## Supported Versions
We only provide security updates for actively maintained versions of this project.

```
| Version | Supported          |
| ------- | ------------------ |
| 1.x     | ✅ Security updates |
| 0.x     | ❌ End of life      |
```

## Reporting a Vulnerability
If you discover a security vulnerability, please **do not open a public issue**.  

Instead, contact us through one of the following: 
- GitHub Security Advisories: [Creating a private report](https://docs.github.com/en/code-security/security-advisories)  

Please include:
- Project version and environment details  
- Steps to reproduce the issue  
- The potential impact/severity  

## Security Best Practices
- Always use the latest stable release.  
- Install dependencies from `requirements.txt` in an isolated environment (`venv`, `pipenv`, or `poetry`).  
- Regularly update dependencies (`pip list --outdated`).  
- Never commit secrets (tokens, passwords, API keys). Use environment variables instead.  

