FROM python:3.11-slim

WORKDIR /app

# Copy challenge and solver
COPY problem.md /app/problem.md
COPY README.md /app/README.md
COPY solver/solve.py /app/solver/solve.py

# Set up environment
ENV PYTHONUNBUFFERED=1

# Run the solver by default
CMD ["python", "solver/solve.py"]
