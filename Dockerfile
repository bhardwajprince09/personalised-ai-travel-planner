# Stage 1: Build frontend
FROM node:18 AS frontend-builder
WORKDIR /app/frontend
# Copy package.json (and lockfile if exists)
COPY frontend/package*.json ./
# Install dependencies (force legacy peer deps for safety)
RUN npm install --legacy-peer-deps
RUN npm run build

# Stage 2: Build backend with frontend assets
FROM python:3.11-slim AS backend
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/app ./app

# Copy built frontend into backend static dir
RUN mkdir -p /app/app/static
COPY --from=frontend-builder /app/frontend/dist /app/app/static

# Expose port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
