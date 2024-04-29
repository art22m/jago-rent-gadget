.DEFAULT_GOAL := run-frontend
POETRY := poetry

FLAKE_CC_MAX_THRESHOLD := 10

.PHONY: update
update:
	rm -rf poetry.lock
	$(POETRY) install

.PHONY: run-frontend
run-frontend:
	$(POETRY) run streamlit run ui/app.py

.PHONY: run-backend
run-backend:
	$(POETRY) run python bin/main.py

.PHONY: test
test:
	$(POETRY) run pytest \
		--junitxml=reports/test-report.xml \
		--html=reports/report.html \

.PHONY: cov
cov:
	$(POETRY) run pytest \
		--junitxml=reports/test-report.xml \
		--html=reports/report.html \
		--cov-report=term-missing \
		--cov=internal \
		--cov-fail-under=60 tests/

.PHONY: lint
lint:
	$(POETRY) run flake8 bin/ internal/ tests/

.PHONY: cc
cc:
	$(POETRY) run flake8 --select=C --max-complexity=$(FLAKE_CC_MAX_THRESHOLD) bin/ internal/ tests/


.PHONY: security
security:
	$(POETRY) run bandit -c pyproject.toml -r bin/ internal/ tests/
