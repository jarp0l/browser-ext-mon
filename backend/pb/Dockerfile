FROM golang:1.21 AS build-backend

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN CGO_ENABLED=0 GOOS=linux go build -o bem-pb .

FROM alpine:3 AS production
COPY --from=build-backend /app .
EXPOSE 8090
CMD ["./bem-pb", "serve", "--http=0.0.0.0:8090", "--dir=/pb_data"]
