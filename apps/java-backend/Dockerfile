FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src ./src
RUN mvn package -DskipTests -q

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
RUN adduser -D -u 1001 appuser
COPY --from=builder /app/target/java-backend-1.0.0.jar app.jar
RUN chown appuser:appuser app.jar
USER appuser
EXPOSE 8080
CMD ["java","-XX:+UseContainerSupport","-XX:MaxRAMPercentage=75.0","-jar","app.jar"]
