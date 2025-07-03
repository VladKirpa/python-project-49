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

brain-even:
		uv run brain-even

	
