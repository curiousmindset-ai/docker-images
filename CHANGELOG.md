# Changelog

All notable changes to this repository will be documented in this file.

The format is based on **Keep a Changelog**,  
and this project adheres to **Semantic Versioning**.

---

## [Unreleased]

### Added
- Initial repository structure for managing multiple Docker images
- CI validation stage for Docker and Terraform workflows
- Terraform validation checks:
  - `terraform fmt -check`
  - `terraform validate`
  - `tflint`
- GitHub Actions workflow for Dockerfile linting (Hadolint)

### Changed
- Standardized Dockerfile layout using multi-stage builds
- Improved CI pipeline validation and early-fail checks

### Security
- Added static analysis and policy checks during validation stage

---

## [0.1.0] – 2026-02-04

### Added
- First functional Docker image(s)
- Initial AWS CodePipeline + CodeBuild integration
- Base CI/CD pipeline structure

---

## Versioning Strategy

- **MAJOR** – Breaking changes (base image changes, incompatible runtime changes)
- **MINOR** – New images, new pipeline stages, backward-compatible improvements
- **PATCH** – Bug fixes, security patches, documentation updates

---

## Notes

- Every change merged into `main` should update the **[Unreleased]** section.
- Releases are cut by promoting `[Unreleased]` to a versioned section.
