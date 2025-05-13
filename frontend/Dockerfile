FROM node:18-alpine

WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Serve using a static server (like nginx or serve)
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "3000"]
