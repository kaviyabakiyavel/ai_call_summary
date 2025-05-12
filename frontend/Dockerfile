# Stage 1
FROM node:18-alpine as build

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

# Stage 2
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
