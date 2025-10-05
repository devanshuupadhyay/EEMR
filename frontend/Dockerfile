FROM node:20-alpine

WORKDIR /app

# Install dependencies first (will be cached)
COPY package*.json ./
RUN npm ci

# The rest of the project is copied via docker-compose volume mount for hot-reloading
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--hostname", "0.0.0.0", "--port", "3000"]