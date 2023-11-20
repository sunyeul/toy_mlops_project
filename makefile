.PHONY: clean_pycache

clean_pycache:
	@echo "Removing __pycache__ directories..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "Cleanup completed."