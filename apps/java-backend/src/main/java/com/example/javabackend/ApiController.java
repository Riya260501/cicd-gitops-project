package com.example.javabackend;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
public class ApiController {
    private static final Logger logger = LoggerFactory.getLogger(ApiController.class);

    @GetMapping("/")
    public Map<String, String> home() {
        logger.info("GET / called");
        return Map.of("service", "java-backend", "status", "running");
    }

    @GetMapping("/health")
    public ResponseEntity<Map<String, String>> health() {
        logger.info("Health check passed");
        return ResponseEntity.ok(Map.of("status", "healthy"));
    }

    @GetMapping("/api/orders")
    public Map<String, Object> orders() {
        logger.info("GET /api/orders called");
        return Map.of(
            "source", "java-backend",
            "orders", List.of(
                Map.of("id", "ORD-001", "status", "shipped"),
                Map.of("id", "ORD-002", "status", "processing")
            )
        );
    }
}
