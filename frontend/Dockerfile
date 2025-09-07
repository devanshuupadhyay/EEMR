FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Copy lockfile too!
COPY package-lock.json ./

# Clean reproducible install
RUN npm ci

# Copy rest of project
COPY . .

EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--hostname", "0.0.0.0", "--port", "3000"]
