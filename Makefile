install:
		uv sync

brain-games:
		uv run brain-games

build:
		uv build

package-install:
		uv tool install dist/*.whl

package-reload:
		uv tool install --force dist/*.whl

ruff-fix:
		uv run ruff check --fix

brain-even:
		uv run brain-even

brain-calc:
		uv run brain-calc

brain-gcd:
		uv run brain-gcd

brain-progression:
		uv run brain-progression
