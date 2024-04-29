.DEFAULT_GOAL := run-frontend
POETRY := poetry

FLAKE_CC_MAX_THRESHOLD := 10

.PHONY: run-frontend
run-frontend:
	$(POETRY) run streamlit run internal/ui/app.py

.PHONY: run-backend
run-backend:
	$(POETRY) run python bin/main.py

.PHONY: test
test:
	$(POETRY) run pytest

.PHONY: lint
lint:
	$(POETRY) run flake8 bin/ internal/ tests/

.PHONY: cc
cc:
	$(POETRY) run flake8 --select=C --max-complexity=$(FLAKE_CC_MAX_THRESHOLD) bin/ internal/ tests/


.PHONY: cc
security:
	$(POETRY) run bandit -c pyproject.toml -r bin/ internal/ tests/
